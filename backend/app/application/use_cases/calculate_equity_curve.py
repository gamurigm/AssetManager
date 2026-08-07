from typing import List, Dict, Any
from datetime import datetime, timedelta
import pandas as pd
from ...domain.entities.equity import EquityCurvePoint

class CalculateEquityCurveUseCase:
    def __init__(self, repository):
        self._repository = repository

    def execute(self, days: int = 730, portfolio_id: str = "main") -> List[Dict[str, Any]]:
        """
        Calculates historical equity curve starting from initial capital.
        Optimized to reduce DB calls and avoid O(N*M) loops.
        """
        # 1. Setup Timeline
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)
        date_range = pd.date_range(start=start_date, end=end_date, freq='D')
        
        # 2. Get Data for the specific portfolio
        portfolio = self._repository.get_portfolio(portfolio_id)
        if not portfolio:
            # Return flat line if no holdings
            base_capital = 50000.0
            return [{"time": int(d.timestamp()), "realized": base_capital, "total": base_capital} for d in date_range]

        transactions = self._repository.get_transactions(portfolio_id)
        
        # 3. Fetch all prices in ONE pass
        symbols = list(set(p['symbol'] for p in portfolio))
        price_map = {}
        
        conn = self._repository._connect(read_only=True)
        try:
            # Fetch all required historical data in one query for all symbols
            symbols_placeholders = ",".join(["?" for _ in symbols])
            query = f"SELECT symbol, date, close FROM ohlcv WHERE symbol IN ({symbols_placeholders}) AND date >= ?"
            params = symbols + [start_date]
            
            all_data = conn.execute(query, params).df()
            
            if not all_data.empty:
                all_data['date'] = pd.to_datetime(all_data['date'])
                for sym in symbols:
                    sym_df = all_data[all_data['symbol'] == sym].copy()
                    if not sym_df.empty:
                        sym_df.set_index('date', inplace=True)
                        sym_df = sym_df.reindex(date_range).ffill().bfill()
                        price_map[sym] = sym_df['close']
        finally:
            conn.close()

        # 4. Pre-calculate Realized PnL Timeline (Cumulative Sum)
        daily_delta = {}
        for t in transactions:
            dt = t['date'][:10] # YYYY-MM-DD
            daily_delta[dt] = daily_delta.get(dt, 0.0) + t['realized_pnl']
            
        # 5. Calculate Daily Curve
        history = []
        base_capital = 50000.0
        running_realized_pnl = 0.0
        
        for current_date in date_range:
            day_str = current_date.strftime("%Y-%m-%d")
            
            # Update realized balance with today's deltas
            running_realized_pnl += daily_delta.get(day_str, 0.0)
            realized_balance = base_capital + running_realized_pnl
            
            # --- Unrealized PnL ---
            unrealized_pnl = 0.0
            for p in portfolio:
                if day_str >= p['purchaseDate']:
                    sym = p['symbol']
                    if sym in price_map:
                        try:
                            current_price = price_map[sym][current_date]
                            unrealized_pnl += p['shares'] * (current_price - p['entryPrice']) * p.get('factor', 1.0)
                        except KeyError:
                            pass
            
            total_equity = realized_balance + unrealized_pnl
            
            history.append({
                "time": int(current_date.timestamp()),
                "realized": round(realized_balance, 2),
                "total": round(total_equity, 2)
            })
            
        return history
