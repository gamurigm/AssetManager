"""
Strategy Validation & Auditor Tests
===================================
Verifies the Look-ahead Bias Guard and Robustness Auditors.
"""

import pytest
import sys
import os

# Ensure backend root is on the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.agents.strategies.engine import ORBFVGEngine, StrategyConfig
from app.agents.strategies.engine.validation import LookAheadGuardProxy, RobustnessAuditor
from app.agents.strategies.engine.models import TradeSignal, TradeRecord

def make_candle(close: float, ts: str):
    return {"timestamp": ts, "open": close, "high": close, "low": close, "close": close, "volume": 1000}

class TestLookAheadGuard:
    
    def test_guard_blocks_future_access(self):
        data = [make_candle(100+i, f"2025-01-01T09:3{i}:00") for i in range(10)]
        proxy = LookAheadGuardProxy(data)
        
        # Simulate loop
        for idx, candle in enumerate(proxy):
            # Accessing past should be fine
            if idx > 0:
                p = proxy[idx-1]
                assert p["close"] == 100 + idx - 1
            
            # Accessing future should FAIL
            with pytest.raises(ValueError, match="LOOK-AHEAD BIAS"):
                _ = proxy[idx+1]

    def test_strategy_is_safe(self):
        """
        Runs the actual ORBFVGEngine with the guard.
        If it passes, it means no look-ahead.
        """
        engine = ORBFVGEngine()
        # Synthetic data for a session
        m5 = [make_candle(100, "2025-01-01T09:30:00")]
        m1 = [make_candle(100, f"2025-01-01T09:3{i+5}:00") for i in range(30)]
        
        proxy_m1 = LookAheadGuardProxy(m1)
        # Should not raise any ValueError
        try:
            engine.run_session(m5, proxy_m1, 10000, StrategyConfig.default())
        except ValueError as e:
            if "LOOK-AHEAD" in str(e):
                pytest.fail(f"Strategy has look-ahead bias! {e}")
            raise e

class TestRobustnessAuditor:
    
    def test_monte_carlo_variability(self):
        # Create some dummy trades
        sig = TradeSignal(
            signal_id="S1", timestamp="...", direction="LONG", orh=101, orl=99,
            fvg_top=100.5, fvg_bottom=100.2, entry=100.3, stop=99.5, tp=102,
            risk_pips=0.8, position_size=10, confidence="high", atr_m1=0.2
        )
        trades = [
            TradeRecord(sig, "win_tp", 102, "...", 2.1, 210, 0),
            TradeRecord(sig, "loss_sl", 99.5, "...", -1.0, -100, 0),
            TradeRecord(sig, "win_tp", 102, "...", 2.1, 210, 0),
        ]
        
        report = RobustnessAuditor.monte_carlo_simulation(trades, iterations=100)
        assert "mean_pnl" in report
        assert report["iterations"] == 100
        assert report["prob_loss"] < 1.0 # Hopefully lol
