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
import tempfile
from pathlib import Path
from typing import List, Optional
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
from .simulation_jobs import InMemorySimulationJobStore, SimulationJob


# --------------------------------------------------------------------------- #
#  Request / Response schemas (simple dicts — Pydantic models live in routes) #
# --------------------------------------------------------------------------- #

class SimulationService:
    """
    Façade that hides the composition details of BacktestRunner, StrategyFactory,
    and KPICalculator from the API layer and agent tools.

    S: only orchestrates simulation runs — no business logic itself.
    """

    def __init__(
        self,
        *,
        max_active_jobs: Optional[int] = None,
        max_history: Optional[int] = None,
        job_store: Optional[InMemorySimulationJobStore] = None,
    ) -> None:
        self._tasks: set[asyncio.Task] = set()
        active_limit = max(
            1,
            max_active_jobs
            if max_active_jobs is not None
            else int(os.getenv("SIMULATION_MAX_ACTIVE_JOBS", "4")),
        )
        history_limit = max(
            10,
            max_history
            if max_history is not None
            else int(os.getenv("SIMULATION_MAX_HISTORY", "100")),
        )
        self._job_store = job_store or InMemorySimulationJobStore(
            max_active_jobs=active_limit,
            max_history=history_limit,
        )
        self._sio = None

    # ================================================================== #
    #  Real-time configuration                                           #
    # ================================================================== #

    def configure_realtime(self, sio) -> None:
        """Register the Socket.IO server so background runs can broadcast events."""
        self._sio = sio

    def pre_register(
        self,
        symbol: str,
        strategy_name: str,
        owner_id: Optional[int] = None,
    ) -> str:
        """Reserve a bounded, queryable simulation job before execution starts."""
        sim_id = self._generate_sim_id(symbol, strategy_name)
        now = datetime.now(timezone.utc).isoformat()
        self._job_store.add(
            SimulationJob(
                sim_id=sim_id,
                symbol=symbol.strip().upper(),
                strategy_name=strategy_name,
                status="queued",
                created_at=now,
                updated_at=now,
                owner_id=owner_id,
            )
        )
        return sim_id

    def start_background(
        self, config: BacktestConfig, owner_id: Optional[int] = None
    ) -> str:
        """Create and retain one background task through the service façade."""
        sim_id = self.pre_register(config.symbol, config.strategy_name, owner_id)
        task = asyncio.create_task(self.run_backtest_background(sim_id, config))
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)
        return sim_id

    def _set_job_state(
        self,
        sim_id: str,
        status: str,
        *,
        result: Optional[BacktestResult] = None,
        error: Optional[str] = None,
    ) -> None:
        self._job_store.update(
            sim_id,
            status=status,
            updated_at=datetime.now(timezone.utc).isoformat(),
            result=result,
            error=error,
        )

    async def _generate_pdf_report(
        self, result: BacktestResult, owner_id: Optional[int] = None
    ) -> Optional[str]:
        """Generate a PDF report in a worker thread and return its filename."""
        from ..agents.strategies.report_generator import generate_pdf_report
        from .artifact_service import publish_report

        with tempfile.TemporaryDirectory(prefix="assetmanager-report-") as directory:
            path = Path(directory) / "backtest.pdf"
            await asyncio.to_thread(generate_pdf_report, result, str(path))
            return await publish_report(path, owner_id)

    def _make_callbacks(
        self,
        sim_id: str,
        loop: asyncio.AbstractEventLoop,
        owner_id: Optional[int] = None,
    ):
        """Return three thread-safe callbacks that emit Socket.IO events."""
        sio = self._sio
        room = f"user:{owner_id}" if owner_id is not None else None

        def on_progress(day: int, total: int) -> None:
            if not sio:
                return
            pct = round(day / total * 100) if total else 0
            asyncio.run_coroutine_threadsafe(
                sio.emit("backtest_progress", {
                    "sim_id": sim_id, "day": day,
                    "total": total, "pct": pct,
                }, room=room),
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
                        "gross_pnl_usd":  round(record.gross_pnl_usd, 2),
                        "fees_usd":       round(record.fees_usd, 2),
                        "entry_price":    record.entry_price,
                        "exit_price":     record.exit_price,
                        "exit_timestamp": str(record.exit_timestamp),
                        "execution_note": record.execution_note,
                    },
                    "equity": round(equity, 2),
                }, room=room),
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
                }, room=room),
                loop,
            )

        return on_progress, on_trade, on_bootstrap

    async def run_backtest_background(self, sim_id: str, config: BacktestConfig) -> None:
        """
        Run a full backtest as a fire-and-forget background task.
        Emits Socket.IO events: backtest_progress, backtest_trade,
        backtest_bootstrap_ready, backtest_complete, backtest_error.
        """
        self._set_job_state(sim_id, "running")
        job = self._job_store.get(sim_id)
        owner_id = job.owner_id if job else None
        loop = asyncio.get_running_loop()
        on_progress, on_trade, on_bootstrap = self._make_callbacks(
            sim_id, loop, owner_id
        )
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
                report_filename = await self._generate_pdf_report(result, owner_id)
                result.report_path = report_filename
            except Exception as pdf_err:
                logfire.error(f"PDF generation failed for {sim_id}: {pdf_err}")

            self._set_job_state(sim_id, "completed", result=result)

            report_url = (
                f"/view-reports/{report_filename}"
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
                }, room=f"user:{owner_id}" if owner_id is not None else None)

        except Exception as exc:
            logfire.error(f"run_backtest_background failed [{sim_id}]: {exc}")
            self._set_job_state(sim_id, "failed", error=str(exc))
            if self._sio:
                await self._sio.emit("backtest_error", {
                    "sim_id": sim_id,
                    "error":  str(exc),
                }, room=f"user:{owner_id}" if owner_id is not None else None)

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
        max_position_size: Optional[float] = None,
        use_atr_slippage: bool = False,
        atr_slippage_factor: float = 0.20,
        fixed_slippage_price: float = 0.0,
        commission_per_trade: float = 0.0,
        intrabar_fill_policy: str = "conservative",
        mark_expired_to_market: bool = True,
        run_bootstrap: bool = False,
        bootstrap_iterations: int = 1000,
        owner_id: Optional[int] = None,
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
            max_position_size=max_position_size,
            use_atr_slippage=use_atr_slippage,
            atr_slippage_factor=atr_slippage_factor,
            fixed_slippage_price=fixed_slippage_price,
            commission_per_trade=commission_per_trade,
            intrabar_fill_policy=intrabar_fill_policy,
            mark_expired_to_market=mark_expired_to_market,
            run_bootstrap=run_bootstrap,
            bootstrap_iterations=bootstrap_iterations
        )

        # Compose dependencies — DIP: runner only sees interfaces
        engine   = StrategyFactory.create(strategy_name)
        kpi_calc = ORBKPICalculator()
        runner   = BacktestRunner(engine, intraday_repository, kpi_calc)

        result = await runner.run(config)
        try:
            result.report_path = await self._generate_pdf_report(result, owner_id)
        except Exception as pdf_err:
            logfire.error(f"PDF generation failed for sync run: {pdf_err}")

        sim_id = self._generate_sim_id(symbol, strategy_name)
        now = datetime.now(timezone.utc).isoformat()
        self._job_store.add(
            SimulationJob(
                sim_id=sim_id,
                symbol=config.symbol,
                strategy_name=config.strategy_name,
                status="completed",
                created_at=now,
                updated_at=now,
                owner_id=owner_id,
                result=result,
            ),
            enforce_capacity=False,
        )

        return sim_id, result

    # ================================================================== #
    #  Retrieve stored result                                             #
    # ================================================================== #

    def get_result(
        self, sim_id: str, owner_id: Optional[int] = None
    ) -> Optional[BacktestResult]:
        job = self._job_store.get(sim_id, owner_id=owner_id)
        return job.result if job else None

    def get_job(self, sim_id: str, owner_id: Optional[int] = None) -> Optional[dict]:
        job = self._job_store.get(sim_id, owner_id=owner_id)
        return job.as_dict() if job else None

    def is_pending(self, sim_id: str) -> bool:
        job = self._job_store.get(sim_id)
        return bool(job and job.status in {"queued", "running"})

    def list_simulations(self, owner_id: Optional[int] = None) -> List[dict]:
        return [
            job.as_dict()
            for job in self._job_store.list(owner_id=owner_id)
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
