"""
PortfolioBacktestService
=======================
Portfolio-level daily backtest for weighted allocations.

Supports two input modes:
  1. Manual asset list with target weights.
  2. Existing DuckDB portfolio holdings, converted into target weights.

Execution modes:
  - Prefer the optional C++ core engine if the pybind module is available.
  - Fall back to a Python implementation otherwise.
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import httpx
import numpy as np
import pandas as pd


_ANNUALIZE = math.sqrt(252)
_REBALANCE_DAYS = {
    "none": 0,
    "weekly": 5,
    "monthly": 21,
    "quarterly": 63,
}
_EXECUTION_MODES = {"auto", "remote", "cpp", "python"}


@dataclass(frozen=True)
class PortfolioAssetTarget:
    symbol: str
    weight: float
    factor: float = 1.0
    name: str = ""


class PortfolioBacktestService:
    def __init__(self) -> None:
        self._repo = None
        self._mds = None
        self._cpp_checked = False
        self._core_module = None
        self._cpp_engine_cls = None
        self._http_client: Optional[httpx.AsyncClient] = None
        self._remote_base_url = os.getenv("PORTFOLIO_CPP_SERVICE_URL", "").strip().rstrip("/")
        self._remote_timeout = httpx.Timeout(30.0, connect=2.0)

    def _get_deps(self) -> None:
        if self._repo is None:
            from ..core.container import duckdb_repo

            self._repo = duckdb_repo

        if self._mds is None:
            from .market_data import market_data_service

            self._mds = market_data_service

        if not self._cpp_checked:
            self._cpp_checked = True
            try:
                import core_engine  # type: ignore

                if hasattr(core_engine, "PortfolioBacktestEngine"):
                    self._core_module = core_engine
                    self._cpp_engine_cls = core_engine.PortfolioBacktestEngine
            except Exception:
                self._core_module = None
                self._cpp_engine_cls = None

    async def run_backtest(
        self,
        start_date: str,
        end_date: str,
        initial_cash: float = 10_000.0,
        assets: Optional[List[Dict[str, Any]]] = None,
        portfolio_id: Optional[str] = None,
        rebalance_frequency: str = "none",
        fee_bps: float = 0.0,
        execution_mode: str = "auto",
    ) -> Dict[str, Any]:
        self._get_deps()

        rebalance_key = rebalance_frequency.lower().strip()
        if rebalance_key not in _REBALANCE_DAYS:
            return {
                "error": "rebalance_frequency must be one of: none, weekly, monthly, quarterly"
            }

        execution_key = execution_mode.lower().strip()
        if execution_key not in _EXECUTION_MODES:
            return {
                "error": "execution_mode must be one of: auto, remote, cpp, python"
            }

        targets = self._resolve_targets(assets or [], portfolio_id)
        if not targets:
            return {
                "error": "Provide assets with weights or a portfolio_id containing long holdings"
            }

        price_matrix = await self._load_price_matrix(
            [target.symbol for target in targets],
            start_date,
            end_date,
        )
        if price_matrix.empty:
            return {"error": "No overlapping historical data available for the selected symbols"}

        rebalance_days = _REBALANCE_DAYS[rebalance_key]
        engine_name = "python"
        raw_result: Dict[str, Any]
        engine_notes: List[str] = []
        raw_result = {}

        if execution_key in ("auto", "remote"):
            if self._remote_base_url:
                try:
                    raw_result = await self._run_remote_engine(
                        remote_url=self._remote_base_url,
                        initial_cash=initial_cash,
                        targets=targets,
                        price_matrix=price_matrix,
                        rebalance_days=rebalance_days,
                        fee_bps=fee_bps,
                    )
                    engine_name = "cpp-remote"
                except Exception as exc:
                    engine_notes.append(f"remote_unavailable: {exc}")
                    if execution_key == "remote":
                        return {"error": f"Remote C++ engine unavailable: {exc}"}
            elif execution_key == "remote":
                return {
                    "error": "execution_mode=remote requires PORTFOLIO_CPP_SERVICE_URL to be configured"
                }

        if not raw_result and execution_key in ("auto", "cpp") and self._cpp_engine_cls is not None and self._core_module is not None:
            try:
                raw_result = self._run_cpp_engine(
                    initial_cash=initial_cash,
                    targets=targets,
                    price_matrix=price_matrix,
                    rebalance_days=rebalance_days,
                    fee_bps=fee_bps,
                )
                engine_name = "cpp"
            except Exception as exc:
                engine_notes.append(f"embedded_cpp_unavailable: {exc}")
                if execution_key == "cpp":
                    return {"error": f"Embedded C++ engine failed: {exc}"}

        if not raw_result and execution_key == "cpp":
            return {"error": "Embedded C++ engine is not available in this backend environment"}

        if not raw_result:
            raw_result = self._run_python_engine(
                initial_cash=initial_cash,
                targets=targets,
                price_matrix=price_matrix,
                rebalance_days=rebalance_days,
                fee_bps=fee_bps,
            )

        equity_curve = raw_result["equity_curve"]
        if not equity_curve:
            return {"error": "Backtest produced no equity curve"}

        metrics = _compute_kpis(initial_cash, equity_curve)
        last_row = price_matrix.iloc[-1]
        allocations = _build_allocation_summary(
            targets=targets,
            quantities=raw_result["quantities"],
            last_prices=last_row.to_dict(),
            initial_cash=initial_cash,
        )

        return {
            "strategy": "PORTFOLIO_BUY_AND_HOLD",
            "engine": engine_name,
            "start_date_requested": start_date,
            "end_date_requested": end_date,
            "start_date_used": price_matrix.index[0].strftime("%Y-%m-%d"),
            "end_date_used": price_matrix.index[-1].strftime("%Y-%m-%d"),
            "initial_cash": round(initial_cash, 2),
            "fee_bps": fee_bps,
            "rebalance_frequency": rebalance_key,
            "source_portfolio_id": portfolio_id,
            "execution_mode": execution_key,
            "assets": allocations,
            "equity_curve": equity_curve,
            "trades": raw_result["trades"],
            "kpis": metrics,
            "engine_notes": engine_notes,
        }

    async def describe_execution_engines(self) -> Dict[str, Any]:
        self._get_deps()

        remote = {
            "configured": bool(self._remote_base_url),
            "url": self._remote_base_url or None,
            "healthy": False,
            "service": None,
            "error": None,
        }
        if self._remote_base_url:
            try:
                client = self._get_http_client()
                response = await client.get(f"{self._remote_base_url}/health")
                response.raise_for_status()
                payload = response.json()
                remote["healthy"] = True
                remote["service"] = payload.get("service")
            except Exception as exc:
                remote["error"] = str(exc)

        return {
            "default_mode": "auto",
            "available_modes": ["auto", "remote", "cpp", "python"],
            "embedded_cpp_available": self._cpp_engine_cls is not None and self._core_module is not None,
            "remote": remote,
        }

    def _resolve_targets(
        self,
        assets: List[Dict[str, Any]],
        portfolio_id: Optional[str],
    ) -> List[PortfolioAssetTarget]:
        if assets:
            return _normalize_asset_targets(assets)

        if not portfolio_id or self._repo is None:
            return []

        holdings = self._repo.get_portfolio(portfolio_id)
        long_holdings = []
        for holding in holdings:
            shares = float(holding.get("shares") or 0.0)
            if shares <= 0:
                continue
            factor = float(holding.get("factor") or 1.0)
            entry_price = float(holding.get("entryPrice") or 0.0)
            notional = shares * entry_price * factor
            if notional <= 0:
                continue
            long_holdings.append(
                {
                    "symbol": holding.get("symbol"),
                    "name": holding.get("name") or holding.get("symbol") or "",
                    "weight": notional,
                    "factor": factor,
                }
            )

        return _normalize_asset_targets(long_holdings)

    async def _load_price_matrix(
        self,
        symbols: List[str],
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:
        frames: List[pd.DataFrame] = []
        start_ts = pd.Timestamp(start_date)
        end_ts = pd.Timestamp(end_date)
        lookback_days = max((end_ts - start_ts).days + 60, 365)

        for symbol in symbols:
            await self._ensure_history(symbol, end_date, lookback_days)
            candles = self._repo.get_history_range(symbol, start_date, end_date)
            if not candles:
                continue
            frame = pd.DataFrame(
                {
                    "date": pd.to_datetime([c.date for c in candles]),
                    symbol: [float(c.close) for c in candles],
                }
            )
            frames.append(frame)

        if not frames:
            return pd.DataFrame()

        merged = frames[0]
        for frame in frames[1:]:
            merged = merged.merge(frame, on="date", how="outer")

        merged = merged.sort_values("date").drop_duplicates(subset=["date"]).set_index("date")
        merged = merged.ffill()
        merged = merged[(merged.index >= start_ts) & (merged.index <= end_ts)]
        merged = merged.dropna(how="any")
        return merged

    async def _ensure_history(self, symbol: str, end_date: str, lookback_days: int) -> None:
        latest = self._repo.get_latest_date(symbol)
        count = self._repo.get_count(symbol)
        if count >= 20 and latest and latest >= end_date:
            return

        try:
            await self._mds.get_historical(symbol, limit=lookback_days)
        except Exception:
            pass

    def _run_cpp_engine(
        self,
        initial_cash: float,
        targets: List[PortfolioAssetTarget],
        price_matrix: pd.DataFrame,
        rebalance_days: int,
        fee_bps: float,
    ) -> Dict[str, Any]:
        engine = self._cpp_engine_cls()
        cpp_targets = []
        cpp_prices = []

        for target in targets:
            item = self._core_module.PortfolioTarget()
            item.symbol = target.symbol
            item.weight = target.weight
            item.factor = target.factor
            cpp_targets.append(item)

        for date, row in price_matrix.iterrows():
            date_str = date.strftime("%Y-%m-%d")
            for target in targets:
                bar = self._core_module.PortfolioPriceBar()
                bar.date = date_str
                bar.symbol = target.symbol
                bar.close = float(row[target.symbol])
                cpp_prices.append(bar)

        result = engine.run_weighted(initial_cash, cpp_targets, cpp_prices, rebalance_days, fee_bps)
        trades = [
            {
                "date": t.date,
                "symbol": t.symbol,
                "side": "BUY" if t.is_buy else "SELL",
                "quantity": round(float(t.quantity), 8),
                "price": round(float(t.price), 6),
                "notional": round(float(t.notional), 4),
                "fee": round(float(t.fee), 4),
            }
            for t in result.trades
        ]
        curve = [
            {
                "date": p.date,
                "equity": round(float(p.equity), 4),
                "cash": round(float(p.cash), 4),
            }
            for p in result.equity_curve
        ]
        quantities = _quantities_from_trades(trades)
        return {
            "trades": trades,
            "equity_curve": curve,
            "quantities": quantities,
        }

    async def _run_remote_engine(
        self,
        remote_url: str,
        initial_cash: float,
        targets: List[PortfolioAssetTarget],
        price_matrix: pd.DataFrame,
        rebalance_days: int,
        fee_bps: float,
    ) -> Dict[str, Any]:
        payload = {
            "initial_cash": initial_cash,
            "rebalance_interval_days": rebalance_days,
            "fee_bps": fee_bps,
            "targets": [
                {
                    "symbol": target.symbol,
                    "weight": target.weight,
                    "factor": target.factor,
                }
                for target in targets
            ],
            "prices": [
                {
                    "date": date.strftime("%Y-%m-%d"),
                    "symbol": target.symbol,
                    "close": float(row[target.symbol]),
                }
                for date, row in price_matrix.iterrows()
                for target in targets
            ],
        }

        client = self._get_http_client()
        response = await client.post(f"{remote_url}/portfolio/backtest", json=payload)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict):
            raise ValueError("Remote engine returned a non-object response")
        if data.get("error"):
            raise ValueError(str(data["error"]))

        trades = []
        for trade in data.get("trades", []):
            side = str(trade.get("side") or ("BUY" if _coerce_bool(trade.get("is_buy")) else "SELL")).upper()
            trades.append(
                {
                    "date": str(trade.get("date") or ""),
                    "symbol": str(trade.get("symbol") or ""),
                    "side": side,
                    "quantity": round(_coerce_float(trade.get("quantity")), 8),
                    "price": round(_coerce_float(trade.get("price")), 6),
                    "notional": round(_coerce_float(trade.get("notional")), 4),
                    "fee": round(_coerce_float(trade.get("fee")), 4),
                }
            )

        curve = [
            {
                "date": str(point.get("date") or ""),
                "equity": round(_coerce_float(point.get("equity")), 4),
                "cash": round(_coerce_float(point.get("cash")), 4),
            }
            for point in data.get("equity_curve", [])
        ]

        return {
            "trades": trades,
            "equity_curve": curve,
            "quantities": _quantities_from_trades(trades),
        }

    def _get_http_client(self) -> httpx.AsyncClient:
        if self._http_client is None:
            self._http_client = httpx.AsyncClient(timeout=self._remote_timeout)
        return self._http_client

    def _run_python_engine(
        self,
        initial_cash: float,
        targets: List[PortfolioAssetTarget],
        price_matrix: pd.DataFrame,
        rebalance_days: int,
        fee_bps: float,
    ) -> Dict[str, Any]:
        fee_rate = fee_bps / 10_000.0
        quantities = {target.symbol: 0.0 for target in targets}
        factors = {target.symbol: target.factor for target in targets}
        trades: List[Dict[str, Any]] = []
        equity_curve: List[Dict[str, Any]] = []
        cash = float(initial_cash)

        for idx, (date, row) in enumerate(price_matrix.iterrows()):
            should_rebalance = idx == 0 or (rebalance_days > 0 and idx % rebalance_days == 0)
            if should_rebalance:
                total_equity = cash + sum(
                    quantities[target.symbol] * float(row[target.symbol]) * factors[target.symbol]
                    for target in targets
                )
                for target in targets:
                    price = float(row[target.symbol])
                    factor = factors[target.symbol]
                    current_qty = quantities[target.symbol]
                    current_value = current_qty * price * factor
                    target_value = total_equity * target.weight
                    diff_value = target_value - current_value
                    if abs(diff_value) < 1e-9:
                        continue

                    if diff_value > 0:
                        quantity = diff_value / (price * factor * (1.0 + fee_rate))
                        notional = quantity * price * factor
                        fee = notional * fee_rate
                        cash -= notional + fee
                        quantities[target.symbol] = current_qty + quantity
                        trades.append(
                            {
                                "date": date.strftime("%Y-%m-%d"),
                                "symbol": target.symbol,
                                "side": "BUY",
                                "quantity": round(quantity, 8),
                                "price": round(price, 6),
                                "notional": round(notional, 4),
                                "fee": round(fee, 4),
                            }
                        )
                    else:
                        quantity = min(abs(diff_value) / (price * factor), current_qty)
                        if quantity <= 0:
                            continue
                        notional = quantity * price * factor
                        fee = notional * fee_rate
                        cash += notional - fee
                        quantities[target.symbol] = current_qty - quantity
                        trades.append(
                            {
                                "date": date.strftime("%Y-%m-%d"),
                                "symbol": target.symbol,
                                "side": "SELL",
                                "quantity": round(quantity, 8),
                                "price": round(price, 6),
                                "notional": round(notional, 4),
                                "fee": round(fee, 4),
                            }
                        )

            equity = cash + sum(
                quantities[target.symbol] * float(row[target.symbol]) * factors[target.symbol]
                for target in targets
            )
            equity_curve.append(
                {
                    "date": date.strftime("%Y-%m-%d"),
                    "equity": round(equity, 4),
                    "cash": round(cash, 4),
                }
            )

        return {
            "trades": trades,
            "equity_curve": equity_curve,
            "quantities": quantities,
        }


def _normalize_asset_targets(assets: List[Dict[str, Any]]) -> List[PortfolioAssetTarget]:
    cleaned = []
    raw_weights = []
    missing_weight_indices: List[int] = []

    for idx, asset in enumerate(assets):
        symbol = str(asset.get("symbol") or "").strip().upper()
        if not symbol:
            continue
        weight = asset.get("weight")
        factor = float(asset.get("factor") or 1.0)
        name = str(asset.get("name") or symbol)
        cleaned.append({"symbol": symbol, "weight": weight, "factor": factor, "name": name})
        if weight is None:
            missing_weight_indices.append(idx)
        else:
            raw_weights.append(float(weight))

    if not cleaned:
        return []

    numeric_weights = [float(item["weight"]) for item in cleaned if item["weight"] is not None]
    if numeric_weights and sum(numeric_weights) > 1.000001 and sum(numeric_weights) <= 100.000001:
        for item in cleaned:
            if item["weight"] is not None:
                item["weight"] = float(item["weight"]) / 100.0

    specified = [float(item["weight"]) for item in cleaned if item["weight"] is not None]
    specified_sum = sum(specified)
    unspecified_count = sum(1 for item in cleaned if item["weight"] is None)

    if unspecified_count == 0 and specified_sum > 0:
        final_weights = [float(item["weight"]) / specified_sum for item in cleaned]
    else:
        remaining = max(1.0 - specified_sum, 0.0)
        fallback = (remaining / unspecified_count) if unspecified_count else 0.0
        final_weights = []
        for item in cleaned:
            if item["weight"] is None:
                final_weights.append(fallback)
            else:
                final_weights.append(float(item["weight"]))
        total = sum(final_weights)
        if total <= 0:
            final_weights = [1.0 / len(cleaned)] * len(cleaned)
        else:
            final_weights = [weight / total for weight in final_weights]

    return [
        PortfolioAssetTarget(
            symbol=item["symbol"],
            weight=final_weights[idx],
            factor=float(item["factor"]),
            name=item["name"],
        )
        for idx, item in enumerate(cleaned)
    ]


def _coerce_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _coerce_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "buy"}
    return bool(value)


def _quantities_from_trades(trades: List[Dict[str, Any]]) -> Dict[str, float]:
    quantities: Dict[str, float] = {}
    for trade in trades:
        symbol = trade["symbol"]
        qty = float(trade["quantity"])
        quantities[symbol] = quantities.get(symbol, 0.0) + (qty if trade["side"] == "BUY" else -qty)
    return quantities


def _build_allocation_summary(
    targets: List[PortfolioAssetTarget],
    quantities: Dict[str, float],
    last_prices: Dict[str, float],
    initial_cash: float,
) -> List[Dict[str, Any]]:
    allocations = []
    for target in targets:
        quantity = float(quantities.get(target.symbol, 0.0))
        last_price = float(last_prices[target.symbol])
        final_value = quantity * last_price * target.factor
        allocations.append(
            {
                "symbol": target.symbol,
                "name": target.name or target.symbol,
                "target_weight": round(target.weight, 6),
                "factor": target.factor,
                "shares": round(quantity, 8),
                "last_price": round(last_price, 6),
                "final_value": round(final_value, 4),
                "pnl_usd_vs_target_cost": round(final_value - (initial_cash * target.weight), 4),
            }
        )
    return allocations


def _compute_kpis(initial_cash: float, equity_curve: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not equity_curve:
        return {
            "total_return_pct": 0.0,
            "cagr": 0.0,
            "max_drawdown_pct": 0.0,
            "volatility_ann_pct": 0.0,
            "sharpe_ratio": 0.0,
            "final_equity": round(initial_cash, 2),
            "trading_days": 0,
        }

    equity = pd.Series([float(point["equity"]) for point in equity_curve], dtype=float)
    final_equity = float(equity.iloc[-1])
    total_return = (final_equity / initial_cash - 1.0) if initial_cash > 0 else 0.0

    rolling_peak = equity.cummax()
    drawdowns = (equity / rolling_peak) - 1.0
    max_drawdown = float(drawdowns.min()) if not drawdowns.empty else 0.0

    daily_returns = equity.pct_change().replace([np.inf, -np.inf], np.nan).dropna()
    if len(daily_returns) > 1:
        volatility = float(daily_returns.std(ddof=1)) * _ANNUALIZE
        sharpe = (float(daily_returns.mean()) / float(daily_returns.std(ddof=1))) * _ANNUALIZE if float(daily_returns.std(ddof=1)) > 0 else 0.0
    else:
        volatility = 0.0
        sharpe = 0.0

    n_days = max(len(equity_curve), 1)
    n_years = max(n_days / 252.0, 1.0 / 252.0)
    cagr = (final_equity / initial_cash) ** (1.0 / n_years) - 1.0 if initial_cash > 0 else 0.0

    return {
        "total_return_pct": round(total_return * 100.0, 4),
        "cagr": round(cagr, 6),
        "max_drawdown_pct": round(abs(max_drawdown) * 100.0, 4),
        "volatility_ann_pct": round(volatility * 100.0, 4),
        "sharpe_ratio": round(sharpe, 4),
        "final_equity": round(final_equity, 4),
        "trading_days": n_days,
    }


portfolio_backtest_service = PortfolioBacktestService()