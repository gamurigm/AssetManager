from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from ..core.container import duckdb_repo
from .math_core import math_core


class PortfolioPolicyService:
    def __init__(self, repo: Any | None = None) -> None:
        self._repo = repo or duckdb_repo

    def build_policy_snapshot(
        self,
        portfolio_id: str = "main",
        holdings: Optional[List[Dict[str, Any]]] = None,
        benchmark: str = "SPY",
        lookback_days: int = 252,
        risk_aversion: float = 0.35,
        turnover_penalty: float = 0.08,
        max_weight: float = 0.35,
        gross_limit: float = 1.0,
    ) -> Dict[str, Any]:
        portfolio_holdings = holdings if holdings is not None else self._repo.get_portfolio(portfolio_id)
        positions = self._aggregate_positions(portfolio_holdings)
        if not positions:
            return {"error": "No active holdings available for policy analysis"}

        gross_exposure = float(sum(abs(position["market_value"]) for position in positions))
        if gross_exposure <= 0:
            return {"error": "Portfolio has zero gross exposure"}

        start_date = (datetime.now(timezone.utc) - timedelta(days=max(lookback_days * 2, 120))).date().isoformat()
        end_date = datetime.now(timezone.utc).date().isoformat()
        history_map = self._load_history([position["symbol"] for position in positions], start_date, end_date)
        benchmark_history = self._repo.get_history_range(benchmark, start_date, end_date)
        benchmark_returns = self._returns_series(benchmark_history, lookback_days)

        current_weights = {
            position["symbol"]: float(position["market_value"] / gross_exposure)
            for position in positions
        }

        metrics: Dict[str, Dict[str, Any]] = {}
        returns_frame_data: Dict[str, pd.Series] = {}
        locked_weights: Dict[str, float] = {}

        for position in positions:
            symbol = position["symbol"]
            candles = history_map.get(symbol, [])
            returns_series = self._returns_series(candles, lookback_days)
            if returns_series is None or len(returns_series) < 30:
                locked_weights[symbol] = current_weights[symbol]
                continue

            metric = self._estimate_asset_metrics(
                symbol=symbol,
                position=position,
                returns_series=returns_series,
                benchmark_returns=benchmark_returns,
                lookback_days=lookback_days,
                risk_aversion=risk_aversion,
            )
            metrics[symbol] = metric
            returns_frame_data[symbol] = returns_series

        valid_symbols = list(metrics.keys())
        locked_weight_total = float(sum(abs(weight) for weight in locked_weights.values()))
        residual_gross_limit = max(0.0, gross_limit - locked_weight_total)

        if valid_symbols and residual_gross_limit > 0:
            returns_df = pd.DataFrame(returns_frame_data).fillna(0.0)
            ordered_symbols = list(returns_df.columns)
            returns_dict = {symbol: returns_df[symbol].to_numpy(dtype=np.float64) for symbol in ordered_symbols}
            _, covariance_matrix = math_core.calculate_covariance_matrix(returns_dict)
            covariance_matrix = np.atleast_2d(np.asarray(covariance_matrix, dtype=np.float64))
            if covariance_matrix.size == 0:
                covariance_matrix = np.eye(len(ordered_symbols), dtype=np.float64) * 1e-6

            expected_returns = np.asarray(
                [metrics[symbol]["expected_return_annual"] for symbol in ordered_symbols],
                dtype=np.float64,
            )
            current_vector = np.asarray(
                [current_weights.get(symbol, 0.0) for symbol in ordered_symbols],
                dtype=np.float64,
            )
            target_vector = self._optimize_weights(
                expected_returns=expected_returns,
                covariance_matrix=covariance_matrix,
                current_weights=current_vector,
                gross_limit=residual_gross_limit,
                max_weight=max_weight,
                risk_aversion=risk_aversion,
                turnover_penalty=turnover_penalty,
            )
            final_weights = dict(locked_weights)
            final_weights.update({symbol: float(weight) for symbol, weight in zip(ordered_symbols, target_vector)})
        else:
            ordered_symbols = []
            covariance_matrix = np.zeros((0, 0), dtype=np.float64)
            expected_returns = np.zeros(0, dtype=np.float64)
            current_vector = np.zeros(0, dtype=np.float64)
            target_vector = np.zeros(0, dtype=np.float64)
            final_weights = dict(locked_weights)

        current_expected_return = float(np.dot(current_vector, expected_returns)) if len(current_vector) else 0.0
        target_expected_return = float(np.dot(target_vector, expected_returns)) if len(target_vector) else 0.0
        current_risk = self._portfolio_risk(current_vector, covariance_matrix)
        target_risk = self._portfolio_risk(target_vector, covariance_matrix)
        realized_trade_ev = float(math_core.expected_value(self._repo.get_transactions(portfolio_id)))

        target_gross = float(sum(abs(final_weights.get(position["symbol"], 0.0)) for position in positions))
        cash_buffer = max(0.0, gross_limit - target_gross)
        coverage_ratio = float(sum(abs(current_weights.get(symbol, 0.0)) for symbol in valid_symbols))
        rebalance_required = any(
            abs(final_weights.get(position["symbol"], current_weights[position["symbol"]]) - current_weights[position["symbol"]]) >= 0.02
            for position in positions
        )

        allocations = []
        for position in positions:
            symbol = position["symbol"]
            current_weight = float(current_weights[symbol])
            target_weight = float(final_weights.get(symbol, current_weight))
            metric = metrics.get(symbol)
            has_data = metric is not None
            target_notional = target_weight * gross_exposure
            delta_notional = target_notional - position["market_value"]
            unit_notional = position["price"] * position["factor"]
            delta_shares = float(delta_notional / unit_notional) if unit_notional else 0.0
            action = self._determine_action(current_weight, target_weight, has_data)

            allocations.append(
                {
                    "symbol": symbol,
                    "name": position["name"],
                    "sector": position["sector"],
                    "type": position["type"],
                    "shares": round(position["shares"], 6),
                    "price": round(position["price"], 6),
                    "factor": round(position["factor"], 6),
                    "current_weight_pct": round(current_weight * 100, 2),
                    "target_weight_pct": round(target_weight * 100, 2),
                    "weight_delta_pct": round((target_weight - current_weight) * 100, 2),
                    "current_direction": self._direction_label(current_weight),
                    "target_direction": self._direction_label(target_weight),
                    "target_notional": round(target_notional, 2),
                    "delta_notional": round(delta_notional, 2),
                    "delta_shares": round(delta_shares, 4),
                    "action": action,
                    "has_data": has_data,
                    "expected_return_pct": round((metric["expected_return_annual"] if metric else 0.0) * 100, 2),
                    "expected_value_pct": round((metric["distribution_ev_annual"] if metric else 0.0) * 100, 2),
                    "volatility_pct": round((metric["volatility_annual"] if metric else 0.0) * 100, 2),
                    "idiosyncratic_risk_pct": round((metric["idiosyncratic_risk"] if metric else 0.0) * 100, 2),
                    "momentum_pct": round((metric["momentum_annual"] if metric else 0.0) * 100, 2),
                    "beta": round(metric["beta"], 4) if metric else None,
                    "alpha_daily": round(metric["alpha_daily"], 6) if metric else None,
                    "confidence": round((metric["confidence"] if metric else 0.0) * 100, 1),
                    "utility_score": round(metric["utility_score"], 4) if metric else 0.0,
                    "rationale": self._build_rationale(position, metric, has_data, action),
                }
            )

        allocations.sort(key=lambda item: (item["action"] == "HOLD", -abs(item["weight_delta_pct"])))
        high_conviction = [
            symbol
            for symbol, metric in sorted(metrics.items(), key=lambda item: item[1]["confidence"], reverse=True)
            if metric["confidence"] >= 0.65
        ][:3]

        return {
            "portfolio_id": portfolio_id,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "policy_mode": "ev_observational_policy",
            "benchmark": benchmark,
            "lookback_days": lookback_days,
            "summary": {
                "rebalance_required": rebalance_required,
                "confidence_pct": round(np.mean([metric["confidence"] for metric in metrics.values()]) * 100, 1) if metrics else 0.0,
                "coverage_percent": round(coverage_ratio * 100, 1),
                "high_conviction_symbols": high_conviction,
                "target_cash_buffer_pct": round(cash_buffer * 100, 2),
            },
            "objective": {
                "risk_aversion": risk_aversion,
                "turnover_penalty": turnover_penalty,
                "max_weight_pct": round(max_weight * 100, 2),
                "gross_limit_pct": round(gross_limit * 100, 2),
                "current_expected_return_pct": round(current_expected_return * 100, 2),
                "target_expected_return_pct": round(target_expected_return * 100, 2),
                "ev_delta_pct": round((target_expected_return - current_expected_return) * 100, 2),
                "current_risk_pct": round(current_risk * 100, 2),
                "target_risk_pct": round(target_risk * 100, 2),
                "risk_delta_pct": round((target_risk - current_risk) * 100, 2),
                "current_gross_exposure_pct": round(sum(abs(current_weights[p["symbol"]]) for p in positions) * 100, 2),
                "target_gross_exposure_pct": round(target_gross * 100, 2),
                "realized_trade_ev": round(realized_trade_ev, 2),
            },
            "allocations": allocations,
        }

    def _aggregate_positions(self, holdings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        merged: Dict[str, Dict[str, Any]] = {}
        for raw_holding in holdings:
            symbol = str(raw_holding.get("symbol", "")).strip().upper()
            shares = float(raw_holding.get("shares", 0) or 0)
            if not symbol or shares == 0:
                continue

            price = float(raw_holding.get("price") or raw_holding.get("entryPrice") or 0)
            factor = float(raw_holding.get("factor") or 1.0)
            name = str(raw_holding.get("name") or symbol)
            sector = str(raw_holding.get("sector") or "Unknown")
            asset_type = str(raw_holding.get("type") or "asset")
            entry_price = float(raw_holding.get("entryPrice") or price or 0)

            if symbol not in merged:
                merged[symbol] = {
                    "symbol": symbol,
                    "name": name,
                    "sector": sector,
                    "type": asset_type,
                    "shares": 0.0,
                    "price": price,
                    "factor": factor,
                    "entry_notional": 0.0,
                    "abs_shares": 0.0,
                }

            merged[symbol]["shares"] += shares
            merged[symbol]["price"] = price or merged[symbol]["price"]
            merged[symbol]["factor"] = factor or merged[symbol]["factor"]
            merged[symbol]["entry_notional"] += abs(shares) * entry_price
            merged[symbol]["abs_shares"] += abs(shares)

        positions: List[Dict[str, Any]] = []
        for merged_position in merged.values():
            shares = float(merged_position["shares"])
            if shares == 0:
                continue
            avg_entry = (
                merged_position["entry_notional"] / merged_position["abs_shares"]
                if merged_position["abs_shares"]
                else merged_position["price"]
            )
            market_value = shares * merged_position["price"] * merged_position["factor"]
            positions.append(
                {
                    "symbol": merged_position["symbol"],
                    "name": merged_position["name"],
                    "sector": merged_position["sector"],
                    "type": merged_position["type"],
                    "shares": shares,
                    "price": float(merged_position["price"]),
                    "factor": float(merged_position["factor"]),
                    "entry_price": float(avg_entry),
                    "market_value": float(market_value),
                }
            )
        return positions

    def _load_history(self, symbols: List[str], start_date: str, end_date: str) -> Dict[str, List[Any]]:
        unique_symbols = sorted({symbol for symbol in symbols if symbol})
        return {
            symbol: self._repo.get_history_range(symbol, start_date, end_date)
            for symbol in unique_symbols
        }

    def _returns_series(self, candles: List[Any], lookback_days: int) -> Optional[pd.Series]:
        if not candles or len(candles) < 3:
            return None

        closes = [float(candle.close) for candle in candles if getattr(candle, "close", None) not in (None, 0)]
        dates = [str(candle.date) for candle in candles if getattr(candle, "close", None) not in (None, 0)]
        if len(closes) < 3 or len(closes) != len(dates):
            return None

        series = pd.Series(closes, index=pd.to_datetime(dates)).sort_index().pct_change().dropna()
        if len(series) > lookback_days:
            series = series.iloc[-lookback_days:]
        return series if len(series) >= 2 else None

    def _estimate_asset_metrics(
        self,
        symbol: str,
        position: Dict[str, Any],
        returns_series: pd.Series,
        benchmark_returns: Optional[pd.Series],
        lookback_days: int,
        risk_aversion: float,
    ) -> Dict[str, Any]:
        returns = returns_series.to_numpy(dtype=np.float64)
        mean_return_annual = float(np.mean(returns) * 252.0)
        distribution_ev_annual = float(self._returns_expected_value(returns) * 252.0)
        volatility_annual = float(np.std(returns, ddof=1) * np.sqrt(252.0)) if len(returns) > 1 else 0.0

        prices = np.asarray([
            float(candle.close)
            for candle in self._repo.get_history_range(symbol, (datetime.now(timezone.utc) - timedelta(days=max(lookback_days * 2, 120))).date().isoformat(), datetime.now(timezone.utc).date().isoformat())
            if getattr(candle, "close", None) not in (None, 0)
        ], dtype=np.float64)
        momentum_annual = self._annualized_momentum(prices)

        beta = 0.0
        alpha_daily = 0.0
        capm_expected = mean_return_annual
        idiosyncratic_risk = volatility_annual

        if benchmark_returns is not None:
            aligned = pd.concat([returns_series, benchmark_returns], axis=1, join="inner").dropna()
            if len(aligned) >= 20:
                asset_returns = aligned.iloc[:, 0].to_numpy(dtype=np.float64)
                market_returns = aligned.iloc[:, 1].to_numpy(dtype=np.float64)
                beta, alpha_daily, capm_expected = math_core.calculate_capm(asset_returns, market_returns)
                idiosyncratic_risk = math_core.calculate_idiosyncratic_risk(asset_returns, market_returns)

        expected_return_annual = self._blend_expected_return(
            distribution_ev_annual=distribution_ev_annual,
            mean_return_annual=mean_return_annual,
            capm_expected=capm_expected,
            momentum_annual=momentum_annual,
            idiosyncratic_risk=idiosyncratic_risk,
            risk_aversion=risk_aversion,
            beta=beta,
        )
        utility_score = float(expected_return_annual / max(volatility_annual, 0.05))
        coverage_factor = min(len(returns) / max(lookback_days, 1), 1.0)
        directional_edge = min(abs(expected_return_annual) / max(volatility_annual, 0.05), 2.5)
        confidence = float(min(0.95, 0.30 + 0.35 * coverage_factor + 0.20 * directional_edge + 0.10 * (1.0 if benchmark_returns is not None else 0.0)))

        return {
            "mean_return_annual": mean_return_annual,
            "distribution_ev_annual": distribution_ev_annual,
            "expected_return_annual": expected_return_annual,
            "volatility_annual": volatility_annual,
            "momentum_annual": momentum_annual,
            "beta": float(beta),
            "alpha_daily": float(alpha_daily),
            "idiosyncratic_risk": float(idiosyncratic_risk),
            "utility_score": utility_score,
            "confidence": confidence,
            "shares": position["shares"],
        }

    def _blend_expected_return(
        self,
        distribution_ev_annual: float,
        mean_return_annual: float,
        capm_expected: float,
        momentum_annual: float,
        idiosyncratic_risk: float,
        risk_aversion: float,
        beta: float,
    ) -> float:
        distribution_component = float(np.clip(distribution_ev_annual, -0.75, 0.75))
        mean_component = float(np.clip(mean_return_annual, -0.75, 0.75))
        momentum_component = float(np.clip(momentum_annual, -0.75, 0.75))
        beta_reliability = float(max(0.15, 1.0 / (1.0 + max(abs(beta) - 1.0, 0.0))))
        capm_component = float(np.clip(capm_expected, -0.50, 0.50)) * beta_reliability
        blended = (
            0.35 * distribution_component
            + 0.25 * mean_component
            + 0.25 * capm_component
            + 0.15 * momentum_component
        )
        blended -= idiosyncratic_risk * min(0.25, 0.10 + risk_aversion * 0.15)
        return float(np.clip(blended, -1.0, 1.0))

    def _returns_expected_value(self, returns: np.ndarray) -> float:
        if len(returns) == 0:
            return 0.0
        winners = returns[returns > 0]
        losers = returns[returns < 0]
        total = len(returns)
        win_component = (len(winners) / total) * float(np.mean(winners)) if len(winners) else 0.0
        loss_component = (len(losers) / total) * float(np.mean(losers)) if len(losers) else 0.0
        return win_component + loss_component

    def _annualized_momentum(self, prices: np.ndarray) -> float:
        if len(prices) < 5:
            return 0.0
        window = min(30, len(prices) - 1)
        base_price = float(prices[-window - 1])
        latest_price = float(prices[-1])
        if base_price <= 0:
            return 0.0
        return float(((latest_price / base_price) - 1.0) * (252.0 / window))

    def _optimize_weights(
        self,
        expected_returns: np.ndarray,
        covariance_matrix: np.ndarray,
        current_weights: np.ndarray,
        gross_limit: float,
        max_weight: float,
        risk_aversion: float,
        turnover_penalty: float,
    ) -> np.ndarray:
        if expected_returns.size == 0 or gross_limit <= 0:
            return np.zeros_like(expected_returns)

        effective_max_weight = max(max_weight, gross_limit / max(len(expected_returns), 1))
        covariance = np.asarray(covariance_matrix, dtype=np.float64)
        covariance += np.eye(len(expected_returns), dtype=np.float64) * 1e-6

        initial = np.clip(current_weights.astype(np.float64), -effective_max_weight, effective_max_weight)
        initial_gross = float(np.sum(np.abs(initial)))
        if initial_gross > gross_limit and initial_gross > 0:
            initial *= gross_limit / initial_gross

        def objective(weights: np.ndarray) -> float:
            utility = (
                float(np.dot(weights, expected_returns))
                - risk_aversion * float(weights @ covariance @ weights)
                - turnover_penalty * float(np.sum((weights - current_weights) ** 2))
            )
            return -utility

        constraints = [{"type": "ineq", "fun": lambda weights: gross_limit - float(np.sum(np.abs(weights)))}]
        bounds = [(-effective_max_weight, effective_max_weight) for _ in expected_returns]

        result = minimize(
            objective,
            initial,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"maxiter": 200, "ftol": 1e-9, "disp": False},
        )

        if result.success and np.all(np.isfinite(result.x)):
            optimized = np.asarray(result.x, dtype=np.float64)
        else:
            vol = np.sqrt(np.maximum(np.diag(covariance), 1e-8))
            optimized = np.divide(expected_returns, np.maximum(vol, 0.05))
            optimized = np.clip(optimized, -effective_max_weight, effective_max_weight)
            optimized_gross = float(np.sum(np.abs(optimized)))
            if optimized_gross > gross_limit and optimized_gross > 0:
                optimized *= gross_limit / optimized_gross

        optimized[np.abs(optimized) < 0.0025] = 0.0
        optimized_gross = float(np.sum(np.abs(optimized)))
        if optimized_gross > gross_limit and optimized_gross > 0:
            optimized *= gross_limit / optimized_gross
        return optimized

    def _portfolio_risk(self, weights: np.ndarray, covariance_matrix: np.ndarray) -> float:
        if weights.size == 0 or covariance_matrix.size == 0:
            return 0.0
        risk = float(weights @ covariance_matrix @ weights)
        return float(np.sqrt(max(risk, 0.0)))

    def _determine_action(self, current_weight: float, target_weight: float, has_data: bool) -> str:
        if not has_data:
            return "LOCK"
        if abs(target_weight - current_weight) < 0.02:
            return "HOLD"
        if abs(target_weight) < 0.005:
            return "EXIT" if current_weight >= 0 else "COVER"
        if target_weight > 0 and current_weight < 0:
            return "REVERSE_LONG"
        if target_weight < 0 and current_weight > 0:
            return "REVERSE_SHORT"
        if abs(target_weight) > abs(current_weight):
            return "BUY" if target_weight > 0 else "ADD_SHORT"
        return "TRIM" if target_weight > 0 else "COVER"

    def _direction_label(self, weight: float) -> str:
        if weight > 0.005:
            return "LONG"
        if weight < -0.005:
            return "SHORT"
        return "FLAT"

    def _build_rationale(
        self,
        position: Dict[str, Any],
        metric: Optional[Dict[str, Any]],
        has_data: bool,
        action: str,
    ) -> str:
        if not has_data or metric is None:
            return f"{position['symbol']} stays observational only because no sufficient history is available in DuckDB."
        return (
            f"{action} because expected return is {metric['expected_return_annual'] * 100:.2f}% annualized, "
            f"volatility is {metric['volatility_annual'] * 100:.2f}% and momentum is {metric['momentum_annual'] * 100:.2f}%."
        )


portfolio_policy_service = PortfolioPolicyService()