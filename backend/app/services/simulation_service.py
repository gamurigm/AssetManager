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

import asyncio
import os
import uuid
from typing import Dict, List, Optional
from datetime import datetime, timezone
import logfire

from ..agents.strategies.engine import (
    StrategyConfig, TradeSignal, ORBKPICalculator, StrategyFactory,
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
        self._results: Dict[str, Optional[BacktestResult]] = {}
        self._sio = None

    # ================================================================== #
    #  Real-time configuration                                           #
    # ================================================================== #

    def configure_realtime(self, sio) -> None:
        """Register the Socket.IO server so background runs can broadcast events."""
        self._sio = sio

    def pre_register(self, symbol: str, strategy_name: str) -> str:
        """Reserve a sim_id before the backtest starts (fills in None as placeholder)."""
        sim_id = self._generate_sim_id(symbol, strategy_name)
        self._results[sim_id] = None
        return sim_id

    async def _generate_pdf_report(self, result: BacktestResult) -> Optional[str]:
        """Generate a PDF report in a worker thread and return its filename."""
        from ..agents.strategies.report_generator import generate_pdf_report

        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"backtest_{result.config.symbol}_{stamp}.pdf"
        full_path = os.path.join(reports_dir, report_filename)

        await asyncio.to_thread(generate_pdf_report, result, full_path)
        logfire.info(f"PDF report generated: {full_path}")
        return report_filename

    def _make_callbacks(
        self, sim_id: str, loop: asyncio.AbstractEventLoop
    ):
        """Return three thread-safe callbacks that emit Socket.IO events."""
        sio = self._sio

        def on_progress(day: int, total: int) -> None:
            if not sio:
                return
            pct = round(day / total * 100) if total else 0
            asyncio.run_coroutine_threadsafe(
                sio.emit("backtest_progress", {
                    "sim_id": sim_id, "day": day,
                    "total": total, "pct": pct,
                }),
                loop,
            )

        def on_trade(record, equity: float) -> None:
            if not sio:
                return
            asyncio.run_coroutine_threadsafe(
                sio.emit("backtest_trade", {
                    "sim_id": sim_id,
                    "trade": {
                        "signal_id":      record.signal.signal_id,
                        "timestamp":      str(record.signal.timestamp),
                        "direction":      record.signal.direction,
                        "entry":          record.signal.entry,
                        "stop":           record.signal.stop,
                        "tp":             record.signal.tp,
                        "outcome":        record.outcome,
                        "pnl_r":          round(record.pnl_r, 3),
                        "pnl_usd":        round(record.pnl_usd, 2),
                        "exit_price":     record.exit_price,
                        "exit_timestamp": str(record.exit_timestamp),
                    },
                    "equity": round(equity, 2),
                }),
                loop,
            )

        def on_bootstrap(stats: dict) -> None:
            if not sio:
                return
            # Cap sample arrays at 500 items to keep socket frames small.
            asyncio.run_coroutine_threadsafe(
                sio.emit("backtest_bootstrap_ready", {
                    "sim_id":                  sim_id,
                    "iterations":              stats.get("iterations", 0),
                    "net_profit_95_ci":        stats.get("net_profit_95_ci", [0, 0]),
                    "max_drawdown_95_ci_pct":  stats.get("max_drawdown_95_ci_pct", [0, 0]),
                    "net_profit_samples":      stats.get("net_profit_samples", [])[:500],
                    "max_drawdown_samples":    stats.get("max_drawdown_samples", [])[:500],
                }),
                loop,
            )

        return on_progress, on_trade, on_bootstrap

    async def run_backtest_background(self, sim_id: str, config: BacktestConfig) -> None:
        """
        Run a full backtest as a fire-and-forget background task.
        Emits Socket.IO events: backtest_progress, backtest_trade,
        backtest_bootstrap_ready, backtest_complete, backtest_error.
        """
        loop = asyncio.get_running_loop()
        on_progress, on_trade, on_bootstrap = self._make_callbacks(sim_id, loop)
        try:
            engine   = StrategyFactory.create(config.strategy_name)
            kpi_calc = ORBKPICalculator()
            runner   = BacktestRunner(
                engine, intraday_repository, kpi_calc,
                on_progress_cb=on_progress,
                on_trade_cb=on_trade,
                on_bootstrap_cb=on_bootstrap,
            )

            result = await runner.run(config)

            # --- Generate PDF report (in thread, non-blocking) ---
            report_filename = None
            try:
                report_filename = await self._generate_pdf_report(result)
                result.report_path = report_filename
            except Exception as pdf_err:
                logfire.error(f"PDF generation failed for {sim_id}: {pdf_err}")

            self._results[sim_id] = result

            report_url = (
                f"http://localhost:8282/view-reports/{report_filename}"
                if report_filename else None
            )
            if self._sio:
                bootstrap_summary = None
                if result.bootstrap_stats:
                    bootstrap_summary = {
                        k: v for k, v in result.bootstrap_stats.items()
                        if k not in ("net_profit_samples", "max_drawdown_samples")
                    }
                await self._sio.emit("backtest_complete", {
                    "sim_id":       sim_id,
                    "kpis":         result.kpis.as_dict(),
                    "trading_days": result.trading_days,
                    "total_trades": result.kpis.total_trades,
                    "bootstrap":    bootstrap_summary,
                    "report_url":   report_url,
                })

        except Exception as exc:
            logfire.error(f"run_backtest_background failed [{sim_id}]: {exc}")
            self._results.pop(sim_id, None)
            if self._sio:
                await self._sio.emit("backtest_error", {
                    "sim_id": sim_id,
                    "error":  str(exc),
                })

    # ================================================================== #
    #  Run full backtest (sync/polling path — kept for tests/backward compat)
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
        try:
            result.report_path = await self._generate_pdf_report(result)
        except Exception as pdf_err:
            logfire.error(f"PDF generation failed for sync run: {pdf_err}")

        sim_id = self._generate_sim_id(symbol, strategy_name)
        self._results[sim_id] = result

        return sim_id, result

    # ================================================================== #
    #  Retrieve stored result                                             #
    # ================================================================== #

    def get_result(self, sim_id: str) -> Optional[BacktestResult]:
        return self._results.get(sim_id)

    def is_pending(self, sim_id: str) -> bool:
        return sim_id in self._results and self._results[sim_id] is None

    def list_simulations(self) -> List[dict]:
        return [
            {"sim_id": sid, "status": "running"} if r is None else {"sim_id": sid, "status": "completed", "summary": r.summary()}
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
        session_signals: List[TradeSignal] = engine.run_session(m5, m1, account_size, config)

        if not session_signals:
            return {"signal": None, "reason": "No valid setup found in current session.", "source": result.get("source")}

        # Return the most recent signal for live display
        signal = session_signals[-1]

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
