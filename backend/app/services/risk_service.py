import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional
from scipy.stats import norm, skew, kurtosis
from ..core.container import duckdb_repo
from .math_core import math_core
from datetime import datetime, timedelta

class RiskService:
    @staticmethod
    def calculate_var(returns: List[float], confidence_level: float = 0.95) -> float:
        """Calculates Value at Risk (VaR) using the Historical Simulation method."""
        if not returns or len(returns) < 2:
            return 0.0
        sorted_returns = sorted(returns)
        index = int((1 - confidence_level) * len(sorted_returns))
        return abs(sorted_returns[index])

    @staticmethod
    def calculate_cvar(returns: List[float], confidence_level: float = 0.95) -> float:
        """Calculates Conditional VaR (Expected Shortfall)."""
        if not returns or len(returns) < 2:
            return 0.0
        sorted_returns = np.sort(returns)
        index = int((1 - confidence_level) * len(sorted_returns))
        if index <= 0: return 0.0
        return abs(np.mean(sorted_returns[:index]))

    @staticmethod
    def calculate_modified_var(returns: List[float], confidence_level: float = 0.95) -> float:
        """Calculates Modified VaR (mVaR) using the Cornish-Fisher expansion."""
        if not returns or len(returns) < 4:
            return RiskService.calculate_var(returns, confidence_level)
        mu = np.mean(returns)
        sigma = np.std(returns)
        s = skew(returns)
        k = kurtosis(returns)
        z_alpha = norm.ppf(1 - confidence_level)
        z_cf = (z_alpha + (1/6)*(z_alpha**2 - 1)*s + (1/24)*(z_alpha**3 - 3*z_alpha)*k - (1/36)*(2*z_alpha**3 - 5*z_alpha)*s**2)
        return abs(mu + z_cf * sigma)

    @staticmethod
    def calculate_modified_cvar(returns: List[float], confidence_level: float = 0.95) -> float:
        """Calculates Modified Expected Shortfall (mES)."""
        m_var = RiskService.calculate_modified_var(returns, confidence_level)
        std_cvar = RiskService.calculate_cvar(returns, confidence_level)
        return max(m_var, std_cvar)

    @classmethod
    def get_portfolio_risk_report(cls, holdings: List[Dict[str, Any]], days: int = 252) -> Dict[str, Any]:
        """Generates a full risk report for the current portfolio."""
        if not holdings:
            return {"error": "No holdings provided"}

        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        all_returns = {}
        total_market_value = sum(h.get('shares', 0) * h.get('price', 0) * h.get('factor', 1.0) for h in holdings)
        
        if total_market_value == 0:
            return {"error": "Portfolio has zero market value"}

        conn = duckdb_repo._connect(read_only=True)
        try:
            found_symbols = []
            symbol_prices = {}
            for h in holdings:
                sym = h['symbol']
                df = conn.execute("SELECT date, close FROM ohlcv WHERE symbol = ? AND date >= ? ORDER BY date ASC", [sym, start_date.date()]).df()
                if not df.empty and len(df) > 10:
                    df['returns'] = df['close'].pct_change().fillna(0)
                    all_returns[sym] = df.set_index('date')['returns']
                    symbol_prices[sym] = df['close'].values
                    found_symbols.append(sym)

            if not all_returns:
                return {"error": "No historical data found for holdings"}

            returns_df = pd.DataFrame(all_returns).fillna(0)
            temp_market_val = sum(h.get('shares', 0) * h.get('price', 0) * h.get('factor', 1.0) for h in holdings if h['symbol'] in found_symbols)
            weights = {h['symbol']: (h.get('shares', 0) * h.get('price', 0) * h.get('factor', 1.0)) / temp_market_val for h in holdings if h['symbol'] in found_symbols}
            portfolio_returns = (returns_df * pd.Series(weights)).sum(axis=1)
            
            # --- Advanced Math Integration ---
            txs = duckdb_repo.get_transactions()
            expected_val = math_core.expected_value(txs)
            sharpe = math_core.sharpe_ratio(portfolio_returns.values)
            
            # Annualized stats for Risk Adjusted Return
            ann_return = portfolio_returns.mean() * 252
            ann_vol = portfolio_returns.std() * np.sqrt(252)
            rar = math_core.risk_adjusted_return(ann_return, ann_vol, total_market_value)
            
            # Momentum via Gradient Descent
            momentum_per_asset = {}
            # --- Factor Analysis (CAPM & Idiosyncratic Risk) ---
            # Automatically uses SPY as benchmark, since it's the safest market proxy
            market_proxy = "SPY"
            try:
                spy_df = conn.execute("SELECT date, close FROM ohlcv WHERE symbol = ? AND date >= ? ORDER BY date ASC", [market_proxy, start_date.date()]).df()
                has_benchmark = not spy_df.empty and len(spy_df) > 10
                if has_benchmark:
                    spy_df['returns'] = spy_df['close'].pct_change().fillna(0)
                    market_returns = spy_df['returns'].values
            except Exception:
                has_benchmark = False

            factor_metrics = {}
            for sym, prices in symbol_prices.items():
                m, _ = math_core.gradient_descent_momentum(prices[-30:]) # Last 30 days
                momentum_per_asset[sym] = m
                
                # If market benchmark available, try CAPM metrics
                if has_benchmark and sym in all_returns:
                    asset_rets = all_returns[sym].values
                    min_len = min(len(asset_rets), len(market_returns))
                    
                    if min_len >= 10: # Ensure valid length
                        asset_rets = asset_rets[-min_len:]
                        market_rets_adj = market_returns[-min_len:]
                        
                        beta, alpha, exp_ret = math_core.calculate_capm(asset_rets, market_rets_adj)
                        idio_risk = math_core.calculate_idiosyncratic_risk(asset_rets, market_rets_adj)
                        factor_metrics[sym] = {
                            "beta": round(beta, 4),
                            "alpha_daily": round(alpha, 6),
                            "expected_return_capm": round(exp_ret * 100, 2), # %
                            "idiosyncratic_risk": round(idio_risk * 100, 2) # %
                        }

            # Covariance matrix & PCA on the portfolio assets
            returns_dict = {sym: df_ret.values for sym, df_ret in all_returns.items()}
            _, cov_matrix = math_core.calculate_covariance_matrix(returns_dict)
            pca_res = math_core.calculate_pca(returns_dict)

            # --- Hedging Strategy ---
            hedging = cls.generate_hedging_strategy(weights, ann_vol, portfolio_returns.tolist())

            return {
                "var_95_percent": round(cls.calculate_var(portfolio_returns.tolist()) * 100, 2),
                "mvar_95_percent": round(cls.calculate_modified_var(portfolio_returns.tolist()) * 100, 2),
                "sharpe_ratio": round(sharpe, 2),
                "expected_value_trade": round(expected_val, 2),
                "risk_adjusted_return": round(rar * 1000000, 4), # Scaled for readability
                "annualized_volatility": round(ann_vol * 100, 2),
                "excess_kurtosis": round(kurtosis(portfolio_returns), 3),
                "skewness": round(skew(portfolio_returns), 3),
                "momentum": {s: round(m, 4) for s, m in momentum_per_asset.items()},
                "exposure": weights,
                "hedging_strategy": hedging,
                "total_aum": round(total_market_value, 2),
                "coverage_percent": round(len(found_symbols) / len(holdings) * 100, 1),
                # New Advanced Data Return:
                "factor_analysis": factor_metrics if has_benchmark else None,
                "pca_variance_explained": [round(v*100, 2) for v in pca_res.get('explained_variance', [])][:3], # Top 3 PC
            }
        finally:
            conn.close()

    @staticmethod
    def generate_hedging_strategy(weights: Dict[str, float], vol: float, returns: List[float]) -> Dict[str, Any]:
        """Algorithmic Hedging Suggestion based on portfolio profile."""
        if vol > 0.25:
            action = "AGGRESSIVE_HEDGING"
            strategy = "Protective Put Collar (Buy Puts at 5% OTM, Sell Calls at 10% OTM)"
        elif vol > 0.15:
            action = "MODERATE_HEDGING"
            strategy = "Protective Puts (Buy Puts 7-10% OTM)"
        else:
            action = "MONITOR"
            strategy = "No immediate hedging required; maintain trailing stops."

        # Suggest specific hedge based on highest weight
        top_asset = max(weights, key=weights.get)
        
        return {
            "action": action,
            "recommended_strategy": strategy,
            "primary_hedge_target": top_asset,
            "hedge_ratio": round(vol * 1.2, 2) # Heuristic ratio
        }

risk_service = RiskService()
