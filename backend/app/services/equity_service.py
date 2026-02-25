from typing import List, Dict, Any
from datetime import datetime, timedelta
import pandas as pd
from ..core.container import duckdb_repo

class EquityService:
    def get_historical_equity_curve(self, days: int = 730) -> List[Dict[str, Any]]:
        """
        Calculates historical equity curve starting from initial capital of $1200.
        Superimposes Realized Balance vs Total Equity.
        """
        # 1. Setup Timeline
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)
        date_range = pd.date_range(start=start_date, end=end_date, freq='D')
        
        # 2. Get Data
        portfolio = duckdb_repo.get_portfolio()
        transactions = duckdb_repo.get_transactions()
        
        # 3. Fetch Prices for all symbols in portfolio
        symbols = [p['symbol'] for p in portfolio]
        price_map = {}
        for sym in symbols:
            # Fetch historical prices from DuckDB
            conn = duckdb_repo._connect(read_only=True)
            try:
                df = conn.execute("SELECT date, close FROM ohlcv WHERE symbol = ? AND date >= ?", [sym, start_date]).df()
                if not df.empty:
                    df['date'] = pd.to_datetime(df['date'])
                    df.set_index('date', inplace=True)
                    # Reindex to full date range to fill missing days (weekends)
                    df = df.reindex(date_range).ffill().bfill()
                    price_map[sym] = df['close']
            finally:
                conn.close()

        # 4. Calculate Daily Curve
        history = []
        # Adjusted base capital to $50,000 to better reflect a professional mandate's equity buffer
        base_capital = 50000.0
        
        for current_date in date_range:
            day_str = current_date.strftime("%Y-%m-%d")
            
            # --- Realized Balance ---
            # Sum up all realized PnL from transactions that occurred ON or BEFORE this date
            realized_pnl = sum(t['realized_pnl'] for t in transactions if t['date'] <= day_str)
            realized_balance = base_capital + realized_pnl
            
            # --- Unrealized PnL ---
            unrealized_pnl = 0.0
            for p in portfolio:
                purchase_date = datetime.strptime(p['purchaseDate'], "%Y-%m-%d").date()
                if current_date.date() >= purchase_date:
                    sym = p['symbol']
                    if sym in price_map and current_date in price_map[sym].index:
                        current_price = price_map[sym][current_date]
                        entry_price = p['entryPrice']
                        shares = p['shares']
                        factor = p.get('factor', 1.0)
                        unrealized_pnl += shares * (current_price - entry_price) * factor
            
            total_equity = realized_balance + unrealized_pnl
            
            history.append({
                "time": int(current_date.timestamp()),
                "realized": round(realized_balance, 2),
                "total": round(total_equity, 2)
            })
            
        return history

equity_service = EquityService()
