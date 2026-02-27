"""
Stationary Bootstrap (stationary_bootstrap.py)
================================================
Implements the Stationary Bootstrap (Politis & Romano, 1994) for
financial time series — the correct alternative to i.i.d. bootstrap
when observations are serially correlated.

Key difference from classical bootstrap:
  - Classical: resample trades individually with replacement (destroys temporal structure)
  - Stationary: resample OVERLAPPING BLOCKS of random geometric length
    (preserves autocorrelation structure)

The expected block length L controls the autocorrelation preservation:
  - L=1  → degenerates to i.i.d. bootstrap
  - L=N  → single block (no resampling, useless)
  - L=5  → good default for daily trading signals

References:
  Politis, D.N. & Romano, J.P. (1994). "The Stationary Bootstrap."
  Journal of the American Statistical Association, 89(428), 1303–1313.

  Sullivan, R., Timmermann, A., & White, H. (1999). "Data-Snooping,
  Technical Trading Rule Performance, and the Bootstrap."
  Journal of Finance, 54(5), 1647–1691.
"""

from __future__ import annotations

import math
import random
import statistics
import numpy as np
from typing import List, Dict, Any, Optional

from .interfaces import TradeRecord


class StationaryBootstrap:
    """
    Stationary Bootstrap for financial trade sequences.

    Parameters
    ----------
    block_length : int
        Expected block length L (geometric distribution parameter).
        Rule of thumb: L ~ N^(1/3) where N = number of trades.
        For daily strategies with ~100 trades: L ≈ 5.
    seed : int | None
        Optional random seed for reproducibility.
    """

    def __init__(self, block_length: int = 5, seed: Optional[int] = None):
        if block_length < 1:
            raise ValueError("block_length must be >= 1")
        self.block_length = block_length
        self._rng = random.Random(seed)

    # ------------------------------------------------------------------ #
    #  Core: generate one bootstrap sample                                #
    # ------------------------------------------------------------------ #

    def _resample_pnl(self, pnl: List[float]) -> List[float]:
        """
        Generate one bootstrap sample of PnL values using stationary
        block bootstrap.

        The probability of starting a new block at each step is p = 1/L,
        where L = block_length. This gives geometrically distributed block
        lengths with mean = L, which is the stationary bootstrap definition.
        """
        n = len(pnl)
        if n == 0:
            return []

        p = 1.0 / self.block_length  # probability of new block start
        sample = []
        start = self._rng.randint(0, n - 1)  # random initial position
        current = start

        while len(sample) < n:
            sample.append(pnl[current])
            # Move to next position: with prob p start a new random block,
            # otherwise advance sequentially (wrap around)
            if self._rng.random() < p:
                current = self._rng.randint(0, n - 1)
            else:
                current = (current + 1) % n

        return sample[:n]

    def _equity_curve(self, pnl_sample: List[float], initial_equity: float) -> List[float]:
        """Compute running equity curve from PnL sample."""
        curve = [initial_equity]
        equity = initial_equity
        for pnl in pnl_sample:
            equity += pnl
            curve.append(equity)
        return curve

    def _max_drawdown(self, equity_curve: List[float]) -> float:
        """Peak-to-trough max drawdown as a fraction."""
        if not equity_curve:
            return 0.0
        peak = equity_curve[0]
        max_dd = 0.0
        for v in equity_curve:
            if v > peak:
                peak = v
            dd = (peak - v) / peak if peak > 0 else 0.0
            max_dd = max(max_dd, dd)
        return max_dd

    # ------------------------------------------------------------------ #
    #  Public: run N iterations                                           #
    # ------------------------------------------------------------------ #

    def run(
        self,
        trades: List[TradeRecord],
        initial_equity: float,
        iterations: int = 10_000,
        return_samples: bool = False,
    ) -> Dict[str, Any]:
        """
        Run stationary bootstrap resampling.

        Parameters
        ----------
        trades : list of TradeRecord
            Must be in chronological order.
        initial_equity : float
            Starting account equity.
        iterations : int
            Number of bootstrap iterations.
        return_samples : bool
            If True, include full per-iteration arrays (needed for charts).

        Returns
        -------
        dict with:
            net_profit_95_ci        : [p2.5, p97.5] in USD
            max_drawdown_95_ci_pct  : [p2.5, p97.5] as fractions
            iterations              : int
            sample_size             : int
            method                  : 'stationary_bootstrap'
            block_length            : int
            [net_profit_samples]    : list of floats (if return_samples)
            [max_drawdown_samples]  : list of floats (if return_samples)
        """
        if not trades:
            return {
                "net_profit_95_ci": [0.0, 0.0],
                "max_drawdown_95_ci_pct": [0.0, 0.0],
                "iterations": 0,
                "sample_size": 0,
                "method": "stationary_bootstrap",
                "block_length": self.block_length,
            }

        pnl = [t.pnl_usd for t in trades]
        n = len(pnl)

        # Auto-select block length if not manually set
        # Rule of thumb: L ~ N^(1/3), minimum 3
        effective_block_length = max(3, min(self.block_length, n // 2))

        # --- CUDA Acceleration Path ---
        from app.core.acceleration import accelerant
        if accelerant.is_available() and iterations >= 100:
            net_profits, max_drawdowns = accelerant.run_bootstrap_parallel(
                np.array(pnl), iterations, effective_block_length, initial_equity
            )
            net_profits = net_profits.tolist()
            max_drawdowns = max_drawdowns.tolist()
        else:
            # --- Legacy CPU Path ---
            net_profits: List[float] = []
            max_drawdowns: List[float] = []

            for _ in range(iterations):
                sample = self._resample_pnl(pnl)
                net_profit = sum(sample)
                curve = self._equity_curve(sample, initial_equity)
                max_dd = self._max_drawdown(curve)
                net_profits.append(net_profit)
                max_drawdowns.append(max_dd)

        # 95% CI = [2.5th percentile, 97.5th percentile]
        net_profits_sorted = sorted(net_profits)
        max_dd_sorted = sorted(max_drawdowns)

        idx_lo = int(math.floor(0.025 * iterations))
        idx_hi = int(math.floor(0.975 * iterations))

        result: Dict[str, Any] = {
            "net_profit_95_ci": [
                round(net_profits_sorted[idx_lo], 2),
                round(net_profits_sorted[idx_hi], 2),
            ],
            "max_drawdown_95_ci_pct": [
                round(max_dd_sorted[idx_lo], 4),
                round(max_dd_sorted[idx_hi], 4),
            ],
            "iterations": iterations,
            "sample_size": n,
            "method": "stationary_bootstrap",
            "block_length": effective_block_length,
            # Bonus stats
            "net_profit_mean": round(statistics.mean(net_profits), 2),
            "net_profit_std": round(statistics.stdev(net_profits) if n > 1 else 0.0, 2),
            "max_dd_mean": round(statistics.mean(max_drawdowns), 4),
        }

        if return_samples:
            result["net_profit_samples"] = net_profits
            result["max_drawdown_samples"] = max_drawdowns

        return result


def recommend_block_length(n_trades: int) -> int:
    """
    Politis & Romano rule of thumb: L ≈ N^(1/3).
    Minimum 3, maximum 20 for typical trade counts.
    """
    return max(3, min(20, round(n_trades ** (1 / 3))))
