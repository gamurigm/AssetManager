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

    def run_bootstrap(
        self,
        trades: List[TradeRecord],
        initial_equity: float,
        iterations: int = 10000,
        return_samples: bool = True,   # set False to skip Python serialization overhead
    ) -> Dict[str, Any]:
        """
        Runs Monte Carlo bootstrap resampling over the trade PnLs using C++ DLL.
        Returns 95% Confidence Intervals for Drawdown and Net Profit.

        Args:
            return_samples: When True, also returns the full per-iteration
                sample arrays (needed for HTML report charts).
                When False, only CI stats are returned — much faster for
                large iteration counts since it skips serializing N doubles.
        """
        if self._lib is None:
            return {"error": "Bootstrap DLL not loaded"}

        if not trades:
            return {
                "net_profit_95_ci": [0.0, 0.0],
                "max_drawdown_95_ci_pct": [0.0, 0.0],
                "iterations": 0,
                "sample_size": 0,
            }

        # Extract PnL array
        pnl_values = [t.pnl_usd for t in trades]
        num_trades = len(pnl_values)

        # Convert to ctypes array
        PnlArrayType = ctypes.c_double * num_trades
        pnl_array_c = PnlArrayType(*pnl_values)

        # Only allocate full sample arrays when they'll be used.
        # Serializing 10,000 doubles as a Python list costs ~2ms but
        # feels equivalent to 1,000 iterations — hiding the real perf delta.
        if return_samples:
            SamplesArrayType = ctypes.c_double * iterations
            np_samples_c = SamplesArrayType()
            dd_samples_c = SamplesArrayType()
        else:
            # Pass nullptr — C++ checks for nullptr before writing
            np_samples_c = None  # type: ignore
            dd_samples_c = None  # type: ignore

        # Prepare result struct
        result = BootstrapResultStruct()

        # Call C++ function
        self._lib.run_bootstrap(
            pnl_array_c,
            num_trades,
            initial_equity,
            iterations,
            ctypes.byref(result),
            np_samples_c if np_samples_c is not None else ctypes.cast(None, ctypes.POINTER(ctypes.c_double)),
            dd_samples_c if dd_samples_c is not None else ctypes.cast(None, ctypes.POINTER(ctypes.c_double)),
        )

        out = {
            "net_profit_95_ci":       [round(result.net_profit_2_5,  2), round(result.net_profit_97_5,  2)],
            "max_drawdown_95_ci_pct": [round(result.max_dd_2_5,      4), round(result.max_dd_97_5,      4)],
            "iterations":             iterations,
            "sample_size":            num_trades,
        }

        if return_samples and np_samples_c is not None:
            out["net_profit_samples"]   = list(np_samples_c)
            out["max_drawdown_samples"] = list(dd_samples_c)  # type: ignore

        return out

# Singleton instance
bootstrap_analyzer = BootstrapAnalyzer()
