"""
DuckDB Repository — Implements IHistoricalRepository.
Stores OHLCV data locally for instant chart loading.

PERFORMANCE: Fast transient connections (no persistent lock).
Write operations use a threading.Lock to serialize.
Windows-safe: no persistent file lock that blocks other modules.
"""

import os
import time
import threading
import duckdb
from typing import List, Dict, Any, Optional
from ...domain.interfaces.data_repository import IHistoricalRepository
from ...domain.entities.market import Candle

DB_PATH = os.path.join(os.path.dirname(__file__), "../../../data/market.duckdb")


class DuckDBRepository(IHistoricalRepository):

    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.db_path = DB_PATH
        self._write_lock = threading.Lock()
        self._init_schema()

    def _connect(self, read_only=False, retries=5, delay=0.2):
        """Fast transient connection with minimal retries."""
        for i in range(retries):
            try:
                return duckdb.connect(self.db_path, read_only=read_only)
            except Exception as e:
                if i < retries - 1 and ("used by another process" in str(e).lower() or "io error" in str(e).lower()):
                    time.sleep(delay)
                else:
                    raise
        raise Exception(f"Could not connect to DuckDB after {retries} retries")

    def _init_schema(self):
        conn = self._connect()
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
            
            # Persistent Portfolio / Holdings Table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS portfolio (
                    symbol VARCHAR PRIMARY KEY,
                    name VARCHAR,
                    shares DOUBLE,
                    entry_price DOUBLE,
                    factor DOUBLE,
                    sector VARCHAR,
                    asset_type VARCHAR,
                    purchase_date VARCHAR,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            # Migration: Add purchase_date if missing
            cols = conn.execute("PRAGMA table_info('portfolio')").fetchall()
            if not any(c[1] == 'purchase_date' for c in cols):
                conn.execute("ALTER TABLE portfolio ADD COLUMN purchase_date VARCHAR DEFAULT '2024-01-01'")

            # Transactions History Table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    type VARCHAR,
                    symbol VARCHAR,
                    shares DOUBLE,
                    price DOUBLE,
                    realized_pnl DOUBLE DEFAULT 0,
                    date VARCHAR,
                    time VARCHAR,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Equity Snapshots Table (Realized vs Total)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS equity_snapshots (
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    realized_balance DOUBLE,
                    total_equity DOUBLE
                )
            """)

            # Initial Seed: If empty, start with 1200 from 2 years ago
            res = conn.execute("SELECT COUNT(*) FROM equity_snapshots").fetchone()
            if res[0] == 0:
                conn.execute("""
                    INSERT INTO equity_snapshots (timestamp, realized_balance, total_equity)
                    VALUES (CURRENT_TIMESTAMP - INTERVAL '2 year', 1200, 1200)
                """)
        finally:
            conn.close()

    def has_data(self, symbol: str, min_rows: int = 10) -> bool:
        conn = self._connect(read_only=True)
        try:
            count = conn.execute(
                "SELECT COUNT(*) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()[0]
            return count >= min_rows
        finally:
            conn.close()

    def get_history(self, symbol: str, limit: int = 300) -> List[Candle]:
        conn = self._connect(read_only=True)
        try:
            rows = conn.execute("""
                SELECT date, open, high, low, close, volume
                FROM ohlcv WHERE symbol = ?
                ORDER BY date DESC LIMIT ?
            """, [symbol, limit]).fetchall()
        finally:
            conn.close()

        return [
            Candle(date=str(r[0]), open=r[1], high=r[2], low=r[3], close=r[4], volume=r[5] or 0)
            for r in reversed(rows)
        ]

    def upsert_candles(self, symbol: str, candles: List[Candle], source: str = "unknown") -> int:
        if not candles:
            return 0

        with self._write_lock:
            conn = self._connect(read_only=False)
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
            finally:
                conn.close()

    def get_stats(self) -> Dict[str, Any]:
        conn = self._connect(read_only=True)
        try:
            total = conn.execute("SELECT COUNT(*) FROM ohlcv").fetchone()[0]
            symbols = conn.execute("SELECT COUNT(DISTINCT symbol) FROM ohlcv").fetchone()[0]
        finally:
            conn.close()
        size = os.path.getsize(self.db_path) / (1024 * 1024) if os.path.exists(self.db_path) else 0
        return {"total_candles": total, "total_symbols": symbols, "db_size_mb": round(size, 2)}

    def get_latest_date(self, symbol: str) -> Optional[str]:
        conn = self._connect(read_only=True)
        try:
            res = conn.execute(
                "SELECT CAST(MAX(date) AS VARCHAR) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()
        finally:
            conn.close()
        return res[0] if res and res[0] else None

    def get_count(self, symbol: str) -> int:
        conn = self._connect(read_only=True)
        try:
            res = conn.execute(
                "SELECT COUNT(*) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()
        finally:
            conn.close()
        return res[0] if res else 0

    # --- Portfolio Persistence ---

    def save_portfolio(self, holdings: List[Dict[str, Any]]):
        """Save current holdings. Replaces entire portfolio table to match current state."""
        with self._write_lock:
            conn = self._connect(read_only=False)
            try:
                conn.execute("DELETE FROM portfolio")
                if holdings:
                    data = [
                        (h['symbol'], h['name'], h['shares'], h['entryPrice'], h['factor'], h['sector'], h['type'], h.get('purchaseDate', '2024-01-01'))
                        for h in holdings
                    ]
                    conn.executemany("""
                        INSERT INTO portfolio (symbol, name, shares, entry_price, factor, sector, asset_type, purchase_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """, data)
                return True
            except Exception as e:
                print(f"[DuckDB] Portfolio save error: {e}")
                return False
            finally:
                conn.close()

    def get_portfolio(self) -> List[Dict[str, Any]]:
        """Retrieve current holdings from storage."""
        conn = self._connect(read_only=True)
        try:
            rows = conn.execute("""
                SELECT symbol, name, shares, entry_price, factor, sector, asset_type, purchase_date
                FROM portfolio
            """).fetchall()
            return [
                {
                    "symbol": r[0], "name": r[1], "shares": r[2], 
                    "entryPrice": r[3], "factor": r[4], "sector": r[5], 
                    "type": r[6], "purchaseDate": r[7]
                }
                for r in rows
            ]
        except Exception as e:
            print(f"[DuckDB] Portfolio load error: {e}")
            return []
        finally:
            conn.close()

    def add_transaction(self, type_str: str, symbol: str, shares: float, price: float, realized_pnl: float = 0):
        """Record a single transaction."""
        from datetime import datetime
        with self._write_lock:
            conn = self._connect(read_only=False)
            try:
                # Simple auto-increment ID
                res = conn.execute("SELECT MAX(id) FROM transactions").fetchone()
                max_id = res[0] if res and res[0] is not None else 0
                new_id = max_id + 1
                
                now = datetime.now()
                date_str = now.strftime("%Y-%m-%d")
                time_str = now.strftime("%I:%M %p")
                
                conn.execute("""
                    INSERT INTO transactions (id, type, symbol, shares, price, realized_pnl, date, time)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, [new_id, type_str, symbol, shares, price, realized_pnl, date_str, time_str])
                return True
            except Exception as e:
                print(f"[DuckDB] Transaction error: {e}")
                return False
            finally:
                conn.close()

    def get_transactions(self) -> List[Dict[str, Any]]:
        """Retrieve all transactions."""
        conn = self._connect(read_only=True)
        try:
            rows = conn.execute("""
                SELECT type, symbol, shares, price, realized_pnl, date, time
                FROM transactions
                ORDER BY timestamp ASC
            """).fetchall()
            return [
                {
                    "type": r[0], "symbol": r[1], "shares": r[2], 
                    "price": r[3], "realized_pnl": r[4], "date": str(r[5]), "time": r[6]
                }
                for r in rows
            ]
        except Exception as e:
            print(f"[DuckDB] Transaction load error: {e}")
            return []
        finally:
            conn.close()

    # --- Equity & Performance History ---

    def get_total_realized_pnl(self) -> float:
        """Sum up all realized_pnl from transactions."""
        conn = self._connect(read_only=True)
        try:
            res = conn.execute("SELECT SUM(realized_pnl) FROM transactions").fetchone()
            return res[0] if res and res[0] is not None else 0.0
        except Exception as e:
            print(f"[DuckDB] Realized PnL error: {e}")
            return 0.0
        finally:
            conn.close()

    def record_equity_snapshot(self, total_equity: float):
        """Record a snapshot of both realized balance and total equity."""
        # Calculate current realized balance (Seed 1200 + sum of all gains/losses)
        realized_gains = self.get_total_realized_pnl()
        current_realized_balance = 1200 + realized_gains
        
        with self._write_lock:
            conn = self._connect(read_only=False)
            try:
                conn.execute("""
                    INSERT INTO equity_snapshots (realized_balance, total_equity)
                    VALUES (?, ?)
                """, [current_realized_balance, total_equity])
                return True
            except Exception as e:
                print(f"[DuckDB] Equity snapshot error: {e}")
                return False
            finally:
                conn.close()

    def get_equity_history(self) -> List[Dict[str, Any]]:
        """Retrieve full history of realized vs total equity."""
        conn = self._connect(read_only=True)
        try:
            rows = conn.execute("""
                SELECT epoch(timestamp), realized_balance, total_equity
                FROM equity_snapshots
                ORDER BY timestamp ASC
            """).fetchall()
            return [
                {
                    "time": int(r[0]), 
                    "realized": r[1],
                    "total": r[2]
                } for r in rows
            ]
        except Exception as e:
            print(f"[DuckDB] Equity history load error: {e}")
            return []
        finally:
            conn.close()
