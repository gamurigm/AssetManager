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
    FoldResult, CrossValidationResult,
)
from .engine.purged_kfold import PurgedKFoldSplitter
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
    # --- Cross-Validation (PurgedKFold) ---
    run_cv: bool = False         # set True to run PurgedKFold CV instead of a single backtest
    cv_n_splits: int = 5         # K folds
    cv_embargo_days: int = 5     # calendar days to exclude around each test window

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
                from .engine.stationary_bootstrap import StationaryBootstrap, recommend_block_length
                # Stationary Bootstrap (Politis & Romano, 1994):
                # Resample BLOCKS of consecutive trades (not individual trades)
                # to preserve the temporal autocorrelation structure.
                # Block length ~ N^(1/3) is the optimal rule of thumb.
                block_len = recommend_block_length(len(trades))
                sb = StationaryBootstrap(block_length=block_len)
                _need_samples = True  # needed for HTML report charts
                bootstrap_stats = sb.run(
                    trades,
                    config.account_size,
                    config.bootstrap_iterations,
                    return_samples=_need_samples,
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
    #  PurgedKFold Cross-Validation                                       #
    # ================================================================== #

    async def run_cv(self, config: BacktestConfig) -> CrossValidationResult:
        """
        Execute K-fold out-of-sample evaluation using PurgedKFold.

        Each fold scores the strategy on a held-out time window that was
        *never seen* during parameter selection, with a configurable
        embargo gap to prevent autocorrelation leakage.

        Returns
        -------
        CrossValidationResult
            Per-fold KPIs + aggregated mean/std statistics.
        """
        import statistics as stats_lib

        with logfire.span("BacktestRunner.run_cv", symbol=config.symbol,
                          n_splits=config.cv_n_splits,
                          embargo_days=config.cv_embargo_days):

            strategy_cfg = config.strategy_config()

            # 1. Fetch ALL candles once
            m1_candles, m5_candles = await self._fetch_candles(config)
            if not m1_candles:
                logfire.warning("run_cv: no M1 candles", symbol=config.symbol)
                return CrossValidationResult(
                    n_splits=config.cv_n_splits,
                    embargo_days=config.cv_embargo_days,
                    folds=[],
                    mean_win_rate=0.0, std_win_rate=0.0,
                    mean_profit_factor=0.0, std_profit_factor=0.0,
                    mean_sharpe=0.0, std_sharpe=0.0,
                    mean_expectancy_r=0.0, std_expectancy_r=0.0,
                )

            # 2. Split into sessions (chronologically sorted)
            all_sessions = self._split_into_sessions(m1_candles, m5_candles)

            if len(all_sessions) < config.cv_n_splits:
                raise ValueError(
                    f"Only {len(all_sessions)} sessions available but "
                    f"cv_n_splits={config.cv_n_splits}. "
                    "Extend the date range or reduce cv_n_splits."
                )

            # 3. Build splitter and iterate
            splitter = PurgedKFoldSplitter(
                n_splits=config.cv_n_splits,
                embargo_days=config.cv_embargo_days,
            )

            fold_results: List[FoldResult] = []

            for fold_idx, (train_sessions, test_sessions) in enumerate(
                splitter.split(all_sessions)
            ):
                if not test_sessions:
                    logfire.warning(f"run_cv: fold {fold_idx} has no test sessions — skipping")
                    continue

                test_start = str(test_sessions[0]["date"])
                test_end   = str(test_sessions[-1]["date"])

                logfire.info(
                    f"[CV] Fold {fold_idx}/{config.cv_n_splits - 1}",
                    test_start=test_start, test_end=test_end,
                    train_sessions=len(train_sessions), test_sessions=len(test_sessions),
                )

                # Score the strategy on the TEST fold only (out-of-sample)
                trades, trading_days, _ = self._run_session_loop(
                    test_sessions, strategy_cfg, config
                )

                kpis = self._kpi_calc.compute(trades, config.account_size, trading_days)

                fold_results.append(FoldResult(
                    fold_index=fold_idx,
                    train_days=len(train_sessions),
                    test_days=len(test_sessions),
                    test_start=test_start,
                    test_end=test_end,
                    kpis=kpis,
                    trades=trades,
                ))

            # 4. Aggregate KPI statistics across folds
            if not fold_results:
                return CrossValidationResult(
                    n_splits=config.cv_n_splits,
                    embargo_days=config.cv_embargo_days,
                    folds=[],
                    mean_win_rate=0.0, std_win_rate=0.0,
                    mean_profit_factor=0.0, std_profit_factor=0.0,
                    mean_sharpe=0.0, std_sharpe=0.0,
                    mean_expectancy_r=0.0, std_expectancy_r=0.0,
                )

            def _safe_std(values):
                return stats_lib.stdev(values) if len(values) > 1 else 0.0

            win_rates       = [f.kpis.win_rate for f in fold_results]
            profit_factors  = [f.kpis.profit_factor for f in fold_results]
            sharpes         = [f.kpis.sharpe_ratio for f in fold_results]
            expectancies    = [f.kpis.expectancy_r for f in fold_results]

            cv_result = CrossValidationResult(
                n_splits=config.cv_n_splits,
                embargo_days=config.cv_embargo_days,
                folds=fold_results,
                mean_win_rate=stats_lib.mean(win_rates),
                std_win_rate=_safe_std(win_rates),
                mean_profit_factor=stats_lib.mean(profit_factors),
                std_profit_factor=_safe_std(profit_factors),
                mean_sharpe=stats_lib.mean(sharpes),
                std_sharpe=_safe_std(sharpes),
                mean_expectancy_r=stats_lib.mean(expectancies),
                std_expectancy_r=_safe_std(expectancies),
            )

            logfire.info(
                "PurgedKFold CV completed",
                folds=len(fold_results),
                mean_win_rate=cv_result.mean_win_rate,
                mean_profit_factor=cv_result.mean_profit_factor,
            )
            return cv_result

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
        Group M1/M5 candles into daily sessions dynamically.
        Uses the first M5 candle of the day as the start of the session (ORB).
        Includes all subsequent M1 candles for that day to allow any strategy to run.
        """
        sessions: Dict[date, Dict] = {}

        # Ensure sorted chronologically
        m5_sorted = sorted(m5_candles, key=lambda x: x["timestamp"])
        m1_sorted = sorted(m1_candles, key=lambda x: x["timestamp"])

        # 1. Detect start of day
        for c in m5_sorted:
            try:
                ts_naive = datetime.fromisoformat(c["timestamp"].replace("Z", ""))
                d  = ts_naive.date()
                if d not in sessions:
                    sessions[d] = {"date": d, "m5": [c], "m1": [], "session_start": ts_naive}
                else:
                    sessions[d]["m5"].append(c)
            except (ValueError, KeyError):
                continue

        # 2. Append all subsequent M1 candles
        for c in m1_sorted:
            try:
                ts_naive = datetime.fromisoformat(c["timestamp"].replace("Z", ""))
                d  = ts_naive.date()
                
                if d in sessions:
                    session_start = sessions[d]["session_start"]
                    # Add M1 candles that happen after the ORB candle start time
                    if ts_naive > session_start:
                        sessions[d]["m1"].append(c)
            except (ValueError, KeyError):
                continue

        return sorted([s for s in sessions.values() if s["m1"]], key=lambda s: s["date"])

    @staticmethod
    def _find_candle_index(candles: List[CandleRow], timestamp: str) -> int:
        """Return the index of the candle matching a timestamp, or -1."""
        for i, c in enumerate(candles):
            if c["timestamp"].startswith(timestamp[:16]):   # compare up to minute
                return i
        return len(candles) - 1  # fallback: last candle
