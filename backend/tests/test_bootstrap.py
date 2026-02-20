import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.agents.strategies.engine.bootstrap_analyzer import bootstrap_analyzer
from app.agents.strategies.engine.interfaces import TradeRecord

class MockSignal:
    direction = "LONG"
    entry = 100.0
    stop = 99.0
    tp = 103.0
    timestamp = "2023-01-01T10:00:00Z"
    risk_pips = 10.0

def test_bootstrap_loader():
    assert bootstrap_analyzer._lib is not None, "DLL failed to load"

def test_run_bootstrap_logic():
    # Create 100 trades: 50 wins of $300, 50 losses of -$100.
    # Expected Expected Value per trade = (300*0.5) + (-100*0.5) = $100
    # Expected Total Net Profit = 100 * 100 = $10000
    
    trades = []
    for _ in range(50):
        # WIN
        trades.append(TradeRecord(
            signal=MockSignal(),
            outcome="win_tp",
            exit_price=103.0,
            exit_timestamp="T",
            pnl_r=3.0,
            pnl_usd=300.0,
            slippage_pips=1.0
        ))
        # LOSS
        trades.append(TradeRecord(
            signal=MockSignal(),
            outcome="loss_sl",
            exit_price=99.0,
            exit_timestamp="T",
            pnl_r=-1.0,
            pnl_usd=-100.0,
            slippage_pips=1.0
        ))
        
    initial_equity = 10000.0
    
    # Run 10000 iterations to get stable results
    stats = bootstrap_analyzer.run_bootstrap(trades, initial_equity, iterations=10000)
    
    assert "net_profit_95_ci" in stats
    assert "max_drawdown_95_ci_pct" in stats
    
    np_ci = stats["net_profit_95_ci"]
    dd_ci = stats["max_drawdown_95_ci_pct"]
    
    print(f"Stats: {stats}")
    
    # The mean net profit should be around 10,000.
    # The 95% CI should contain 10000 but have a spread.
    assert np_ci[0] < 10000 < np_ci[1], "10000 should be in the CI"
    
    # Expected standard deviation of sum of 100 binomial trades:
    # Var(1 trade) = 0.5 * (300 - 100)^2 + 0.5 * (-100 - 100)^2 = 0.5 * 40000 + 0.5 * 40000 = 40000
    # SD(100 trades) = sqrt(100 * 40000) = sqrt(4,000,000) = 2000
    # 95% CI roughly mean +/- 1.96 * SD => 10000 +/- 3920 => [6080, 13920] roughly
    
    assert 4000 < np_ci[0] < 8000, f"Lower bound {np_ci[0]} out of expected range"
    assert 12000 < np_ci[1] < 16000, f"Upper bound {np_ci[1]} out of expected range"

if __name__ == "__main__":
    test_run_bootstrap_logic()
    print("Tests passed")
