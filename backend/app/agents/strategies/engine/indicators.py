"""
Strategy Engine — Technical Indicators (indicators.py)
=======================================================
High-performance technical indicators using Jesse-Rust (compiled Rust).
Optimized for low latency.

Dependencies:
- numpy
- jesse-rust (pip install jesse-rust)
"""

from __future__ import annotations
from typing import List, Dict, Any, Union, Tuple
import numpy as np

try:
    import jesse_rust
    # Explicitly import submodules or functions if needed, 
    # but jesse_rust exposes them at top level usually.
    # Checking availability:
    from jesse_rust import sma as sma_rust
    from jesse_rust import ema as ema_rust
    from jesse_rust import wma as wma_rust
    from jesse_rust import rsi as rsi_rust
    from jesse_rust import atr as atr_rust
    from jesse_rust import bollinger_bands as bb_rust
except ImportError:
    raise ImportError("CRITICAL: jesse-rust is required but not installed. Install via 'pip install jesse-rust'.")

# CandleRow shape: {timestamp: str, open: float, high: float, low: float, close: float, volume: int}
CandleRow = Dict[str, Any]

def candles_to_numpy(candles: List[CandleRow]) -> np.ndarray:
    """
    Convert dictionary-based candles to Jesse-compatible NumPy array (Float64).
    Standard Jesse order: timestamp(0), open(1), close(2), high(3), low(4), volume(5)
    """
    if not candles:
        return np.array([])
    
    # Pre-allocate for performance
    count = len(candles)
    arr = np.zeros((count, 6), dtype=np.float64)
    
    for i, c in enumerate(candles):
        # We assume timestamp is convertible to float or handled upstream if it's a string date
        # If timestamp is ISO string, we might need 0. For now, put 0 if not numeric.
        ts = c.get("timestamp_int", 0) 
        if not ts and isinstance(c["timestamp"], (int, float)):
             ts = c["timestamp"]
        
        arr[i, 0] = ts
        arr[i, 1] = c["open"]
        arr[i, 2] = c["close"]
        arr[i, 3] = c["high"]
        arr[i, 4] = c["low"]
        arr[i, 5] = c["volume"]
        
    return arr

# --------------------------------------------------------------------------- #
#  Indicators (Jesse-Rust / Rust Compiled)                                    #
# --------------------------------------------------------------------------- #

def compute_ATR(candles: Union[List[CandleRow], np.ndarray], period: int = 14) -> float:
    """Average True Range (Wilder's Smoothing) via Rust"""
    if isinstance(candles, list): candles = candles_to_numpy(candles)
    
    if len(candles) < period + 1: return 0.0

    # jesse_rust.atr expects the full candles array
    res = atr_rust(candles, period)
    return res[-1] if isinstance(res, np.ndarray) else res

def rsi(candles: Union[List[CandleRow], np.ndarray], period: int = 14) -> float:
    """Relative Strength Index via Rust"""
    if isinstance(candles, list): candles = candles_to_numpy(candles)
    
    if len(candles) < period + 1: return 0.0
    
    # Extract Close prices (index 2)
    close = candles[:, 2]
    res = rsi_rust(close, period)
    return res[-1]

def sma(candles: Union[List[CandleRow], np.ndarray], period: int) -> float:
    """Simple Moving Average via Rust"""
    if isinstance(candles, list): candles = candles_to_numpy(candles)
    if len(candles) < period: return 0.0
    
    close = candles[:, 2]
    res = sma_rust(close, period)
    return res[-1]

def ema(candles: Union[List[CandleRow], np.ndarray], period: int) -> float:
    """Exponential Moving Average via Rust"""
    if isinstance(candles, list): candles = candles_to_numpy(candles)
    if len(candles) < period: return 0.0
    
    close = candles[:, 2]
    res = ema_rust(close, period)
    return res[-1]

def wma(candles: Union[List[CandleRow], np.ndarray], period: int) -> float:
    """Weighted Moving Average via Rust"""
    if isinstance(candles, list): candles = candles_to_numpy(candles)
    if len(candles) < period: return 0.0
    
    close = candles[:, 2]
    res = wma_rust(close, period)
    return res[-1]

def bollinger_bands(candles: Union[List[CandleRow], np.ndarray], period: int = 20, dev: float = 2.0) -> Tuple[float, float, float]:
    """Bollinger Bands (Upper, Middle, Lower) via Rust"""
    if isinstance(candles, list): candles = candles_to_numpy(candles)
    if len(candles) < period: return (0.0, 0.0, 0.0)
    
    close = candles[:, 2]
    # jesse_rust.bollinger_bands(source, period, mult, matype) -> (upper, mid, lower)
    # matype 0 = SMA (standard BB)
    res = bb_rust(close, period, dev, 0)
    
    # Returns tuple of arrays, we want last value
    return (res[0][-1], res[1][-1], res[2][-1])

# --------------------------------------------------------------------------- #
#  Volume & Utils (NumPy Optimized)                                           #
# --------------------------------------------------------------------------- #

def compute_avg_volume(candles: Union[List[CandleRow], np.ndarray], period: int = 20) -> float:
    """Average Volume"""
    if isinstance(candles, list): candles = candles_to_numpy(candles)
    if len(candles) == 0: return 1.0
    
    # Volume is index 5
    vols = candles[:, 5]
    if len(vols) < period:
        return float(np.mean(vols))
        
    return float(np.mean(vols[-period:]))

def body_ratio(candle: CandleRow) -> float:
    """|Close - Open| / (High - Low)"""
    total_range = candle["high"] - candle["low"]
    if total_range == 0: return 0.0
    return abs(candle["close"] - candle["open"]) / total_range

def is_bullish(candle: CandleRow) -> bool:
    return candle["close"] > candle["open"]

def is_bearish(candle: CandleRow) -> bool:
    return candle["close"] < candle["open"]
