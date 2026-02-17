import numpy as np
from typing import List, Dict
from scipy.stats import norm

class RiskService:
    @staticmethod
    def calculate_var(returns: List[float], confidence_level: float = 0.95) -> float:
        """
        Calculates Value at Risk (VaR) using the Historical Simulation method.
        """
        if not returns or len(returns) < 2:
            return 0.0
        
        # Sort returns and find the quantile
        sorted_returns = sorted(returns)
        index = int((1 - confidence_level) * len(sorted_returns))
        var_value = abs(sorted_returns[index])
        return var_value

    @staticmethod
    def calculate_cvar(returns: List[float], confidence_level: float = 0.95) -> float:
        """
        Calculates Conditional VaR (Expected Shortfall).
        """
        if not returns or len(returns) < 2:
            return 0.0
            
        sorted_returns = np.sort(returns)
        index = int((1 - confidence_level) * len(sorted_returns))
        cvar_value = abs(np.mean(sorted_returns[:index]))
        return cvar_value

    @staticmethod
    def calculate_beta(portfolio_returns: List[float], benchmark_returns: List[float]) -> float:
        """
        Calculates the Beta coefficient relative to a benchmark.
        Beta = Cov(Rp, Rb) / Var(Rb)
        """
        if len(portfolio_returns) != len(benchmark_returns) or len(portfolio_returns) < 2:
            return 1.0 # Default to market beta if data is insufficient
            
        covariance_matrix = np.cov(portfolio_returns, benchmark_returns)
        covariance = covariance_matrix[0, 1]
        benchmark_variance = np.var(benchmark_returns)
        
        if benchmark_variance == 0:
            return 1.0
            
        return covariance / benchmark_variance

    @staticmethod
    def calculate_sharpe_ratio(returns: List[float], risk_free_rate: float = 0.02) -> float:
        """
        Calculates the Sharpe Ratio.
        """
        if not returns or len(returns) < 2:
            return 0.0
            
        avg_return = np.mean(returns)
        volatility = np.std(returns)
        
        if volatility == 0:
            return 0.0
            
        return (avg_return - (risk_free_rate / 252)) / volatility # Daily sharpe
