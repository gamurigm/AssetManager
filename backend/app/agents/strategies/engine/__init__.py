"""
Strategy Engine — Public API
============================
External code should import from here, not from submodules directly.
This keeps internal structure free to change without breaking imports.
"""

from .models import CandleRow, ExecutionSettings, StrategyConfig, ORBLevel, FVG, TradeSignal, TradeRecord, KPIResult, SessionState, FoldResult, CrossValidationResult
from .interfaces import IPositionSizer, IStrategyEngine, ITradeExecutionModel, IKPICalculator
from .execution_model import OHLCExecutionModel
from .position_sizer import FixedFractionPositionSizer
from .orb_fvg_engine import ORBFVGEngine
from .kpi_calculator import ORBKPICalculator
from .strategy_factory import StrategyFactory
from .circuit_breaker import CircuitBreaker

__all__ = [
    # Models
    "CandleRow", "ExecutionSettings", "StrategyConfig", "ORBLevel", "FVG", "TradeSignal", "TradeRecord", "KPIResult", "SessionState",
    "FoldResult", "CrossValidationResult",
    # Interfaces
    "IPositionSizer", "IStrategyEngine", "ITradeExecutionModel", "IKPICalculator",
    # Implementations
    "FixedFractionPositionSizer", "ORBFVGEngine", "OHLCExecutionModel", "ORBKPICalculator",
    # Factory
    "StrategyFactory",
    # Circuit Breaker
    "CircuitBreaker",
]
