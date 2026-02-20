"""
Strategy Engine — Interfaces (ISP + DIP)
=========================================
All interfaces use Python's `typing.Protocol` (structural subtyping).
No ABC, no inheritance — callers depend on these contracts, not implementations.

Applied SOLID principles:
  - I (Interface Segregation): each Protocol exposes only what its consumers need.
  - D (Dependency Inversion): BacktestRunner, SimulationService, etc. import
    these Protocols only — never the concrete classes.
"""

from __future__ import annotations

from typing import Protocol, List, Optional, runtime_checkable
from .models import StrategyConfig, TradeSignal, TradeRecord, KPIResult

# CandleRow is a TypedDict — avoid importing from services to keep engine layer pure
# The engine layer accepts any dict with {timestamp, open, high, low, close, volume}


# --------------------------------------------------------------------------- #
#  IStrategyEngine — The Strategy Pattern contract                             #
#    Concrete: ORBFVGEngine  (Phase 2)                                         #
#    Future:   VWAPPullbackEngine, ICTEngine, …  (just implement Protocol)    #
# --------------------------------------------------------------------------- #

@runtime_checkable
class IStrategyEngine(Protocol):
    """
    A Strategy Engine evaluates one trading session and optionally returns a signal.
    The session is atomic: either a setup exists and is valid, or it's None.
    """

    def run_session(
        self,
        m5_candles: List[CandleRow],    # ≥ 1 candle: the 9:30 opening candle minimum
        m1_candles: List[CandleRow],    # Session M1 candles starting at 9:35
        account_size: float,
        config: StrategyConfig,
    ) -> Optional[TradeSignal]:
        """
        Evaluate one trading session.
        Returns a TradeSignal if all conditions are met, otherwise None.
        Must be a pure function: no I/O, no side effects.
        """
        ...


# --------------------------------------------------------------------------- #
#  IKPICalculator — Computes statistics over a list of trade records           #
#    Concrete: ORBKPICalculator  (Phase 3)                                     #
# --------------------------------------------------------------------------- #

@runtime_checkable
class IKPICalculator(Protocol):
    """
    Computes post-backtest KPIs from a list of completed TradeRecords.
    Pure computation — no storage, no I/O.
    """

    def compute(
        self,
        trades: List[TradeRecord],
        initial_equity: float,
        trading_days: int,
    ) -> KPIResult:
        """
        Calculate all KPIs as defined in Section 8 of the ORB strategy doc.
        """
        ...
