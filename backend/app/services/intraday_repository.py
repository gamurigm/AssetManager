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
import threading
import asyncio
import duckdb
import pandas as pd
from datetime import date
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

    async def fetch_intraday(
        self, symbol: str, interval: str, start: date, end: date
    ) -> List[CandleRow]:
        """Fetch candles (Local Cache -> Remote API -> Sync)."""
        ...


# --------------------------------------------------------------------------- #
#  Concrete Implementation — DuckDB                                            #
# --------------------------------------------------------------------------- #

_DB_PATH = os.path.join(os.path.dirname(__file__), "../../data/market2.duckdb")


class DuckDBIntradayRepository:
    """
    DuckDB-backed intraday repository.
    Stores M1/M5 candles in `ohlcv_intraday` table alongside the existing
    daily `ohlcv` table — same file, zero extra dependencies.
    """

    def __init__(self, db_path: str = _DB_PATH):
        self._db_path = db_path
        os.makedirs(os.path.dirname(self._db_path), exist_ok=True)
        self._initialized = False
        self._write_lock = threading.RLock()

    def _ensure_initialized(self):
        if not self._initialized:
            self._init_schema()
            self._initialized = True

    import contextlib
    import time

    @contextlib.contextmanager
    def _connection(self, retries: int = 50, delay: float = 0.1, read_only=False):
        """
        Returns a new DuckDB connection. Uses read_only when possible
        to avoid exclusive WAL lock contention with other processes.
        """
        last_exception = None
        for i in range(retries):
            try:
                conn = duckdb.connect(self._db_path, read_only=False)
                conn.execute("PRAGMA memory_limit='1GB'")
                conn.execute("PRAGMA threads=4")
                try:
                    yield conn
                finally:
                    conn.close()
                return
            except Exception as e:
                last_exception = e
                err_str = str(e).lower()
                if "used by another process" in err_str or "io error" in err_str or "locked" in err_str:
                    import time
                    time.sleep(delay)
                else:
                    raise e
        
        raise last_exception or Exception(f"Could not connect to DuckDB Intraday after retries.")

    def _init_schema(self) -> None:
        with self._connection() as conn:
            # PERFORMANCE PRAGMAS
            conn.execute("PRAGMA memory_limit='1GB'")
            conn.execute("PRAGMA threads=4")
            
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

    # ------------------------------------------------------------------ #
    #  Public Interface                                                    #
    # ------------------------------------------------------------------ #

    def save(self, symbol: str, interval: str, candles: List[CandleRow], source: str = "unknown") -> int:
        """Vectorized bulk upsert using pandas + DuckDB register. Handles 200k rows in ms."""
        self._ensure_initialized()
        if not candles:
            return 0

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

        with self._connection() as conn:
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

    def get(
        self,
        symbol: str,
        interval: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        limit: int = 500_000,
    ) -> List[CandleRow]:
        """Retrieve candles in chronological order."""
        self._ensure_initialized()
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
        with self._connection(read_only=True) as conn:
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

    def has_data(self, symbol: str, interval: str, start: str, end: str,
                 min_count: int = 10) -> bool:
        """
        Returns True if there are at least `min_count` candles in [start, end]
        for the given symbol+interval.
        """
        self._ensure_initialized()
        with self._connection(read_only=True) as conn:
            count = conn.execute(
                """
                SELECT COUNT(*) FROM ohlcv_intraday
                WHERE symbol = ? AND interval = ? AND ts >= ? AND ts <= ?
                """,
                [symbol, interval, start, end],
            ).fetchone()[0]
        return count >= min_count

    async def fetch_intraday(
        self, symbol: str, interval: str, start: date, end: date
    ) -> List[CandleRow]:
        """
        High-level orchestrator: RAM -> DuckDB -> Yahoo Finance Fallback -> DuckDB -> Return.
        """
        # 1. Local Cache Check
        # Convert date to timestamp strings for query
        start_ts = start.isoformat() + " 00:00:00"
        end_ts = end.isoformat() + " 23:59:59"

        if self.has_data(symbol, interval, start_ts, end_ts, min_count=20):
            print(f"[IntradayRepo] 🦆 Cache hit for {symbol} ({interval})")
            return self.get(symbol, interval, start_ts, end_ts)

        # 2. Yahoo Finance Fallback
        print(f"[IntradayRepo] ⚡ Cache miss for {symbol}. Syncing {interval} from Yahoo...")
        import yfinance as yf
        
        # Normalize symbol for Yahoo
        yf_sym = symbol
        if symbol == "BTC/USD": yf_sym = "BTC-USD"
        elif symbol == "ETH/USD": yf_sym = "ETH-USD"
        elif "/" in symbol: yf_sym = symbol.replace("/", "-")
        
        def _sync_fetch():
            ticker = yf.Ticker(yf_sym)
            # Use '1mo' period to get recent intraday if start/end are close
            return ticker.history(start=start, end=end, interval=interval)

        try:
            df = await asyncio.to_thread(_sync_fetch)
            if df.empty:
                print(f"[IntradayRepo] ⚠️ Yahoo returned no data for {symbol} ({interval})")
                return []
            
            # 3. Transform to CandleRow
            candles = []
            for ts, row in df.iterrows():
                candles.append(CandleRow(
                    timestamp=ts.strftime("%Y-%m-%dT%H:%M:%S") if hasattr(ts, 'strftime') else str(ts),
                    open=float(row["Open"]),
                    high=float(row["High"]),
                    low=float(row["Low"]),
                    close=float(row["Close"]),
                    volume=int(row.get("Volume", 0)),
                ))
            
            # 4. Persist and Return
            if candles:
                self.save(symbol, interval, candles, source="yahoo_sync")
            return candles

        except Exception as e:
            print(f"[IntradayRepo] ❌ Remote fetch failed for {symbol}: {e}")
            return []

    def get_stats(self) -> dict:
        """Diagnostic stats — mirrors DuckDBStore.get_stats()."""
        self._ensure_initialized()
        with self._connection(read_only=True) as conn:
            total = conn.execute("SELECT COUNT(*) FROM ohlcv_intraday").fetchone()[0]
            syms  = conn.execute("SELECT COUNT(DISTINCT symbol) FROM ohlcv_intraday").fetchone()[0]
        return {"total_intraday_candles": total, "total_symbols": syms}


# --------------------------------------------------------------------------- #
#  Singleton (same convention as the rest of the codebase)                    #
# --------------------------------------------------------------------------- #

intraday_repository: DuckDBIntradayRepository = DuckDBIntradayRepository()
