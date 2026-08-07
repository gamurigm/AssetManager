"""
Strategy Factory (strategy_factory.py)
========================================
Factory Pattern + Open/Closed Principle:
  - New strategies are registered externally via StrategyFactory.register().
  - The factory itself never changes — it's closed for modification, open for extension.

Usage:
    engine = StrategyFactory.create("ORB_FVG_ENGULFING")

To add a new strategy in the future:
    StrategyFactory.register("VWAP_PULLBACK", VWAPPullbackEngine)
"""

from __future__ import annotations

import inspect
import os
from typing import Dict, Type
from .interfaces import IStrategyEngine
from .orb_fvg_engine import ORBFVGEngine
from .ict_vp_engine import IctVpEngine


class StrategyFactory:
    """
    Central registry of strategy engines.
    Thread-safe for reads (dict is not mutated during runtime after startup).
    """

    _registry: Dict[str, Type] = {
        "ORB_FVG_ENGULFING": ORBFVGEngine,
        "ICT_VP": IctVpEngine,
    }

    @classmethod
    def create(cls, name: str) -> IStrategyEngine:
        """
        Instantiate a strategy engine by name.

        Args:
            name:   Registry key, e.g. "ORB_FVG_ENGULFING".
        Raises:
            ValueError: When the strategy name is not registered.
        """
        normalized_name = name.strip().upper()
        klass = cls._registry.get(normalized_name)
        if klass is None:
            available = ", ".join(cls._registry.keys())
            raise ValueError(
                f"Strategy '{normalized_name}' is not registered. Available: {available}"
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
        normalized_name = name.strip().upper()
        if not normalized_name:
            raise ValueError("strategy name cannot be empty")
        instance = engine_class()
        if not isinstance(instance, IStrategyEngine):
            raise TypeError("engine_class must implement run_session")
        signature = inspect.signature(instance.run_session)
        parameters = list(signature.parameters.values())
        accepts_varargs = any(
            parameter.kind is inspect.Parameter.VAR_POSITIONAL
            for parameter in parameters
        )
        if not accepts_varargs and len(parameters) != 4:
            raise TypeError(
                "run_session must accept m5_candles, m1_candles, "
                "account_size, and config"
            )
        cls._registry[normalized_name] = engine_class

    @classmethod
    def unregister(cls, name: str) -> None:
        """Remove a non-core registration, mainly for isolated development/tests."""
        cls._registry.pop(name.strip().upper(), None)

    @classmethod
    def load_from_code(cls, strategy_name: str, code: str) -> None:
        """
        Dynamically loads a Python code string defining an IStrategyEngine.
        This allows the AI agent to write strategies and immediately test them.
        """
        if os.getenv("ALLOW_DYNAMIC_STRATEGIES", "false").lower() != "true":
            raise PermissionError(
                "Dynamic strategy loading is disabled. "
                "Set ALLOW_DYNAMIC_STRATEGIES=true only in an isolated development environment."
            )

        from .interfaces import IStrategyEngine
        
        module_name = f"dynamic_strategy_{strategy_name.lower().replace(' ', '_')}"
        env = {
            "__builtins__": __builtins__,
            "__name__": module_name,
            "__package__": __package__,
            "IStrategyEngine": IStrategyEngine,
        }
        
        exec(code, env)

        strategy_class = next(
            (
                obj
                for obj in env.values()
                if inspect.isclass(obj)
                and obj is not IStrategyEngine
                and obj.__module__ == module_name
                and hasattr(obj, "run_session")
                and callable(getattr(obj, "run_session"))
            ),
            None,
        )
        if strategy_class is None:
            raise ValueError(
                f"No class implementing run_session found in code for {strategy_name}."
            )
        cls.register(strategy_name, strategy_class)

    @classmethod
    def available(cls) -> list:
        """Return list of registered strategy names."""
        return sorted(cls._registry.keys())

    @classmethod
    def auto_discover(cls):
        """
        Scans the directory where this file is located and automatically 
        loads any .py files as strategies (except core engine files).
        This ensures AI-generated files persist across server restarts.
        """
        import os
        import glob
        
        engine_dir = os.path.dirname(__file__)
        py_files = glob.glob(os.path.join(engine_dir, "*.py"))
        
        # Files to ignore (factory, interfaces, models, etc)
        ignore_files = {
            "__init__.py", "factory.py", "strategy_factory.py", 
            "interfaces.py", "models.py", "kpi_calculator.py",
            "circuit_breaker.py", "indicators.py", "volume_profile.py",
            "bootstrap_analyzer.py", "stationary_bootstrap.py", "purged_kfold.py",
            "execution_model.py",
            # We already hardcoded these in _registry at the top:
            "orb_fvg_engine.py", "ict_vp_engine.py"
        }
        
        for file_path in py_files:
            file_name = os.path.basename(file_path)
            if file_name in ignore_files:
                continue
                
            try:
                # Read the code
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()
                
                # Derive a strategy name from the filename: "sma_cross.py" -> "SMA_CROSS"
                strategy_name = file_name.replace(".py", "").upper()
                
                # Load it via the dynamic code loader
                cls.load_from_code(strategy_name, code)
                print(f"[StrategyFactory] Auto-discovered and loaded strategy: {strategy_name}")
            except Exception as e:
                print(f"[StrategyFactory] Error auto-discovering {file_name}: {e}")
