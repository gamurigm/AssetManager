"""
DuckDB Repository — Implements IHistoricalRepository.
Stores OHLCV data locally for instant chart loading.
"""

import os
import duckdb
from typing import List, Dict, Any, Optional
from ...domain.interfaces.data_repository import IHistoricalRepository
from ...domain.entities.market import Candle

DB_PATH = os.path.join(os.path.dirname(__file__), "../../../data/market.duckdb")


class DuckDBRepository(IHistoricalRepository):

    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.db_path = DB_PATH
        self._init_schema()

    def _conn(self):
        return duckdb.connect(self.db_path)

    def _init_schema(self):
        conn = self._conn()
        try:
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
        finally:
            conn.close()

    def has_data(self, symbol: str, min_rows: int = 10) -> bool:
        conn = self._conn()
        try:
            count = conn.execute(
                "SELECT COUNT(*) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()[0]
            return count >= min_rows
        finally:
            conn.close()

    def get_history(self, symbol: str, limit: int = 300) -> List[Candle]:
        conn = self._conn()
        try:
            rows = conn.execute("""
                SELECT date, open, high, low, close, volume
                FROM ohlcv WHERE symbol = ?
                ORDER BY date DESC LIMIT ?
            """, [symbol, limit]).fetchall()

            return [
                Candle(date=str(r[0]), open=r[1], high=r[2], low=r[3], close=r[4], volume=r[5] or 0)
                for r in reversed(rows)
            ]
        finally:
            conn.close()

    def upsert_candles(self, symbol: str, candles: List[Candle], source: str = "unknown") -> int:
        if not candles:
            return 0
        conn = self._conn()
        try:
            # Using executemany for performance
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
        finally:
            conn.close()

    def get_stats(self) -> Dict[str, Any]:
        conn = self._conn()
        try:
            total = conn.execute("SELECT COUNT(*) FROM ohlcv").fetchone()[0]
            symbols = conn.execute("SELECT COUNT(DISTINCT symbol) FROM ohlcv").fetchone()[0]
            size = os.path.getsize(self.db_path) / (1024 * 1024) if os.path.exists(self.db_path) else 0
            return {"total_candles": total, "total_symbols": symbols, "db_size_mb": round(size, 2)}
        finally:
            conn.close()

    def get_latest_date(self, symbol: str) -> Optional[str]:
        conn = self._conn()
        try:
            res = conn.execute(
                "SELECT CAST(MAX(date) AS VARCHAR) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()
            return res[0] if res and res[0] else None
        finally:
            conn.close()

    def get_count(self, symbol: str) -> int:
        conn = self._conn()
        try:
            res = conn.execute(
                "SELECT COUNT(*) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()
            return res[0] if res else 0
        finally:
            conn.close()

