"""
Strategy Engine — Circuit Breaker (circuit_breaker.py)
=======================================================
Implements the Observer Pattern:
  - CircuitBreaker maintains internal state.
  - On every loss/drawdown event it calls registered callbacks.
  - BacktestRunner registers a callback to stop the session loop.

SOLID:
  - S: Only manages daily/monthly risk limits, nothing else.
  - O: Add new trigger conditions by subclassing or via callbacks.
  - D: BacktestRunner receives a CircuitBreaker instance, not a concrete type.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional
import logfire


# --------------------------------------------------------------------------- #
#  Circuit Breaker                                                             #
# --------------------------------------------------------------------------- #

@dataclass
class CircuitBreaker:
    """
    Tracks intra-day and intra-month risk thresholds as defined in
    Sections 4.3 and 9.1 of the strategy document.

    Callbacks are called once when the breaker trips.
    """
    max_daily_losses: int = 2
    max_daily_drawdown_pct: float = 0.02        # 2% intraday
    max_monthly_drawdown_pct: float = 0.10       # 10% monthly

    _daily_losses: int = field(default=0, init=False, repr=False)
    _daily_drawdown_pct: float = field(default=0.0, init=False, repr=False)
    _monthly_drawdown_pct: float = field(default=0.0, init=False, repr=False)
    _triggered: bool = field(default=False, init=False, repr=False)
    _triggered_reason: Optional[str] = field(default=None, init=False, repr=False)
    _callbacks: List[Callable[[str], None]] = field(default_factory=list, init=False, repr=False)

    # ------------------------------------------------------------------ #
    #  Observer registration                                              #
    # ------------------------------------------------------------------ #

    def on_trip(self, callback: Callable[[str], None]) -> None:
        """Register a callback to be called when the breaker trips."""
        self._callbacks.append(callback)

    # ------------------------------------------------------------------ #
    #  Recording events                                                   #
    # ------------------------------------------------------------------ #

    def record_loss(self, loss_pct: float = 0.0) -> bool:
        """
        Record a losing trade.
        Args:
            loss_pct: The loss as a fraction of account (e.g. 0.005 for 0.5%).
        Returns:
            True if the circuit breaker was just triggered.
        """
        self._daily_losses += 1
        self._daily_drawdown_pct += loss_pct
        self._monthly_drawdown_pct += loss_pct
        return self._check()

    def record_win(self, gain_pct: float = 0.0) -> None:
        """Record a winning trade (resets consecutive-loss counter)."""
        # wins do not reset monthly drawdown — only equity recovery does
        self._daily_drawdown_pct = max(0.0, self._daily_drawdown_pct - gain_pct)

    # ------------------------------------------------------------------ #
    #  State queries                                                      #
    # ------------------------------------------------------------------ #

    def is_triggered(self) -> bool:
        return self._triggered

    def reason(self) -> Optional[str]:
        return self._triggered_reason

    def daily_losses(self) -> int:
        return self._daily_losses

    # ------------------------------------------------------------------ #
    #  Day/month resets                                                   #
    # ------------------------------------------------------------------ #

    def new_day(self) -> None:
        """Call at the start of each trading day to reset daily counters."""
        self._daily_losses = 0
        self._daily_drawdown_pct = 0.0
        self._triggered = False
        self._triggered_reason = None

    def new_month(self) -> None:
        """Call at month boundary to reset monthly counters."""
        self.new_day()
        self._monthly_drawdown_pct = 0.0

    # ------------------------------------------------------------------ #
    #  Internal trigger logic                                             #
    # ------------------------------------------------------------------ #

    def _check(self) -> bool:
        """Evaluate all conditions; trip the breaker if any is exceeded."""
        if self._triggered:
            return False  # already tripped

        reason: Optional[str] = None

        if self._daily_losses >= self.max_daily_losses:
            reason = (
                f"Daily loss limit reached: {self._daily_losses} consecutive losses "
                f"(max={self.max_daily_losses})"
            )
        elif self._daily_drawdown_pct >= self.max_daily_drawdown_pct:
            reason = (
                f"Intraday drawdown limit: {self._daily_drawdown_pct:.2%} "
                f"(max={self.max_daily_drawdown_pct:.2%})"
            )
        elif self._monthly_drawdown_pct >= self.max_monthly_drawdown_pct:
            reason = (
                f"Monthly drawdown limit: {self._monthly_drawdown_pct:.2%} "
                f"(max={self.max_monthly_drawdown_pct:.2%})"
            )

        if reason:
            self._triggered = True
            self._triggered_reason = reason
            logfire.warning(f"[CircuitBreaker] TRIPPED: {reason}")
            for cb in self._callbacks:
                try:
                    cb(reason)
                except Exception as exc:  # never let observer kill the loop
                    logfire.error(f"[CircuitBreaker] Callback error: {exc}")
            return True

        return False
