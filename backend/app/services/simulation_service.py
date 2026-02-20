"""
Simulation Service (simulation_service.py)
==========================================
Façade Pattern — one unified entry point for all simulation operations.
API routes, agents, and tests interact only with this class.

Wires up: StrategyFactory + BacktestRunner + DuckDBIntradayRepository + ORBKPICalculator.
Stores results in-memory with a simple dict (extendable to DB with no API changes).

Follows the same singleton pattern as the rest of the codebase
(market_data_service, duckdb_store, etc.).
"""

from __future__ import annotations

import uuid
from typing import Dict, List, Optional
from datetime import datetime, timezone
import logfire

from ..agents.strategies.engine import (
    StrategyConfig, TradeSignal, KPIResult,
    ORBFVGEngine, ORBKPICalculator, StrategyFactory,
)
from ..agents.strategies.backtest_runner import (
    BacktestRunner, BacktestConfig, BacktestResult,
)
from .intraday_repository import intraday_repository
from .market_data import market_data_service


# --------------------------------------------------------------------------- #
#  Request / Response schemas (simple dicts — Pydantic models live in routes) #
# --------------------------------------------------------------------------- #

class SimulationService:
    """
    Façade that hides the composition details of BacktestRunner, StrategyFactory,
    and KPICalculator from the API layer and agent tools.

    S: only orchestrates simulation runs — no business logic itself.
    """

    def __init__(self) -> None:
        self._results: Dict[str, BacktestResult] = {}

    # ================================================================== #
    #  Run full backtest                                                  #
    # ================================================================== #

    async def run_backtest(
        self,
        symbol: str,
        start_date: str,
        end_date: str,
        account_size: float = 10_000.0,
        strategy_name: str = "ORB_FVG_ENGULFING",
        strategy_params: Optional[dict] = None,
        pip_value: float = 1.0,
        run_bootstrap: bool = False,
        bootstrap_iterations: int = 1000,
    ) -> tuple[str, BacktestResult]:
        """
        Execute a full backtest and store the result.

        Returns:
            (sim_id, BacktestResult)
        """
        logfire.info("SimulationService.run_backtest",
                     symbol=symbol, strategy=strategy_name,
                     start=start_date, end=end_date)

        config = BacktestConfig(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            account_size=account_size,
            strategy_name=strategy_name,
            strategy_params=strategy_params or {},
            pip_value=pip_value,
            run_bootstrap=run_bootstrap,
            bootstrap_iterations=bootstrap_iterations
        )

        # Compose dependencies — DIP: runner only sees interfaces
        engine   = StrategyFactory.create(strategy_name)
        kpi_calc = ORBKPICalculator()
        runner   = BacktestRunner(engine, intraday_repository, kpi_calc)

        result = await runner.run(config)

        sim_id = self._generate_sim_id(symbol, strategy_name)
        self._results[sim_id] = result

        return sim_id, result

    # ================================================================== #
    #  Retrieve stored result                                             #
    # ================================================================== #

    def get_result(self, sim_id: str) -> Optional[BacktestResult]:
        return self._results.get(sim_id)

    def list_simulations(self) -> List[dict]:
        return [
            {"sim_id": sid, "summary": r.summary()}
            for sid, r in self._results.items()
        ]

    # ================================================================== #
    #  Live signal (today's session)                                      #
    # ================================================================== #

    async def get_live_signal(
        self,
        symbol: str,
        strategy_name: str = "ORB_FVG_ENGULFING",
        strategy_params: Optional[dict] = None,
        account_size: float = 10_000.0,
    ) -> dict:
        """
        Fetch the most recent M1/M5 intraday candles and run the engine
        on the current (or most recent) trading session.

        Returns:
            { "signal": TradeSignal | None, "reason": str, "source": str }
        """
        config = StrategyConfig.from_dict(strategy_params or {}) if strategy_params else StrategyConfig.default()

        result = await market_data_service.get_intraday(symbol, "1m", "1d")
        m1 = result.get("candles", [])

        result_m5 = await market_data_service.get_intraday(symbol, "5m", "1d")
        m5 = result_m5.get("candles", [])

        if not m1 or not m5:
            return {"signal": None, "reason": "Insufficient intraday data for live signal.", "source": result.get("source")}

        engine = StrategyFactory.create(strategy_name)
        signal: Optional[TradeSignal] = engine.run_session(m5, m1, account_size, config)

        if signal is None:
            return {"signal": None, "reason": "No valid setup found in current session.", "source": result.get("source")}

        return {
            "signal": {
                "signal_id":     signal.signal_id,
                "timestamp":     signal.timestamp,
                "direction":     signal.direction,
                "orh":           signal.orh,
                "orl":           signal.orl,
                "fvg_top":       signal.fvg_top,
                "fvg_bottom":    signal.fvg_bottom,
                "entry":         signal.entry,
                "stop":          signal.stop,
                "tp":            signal.tp,
                "risk_pips":     signal.risk_pips,
                "position_size": signal.position_size,
                "confidence":    signal.confidence,
                "atr_m1":        signal.atr_m1,
            },
            "reason": "Signal found.",
            "source": result.get("source"),
        }

    # ================================================================== #
    #  Private helpers                                                    #
    # ================================================================== #

    @staticmethod
    def _generate_sim_id(symbol: str, strategy: str) -> str:
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
        short_uid = uuid.uuid4().hex[:6].upper()
        return f"{ts}_{symbol}_{strategy}_{short_uid}"


# Singleton — same convention as market_data_service, duckdb_store
simulation_service = SimulationService()
