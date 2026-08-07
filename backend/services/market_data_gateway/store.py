"""Single-writer tick store with a transactional Kafka outbox."""

from __future__ import annotations

from pathlib import Path
from threading import RLock

import duckdb

from services.contracts.events import MarketTickV1


class MarketDataStore:
    def __init__(self, db_path: str | Path) -> None:
        self.db_path = str(Path(db_path).resolve())
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        self._lock = RLock()
        self._initialize()

    def _connect(self):
        return duckdb.connect(self.db_path)

    def _initialize(self) -> None:
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS market_ticks_v1 (
                        event_id VARCHAR PRIMARY KEY,
                        symbol VARCHAR NOT NULL,
                        price DOUBLE NOT NULL,
                        volume DOUBLE NOT NULL,
                        observed_at TIMESTAMPTZ NOT NULL,
                        source VARCHAR NOT NULL,
                        received_at TIMESTAMPTZ NOT NULL
                    )
                    """
                )
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS market_outbox_v1 (
                        event_id VARCHAR PRIMARY KEY,
                        topic VARCHAR NOT NULL,
                        event_json VARCHAR NOT NULL,
                        created_at TIMESTAMPTZ NOT NULL,
                        published_at TIMESTAMPTZ
                    )
                    """
                )
            finally:
                conn.close()
    def record_tick(self, event: MarketTickV1) -> bool:
        """Persist tick and event atomically; duplicate event IDs are harmless."""
        with self._lock:
            conn = self._connect()
            try:
                conn.execute("BEGIN TRANSACTION")
                exists = conn.execute(
                    "SELECT 1 FROM market_ticks_v1 WHERE event_id = ?",
                    [event.event_id],
                ).fetchone()
                if exists:
                    conn.execute("ROLLBACK")
                    return False
                conn.execute(
                    """
                    INSERT INTO market_ticks_v1
                        (event_id, symbol, price, volume, observed_at, source, received_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    [
                        event.event_id,
                        event.symbol,
                        event.price,
                        event.volume,
                        event.observed_at,
                        event.source,
                        event.occurred_at,
                    ],
                )
                conn.execute(
                    """
                    INSERT INTO market_outbox_v1
                        (event_id, topic, event_json, created_at, published_at)
                    VALUES (?, 'market.ticks.v1', ?, ?, NULL)
                    """,
                    [event.event_id, event.model_dump_json(), event.occurred_at],
                )
                conn.execute("COMMIT")
                return True
            except Exception:
                conn.execute("ROLLBACK")
                raise
            finally:
                conn.close()

    def pending_events(self, limit: int = 100) -> list[MarketTickV1]:
        safe_limit = max(1, min(int(limit), 10_000))
        with self._lock:
            conn = self._connect()
            try:
                rows = conn.execute(
                    """
                    SELECT event_json
                    FROM market_outbox_v1
                    WHERE published_at IS NULL
                    ORDER BY created_at, event_id
                    LIMIT ?
                    """,
                    [safe_limit],
                ).fetchall()
            finally:
                conn.close()
        return [MarketTickV1.model_validate_json(row[0]) for row in rows]

    def mark_published(self, event_id: str) -> None:
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    UPDATE market_outbox_v1
                    SET published_at = CURRENT_TIMESTAMP
                    WHERE event_id = ? AND published_at IS NULL
                    """,
                    [event_id],
                )
            finally:
                conn.close()
