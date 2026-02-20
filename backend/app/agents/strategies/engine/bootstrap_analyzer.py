"""
Bootstrap Analyzer
===================
Uses a fast C++ compiled DLL to perform Bootstrap Resampling on backtest results.
Calculates 95% Confidence Intervals for Maximum Drawdown and Net Profit.
"""

import ctypes
import os
from typing import List, Dict, Any
from .interfaces import TradeRecord

# Define the C struct for ctypes
class BootstrapResultStruct(ctypes.Structure):
    _fields_ = [
        ("net_profit_2_5", ctypes.c_double),
        ("net_profit_97_5", ctypes.c_double),
        ("max_dd_2_5", ctypes.c_double),
        ("max_dd_97_5", ctypes.c_double),
    ]

class BootstrapAnalyzer:
    def __init__(self):
        self.dll_path = os.path.join(os.path.dirname(__file__), "bootstrap.dll")
        self._lib = None
        self._load_lib()

    def _load_lib(self):
        try:
            import sys
            if sys.platform == "win32":
                self._lib = ctypes.CDLL(self.dll_path, winmode=0)
            else:
                self._lib = ctypes.CDLL(self.dll_path)
                
            # void run_bootstrap(const double* pnl_array, int num_trades, double initial_equity, int iterations, BootstrapResult* result_out)
            self._lib.run_bootstrap.argtypes = [
                ctypes.POINTER(ctypes.c_double),
                ctypes.c_int,
                ctypes.c_double,
                ctypes.c_int,
                ctypes.POINTER(BootstrapResultStruct),
                ctypes.POINTER(ctypes.c_double),
                ctypes.POINTER(ctypes.c_double)
            ]
            self._lib.run_bootstrap.restype = None
        except Exception as e:
            print(f"Warning: Could not load bootstrap.dll: {e}")

    def run_bootstrap(self, trades: List[TradeRecord], initial_equity: float, iterations: int = 10000) -> Dict[str, Any]:
        """
        Runs Monte Carlo bootstrap resampling over the trade PnLs.
        Returns 95% Confidence Intervals for Drawdown and Net Profit.
        """
        if self._lib is None:
            return {"error": "Bootstrap DLL not loaded"}

        if not trades:
            return {
                "net_profit_95_ci": [0.0, 0.0],
                "max_drawdown_95_ci": [0.0, 0.0]
            }

        # Extract PnL array
        pnl_values = [t.pnl_usd for t in trades]
        num_trades = len(pnl_values)

        # Convert to ctypes array
        PnlArrayType = ctypes.c_double * num_trades
        pnl_array_c = PnlArrayType(*pnl_values)

        # Prepare arrays for the full samples
        SamplesArrayType = ctypes.c_double * iterations
        np_samples_c = SamplesArrayType()
        dd_samples_c = SamplesArrayType()

        # Prepare result struct
        result = BootstrapResultStruct()

        # Call C++ function
        self._lib.run_bootstrap(
            pnl_array_c, 
            num_trades, 
            initial_equity, 
            iterations, 
            ctypes.byref(result),
            np_samples_c,
            dd_samples_c
        )

        return {
            "net_profit_95_ci": [round(result.net_profit_2_5, 2), round(result.net_profit_97_5, 2)],
            "max_drawdown_95_ci_pct": [round(result.max_dd_2_5, 2), round(result.max_dd_97_5, 2)],
            "iterations": iterations,
            "sample_size": num_trades,
            "net_profit_samples": list(np_samples_c),
            "max_drawdown_samples": list(dd_samples_c)
        }

# Singleton instance
bootstrap_analyzer = BootstrapAnalyzer()
