"""
Strategy Factory (strategy_factory.py)
========================================
Factory Pattern + Open/Closed Principle:
  - New strategies are registered externally via StrategyFactory.register().
  - The factory itself never changes — it's closed for modification, open for extension.

Usage:
    engine = StrategyFactory.create("ORB_FVG_ENGULFING", config)

To add a new strategy in the future:
    StrategyFactory.register("VWAP_PULLBACK", VWAPPullbackEngine)
"""

from __future__ import annotations

from typing import Dict, Type, Optional
from .interfaces import IStrategyEngine
from .models import StrategyConfig
from .orb_fvg_engine import ORBFVGEngine


class StrategyFactory:
    """
    Central registry of strategy engines.
    Thread-safe for reads (dict is not mutated during runtime after startup).
    """

    _registry: Dict[str, Type] = {
        "ORB_FVG_ENGULFING": ORBFVGEngine,
    }

    @classmethod
    def create(cls, name: str, config: Optional[StrategyConfig] = None) -> IStrategyEngine:
        """
        Instantiate a strategy engine by name.

        Args:
            name:   Registry key, e.g. "ORB_FVG_ENGULFING".
            config: Not passed to __init__ (engines are stateless);
                    config is passed per run_session() call.

        Raises:
            ValueError: When the strategy name is not registered.
        """
        klass = cls._registry.get(name)
        if klass is None:
            available = ", ".join(cls._registry.keys())
            raise ValueError(
                f"Strategy '{name}' is not registered. Available: {available}"
            )
        return klass()

    @classmethod
    def register(cls, name: str, engine_class: Type) -> None:
        """
        Register a new strategy engine class.
        OCP: this is the extension point — the factory code itself stays untouched.
        """
        if not callable(engine_class):
            raise TypeError(f"engine_class must be a class, got {type(engine_class)}")
        cls._registry[name] = engine_class

    @classmethod
    def available(cls) -> list:
        """Return list of registered strategy names."""
        return list(cls._registry.keys())
