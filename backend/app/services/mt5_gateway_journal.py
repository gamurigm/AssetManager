"""Durable, fail-closed journal for MetaTrader 5 expert signals.

The journal intentionally lives outside the analytical DuckDB database.  Its
unique signal_id constraint is the first line of defence against an Expert
Advisor retrying the same signal after a timeout or backend restart.
"""

from __future__ import annotations

import json
import sqlite3
import threading
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


class MT5GatewayJournal:
    def __init__(self, db_path: Optional[Path] = None) -> None:
        backend_root = Path(__file__).resolve().parents[2]
        self.db_path = db_path or backend_root / "data" / "mt5_gateway.sqlite3"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._initialize()

    @contextmanager
    def _connection(self):
        conn = sqlite3.connect(self.db_path, timeout=5.0)
        try:
            conn.row_factory = sqlite3.Row
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("PRAGMA busy_timeout=5000")
            yield conn
            conn.commit()
        finally:
            conn.close()

    def _initialize(self) -> None:
        with self._lock, self._connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS mt5_order_journal (
                    signal_id TEXT PRIMARY KEY,
                    expert_id TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    side TEXT NOT NULL,
                    volume REAL NOT NULL,
                    execution_mode TEXT NOT NULL,
                    state TEXT NOT NULL,
                    request_json TEXT NOT NULL,
                    result_json TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS mt5_gateway_control (
                    control_key TEXT PRIMARY KEY,
                    value_json TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )

    def reserve(
        self,
        *,
        signal_id: str,
        expert_id: str,
        symbol: str,
        side: str,
        volume: float,
        execution_mode: str,
        request: Dict[str, Any],
    ) -> bool:
        now = datetime.now(timezone.utc).isoformat()
        with self._lock, self._connection() as conn:
            try:
                conn.execute(
                    """
                    INSERT INTO mt5_order_journal (
                        signal_id, expert_id, symbol, side, volume,
                        execution_mode, state, request_json, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, 'submitting', ?, ?, ?)
                    """,
                    (
                        signal_id,
                        expert_id,
                        symbol,
                        side,
                        volume,
                        execution_mode,
                        json.dumps(request, sort_keys=True, default=str),
                        now,
                        now,
                    ),
                )
                return True
            except sqlite3.IntegrityError:
                return False

    def complete(self, signal_id: str, state: str, result: Dict[str, Any]) -> None:
        now = datetime.now(timezone.utc).isoformat()
        with self._lock, self._connection() as conn:
            conn.execute(
                """
                UPDATE mt5_order_journal
                SET state = ?, result_json = ?, updated_at = ?
                WHERE signal_id = ?
                """,
                (state, json.dumps(result, sort_keys=True, default=str), now, signal_id),
            )

    def reconcile(
        self,
        signal_id: str,
        state: str,
        details: Dict[str, Any],
    ) -> None:
        existing = self.get(signal_id)
        if existing is None:
            return
        result = dict(existing.get("result") or {})
        result["reconciliation"] = details
        self.complete(signal_id, state, result)

    def get(self, signal_id: str) -> Optional[Dict[str, Any]]:
        with self._lock, self._connection() as conn:
            row = conn.execute(
                "SELECT * FROM mt5_order_journal WHERE signal_id = ?", (signal_id,)
            ).fetchone()
        return self._row_to_dict(row) if row else None

    def list_recent(self, limit: int = 50) -> List[Dict[str, Any]]:
        safe_limit = max(1, min(int(limit), 200))
        with self._lock, self._connection() as conn:
            rows = conn.execute(
                """
                SELECT * FROM mt5_order_journal
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (safe_limit,),
            ).fetchall()
        return [self._row_to_dict(row) for row in rows]

    def list_by_states(
        self,
        states: List[str],
        limit: int = 200,
    ) -> List[Dict[str, Any]]:
        normalized = [state.strip().lower() for state in states if state.strip()]
        if not normalized:
            return []
        placeholders = ",".join("?" for _ in normalized)
        safe_limit = max(1, min(int(limit), 500))
        with self._lock, self._connection() as conn:
            rows = conn.execute(
                f"""
                SELECT * FROM mt5_order_journal
                WHERE state IN ({placeholders})
                ORDER BY created_at ASC
                LIMIT ?
                """,
                (*normalized, safe_limit),
            ).fetchall()
        return [self._row_to_dict(row) for row in rows]

    def count_recent_executions(self, seconds: int = 60) -> int:
        cutoff = (
            datetime.now(timezone.utc) - timedelta(seconds=max(1, seconds))
        ).isoformat()
        with self._lock, self._connection() as conn:
            row = conn.execute(
                """
                SELECT COUNT(*) AS count
                FROM mt5_order_journal
                WHERE created_at >= ?
                  AND execution_mode IN ('paper', 'live')
                """,
                (cutoff,),
            ).fetchone()
        return int(row["count"] if row else 0)

    def set_control(self, key: str, value: Dict[str, Any]) -> Dict[str, Any]:
        now = datetime.now(timezone.utc).isoformat()
        with self._lock, self._connection() as conn:
            conn.execute(
                """
                INSERT INTO mt5_gateway_control (control_key, value_json, updated_at)
                VALUES (?, ?, ?)
                ON CONFLICT(control_key) DO UPDATE SET
                    value_json = excluded.value_json,
                    updated_at = excluded.updated_at
                """,
                (key, json.dumps(value, sort_keys=True, default=str), now),
            )
        return {**value, "updated_at": now}

    def get_control(self, key: str) -> Optional[Dict[str, Any]]:
        with self._lock, self._connection() as conn:
            row = conn.execute(
                """
                SELECT value_json, updated_at
                FROM mt5_gateway_control
                WHERE control_key = ?
                """,
                (key,),
            ).fetchone()
        if row is None:
            return None
        return {**json.loads(row["value_json"]), "updated_at": row["updated_at"]}

    @staticmethod
    def _row_to_dict(row: sqlite3.Row) -> Dict[str, Any]:
        item = dict(row)
        for key in ("request_json", "result_json"):
            value = item.pop(key, None)
            item[key.removesuffix("_json")] = json.loads(value) if value else None
        return item


mt5_gateway_journal = MT5GatewayJournal()
