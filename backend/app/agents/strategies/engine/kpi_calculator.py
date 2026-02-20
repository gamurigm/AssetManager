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
                max_drawdown_pct=0.0, sharpe_ratio=0.0, avg_rr_realized=0.0,
                total_r=0.0, final_equity=initial_equity, cagr=0.0,
            )

        wins   = [t for t in trades if t.is_win]
        losses = [t for t in trades if t.is_loss]

        total_trades = len(trades)
        n_wins   = len(wins)
        n_losses = len(losses)
        win_rate = n_wins / total_trades if total_trades > 0 else 0.0

        # — Expectancy (in R) —
        avg_win_r  = statistics.mean(t.pnl_r for t in wins)   if wins   else 0.0
        avg_loss_r = statistics.mean(abs(t.pnl_r) for t in losses) if losses else 0.0
        loss_rate  = 1.0 - win_rate
        expectancy_r = (win_rate * avg_win_r) - (loss_rate * avg_loss_r)

        # — Profit Factor —
        gross_profit = sum(t.pnl_usd for t in wins)
        gross_loss   = sum(abs(t.pnl_usd) for t in losses)
        profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else float("inf")

        # — Running equity & Max Drawdown —
        equity = initial_equity
        peak   = initial_equity
        max_dd = 0.0
        daily_returns: List[float] = []

        for t in trades:
            prev_equity = equity
            equity += t.pnl_usd
            daily_returns.append((equity - prev_equity) / prev_equity if prev_equity > 0 else 0.0)
            if equity > peak:
                peak = equity
            dd = (peak - equity) / peak if peak > 0 else 0.0
            max_dd = max(max_dd, dd)

        # — Sharpe Ratio (annualised, risk-free ≈ 0) —
        if len(daily_returns) > 1:
            avg_ret = statistics.mean(daily_returns)
            std_ret = statistics.stdev(daily_returns)
            # Annualise: √252 trading days
            sharpe = (avg_ret / std_ret * math.sqrt(252)) if std_ret > 0 else 0.0
        else:
            sharpe = 0.0

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
