"""
DuckDB Repository — Implements IHistoricalRepository.
Stores OHLCV data locally for instant chart loading.
"""

import os
import time
import duckdb
import contextlib
from typing import List, Dict, Any, Optional
from ...domain.interfaces.data_repository import IHistoricalRepository
from ...domain.entities.market import Candle

DB_PATH = os.path.join(os.path.dirname(__file__), "../../../data/market.duckdb")

class DuckDBRepository(IHistoricalRepository):
    
    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.db_path = DB_PATH
        self._init_schema()

    @contextlib.contextmanager
    def _connection(self, retries: int = 50, delay: float = 0.1, read_only=False):
        """Creates a transient connection with file-system lock retries."""
        conn = None
        last_exception = None
        for i in range(retries):
            try:
                conn = duckdb.connect(self.db_path, read_only=read_only)
                break
            except Exception as e:
                last_exception = e
                err_str = str(e).lower()
                if "used by another process" in err_str or "io error" in err_str:
                    time.sleep(delay)
                else:
                    raise e
        
        if conn is None:
            raise last_exception or Exception(f"Could not connect to DuckDB (read_only={read_only}) after retries.")

        try:
            yield conn
        finally:
            if conn:
                conn.close()

    def _init_schema(self):
        with self._connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS ohlcv (
                    symbol VARCHAR NOT NULL, date DATE NOT NULL,
                    open DOUBLE, high DOUBLE, low DOUBLE, close DOUBLE,
                    volume BIGINT, source VARCHAR,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (symbol, date)
                )
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_ohlcv_sym ON ohlcv(symbol)")

    def has_data(self, symbol: str, min_rows: int = 10) -> bool:
        with self._connection(read_only=True) as conn:
            count = conn.execute(
                "SELECT COUNT(*) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()[0]
            return count >= min_rows

    def get_history(self, symbol: str, limit: int = 300) -> List[Candle]:
        with self._connection(read_only=True) as conn:
            rows = conn.execute("""
                SELECT date, open, high, low, close, volume
                FROM ohlcv WHERE symbol = ?
                ORDER BY date DESC LIMIT ?
            """, [symbol, limit]).fetchall()

            return [
                Candle(date=str(r[0]), open=r[1], high=r[2], low=r[3], close=r[4], volume=r[5] or 0)
                for r in reversed(rows)
            ]

    def upsert_candles(self, symbol: str, candles: List[Candle], source: str = "unknown") -> int:
        if not candles:
            return 0
        
        with self._connection() as conn:
            try:
                data = [
                    (symbol, c.date, c.open, c.high, c.low, c.close, c.volume, source)
                    for c in candles
                ]
                conn.executemany("""
                    INSERT OR REPLACE INTO ohlcv (symbol, date, open, high, low, close, volume, source, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                """, data)
                return len(candles)
            except Exception as e:
                print(f"[DuckDB] Upsert error for {symbol}: {e}")
                return 0

    def get_stats(self) -> Dict[str, Any]:
        with self._connection(read_only=True) as conn:
            total = conn.execute("SELECT COUNT(*) FROM ohlcv").fetchone()[0]
            symbols = conn.execute("SELECT COUNT(DISTINCT symbol) FROM ohlcv").fetchone()[0]
        size = os.path.getsize(self.db_path) / (1024 * 1024) if os.path.exists(self.db_path) else 0
        return {"total_candles": total, "total_symbols": symbols, "db_size_mb": round(size, 2)}

    def get_latest_date(self, symbol: str) -> Optional[str]:
        with self._connection(read_only=True) as conn:
            res = conn.execute(
                "SELECT CAST(MAX(date) AS VARCHAR) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()
            return res[0] if res and res[0] else None

    def get_count(self, symbol: str) -> int:
        with self._connection(read_only=True) as conn:
            res = conn.execute(
                "SELECT COUNT(*) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()
            return res[0] if res else 0


