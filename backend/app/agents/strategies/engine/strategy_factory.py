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
    def load_from_code(cls, strategy_name: str, code: str) -> None:
        """
        Dynamically loads a Python code string defining an IStrategyEngine.
        This allows the AI agent to write strategies and immediately test them.
        """
        import sys
        import types
        import inspect
        from .interfaces import IStrategyEngine
        
        # Create a dynamic module
        module_name = f"dynamic_strategy_{strategy_name.lower().replace(' ', '_')}"
        new_module = types.ModuleType(module_name)
        
        # We need to make sure the dynamically loaded code can resolve local imports 
        # (like `from .interfaces import IStrategyEngine`)
        # To do this safely, we execute the code in a dictionary that has the current globals
        env = globals().copy()
        
        try:
            # Execute the code in this environment
            exec(code, env)
            
            # Find the class that implements IStrategyEngine
            strategy_class = None
            for name, obj in env.items():
                if inspect.isclass(obj) and obj is not IStrategyEngine:
                    # Check if it inherits from IStrategyEngine, or has the required methods
                    # Using a duck-typing approach since direct inheritance check might fail across dynamic modules
                    if hasattr(obj, 'run_session') and callable(getattr(obj, 'run_session')):
                        strategy_class = obj
                        break
                        
            if not strategy_class:
                raise ValueError(f"No class implementing `run_session` found in the provided code for {strategy_name}.")
                
            # Register it
            cls.register(strategy_name, strategy_class)
            print(f"[StrategyFactory] Successfully loaded and registered dynamic strategy: {strategy_name}")
            
        except Exception as e:
            print(f"[StrategyFactory] Failed to load dynamic strategy {strategy_name}: {e}")
            raise e

    @classmethod
    def available(cls) -> list:
        """Return list of registered strategy names."""
        return list(cls._registry.keys())

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

# Run auto-discovery on module import Uvicorn starts
try:
    StrategyFactory.auto_discover()
except Exception as e:
    print(f"[StrategyFactory] Early auto-discovery warning: {e}")

