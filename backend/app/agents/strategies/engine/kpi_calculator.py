"""
KPI Calculator (kpi_calculator.py)
=====================================
Implements IKPICalculator.
All formulas from Section 8 of the strategy document.
Pure functions — no I/O, no state.
"""

from __future__ import annotations

import math
import statistics
from typing import List

from .models import TradeRecord, KPIResult


class ORBKPICalculator:
    """
    Concrete IKPICalculator for the ORB FVG Engulfing strategy.
    S: Sole responsibility is computing KPIs.
    """

    def compute(
        self,
        trades: List[TradeRecord],
        initial_equity: float,
        trading_days: int,
    ) -> KPIResult:
        """
        Args:
            trades:        All TradeRecords from the backtest.
            initial_equity: Starting account value.
            trading_days:  Actual number of trading days in the backtest window.

        Returns:
            KPIResult with all metrics from Section 8.
        """
        if not trades:
            return KPIResult(
                total_trades=0, wins=0, losses=0,
                win_rate=0.0, expectancy_r=0.0, profit_factor=0.0,
                max_drawdown_pct=0.0, sharpe_ratio=0.0, sortino_ratio=0.0,
                avg_rr_realized=0.0, total_r=0.0, final_equity=initial_equity, cagr=0.0,
            )

        wins   = [t for t in trades if t.is_win]
        losses = [t for t in trades if t.is_loss]

        total_trades = len(trades)
        n_wins   = len(wins)
        n_losses = len(losses)
        resolved_trades = n_wins + n_losses
        win_rate = n_wins / resolved_trades if resolved_trades > 0 else 0.0

        # — Expectancy (in R) —
        avg_win_r  = statistics.mean(t.pnl_r for t in wins)   if wins   else 0.0
        avg_loss_r = statistics.mean(abs(t.pnl_r) for t in losses) if losses else 0.0
        loss_rate  = n_losses / resolved_trades if resolved_trades > 0 else 0.0
        expectancy_r = (win_rate * avg_win_r) - (loss_rate * avg_loss_r)

        # — Profit Factor —
        gross_profit = sum(t.pnl_usd for t in wins)
        gross_loss   = sum(abs(t.pnl_usd) for t in losses)
        profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else float("inf")

        # — Running equity & Max Drawdown —
        equity = initial_equity
        peak   = initial_equity
        max_dd = 0.0
        
        # Group trades by date for daily return series
        daily_pnl: Dict[str, float] = {}
        
        for t in trades:
            # signal.timestamp is ISO-8601 like "2026-03-11T09:35:42Z"
            day_key = t.signal.timestamp[:10]
            daily_pnl[day_key] = daily_pnl.get(day_key, 0.0) + t.pnl_usd
            
            # Update equity & peak for max drawdown (per trade resolution is safer for DD)
            equity += t.pnl_usd
            if equity > peak:
                peak = equity
            dd = (peak - equity) / peak if peak > 0 else 0.0
            max_dd = max(max_dd, dd)

        # — Corrected Sharpe Ratio (annualised) —
        # Strategy returns are often sparse (e.g. 19 trades in 252 days).
        # We MUST include 233 zero-return days to get a realistic volatility.
        num_active_days = len(daily_pnl)
        num_zero_days = max(0, trading_days - num_active_days)
        
        daily_returns: List[float] = []
        running_equity_for_ret = initial_equity
        
        # Add active days
        for day in sorted(daily_pnl):
            pnl = daily_pnl[day]
            daily_returns.append(pnl / running_equity_for_ret if running_equity_for_ret > 0 else 0.0)
            running_equity_for_ret += pnl
            
        # Add inactive days
        daily_returns.extend([0.0] * num_zero_days)

        if len(daily_returns) > 1:
            avg_ret = statistics.mean(daily_returns)
            std_ret = statistics.stdev(daily_returns)
            sharpe = (avg_ret / std_ret * math.sqrt(252)) if std_ret > 0 else 0.0
            
            # — Corrected Sortino Ratio (annualised) —
            downside_returns = [r for r in daily_returns if r < 0]
            if downside_returns:
                downside_std = statistics.stdev(downside_returns + [0.0] * (len(daily_returns) - len(downside_returns)))
                sortino = (avg_ret / downside_std * math.sqrt(252)) if downside_std > 0 else 0.0
            else:
                sortino = sharpe # if no losses, sortino is infinite or same as sharpe conceptually here
        else:
            sharpe = 0.0
            sortino = 0.0

        # — Average Realised RR —
        avg_rr = statistics.mean(abs(t.pnl_r) for t in wins) if wins else 0.0

        # — Total R —
        total_r = sum(t.pnl_r for t in trades)

        # — CAGR —
        cagr = self._cagr(initial_equity, equity, trading_days)

        return KPIResult(
            total_trades=total_trades,
            wins=n_wins,
            losses=n_losses,
            win_rate=round(win_rate, 4),
            expectancy_r=round(expectancy_r, 4),
            profit_factor=round(profit_factor, 4),
            max_drawdown_pct=round(max_dd, 4),
            sharpe_ratio=round(sharpe, 4),
            sortino_ratio=round(sortino, 4),
            avg_rr_realized=round(avg_rr, 4),
            total_r=round(total_r, 4),
            final_equity=round(equity, 2),
            cagr=round(cagr, 4),
        )

    @staticmethod
    def _cagr(start: float, end: float, trading_days: int) -> float:
        """
        Compound Annual Growth Rate.
        CAGR = (end/start)^(252/trading_days) - 1
        """
        if start <= 0 or trading_days <= 0:
            return 0.0
        years = trading_days / 252.0
        if years == 0:
            return 0.0
        ratio = end / start
        if ratio <= 0:
            return -1.0
        return ratio ** (1.0 / years) - 1.0
