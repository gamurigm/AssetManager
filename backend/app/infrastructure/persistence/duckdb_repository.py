"""
DuckDB Repository — Implements IHistoricalRepository.
Stores OHLCV data locally for instant chart loading.

PERFORMANCE: Fast transient connections (no persistent lock).
Write operations use a threading.RLock to serialize.
Windows-safe: no persistent file lock that blocks other modules.
"""

import os
import time
import threading
import duckdb
from typing import List, Dict, Any, Optional
from ...domain.interfaces.data_repository import IHistoricalRepository
from ...domain.interfaces.portfolio_repository import IPortfolioRepository
from ...domain.entities.market import Candle

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../data/market.duckdb"))


class DuckDBRepository(IHistoricalRepository, IPortfolioRepository):

    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.db_path = DB_PATH
        self._write_lock = threading.RLock()
        self._initialized = False
        try:
            self._ensure_initialized()
        except duckdb.IOException as exc:
            if self._is_lock_error(exc):
                print("[DuckDB] Database locked during startup; schema initialization deferred.")
            else:
                raise

    @staticmethod
    def _is_lock_error(exc: Exception) -> bool:
        message = str(exc).lower()
        return (
            "used by another process" in message
            or "cannot access the file" in message
            or "io error" in message
            or "database is locked" in message
        )

    def _open_connection(self, read_only: bool = False, retries: int = 30, delay: float = 0.15):
        """
        Returns a new DuckDB connection, always in read-write mode.

        NOTE: On Windows, DuckDB read_only=True still requires exclusive WAL
        access and will conflict with any concurrent writer connection, causing
        IOException.  We therefore ALWAYS open in read-write mode and rely on
        _write_lock to serialise mutations.  The read_only parameter is accepted
        but intentionally ignored so callers need no changes.
        """
        last_exc: Optional[Exception] = None
        for attempt in range(retries):
            try:
                conn = duckdb.connect(self.db_path, read_only=False)
                conn.execute("PRAGMA memory_limit='1GB'")
                conn.execute("PRAGMA threads=4")
                return conn
            except duckdb.IOException as exc:
                last_exc = exc
                if self._is_lock_error(exc):
                    time.sleep(delay)
                    continue
                raise

        if last_exc:
            raise last_exc  # type: ignore
        raise RuntimeError("Could not connect to DuckDB")

    def _ensure_initialized(self):
        if self._initialized:
            return
        with self._write_lock:
            if self._initialized:
                return
            self._init_schema()
            self._initialized = True

    def _connect(self, read_only=False):
        """
        Retrieve a DuckDB connection (always read-write; see _open_connection).
        """
        self._ensure_initialized()
        return self._open_connection(read_only=False)

    def _init_schema(self):
        conn = self._open_connection(read_only=False)
        try:
            # Pragmas are now handled in _open_init during connection creation
            
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
                    portfolio_id VARCHAR DEFAULT 'main',
                    symbol VARCHAR,
                    name VARCHAR,
                    shares DOUBLE,
                    entry_price DOUBLE,
                    factor DOUBLE,
                    sector VARCHAR,
                    asset_type VARCHAR,
                    purchase_date VARCHAR,
                    sl DOUBLE,
                    tp DOUBLE,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (portfolio_id, symbol)
                )
            """)
            # Migration: Add purchase_date if missing, and migrate to multi-portfolio format
            cols = conn.execute("PRAGMA table_info('portfolio')").fetchall()
            col_names = [c[1] for c in cols]
            
            # Simple column additions for older DBs before multi-portfolio
            if 'purchase_date' not in col_names and 'sl' not in col_names:
                conn.execute("ALTER TABLE portfolio ADD COLUMN purchase_date VARCHAR DEFAULT '2024-01-01'")
                conn.execute("ALTER TABLE portfolio ADD COLUMN sl DOUBLE")
                conn.execute("ALTER TABLE portfolio ADD COLUMN tp DOUBLE")
                
            # Upgrading to multi-portfolio format
            cols = conn.execute("PRAGMA table_info('portfolio')").fetchall()
            col_names = [c[1] for c in cols]
            if 'portfolio_id' not in col_names:
                conn.execute("ALTER TABLE portfolio RENAME TO portfolio_old")
                conn.execute("""
                    CREATE TABLE portfolio (
                        portfolio_id VARCHAR DEFAULT 'main',
                        symbol VARCHAR,
                        name VARCHAR,
                        shares DOUBLE,
                        entry_price DOUBLE,
                        factor DOUBLE,
                        sector VARCHAR,
                        asset_type VARCHAR,
                        purchase_date VARCHAR,
                        sl DOUBLE,
                        tp DOUBLE,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        PRIMARY KEY (portfolio_id, symbol)
                    )
                """)
                conn.execute("""
                    INSERT INTO portfolio (portfolio_id, symbol, name, shares, entry_price, factor, sector, asset_type, purchase_date, sl, tp)
                    SELECT 'main', symbol, name, shares, entry_price, factor, sector, asset_type, purchase_date, sl, tp FROM portfolio_old
                """)
                conn.execute("DROP TABLE portfolio_old")

            # Transactions History Table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    portfolio_id VARCHAR DEFAULT 'main',
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
            
            # Migration: Add missing columns to transactions
            cols_t = conn.execute("PRAGMA table_info('transactions')").fetchall()
            existing_t = [c[1] for c in cols_t]
            if 'type' not in existing_t:
                conn.execute("ALTER TABLE transactions ADD COLUMN type VARCHAR")
            if 'symbol' not in existing_t:
                conn.execute("ALTER TABLE transactions ADD COLUMN symbol VARCHAR")
            if 'shares' not in existing_t:
                conn.execute("ALTER TABLE transactions ADD COLUMN shares DOUBLE")
            if 'realized_pnl' not in existing_t:
                conn.execute("ALTER TABLE transactions ADD COLUMN realized_pnl DOUBLE DEFAULT 0")
            if 'date' not in existing_t:
                conn.execute("ALTER TABLE transactions ADD COLUMN date VARCHAR")
            if 'time' not in existing_t:
                conn.execute("ALTER TABLE transactions ADD COLUMN time VARCHAR")
            if 'portfolio_id' not in existing_t:
                conn.execute("ALTER TABLE transactions ADD COLUMN portfolio_id VARCHAR DEFAULT 'main'")

            # Equity Snapshots Table (Realized vs Total)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS equity_snapshots (
                    portfolio_id VARCHAR DEFAULT 'main',
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    realized_balance DOUBLE,
                    total_equity DOUBLE
                )
            """)
            
            cols_e = conn.execute("PRAGMA table_info('equity_snapshots')").fetchall()
            existing_e = [c[1] for c in cols_e]
            if 'portfolio_id' not in existing_e:
                conn.execute("ALTER TABLE equity_snapshots ADD COLUMN portfolio_id VARCHAR DEFAULT 'main'")

            # Insider Trading Table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS insider_trading (
                    ticker VARCHAR NOT NULL,
                    owner VARCHAR NOT NULL,
                    relationship VARCHAR,
                    trade_date DATE NOT NULL,
                    transaction VARCHAR,
                    cost DOUBLE,
                    shares BIGINT,
                    value DOUBLE,
                    shares_total BIGINT,
                    sec_form_4 VARCHAR,
                    sec_url VARCHAR,
                    type VARCHAR,
                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (ticker, owner, trade_date, transaction, shares, value)
                )
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_insider_ticker ON insider_trading(ticker)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_insider_date ON insider_trading(trade_date)")

            conn.execute("""
                CREATE TABLE IF NOT EXISTS asset_classifications (
                    symbol VARCHAR NOT NULL,
                    benchmark VARCHAR DEFAULT 'SPY',
                    asset_type VARCHAR,
                    sector VARCHAR,
                    sector_etf VARCHAR,
                    industry_group VARCHAR,
                    industry VARCHAR,
                    sub_industry VARCHAR,
                    company_name VARCHAR,
                    source VARCHAR,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (symbol, benchmark)
                )
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_asset_classifications_symbol ON asset_classifications(symbol)")

            # Initial Seed: If empty, start with 1200 from 2 years ago for 'main'
            res = conn.execute("SELECT COUNT(*) FROM equity_snapshots").fetchone()
            if res[0] == 0:
                conn.execute("""
                    INSERT INTO equity_snapshots (portfolio_id, timestamp, realized_balance, total_equity)
                    VALUES ('main', CURRENT_TIMESTAMP - INTERVAL '2 year', 1200, 1200)
                """)
            
            # --- REAL-TIME DATA LAKE ---
            conn.execute("""
                CREATE TABLE IF NOT EXISTS market_ticks (
                    symbol VARCHAR NOT NULL,
                    price DOUBLE NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    source VARCHAR,
                    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_ticks_sym_ts ON market_ticks(symbol, timestamp)")
            
        finally:
            conn.close()

    def has_data(self, symbol: str, min_rows: int = 10) -> bool:
        conn = self._connect(read_only=True)
        try:
            count = conn.execute(
                "SELECT COUNT(*) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()[0]
            return count >= min_rows
        except Exception:
            return False
        finally:
            conn.close()
        return False

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

    def get_history_range(self, symbol: str, start_date: str, end_date: str) -> List[Candle]:
        """Return daily candles for a symbol within an inclusive date range."""
        conn = self._connect(read_only=True)
        try:
            rows = conn.execute("""
                SELECT date, open, high, low, close, volume
                FROM ohlcv
                WHERE symbol = ?
                  AND date >= ?
                  AND date <= ?
                ORDER BY date ASC
            """, [symbol, start_date, end_date]).fetchall()
        finally:
            conn.close()

        return [
            Candle(date=str(r[0]), open=r[1], high=r[2], low=r[3], close=r[4], volume=r[5] or 0)
            for r in rows
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
        return 0

    def save_tick(self, symbol: str, price: float, timestamp: Any, source: str = "unknown"):
        """Save a single real-time tick to the data lake."""
        with self._write_lock:
            conn = self._connect(read_only=False)
            try:
                conn.execute("""
                    INSERT INTO market_ticks (symbol, price, timestamp, source)
                    VALUES (?, ?, ?, ?)
                """, [symbol, price, timestamp, source])
                return True
            except Exception as e:
                print(f"[DuckDB] Tick save error for {symbol}: {e}")
                return False
            finally:
                conn.close()

    def get_stats(self) -> Dict[str, Any]:
        conn = self._connect(read_only=True)
        try:
            total = conn.execute("SELECT COUNT(*) FROM ohlcv").fetchone()[0]
            symbols = conn.execute("SELECT COUNT(DISTINCT symbol) FROM ohlcv").fetchone()[0]
        finally:
            conn.close()
        size = float(os.path.getsize(self.db_path)) / (1024 * 1024) if os.path.exists(self.db_path) else 0.0
        return {"total_candles": total, "total_symbols": symbols, "db_size_mb": round(size, 2)}  # type: ignore

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

    def get_last_sync_time(self, symbol: str) -> Optional[float]:
        conn = self._connect(read_only=True)
        try:
            res = conn.execute(
                "SELECT CAST(MAX(epoch(updated_at)) AS DOUBLE) FROM ohlcv WHERE symbol = ?", [symbol]
            ).fetchone()
        finally:
            conn.close()
        return res[0] if res and res[0] else None

    # --- Portfolio Persistence ---

    def save_portfolio(self, holdings: List[Dict[str, Any]], portfolio_id: str = "main"):
        """Save current holdings for a specific portfolio. Replaces entire portfolio subset."""
        with self._write_lock:
            conn = self._connect(read_only=False)
            try:
                conn.execute("DELETE FROM portfolio WHERE portfolio_id = ?", [portfolio_id])
                if holdings:
                    data = [
                        (portfolio_id, h['symbol'], h['name'], h['shares'], h['entryPrice'], h['factor'], h['sector'], h['type'], h.get('purchaseDate', '2024-01-01'), h.get('sl'), h.get('tp'))
                        for h in holdings
                    ]
                    conn.executemany("""
                        INSERT INTO portfolio (portfolio_id, symbol, name, shares, entry_price, factor, sector, asset_type, purchase_date, sl, tp)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, data)
                return True
            except Exception as e:
                print(f"[DuckDB] Portfolio save error: {e}")
                return False
            finally:
                conn.close()

    def get_portfolio(self, portfolio_id: str = "main") -> List[Dict[str, Any]]:
        """Retrieve current holdings from storage for a specific portfolio."""
        conn = self._connect(read_only=True)
        try:
            rows = conn.execute("""
                SELECT symbol, name, shares, entry_price, factor, sector, asset_type, purchase_date, sl, tp
                FROM portfolio
                WHERE portfolio_id = ?
            """, [portfolio_id]).fetchall()
            return [
                {
                    "symbol": r[0], "name": r[1], "shares": r[2], 
                    "entryPrice": r[3], "factor": r[4], "sector": r[5], 
                    "type": r[6], "purchaseDate": r[7],
                    "sl": r[8], "tp": r[9]
                }
                for r in rows
            ]
        except Exception as e:
            print(f"[DuckDB] Portfolio load error: {e}")
            return []
        finally:
            conn.close()
        return []

    def add_transaction(self, type_str: str, symbol: str, shares: float, price: float, realized_pnl: float = 0, custom_date: Optional[str] = None, portfolio_id: str = "main"):
        """Record a single transaction with optional custom date for a specific portfolio."""
        from datetime import datetime
        with self._write_lock:
            conn = self._connect(read_only=False)
            try:
                # Simple auto-increment ID
                res = conn.execute("SELECT MAX(id) FROM transactions").fetchone()
                max_id = res[0] if res and res[0] is not None else 0
                new_id = max_id + 1
                
                now = datetime.now()
                # Use custom_date if provided (YYYY-MM-DD), otherwise now
                date_str = custom_date if custom_date else now.strftime("%Y-%m-%d")
                time_str = now.strftime("%I:%M %p")
                
                conn.execute("""
                    INSERT INTO transactions (id, portfolio_id, type, symbol, shares, price, realized_pnl, date, time)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, [new_id, portfolio_id, type_str, symbol, shares, price, realized_pnl, date_str, time_str])
                return True
            except Exception as e:
                print(f"[DuckDB] Transaction error: {e}")
                return False
            finally:
                conn.close()

    def get_transactions(self, portfolio_id: str = "main") -> List[Dict[str, Any]]:
        """Retrieve all transactions for a specific portfolio."""
        conn = self._connect(read_only=True)
        try:
            rows = conn.execute("""
                SELECT type, symbol, shares, price, realized_pnl, date, time, epoch(timestamp)
                FROM transactions
                WHERE portfolio_id = ?
                ORDER BY timestamp ASC
            """, [portfolio_id]).fetchall()
            return [
                {
                    "type": r[0], "symbol": r[1], "shares": r[2], 
                    "price": r[3], "realized_pnl": r[4], "date": str(r[5]), "time": r[6],
                    "timestamp": r[7]
                }
                for r in rows
            ]
        except Exception as e:
            print(f"[DuckDB] Transaction load error: {e}")
            return []
        finally:
            conn.close()
        return []

    # --- Equity & Performance History ---

    def get_total_realized_pnl(self, portfolio_id: str = "main") -> float:
        """Sum up all realized_pnl from transactions for a specific portfolio."""
        conn = self._connect(read_only=True)
        try:
            res = conn.execute("SELECT SUM(realized_pnl) FROM transactions WHERE portfolio_id = ?", [portfolio_id]).fetchone()
            return res[0] if res and res[0] is not None else 0.0
        except Exception as e:
            print(f"[DuckDB] Realized PnL error: {e}")
            return 0.0
        finally:
            conn.close()
        return 0.0

    def record_equity_snapshot(self, total_equity: float, portfolio_id: str = "main"):
        """Record a snapshot of both realized balance and total equity."""
        # Calculate current realized balance (Seed 1200 + sum of all gains/losses)
        realized_gains = self.get_total_realized_pnl(portfolio_id)
        current_realized_balance = 1200 + realized_gains
        
        with self._write_lock:
            conn = self._connect(read_only=False)
            try:
                conn.execute("""
                    INSERT INTO equity_snapshots (portfolio_id, realized_balance, total_equity)
                    VALUES (?, ?, ?)
                """, [portfolio_id, current_realized_balance, total_equity])
                return True
            except Exception as e:
                print(f"[DuckDB] Equity snapshot error: {e}")
                return False
            finally:
                conn.close()

    def get_equity_history(self, portfolio_id: str = "main") -> List[Dict[str, Any]]:
        """Retrieve full history of realized vs total equity for a specific portfolio."""
        conn = self._connect(read_only=True)
        try:
            rows = conn.execute("""
                SELECT epoch(timestamp), realized_balance, total_equity
                FROM equity_snapshots
                WHERE portfolio_id = ?
                ORDER BY timestamp ASC
            """, [portfolio_id]).fetchall()
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
        return []

    # --- Asset Classification Persistence ---

    def get_asset_classification(self, symbol: str, benchmark: str = "SPY") -> Optional[Dict[str, Any]]:
        conn = self._connect(read_only=True)
        try:
            row = conn.execute(
                """
                SELECT symbol, asset_type, sector, sector_etf, industry_group,
                       industry, sub_industry, company_name, source
                FROM asset_classifications
                WHERE symbol = ? AND benchmark = ?
                """,
                [symbol.upper(), benchmark.upper()],
            ).fetchone()
            if not row:
                return None
            return {
                "ticker": row[0],
                "asset_type": row[1] or "equity",
                "sector": row[2] or "Unclassified",
                "sector_etf": row[3] or benchmark.upper(),
                "industry_group": row[4] or "Unclassified",
                "industry": row[5] or "Unclassified",
                "sub_industry": row[6] or "Unclassified",
                "company_name": row[7] or "",
                "source": row[8] or "database",
            }
        except Exception as e:
            print(f"[DuckDB] Asset classification load error for {symbol}: {e}")
            return None
        finally:
            conn.close()

    def upsert_asset_classifications(self, classifications: List[Dict[str, Any]], benchmark: str = "SPY") -> int:
        if not classifications:
            return 0

        with self._write_lock:
            conn = self._connect(read_only=False)
            try:
                rows = [
                    (
                        classification["ticker"],
                        benchmark.upper(),
                        classification.get("asset_type", "equity"),
                        classification.get("sector", "Unclassified"),
                        classification.get("sector_etf", benchmark.upper()),
                        classification.get("industry_group", "Unclassified"),
                        classification.get("industry", "Unclassified"),
                        classification.get("sub_industry", "Unclassified"),
                        classification.get("company_name", ""),
                        classification.get("source", "backend"),
                    )
                    for classification in classifications
                ]
                conn.executemany(
                    """
                    INSERT OR REPLACE INTO asset_classifications (
                        symbol, benchmark, asset_type, sector, sector_etf,
                        industry_group, industry, sub_industry, company_name,
                        source, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    """,
                    rows,
                )
                return len(rows)
            except Exception as e:
                print(f"[DuckDB] Asset classification save error: {e}")
                return 0
            finally:
                conn.close()
        return 0

    # --- Insider Trading Persistence ---

    def save_insider_trades(self, trades: List[Dict[str, Any]]) -> int:
        """Upsert insider trading records. Deduplicates by primary key."""
        if not trades:
            return 0
        
        with self._write_lock:
            conn = self._connect(read_only=False)
            try:
                count = 0
                for t in trades:
                    # Map 'date' to 'trade_date' and exclude internal '_row_class'
                    try:
                        conn.execute("""
                            INSERT OR IGNORE INTO insider_trading (
                                ticker, owner, relationship, trade_date, transaction,
                                cost, shares, value, shares_total, sec_form_4,
                                sec_url, type, scraped_at
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                        """, [
                            t.get('ticker'), t.get('owner'), t.get('relationship'),
                            t.get('date'), t.get('transaction'), t.get('cost'),
                            t.get('shares'), t.get('value'), t.get('shares_total'),
                            t.get('sec_form_4'), t.get('sec_url'), t.get('type')
                        ])
                        count += 1
                    except Exception as e:
                        # Skip individual failures (e.g. malformed dates)
                        continue
                return count
            except Exception as e:
                print(f"[DuckDB] Insider trade save error: {e}")
                return 0
            finally:
                conn.close()
        return 0

    def get_insider_trades(self, ticker: Optional[str] = None, limit: int = 100) -> List[Dict[str, Any]]:
        """Retrieve recent insider trades, optionally filtered by ticker."""
        conn = self._connect(read_only=True)
        try:
            query = "SELECT * FROM insider_trading"
            params: List[Any] = []
            if ticker:
                query += " WHERE ticker = ?"
                params.append(ticker.upper())
            
            query += " ORDER BY trade_date DESC, scraped_at DESC LIMIT ?"
            params.append(limit)
            
            result = conn.execute(query, params).fetchall()
            columns = [
                "ticker", "owner", "relationship", "date", "transaction",
                "cost", "shares", "value", "shares_total", "sec_form_4",
                "sec_url", "type", "scraped_at"
            ]
            return [dict(zip(columns, row)) for row in result]
        except Exception as e:
            print(f"[DuckDB] Insider trades load error: {e}")
            return []
        finally:
            conn.close()
        return []

