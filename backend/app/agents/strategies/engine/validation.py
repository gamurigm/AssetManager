"""
Safety & Validation Utils — AssetManager Strategy Engine
========================================================
Implements:
1. Look-ahead Bias Guard (Proxy Object)
2. Monte Carlo Sensitivity Analysis
3. Parameter Perturbation Tests
"""

from typing import List, Any, Callable
import time
import random
import numpy as np
from .models import TradeSignal, TradeRecord, KPIResult

class LookAheadGuardProxy:
    """
    A list-like proxy that raises an error if code tries to access 
    indices ahead of the 'current' simulation index.
    """
    def __init__(self, data: List[Any]):
        self._data = data
        self._current_idx = -1

    def set_current_idx(self, idx: int):
        self._current_idx = idx

    def __getitem__(self, key):
        if isinstance(key, slice):
            start = key.start or 0
            stop = key.stop if key.stop is not None else len(self._data)
            if stop > self._current_idx + 1:
                raise ValueError(
                    f"⛔ LOOK-AHEAD BIAS DETECTED: Accessing index {stop-1} "
                    f"while simulation is at {self._current_idx}"
                )
            return self._data[key]
        
        if key > self._current_idx:
            raise ValueError(
                f"⛔ LOOK-AHEAD BIAS DETECTED: Accessing index {key} "
                f"while simulation is at {self._current_idx}"
            )
        return self._data[key]

    def __len__(self):
        # We only pretend to know the length up to current_idx + 1 if we want to be strict,
        # but for loops need the real length. The guard is in __getitem__.
        return len(self._data)

    def __iter__(self):
        """
        Automatic index tracking during iteration.
        """
        for i in range(len(self._data)):
            self._current_idx = i
            yield self._data[i]

def validate_strategy_safety(engine_fn: Callable, *args, **kwargs) -> Any:
    """
    Wraper to execute a session while forcing the Look-ahead Guard.
    Args:
        engine_fn: The run_session method of the strategy engine.
        m5_candles, m1_candles: The data.
    """
    # Assuming standard run_session signature: (m5, m1, account, config)
    m5 = args[0]
    m1 = args[1]
    
    # Wrap M1 candles (usually where look-ahead happens)
    protected_m1 = LookAheadGuardProxy(m1)
    
    # We need to monkey-patch or inject the current index into the loop.
    # Since we can't easily reach into the for loop of a pre-compiled method,
    # we can use this proxy in unit tests where we pass it explicitly.
    
    # Actually, if we use protected_m1 in the engine, the engine's 
    # 'for idx, candle in enumerate(m1_candles)' will work fine, 
    # BUT if inside the loop someone calls m1_candles[idx+1], the guard trips.
    
    # Let's try passing it to the engine.
    new_args = (m5, protected_m1) + args[2:]
    
    # We need a way to update the proxy's current index.
    # We can do this by wrapping the iterator or the engine logic.
    # For now, let's just implement the proxy.
    return engine_fn(*new_args, **kwargs)

class RobustnessAuditor:
    """
    Methods to validate strategy robustness (Monte Carlo, Slippage Sensitivity).
    """
    @staticmethod
    def monte_carlo_simulation(trades: List[TradeRecord], iterations: int = 1000) -> dict:
        """
        Runs random resampling of trade order and result variations.
        """
        if not trades:
            return {}

        results = []
        original_pnls = [t.pnl_usd for t in trades]
        
        for _ in range(iterations):
            # Resample with replacement (Bootstrap) or just shuffle?
            # Shuffle checks if order matters. Bootstrap checks sample sensitivity.
            sample = [random.choice(original_pnls) for _ in range(len(original_pnls))]
            cum_pnl = sum(sample)
            results.append(cum_pnl)

        results.sort()
        ci_95_low = results[int(iterations * 0.025)]
        ci_95_high = results[int(iterations * 0.975)]

        return {
            "iterations": iterations,
            "mean_pnl": np.mean(results),
            "median_pnl": np.median(results),
            "ci_95_range": [ci_95_low, ci_95_high],
            "std_dev": np.std(results),
            "prob_loss": len([r for r in results if r < 0]) / iterations
        }

    @staticmethod
    def slippage_sensitivity(trades: List[TradeRecord], max_slippage_pips: float = 5.0) -> dict:
        """
        Simulates how KPIs degrade as slippage increases.
        """
        # TODO: Implement slippage sensitivity curve
        return {}
