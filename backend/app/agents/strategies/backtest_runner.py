"""
Backtest Runner (backtest_runner.py)
======================================
Orchestrates a full historical simulation over multiple sessions.

Design Patterns applied:
  - Template Method: _run_session_loop() defines the algorithm skeleton.
    Subclasses can override _on_signal(), _on_trade_close() for hooks.
  - Dependency Inversion: depends on IStrategyEngine, IIntradayRepository,
    IKPICalculator — all interfaces, not concrete classes.
  - Observer: CircuitBreaker registers a stop callback.

Entry point: SimulationService (Façade) calls BacktestRunner.run().
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, date, timedelta, timezone
from typing import List, Optional, Dict
import logfire

from .engine import (
    IStrategyEngine, IKPICalculator,
    StrategyConfig, TradeSignal, TradeRecord, KPIResult, CircuitBreaker,
    ORBFVGEngine, ORBKPICalculator,
)
from ...services.intraday_repository import IIntradayRepository, CandleRow, intraday_repository


# --------------------------------------------------------------------------- #
#  Configuration                                                               #
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class BacktestConfig:
    """Input parameters for one backtest run."""
    symbol: str
    start_date: str         # YYYY-MM-DD
    end_date: str           # YYYY-MM-DD
    account_size: float = 10_000.0
    strategy_name: str = "ORB_FVG_ENGULFING"
    strategy_params: dict = field(default_factory=dict)
    pip_value: float = 1.0  # 1.0 per pip/unit (set per instrument)
    run_bootstrap: bool = False
    bootstrap_iterations: int = 10000

    def strategy_config(self) -> StrategyConfig:
        return StrategyConfig.from_dict(self.strategy_params) if self.strategy_params else StrategyConfig.default()


@dataclass
class BacktestResult:
    """Full result from one backtest run."""
    config: BacktestConfig
    trades: List[TradeRecord]
    kpis: KPIResult
    trading_days: int
    missing_data_days: int
    bootstrap_stats: Optional[dict] = None
    report_path: Optional[str] = None

    def summary(self) -> dict:
        summary_dict = {
            "symbol": self.config.symbol,
            "start_date": self.config.start_date,
            "end_date": self.config.end_date,
            "account_size": self.config.account_size,
            "strategy": self.config.strategy_name,
            "trading_days": self.trading_days,
            "missing_data_days": self.missing_data_days,
            "report_path": self.report_path,
            **self.kpis.as_dict(),
        }
        if self.bootstrap_stats:
            summary_dict["bootstrap"] = self.bootstrap_stats
        return summary_dict


# --------------------------------------------------------------------------- #
#  Backtest Runner                                                             #
# --------------------------------------------------------------------------- #

# NY session window for ORB strategy
_SESSION_START_H = 9
_SESSION_START_M = 30
_SESSION_END_H   = 11
_SESSION_END_M   = 0


class BacktestRunner:
    """
    Runs a multi-day historical simulation.

    Args:
        strategy:   IStrategyEngine — concrete engine (e.g. ORBFVGEngine).
        repository: IIntradayRepository — data source.
        kpi_calc:   IKPICalculator — post-processing.
    """

    def __init__(
        self,
        strategy: IStrategyEngine,
        repository: IIntradayRepository,
        kpi_calc: IKPICalculator,
    ):
        # DIP: all dependencies are injected as abstractions
        self._strategy   = strategy
        self._repository = repository
        self._kpi_calc   = kpi_calc
        self._stop_flag  = False

    # ================================================================== #
    #  Public entry point                                                 #
    # ================================================================== #

    async def run(self, config: BacktestConfig) -> BacktestResult:
        """
        Execute the full backtest.
        Template Method pattern: skeleton defined here, details in helpers.
        """
        with logfire.span("BacktestRunner.run", symbol=config.symbol,
                          start=config.start_date, end=config.end_date):

            strategy_cfg = config.strategy_config()

            # --- Fetch all intraday candles (M1 + M5) ---
            m1_candles, m5_candles = await self._fetch_candles(config)

            if not m1_candles:
                logfire.warning("BacktestRunner: no M1 candles available", symbol=config.symbol)
                empty_kpis = self._kpi_calc.compute([], config.account_size, 0)
                return BacktestResult(config=config, trades=[], kpis=empty_kpis,
                                      trading_days=0, missing_data_days=0, bootstrap_stats=None)

            # --- Group into sessions ---
            sessions = self._split_into_sessions(m1_candles, m5_candles)

            # --- Run session loop ---
            trades, trading_days, missing_days = self._run_session_loop(
                sessions, strategy_cfg, config
            )

            # --- Compute KPIs ---
            kpis = self._kpi_calc.compute(trades, config.account_size, trading_days)

            # --- Bootstrap Resampling (Optional) ---
            bootstrap_stats = None
            if config.run_bootstrap and len(trades) > 0:
                from .engine.bootstrap_analyzer import bootstrap_analyzer
                bootstrap_stats = bootstrap_analyzer.run_bootstrap(
                    trades, 
                    config.account_size, 
                    config.bootstrap_iterations
                )

            logfire.info("Backtest completed",
                         symbol=config.symbol, trades=len(trades),
                         win_rate=kpis.win_rate, profit_factor=kpis.profit_factor)

            result = BacktestResult(
                config=config,
                trades=trades,
                kpis=kpis,
                trading_days=trading_days,
                missing_data_days=missing_days,
                bootstrap_stats=bootstrap_stats
            )

            # --- Generate Visual Report if Bootstrap is active ---
            report_path = None
            if bootstrap_stats is not None:
                try:
                    from .report_generator import generate_html_report
                    import os
                    from datetime import datetime
                    
                    reports_dir = os.path.join(os.getcwd(), "reports")
                    os.makedirs(reports_dir, exist_ok=True)
                    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    report_filename = f"bootstrap_report_{config.symbol}_{stamp}.html"
                    full_report_path = os.path.join(reports_dir, report_filename)
                    
                    generate_html_report(
                        BacktestResult(config, trades, kpis, trading_days, missing_days, bootstrap_stats), 
                        full_report_path
                    )
                    report_path = report_filename # Store only filename for URL construction
                    logfire.info(f"Visual Bootstrap Report generated: {full_report_path}")
                except Exception as e:
                    logfire.error(f"Failed to generate HTML report: {e}")

            return BacktestResult(
                config=config,
                trades=trades,
                kpis=kpis,
                trading_days=trading_days,
                missing_data_days=missing_days,
                bootstrap_stats=bootstrap_stats,
                report_path=report_path
            )

    # ================================================================== #
    #  Template Method — session loop                                     #
    # ================================================================== #

    def _run_session_loop(
        self,
        sessions: List[Dict],
        cfg: StrategyConfig,
        run_config: BacktestConfig,
    ) -> tuple:
        """
        Core loop — iterates over sessions, runs the engine, simulates trades.
        Circuit breaker is per-run (not per-day: monthly DD tracked across days).
        """
        trades: List[TradeRecord] = []
        trading_days = 0
        missing_days = 0
        current_equity = run_config.account_size
        last_month: Optional[int] = None

        breaker = CircuitBreaker(
            max_daily_losses=cfg.max_daily_losses,
            max_daily_drawdown_pct=cfg.max_daily_drawdown_pct,
            max_monthly_drawdown_pct=cfg.max_monthly_drawdown_pct,
        )
        breaker.on_trip(lambda reason: logfire.warning(f"[Backtest] CircuitBreaker: {reason}"))

        for session in sessions:
            session_date: date = session["date"]
            m5 = session["m5"]
            m1 = session["m1"]

            if not m1 or not m5:
                missing_days += 1
                continue

            trading_days += 1

            # Monthly reset
            if last_month is not None and session_date.month != last_month:
                breaker.new_month()
            last_month = session_date.month

            # Daily reset of daily counters
            breaker.new_day()

            # Circuit breaker check (monthly may still be tripped)
            if breaker.is_triggered():
                logfire.info(f"[Backtest] Day {session_date} skipped — breaker tripped")
                continue

            # Run strategy engine — pure, deterministic
            signal = self._strategy.run_session(
                m5_candles=m5,
                m1_candles=m1,
                account_size=current_equity,
                config=cfg,
            )

            if signal is None:
                continue

            # Hook for subclasses
            self._on_signal(signal, session_date)

            # Simulate the trade against remaining M1 candles
            confirmation_idx = self._find_candle_index(m1, signal.timestamp)
            remaining_m1 = m1[confirmation_idx + 1:] if confirmation_idx >= 0 else []

            record = self._simulate_trade(signal, remaining_m1, run_config.pip_value)
            trades.append(record)

            # Update equity
            current_equity += record.pnl_usd

            # Notify circuit breaker
            risk_amount = run_config.account_size * cfg.risk_per_trade
            loss_pct = risk_amount / run_config.account_size

            if record.is_loss:
                breaker.record_loss(loss_pct)
            elif record.is_win:
                gain_pct = record.pnl_usd / run_config.account_size
                breaker.record_win(gain_pct)

            self._on_trade_close(record, current_equity)

        return trades, trading_days, missing_days

    # ================================================================== #
    #  Template Method hooks (override in subclasses for extensions)      #
    # ================================================================== #

    def _on_signal(self, signal: TradeSignal, session_date: date) -> None:
        """Called when a valid signal is generated. Override for side-effects."""
        logfire.info(f"[Backtest] Signal generated",
                     date=str(session_date), direction=signal.direction,
                     entry=signal.entry, stop=signal.stop, tp=signal.tp)

    def _on_trade_close(self, record: TradeRecord, equity: float) -> None:
        """Called after each trade is resolved. Override for logging, UI push, etc."""
        logfire.info(f"[Backtest] Trade closed",
                     outcome=record.outcome, pnl_r=record.pnl_r,
                     pnl_usd=record.pnl_usd, equity=equity)

    # ================================================================== #
    #  Trade Simulation                                                   #
    # ================================================================== #

    @staticmethod
    def _simulate_trade(
        signal: TradeSignal,
        remaining_m1: List[CandleRow],
        pip_value: float = 1.0,
    ) -> TradeRecord:
        """
        Walk forward through M1 candles until SL or TP is hit.
        Slippage model: 1 pip assumed on entry.
        """
        slippage_pips = 1.0  # conservative fixed slippage

        for candle in remaining_m1:
            h = candle["high"]
            l = candle["low"]

            if signal.direction == "SHORT":
                if l <= signal.tp:        # TP hit first (price moved down)
                    pnl_r    = signal.tp / signal.risk_pips if signal.risk_pips else 0
                    pnl_usd  = signal.risk_pips * pip_value * 3.0  # 3R
                    return TradeRecord(
                        signal=signal, outcome="win_tp",
                        exit_price=signal.tp,
                        exit_timestamp=candle["timestamp"],
                        pnl_r=3.0,
                        pnl_usd=pnl_usd,
                        slippage_pips=slippage_pips,
                    )
                if h >= signal.stop:      # SL hit
                    pnl_usd = -(signal.risk_pips * pip_value * 1.0)  # -1R
                    return TradeRecord(
                        signal=signal, outcome="loss_sl",
                        exit_price=signal.stop + slippage_pips,
                        exit_timestamp=candle["timestamp"],
                        pnl_r=-1.0,
                        pnl_usd=pnl_usd,
                        slippage_pips=slippage_pips,
                    )
            else:  # LONG
                if h >= signal.tp:        # TP hit
                    pnl_usd = signal.risk_pips * pip_value * 3.0
                    return TradeRecord(
                        signal=signal, outcome="win_tp",
                        exit_price=signal.tp,
                        exit_timestamp=candle["timestamp"],
                        pnl_r=3.0,
                        pnl_usd=pnl_usd,
                        slippage_pips=slippage_pips,
                    )
                if l <= signal.stop:      # SL hit
                    pnl_usd = -(signal.risk_pips * pip_value * 1.0)
                    return TradeRecord(
                        signal=signal, outcome="loss_sl",
                        exit_price=signal.stop - slippage_pips,
                        exit_timestamp=candle["timestamp"],
                        pnl_r=-1.0,
                        pnl_usd=pnl_usd,
                        slippage_pips=slippage_pips,
                    )

        # Expired: no SL/TP hit before session end
        return TradeRecord(
            signal=signal, outcome="expired",
            exit_price=signal.entry,
            exit_timestamp="",
            pnl_r=0.0,
            pnl_usd=0.0,
            slippage_pips=slippage_pips,
        )

    # ================================================================== #
    #  Data Fetching & Session Splitting                                  #
    # ================================================================== #

    async def _fetch_candles(self, config: BacktestConfig) -> tuple:
        """
        Fetch M1 and M5 candles from the repository (DuckDB) or Yahoo Finance.
        Runs both fetches concurrently.
        """
        from ...services.market_data import market_data_service

        # Yahoo finance period ~ '5d', '1mo', '3mo' (limited to 7 days for 1m)
        # For backtests > 7 days, we rely on DuckDB if pre-populated.
        # period="1mo" returns 5m data for months; "7d" returns 1m data.
        period_m1 = "7d"    # max for 1m
        period_m5 = "1mo"   # longer range for 5m

        m1_task = asyncio.create_task(
            market_data_service.get_intraday(config.symbol, "1m", period_m1,
                                              config.start_date, config.end_date)
        )
        m5_task = asyncio.create_task(
            market_data_service.get_intraday(config.symbol, "5m", period_m5,
                                              config.start_date, config.end_date)
        )
        m1_result, m5_result = await asyncio.gather(m1_task, m5_task)

        m1_candles: List[CandleRow] = m1_result.get("candles", []) if "candles" in m1_result else []
        m5_candles: List[CandleRow] = m5_result.get("candles", []) if "candles" in m5_result else []

        return m1_candles, m5_candles

    @staticmethod
    def _split_into_sessions(
        m1_candles: List[CandleRow],
        m5_candles: List[CandleRow],
    ) -> List[Dict]:
        """
        Group M1/M5 candles into daily sessions: 09:30–11:00 NY.
        Returns list of {date, m5: [CandleRow], m1: [CandleRow]}.
        """
        import pytz
        utc_zone = pytz.utc
        ny_zone = pytz.timezone("America/New_York")
        sessions: Dict[date, Dict] = {}

        for c in m5_candles:
            try:
                # Timestamps from our providers (Yahoo/Polygon) are generally localized 
                # to the market timezone (NY) in naive format
                ts_naive = datetime.fromisoformat(c["timestamp"].replace("Z", ""))
                d  = ts_naive.date()
                if ts_naive.hour == _SESSION_START_H and ts_naive.minute == _SESSION_START_M:
                    sessions.setdefault(d, {"date": d, "m5": [], "m1": []})["m5"].append(c)
            except (ValueError, KeyError):
                continue

        for c in m1_candles:
            try:
                ts_naive = datetime.fromisoformat(c["timestamp"].replace("Z", ""))
                d  = ts_naive.date()
                
                # We need to capture candles in the window 09:35 to 11:00 for M1
                # Wait: _SESSION_START_H is 9, _SESSION_START_M is 30. M1 starts at 9:35
                in_window = False
                if ts_naive.hour == _SESSION_START_H and ts_naive.minute >= _SESSION_START_M + 5:
                    in_window = True
                elif ts_naive.hour > _SESSION_START_H and ts_naive.hour < _SESSION_END_H:
                    in_window = True
                elif ts_naive.hour == _SESSION_END_H and ts_naive.minute == _SESSION_END_M:
                    in_window = True

                if in_window:
                    if d not in sessions:
                        sessions[d] = {"date": d, "m5": [], "m1": []}
                    sessions[d]["m1"].append(c)
            except (ValueError, KeyError):
                continue

        return sorted(sessions.values(), key=lambda s: s["date"])

    @staticmethod
    def _find_candle_index(candles: List[CandleRow], timestamp: str) -> int:
        """Return the index of the candle matching a timestamp, or -1."""
        for i, c in enumerate(candles):
            if c["timestamp"].startswith(timestamp[:16]):   # compare up to minute
                return i
        return len(candles) - 1  # fallback: last candle
