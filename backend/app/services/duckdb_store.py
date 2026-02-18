"""
DuckDB Historical Data Store
Local OLAP database for storing and querying OHLCV candle data.
Supports millions of rows with sub-second queries.
"""

import os
import duckdb
from typing import List, Dict, Any, Optional
from datetime import datetime, date

DB_PATH = os.path.join(os.path.dirname(__file__), "../../data/market.duckdb")


class DuckDBStore:
    """Persistent DuckDB store for historical market data."""

    def __init__(self):
        # Ensure data directory exists
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.db_path = DB_PATH
        self._init_schema()

    def _get_conn(self):
        """Get a connection to the DuckDB database."""
        return duckdb.connect(self.db_path)

    def _init_schema(self):
        """Create tables if they don't exist."""
        conn = self._get_conn()
        try:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS ohlcv (
                    symbol      VARCHAR NOT NULL,
                    date        DATE NOT NULL,
                    open        DOUBLE,
                    high        DOUBLE,
                    low         DOUBLE,
                    close       DOUBLE,
                    volume      BIGINT,
                    source      VARCHAR,
                    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (symbol, date)
                )
            """)

            conn.execute("""
                CREATE TABLE IF NOT EXISTS universe (
                    symbol      VARCHAR PRIMARY KEY,
                    name        VARCHAR,
                    asset_type  VARCHAR,
                    sector      VARCHAR,
                    exchange    VARCHAR,
                    last_synced TIMESTAMP,
                    is_active   BOOLEAN DEFAULT TRUE
                )
            """)

            # Index for fast lookups
            conn.execute("CREATE INDEX IF NOT EXISTS idx_ohlcv_symbol ON ohlcv(symbol)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_ohlcv_date ON ohlcv(date)")
            print(f"[DuckDB] Schema initialized at {self.db_path}")
        finally:
            conn.close()

    def upsert_candles(self, symbol: str, candles: List[Dict[str, Any]], source: str = "unknown"):
        """
        Insert or update OHLCV candles for a symbol.
        Uses INSERT OR REPLACE to handle duplicates.
        """
        if not candles:
            return 0

        conn = self._get_conn()
        try:
            count = 0
            for c in candles:
                conn.execute("""
                    INSERT OR REPLACE INTO ohlcv (symbol, date, open, high, low, close, volume, source, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                """, [
                    symbol,
                    c.get("date"),
                    c.get("open"),
                    c.get("high"),
                    c.get("low"),
                    c.get("close"),
                    c.get("volume", 0),
                    source,
                ])
                count += 1
            print(f"[DuckDB] Upserted {count} candles for {symbol}")
            return count
        finally:
            conn.close()

    def get_history(self, symbol: str, limit: int = 300) -> List[Dict[str, Any]]:
        """
        Get historical OHLCV data for a symbol.
        Returns newest first, limited to `limit` rows.
        """
        conn = self._get_conn()
        try:
            result = conn.execute("""
                SELECT date, open, high, low, close, volume, source
                FROM ohlcv
                WHERE symbol = ?
                ORDER BY date DESC
                LIMIT ?
            """, [symbol, limit]).fetchall()

            return [
                {
                    "date": str(row[0]),
                    "open": row[1],
                    "high": row[2],
                    "low": row[3],
                    "close": row[4],
                    "volume": row[5],
                    "source": row[6],
                }
                for row in reversed(result)  # Return in chronological order
            ]
        finally:
            conn.close()

    def has_data(self, symbol: str, min_rows: int = 10) -> bool:
        """Check if we have enough historical data for a symbol."""
        conn = self._get_conn()
        try:
            count = conn.execute(
                "SELECT COUNT(*) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()[0]
            return count >= min_rows
        finally:
            conn.close()

    def get_latest_date(self, symbol: str) -> Optional[str]:
        """Get the most recent date we have data for."""
        conn = self._get_conn()
        try:
            result = conn.execute(
                "SELECT MAX(date) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()
            return str(result[0]) if result and result[0] else None
        finally:
            conn.close()

    def get_stats(self) -> Dict[str, Any]:
        """Get database statistics for monitoring."""
        conn = self._get_conn()
        try:
            total_candles = conn.execute("SELECT COUNT(*) FROM ohlcv").fetchone()[0]
            total_symbols = conn.execute("SELECT COUNT(DISTINCT symbol) FROM ohlcv").fetchone()[0]
            db_size_mb = os.path.getsize(self.db_path) / (1024 * 1024) if os.path.exists(self.db_path) else 0
            return {
                "total_candles": total_candles,
                "total_symbols": total_symbols,
                "db_size_mb": round(db_size_mb, 2),
            }
        finally:
            conn.close()

    def register_symbol(self, symbol: str, name: str = "", asset_type: str = "stock",
                         sector: str = "", exchange: str = ""):
        """Register a symbol in the universe tracker."""
        conn = self._get_conn()
        try:
            conn.execute("""
                INSERT OR REPLACE INTO universe (symbol, name, asset_type, sector, exchange, is_active)
                VALUES (?, ?, ?, ?, ?, TRUE)
            """, [symbol, name, asset_type, sector, exchange])
        finally:
            conn.close()

    def get_universe(self, asset_type: str = None) -> List[Dict[str, Any]]:
        """Get all symbols in the universe, optionally filtered by type."""
        conn = self._get_conn()
        try:
            if asset_type:
                result = conn.execute(
                    "SELECT * FROM universe WHERE asset_type = ? AND is_active = TRUE", [asset_type]
                ).fetchall()
            else:
                result = conn.execute(
                    "SELECT * FROM universe WHERE is_active = TRUE"
                ).fetchall()

            columns = ["symbol", "name", "asset_type", "sector", "exchange", "last_synced", "is_active"]
            return [dict(zip(columns, row)) for row in result]
        finally:
            conn.close()


# Singleton instance
duckdb_store = DuckDBStore()
