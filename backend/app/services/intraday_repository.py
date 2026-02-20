"""
Intraday Repository — SOLID / Repository Pattern
=================================================
IIntradayRepository (Protocol) defines the contract.
DuckDBIntradayRepository is the concrete implementation backed by DuckDB.

Design:
  - S: Sole responsibility is persisting/querying intraday candles.
  - O: New storage backends (InfluxDB, Parquet) implement IIntradayRepository without touching callers.
  - L: Any implementation is a drop-in replacement.
  - I: Minimal interface — only what BacktestRunner and SimulationService actually need.
  - D: Callers depend on IIntradayRepository, not DuckDBIntradayRepository.
"""

from __future__ import annotations

import os
import duckdb
import pandas as pd
from typing import Protocol, List, TypedDict, Optional, runtime_checkable


# --------------------------------------------------------------------------- #
#  Value type for raw candle rows                                              #
# --------------------------------------------------------------------------- #

class CandleRow(TypedDict):
    timestamp: str       # ISO 8601: "2025-11-01T09:30:00"
    open: float
    high: float
    low: float
    close: float
    volume: int


# --------------------------------------------------------------------------- #
#  Interface (Protocol = structural subtyping, no ABC overhead)                #
# --------------------------------------------------------------------------- #

@runtime_checkable
class IIntradayRepository(Protocol):
    """Contract for intraday candle persistence. ISP: only what is needed."""

    def save(self, symbol: str, interval: str, candles: List[CandleRow], source: str = "unknown") -> int:
        """Persist candles; return number of rows upserted."""
        ...

    def get(
        self,
        symbol: str,
        interval: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        limit: int = 10_000,
    ) -> List[CandleRow]:
        """Retrieve candles in chronological order."""
        ...

    def has_data(self, symbol: str, interval: str, start: str, end: str) -> bool:
        """Check whether sufficient data already exists (avoids redundant downloads)."""
        ...


# --------------------------------------------------------------------------- #
#  Concrete Implementation — DuckDB                                            #
# --------------------------------------------------------------------------- #

_DB_PATH = os.path.join(os.path.dirname(__file__), "../../data/market.duckdb")


class DuckDBIntradayRepository:
    """
    DuckDB-backed intraday repository.
    Stores M1/M5 candles in `ohlcv_intraday` table alongside the existing
    daily `ohlcv` table — same file, zero extra dependencies.
    """

    def __init__(self, db_path: str = _DB_PATH):
        self._db_path = db_path
        os.makedirs(os.path.dirname(self._db_path), exist_ok=True)
        self._init_schema()

    # ------------------------------------------------------------------ #
    #  Private helpers                                                     #
    # ------------------------------------------------------------------ #

    def _conn(self) -> duckdb.DuckDBPyConnection:
        return duckdb.connect(self._db_path)

    def _init_schema(self) -> None:
        conn = self._conn()
        try:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS ohlcv_intraday (
                    symbol    VARCHAR      NOT NULL,
                    ts        TIMESTAMP    NOT NULL,
                    interval  VARCHAR      NOT NULL,
                    open      DOUBLE,
                    high      DOUBLE,
                    low       DOUBLE,
                    close     DOUBLE,
                    volume    BIGINT,
                    source    VARCHAR,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (symbol, ts, interval)
                )
            """)
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_intraday_sym_ts "
                "ON ohlcv_intraday(symbol, ts)"
            )
        finally:
            conn.close()

    # ------------------------------------------------------------------ #
    #  Public Interface                                                    #
    # ------------------------------------------------------------------ #

    def save(self, symbol: str, interval: str, candles: List[CandleRow], source: str = "unknown") -> int:
        """Vectorized bulk upsert using pandas + DuckDB register. Handles 200k rows in ms."""
        if not candles:
            return 0

        # Build DataFrame — native types only (no dicts)
        df = pd.DataFrame({
            "symbol":   symbol,
            "ts":       pd.to_datetime([c["timestamp"] for c in candles]),
            "interval": interval,
            "open":     [c.get("open")    for c in candles],
            "high":     [c.get("high")    for c in candles],
            "low":      [c.get("low")     for c in candles],
            "close":    [c.get("close")   for c in candles],
            "volume":   [c.get("volume", 0) for c in candles],
            "source":   source,
        })

        conn = self._conn()
        try:
            conn.register("_df_batch", df)
            conn.execute("""
                INSERT OR REPLACE INTO ohlcv_intraday
                    (symbol, ts, interval, open, high, low, close, volume, source, updated_at)
                SELECT symbol, ts, interval, open, high, low, close, volume, source,
                       CURRENT_TIMESTAMP
                FROM _df_batch
            """)
            conn.unregister("_df_batch")
            count = len(df)
            print(f"[IntradayRepo] Bulk Upserted {count} {interval} candles for {symbol} (vectorized)")
            return count
        finally:
            conn.close()

    def get(
        self,
        symbol: str,
        interval: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        limit: int = 500_000,
    ) -> List[CandleRow]:
        """Retrieve candles in chronological order."""
        conn = self._conn()
        try:
            where_clauses = ["symbol = ?", "interval = ?"]
            params: list = [symbol, interval]

            if start:
                where_clauses.append("ts >= ?")
                params.append(start)
            if end:
                where_clauses.append("ts <= ?")
                params.append(end)

            params.append(limit)
            sql = f"""
                SELECT ts, open, high, low, close, volume
                FROM ohlcv_intraday
                WHERE {" AND ".join(where_clauses)}
                ORDER BY ts ASC
                LIMIT ?
            """
            rows = conn.execute(sql, params).fetchall()
            return [
                CandleRow(
                    timestamp=str(row[0]),
                    open=row[1],
                    high=row[2],
                    low=row[3],
                    close=row[4],
                    volume=row[5],
                )
                for row in rows
            ]
        finally:
            conn.close()

    def has_data(self, symbol: str, interval: str, start: str, end: str) -> bool:
        """
        Returns True if there are any candles in [start, end] for the given
        symbol+interval.  Threshold: at least 10 rows (avoids treating a
        partial/corrupt download as 'complete').
        """
        conn = self._conn()
        try:
            count = conn.execute(
                """
                SELECT COUNT(*) FROM ohlcv_intraday
                WHERE symbol = ? AND interval = ? AND ts >= ? AND ts <= ?
                """,
                [symbol, interval, start, end],
            ).fetchone()[0]
            return count >= 10
        finally:
            conn.close()

    def get_stats(self) -> dict:
        """Diagnostic stats — mirrors DuckDBStore.get_stats()."""
        conn = self._conn()
        try:
            total = conn.execute("SELECT COUNT(*) FROM ohlcv_intraday").fetchone()[0]
            syms  = conn.execute("SELECT COUNT(DISTINCT symbol) FROM ohlcv_intraday").fetchone()[0]
            return {"total_intraday_candles": total, "total_symbols": syms}
        finally:
            conn.close()


# --------------------------------------------------------------------------- #
#  Singleton (same convention as the rest of the codebase)                    #
# --------------------------------------------------------------------------- #

intraday_repository: DuckDBIntradayRepository = DuckDBIntradayRepository()
