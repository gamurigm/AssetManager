"""
Mathematical Core for Advanced Risk & Alpha Analysis
Implements mathematical and statistical primitives defined in the MMAM mandate.

Formulas:
  E[x]  = P(W)·V(W) + P(L)·V(L)
  S     = (Rp - Rf) / σp                            (Sharpe Ratio, annualized)
  RAR   = E(R) / (σ · C)                            (Risk Adjusted Return)
  GD    : w := w − η·∂L/∂w,  b := b − η·∂L/∂b      (Gradient Descent on MSE)
"""

import numpy as np
from typing import List, Dict, Any, Tuple


class FinancialMathCore:

    # ── Expected Value ──────────────────────────────────────────────
    @staticmethod
    def expected_value(transactions: List[Dict[str, Any]]) -> float:
        """
        E[x] = P(W)·V(W) + P(L)·V(L)

        P(W) = #wins / #total,  V(W) = mean(wins)
        P(L) = #losses / #total, V(L) = mean(losses)
        """
        if not transactions:
            return 0.0

        pnls = [t.get("realized_pnl", 0) for t in transactions if t.get("realized_pnl", 0) != 0]
        if not pnls:
            return 0.0

        wins   = [p for p in pnls if p > 0]
        losses = [p for p in pnls if p < 0]
        n      = len(pnls)

        p_w = len(wins)   / n
        p_l = len(losses)  / n
        v_w = float(np.mean(wins))   if wins   else 0.0
        v_l = float(np.mean(losses)) if losses else 0.0

        return p_w * v_w + p_l * v_l

    # ── Sharpe Ratio (annualized) ───────────────────────────────────
    @staticmethod
    def sharpe_ratio(returns: np.ndarray, risk_free_rate: float = 0.04) -> float:
        """
        S = (Rp − Rf) / σp

        All inputs are daily returns; the result is annualized.
        Rf_daily  = Rf_annual / 252
        Rp_annual = E[r_daily] · 252
        σ_annual  = σ_daily · √252
        """
        if len(returns) < 2:
            return 0.0

        mu    = float(np.mean(returns))
        sigma = float(np.std(returns, ddof=1))
        if sigma == 0:
            return 0.0

        rf_daily = risk_free_rate / 252.0
        return ((mu - rf_daily) * 252.0) / (sigma * np.sqrt(252.0))

    # ── Risk Adjusted Return ────────────────────────────────────────
    @staticmethod
    def risk_adjusted_return(
        expected_return_annual: float,
        annual_volatility: float,
        capital_at_risk: float,
    ) -> float:
        """
        RAR = E(R) / (σ · C)

        Where C is the total capital at risk (AUM).
        """
        if annual_volatility == 0 or capital_at_risk == 0:
            return 0.0
        return expected_return_annual / (annual_volatility * capital_at_risk)

    # ── Gradient Descent → Linear Regression (Momentum) ─────────────
    @staticmethod
    def gradient_descent_momentum(
        prices: np.ndarray,
        epochs: int = 1000,
        learning_rate: float = 0.01,
    ) -> Tuple[float, float]:
        """
        Finds (w, b) for  ŷ = w·x + b  by minimizing MSE loss via
        Gradient Descent:

            L  = (1/N) Σ (ŷᵢ − yᵢ)²
            ∂L/∂w = (2/N) Σ (ŷᵢ − yᵢ)·xᵢ
            ∂L/∂b = (2/N) Σ (ŷᵢ − yᵢ)

            w := w − η · ∂L/∂w
            b := b − η · ∂L/∂b

        Returns (w, b).  w is the 'Momentum' — the slope of the
        regression line over the price window.
        """
        prices = np.asarray(prices, dtype=np.float64)
        if len(prices) < 2:
            return 0.0, 0.0

        n = len(prices)

        # Normalise so GD converges cleanly
        x = np.linspace(0.0, 1.0, n)
        y_mean = np.mean(prices)
        y_std  = np.std(prices)
        y_std  = y_std if y_std > 0 else 1.0
        y = (prices - y_mean) / y_std

        w = 0.0
        b = 0.0
        eta = learning_rate

        for _ in range(epochs):
            y_hat  = w * x + b            # predictions
            error  = y_hat - y            # residuals

            # ∂L/∂w and ∂L/∂b
            dw = (2.0 / n) * np.dot(error, x)
            db = (2.0 / n) * np.sum(error)

            # Update rule: w := w − η·∂L/∂w
            w -= eta * dw
            b -= eta * db

        # De-normalise w back to the original price scale
        # (momentum = total price change from x=0 to x=1)
        raw_w = w * y_std
        raw_b = b * y_std + y_mean

        return float(raw_w), float(raw_b)

    # ── Helper: daily log-returns from prices ───────────────────────
    @staticmethod
    def returns_from_prices(prices: np.ndarray) -> np.ndarray:
        """Daily log-returns: rₜ = ln(pₜ / pₜ₋₁)."""
        prices = np.asarray(prices, dtype=np.float64)
        return np.diff(np.log(prices))

    # ── CAPM (Capital Asset Pricing Model) ──────────────────────────
    @staticmethod
    def calculate_capm(asset_returns: np.ndarray, market_returns: np.ndarray, risk_free_rate_annual: float = 0.04) -> Tuple[float, float, float]:
        """
        CAPM Regression
        R_i = R_f + Beta * (R_m - R_f) + Alpha + error

        Returns:
            Beta (market sensitivity)
            Alpha (daily abnormal return)
            Expected Return (annualized based on CAPM)
        """
        if len(asset_returns) < 2 or len(asset_returns) != len(market_returns):
            return 0.0, 0.0, 0.0

        covariance = np.cov(asset_returns, market_returns)[0][1]
        market_variance = np.var(market_returns, ddof=1)
        
        if market_variance == 0:
            return 0.0, 0.0, 0.0
            
        beta = covariance / market_variance
        alpha = np.mean(asset_returns) - (beta * np.mean(market_returns))
        
        # CAPM expected return (annualized)
        market_return_annual = np.mean(market_returns) * 252.0
        expected_return_annual = risk_free_rate_annual + beta * (market_return_annual - risk_free_rate_annual)
        
        return float(beta), float(alpha), float(expected_return_annual)

    # ── Idiosyncratic Risk ──────────────────────────────────────────
    @staticmethod
    def calculate_idiosyncratic_risk(asset_returns: np.ndarray, market_returns: np.ndarray) -> float:
        """
        Idiosyncratic Risk (annualized volatility of the residuals).
        Returns variance of (asset_returns - (alpha + beta * market_returns)).
        """
        if len(asset_returns) < 2 or len(asset_returns) != len(market_returns):
            return 0.0

        covariance = np.cov(asset_returns, market_returns)[0][1]
        market_variance = np.var(market_returns, ddof=1)
        
        if market_variance == 0:
            return float(np.std(asset_returns, ddof=1) * np.sqrt(252.0))
            
        beta = covariance / market_variance
        alpha = np.mean(asset_returns) - (beta * np.mean(market_returns))
        
        predicted_returns = alpha + beta * market_returns
        residuals = asset_returns - predicted_returns
        
        # Annualized idiosyncratic volatility
        idiosyncratic_volatility = np.std(residuals, ddof=1) * np.sqrt(252.0)
        return float(idiosyncratic_volatility)

    # ── Covariance Matrix ───────────────────────────────────────────
    @staticmethod
    def calculate_covariance_matrix(returns_dict: Dict[str, np.ndarray]) -> Tuple[List[str], np.ndarray]:
        """
        Calculates the covariance matrix across multiple assets.
        Ensures all arrays are of the same length (pads or truncates to match).
        Returns:
            headers: List of asset symbols
            cov_matrix: Annualized covariance matrix
        """
        tickers = list(returns_dict.keys())
        if not tickers:
            return [], np.array([])
            
        # Align lengths
        min_len = min(len(arr) for arr in returns_dict.values())
        if min_len < 2:
            return tickers, np.zeros((len(tickers), len(tickers)))
            
        aligned_returns = [returns_dict[t][-min_len:] for t in tickers]
        matrix = np.vstack(aligned_returns)
        
        # Annualized covariance matrix
        cov_matrix = np.cov(matrix) * 252.0
        return tickers, cov_matrix

    # ── PCA Spectral Decomposition ──────────────────────────────────
    @staticmethod
    def calculate_pca(returns_dict: Dict[str, np.ndarray]) -> Dict[str, Any]:
        """
        Performs Principal Component Analysis via Eigen-decomposition of correlation matrix.
        """
        tickers, cov_matrix = FinancialMathCore.calculate_covariance_matrix(returns_dict)
        n = len(tickers)
        if n < 2:
            return {"eigenvalues": [], "eigenvectors": [], "cumulative_variance": []}
            
        # Convert Covariance to Correlation matrix for PCA
        stds = np.sqrt(np.diag(cov_matrix))
        # Handle zero division
        stds[stds == 0] = 1.0
        corr_matrix = cov_matrix / np.outer(stds, stds)
        
        eigenvalues, eigenvectors = np.linalg.eigh(corr_matrix)
        
        # Sort in descending order
        sorted_idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[sorted_idx]
        eigenvectors = eigenvectors[:, sorted_idx]
        
        total_var = np.sum(eigenvalues)
        explained_variance = eigenvalues / total_var
        cumulative_variance = np.cumsum(explained_variance)
        
        return {
            "eigenvalues": eigenvalues.tolist(),
            "explained_variance": explained_variance.tolist(),
            "cumulative_variance": cumulative_variance.tolist(),
            "components": eigenvectors.tolist(),
            "tickers": tickers
        }


math_core = FinancialMathCore()
