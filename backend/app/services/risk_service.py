"""Portfolio risk calculations independent from persistence details."""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd
from scipy.stats import kurtosis, norm, skew

from .math_core import math_core
from .risk_data_source import DuckDBRiskDataSource, IRiskDataSource


class RiskService:
    def __init__(self, data_source: Optional[IRiskDataSource] = None) -> None:
        self._data_source = data_source or DuckDBRiskDataSource()

    @staticmethod
    def _clean_returns(returns: List[float]) -> np.ndarray:
        values = np.asarray(returns, dtype=np.float64)
        return values[np.isfinite(values)]

    @staticmethod
    def _validate_confidence(confidence_level: float) -> None:
        if not 0 < confidence_level < 1:
            raise ValueError("confidence_level must be between 0 and 1")

    @classmethod
    def calculate_var(
        cls,
        returns: List[float],
        confidence_level: float = 0.95,
    ) -> float:
        """Historical one-period loss VaR expressed as a positive fraction."""
        cls._validate_confidence(confidence_level)
        values = cls._clean_returns(returns)
        if values.size < 2:
            return 0.0
        quantile = float(
            np.quantile(values, 1 - confidence_level, method="lower")
        )
        return max(0.0, -quantile)

    @classmethod
    def calculate_cvar(
        cls,
        returns: List[float],
        confidence_level: float = 0.95,
    ) -> float:
        """Historical expected shortfall over the VaR tail."""
        cls._validate_confidence(confidence_level)
        values = np.sort(cls._clean_returns(returns))
        if values.size < 2:
            return 0.0
        tail_size = max(1, int(np.ceil((1 - confidence_level) * values.size)))
        return max(0.0, -float(np.mean(values[:tail_size])))

    @classmethod
    def calculate_modified_var(
        cls,
        returns: List[float],
        confidence_level: float = 0.95,
    ) -> float:
        """Cornish-Fisher VaR adjusted for skewness and excess kurtosis."""
        cls._validate_confidence(confidence_level)
        values = cls._clean_returns(returns)
        if values.size < 4:
            return cls.calculate_var(values.tolist(), confidence_level)
        sigma = float(np.std(values, ddof=1))
        if sigma == 0:
            return 0.0
        mean = float(np.mean(values))
        sample_skew = float(skew(values))
        excess_kurtosis = float(kurtosis(values))
        z_alpha = float(norm.ppf(1 - confidence_level))
        z_cf = (
            z_alpha
            + ((z_alpha**2 - 1) * sample_skew / 6)
            + ((z_alpha**3 - 3 * z_alpha) * excess_kurtosis / 24)
            - ((2 * z_alpha**3 - 5 * z_alpha) * sample_skew**2 / 36)
        )
        return max(0.0, -(mean + z_cf * sigma))

    @classmethod
    def calculate_modified_cvar(
        cls,
        returns: List[float],
        confidence_level: float = 0.95,
    ) -> float:
        return max(
            cls.calculate_modified_var(returns, confidence_level),
            cls.calculate_cvar(returns, confidence_level),
        )

    def get_portfolio_risk_report(
        self,
        holdings: List[Dict[str, Any]],
        days: int = 252,
    ) -> Dict[str, Any]:
        if not holdings:
            return {"error": "No holdings provided"}
        if days < 20:
            return {"error": "At least 20 calendar days are required"}

        exposure_by_symbol: Dict[str, float] = {}
        for holding in holdings:
            symbol = str(holding.get("symbol", "")).strip().upper()
            market_value = (
                float(holding.get("shares", 0) or 0)
                * float(holding.get("price", 0) or 0)
                * float(holding.get("factor", 1.0) or 1.0)
            )
            if symbol and market_value:
                exposure_by_symbol[symbol] = (
                    exposure_by_symbol.get(symbol, 0.0) + market_value
                )

        total_gross_value = sum(abs(value) for value in exposure_by_symbol.values())
        if total_gross_value <= 0:
            return {"error": "Portfolio has zero gross market value"}

        start_date = datetime.now() - timedelta(days=days)
        requested_symbols = [*exposure_by_symbol, "SPY"]
        price_series = self._data_source.load_close_prices(
            requested_symbols,
            start_date,
        )
        asset_returns = {
            symbol: series.pct_change().dropna()
            for symbol, series in price_series.items()
            if symbol in exposure_by_symbol and len(series) > 10
        }
        if not asset_returns:
            return {"error": "No historical data found for holdings"}

        returns_frame = pd.concat(
            asset_returns,
            axis=1,
            join="inner",
        ).dropna()
        if len(returns_frame) < 2:
            return {"error": "Holdings do not have enough overlapping return history"}

        found_symbols = list(returns_frame.columns)
        covered_gross_value = sum(
            abs(exposure_by_symbol[symbol]) for symbol in found_symbols
        )
        if covered_gross_value <= 0:
            return {"error": "Covered holdings have zero gross market value"}

        weights = {
            symbol: exposure_by_symbol[symbol] / covered_gross_value
            for symbol in found_symbols
        }
        weight_series = pd.Series(weights, dtype=float)
        portfolio_returns = returns_frame.mul(weight_series, axis=1).sum(axis=1)
        return_values = portfolio_returns.to_numpy(dtype=float)

        transactions = self._data_source.get_transactions()
        expected_value = math_core.expected_value(transactions)
        sharpe_ratio = math_core.sharpe_ratio(return_values)
        annual_return = float(portfolio_returns.mean() * 252)
        annual_volatility = float(portfolio_returns.std(ddof=1) * np.sqrt(252))
        risk_adjusted_return = math_core.risk_adjusted_return(
            annual_return,
            annual_volatility,
        )

        momentum_per_asset: Dict[str, float] = {}
        for symbol in found_symbols:
            prices = price_series[symbol].to_numpy(dtype=float)
            momentum, _ = math_core.gradient_descent_momentum(prices[-30:])
            momentum_per_asset[symbol] = momentum

        benchmark_returns = (
            price_series["SPY"].pct_change().dropna()
            if "SPY" in price_series else None
        )
        factor_metrics: Dict[str, dict] = {}
        if benchmark_returns is not None:
            for symbol in found_symbols:
                aligned = pd.concat(
                    [asset_returns[symbol], benchmark_returns],
                    axis=1,
                    join="inner",
                ).dropna()
                if len(aligned) < 10:
                    continue
                asset_values = aligned.iloc[:, 0].to_numpy(dtype=float)
                benchmark_values = aligned.iloc[:, 1].to_numpy(dtype=float)
                beta, alpha, expected_return = math_core.calculate_capm(
                    asset_values,
                    benchmark_values,
                )
                idiosyncratic_risk = math_core.calculate_idiosyncratic_risk(
                    asset_values,
                    benchmark_values,
                )
                factor_metrics[symbol] = {
                    "beta": round(beta, 4),
                    "alpha_daily": round(alpha, 6),
                    "expected_return_capm": round(expected_return * 100, 2),
                    "idiosyncratic_risk": round(idiosyncratic_risk * 100, 2),
                }

        aligned_returns = {
            symbol: returns_frame[symbol].to_numpy(dtype=float)
            for symbol in found_symbols
        }
        pca_result = math_core.calculate_pca(aligned_returns)
        hedging = self.generate_hedging_strategy(
            weights,
            annual_volatility,
        )

        sample_skew = float(skew(return_values)) if len(return_values) >= 3 else 0.0
        sample_kurtosis = (
            float(kurtosis(return_values)) if len(return_values) >= 4 else 0.0
        )
        sample_skew = sample_skew if np.isfinite(sample_skew) else 0.0
        sample_kurtosis = sample_kurtosis if np.isfinite(sample_kurtosis) else 0.0

        return {
            "var_95_percent": round(self.calculate_var(return_values.tolist()) * 100, 2),
            "cvar_95_percent": round(self.calculate_cvar(return_values.tolist()) * 100, 2),
            "mvar_95_percent": round(self.calculate_modified_var(return_values.tolist()) * 100, 2),
            "mcvar_95_percent": round(self.calculate_modified_cvar(return_values.tolist()) * 100, 2),
            "sharpe_ratio": round(sharpe_ratio, 2),
            "expected_value_trade": round(expected_value, 2),
            "risk_adjusted_return": round(risk_adjusted_return, 4),
            "annualized_return": round(annual_return * 100, 2),
            "annualized_volatility": round(annual_volatility * 100, 2),
            "excess_kurtosis": round(sample_kurtosis, 3),
            "skewness": round(sample_skew, 3),
            "momentum": {
                symbol: round(value, 4)
                for symbol, value in momentum_per_asset.items()
            },
            "exposure": weights,
            "hedging_strategy": hedging,
            "total_aum": round(total_gross_value, 2),
            "covered_aum": round(covered_gross_value, 2),
            "coverage_percent": round(
                len(found_symbols) / len(exposure_by_symbol) * 100,
                1,
            ),
            "coverage_value_percent": round(
                covered_gross_value / total_gross_value * 100,
                1,
            ),
            "factor_analysis": factor_metrics or None,
            "pca_variance_explained": [
                round(value * 100, 2)
                for value in pca_result.get("explained_variance", [])
            ][:3],
        }

    @staticmethod
    def generate_hedging_strategy(
        weights: Dict[str, float],
        vol: float,
    ) -> Dict[str, Any]:
        if vol > 0.25:
            action = "AGGRESSIVE_HEDGING"
            strategy = "Protective Put Collar (Buy Puts at 5% OTM, Sell Calls at 10% OTM)"
        elif vol > 0.15:
            action = "MODERATE_HEDGING"
            strategy = "Protective Puts (Buy Puts 7-10% OTM)"
        else:
            action = "MONITOR"
            strategy = "No immediate hedging required; maintain trailing stops."

        top_asset = max(weights, key=lambda symbol: abs(weights[symbol]))
        return {
            "action": action,
            "recommended_strategy": strategy,
            "primary_hedge_target": top_asset,
            "hedge_ratio": round(vol * 1.2, 2),
        }


risk_service = RiskService()
