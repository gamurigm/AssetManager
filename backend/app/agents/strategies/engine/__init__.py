"""
Strategy Engine — Public API
============================
External code should import from here, not from submodules directly.
This keeps internal structure free to change without breaking imports.
"""

from .models import StrategyConfig, ORBLevel, FVG, TradeSignal, TradeRecord, KPIResult, SessionState
from .interfaces import IStrategyEngine, IKPICalculator
from .orb_fvg_engine import ORBFVGEngine
from .kpi_calculator import ORBKPICalculator
from .strategy_factory import StrategyFactory
from .circuit_breaker import CircuitBreaker

__all__ = [
    # Models
    "StrategyConfig", "ORBLevel", "FVG", "TradeSignal", "TradeRecord", "KPIResult", "SessionState",
    # Interfaces
    "IStrategyEngine", "IKPICalculator",
    # Implementations
    "ORBFVGEngine", "ORBKPICalculator",
    # Factory
    "StrategyFactory",
    # Circuit Breaker
    "CircuitBreaker",
]
