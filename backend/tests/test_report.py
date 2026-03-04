import os
import sys

# Ensure we can import from the app
sys.path.append('c:\\AssetManager\\backend')

from app.agents.strategies.engine.indicators import is_bullish # Dummy import to check path
from app.agents.strategies.backtest_runner import BacktestResult, BacktestConfig
from app.agents.strategies.engine.interfaces import TradeRecord, KPIResult
from app.agents.strategies.report_generator import generate_html_report

class MockSignal:
    direction = "LONG"
    entry = 100.0
    stop = 99.0
    tp = 103.0
    risk_pips = 10.0

def generate_mock_report():
    config = BacktestConfig(symbol="TEST_ASSET", start_date="2023-01-01", end_date="2023-12-31")
    kpis = KPIResult(
        total_trades=100, wins=50, losses=50, win_rate=0.5,
        expectancy_r=1.0, profit_factor=2.0, max_drawdown_pct=5.0,
        sharpe_ratio=1.5, avg_rr_realized=3.0, total_r=100.0,
        final_equity=20000.0, cagr=1.0
    )
    
    trades = []
    for i in range(100):
        if i % 2 == 0:
            trades.append(TradeRecord(signal=MockSignal(), outcome="win_tp", exit_price=103, exit_timestamp=f"T{i}", pnl_r=3, pnl_usd=300, slippage_pips=1))
        else:
            trades.append(TradeRecord(signal=MockSignal(), outcome="loss_sl", exit_price=99, exit_timestamp=f"T{i}", pnl_r=-1, pnl_usd=-100, slippage_pips=1))
            
    # Mock bootstrap output from C++ extension
    import numpy as np
    np_samples = np.random.normal(10000, 2000, 10000).tolist()
    dd_samples = np.random.normal(5.0, 1.5, 10000).tolist()
    
    bootstrap_stats = {
        "net_profit_95_ci": [6000.0, 14000.0],
        "max_drawdown_95_ci_pct": [2.0, 8.0],
        "iterations": 10000,
        "sample_size": 100,
        "net_profit_samples": np_samples,
        "max_drawdown_samples": dd_samples
    }
    
    result = BacktestResult(config=config, trades=trades, kpis=kpis, trading_days=50, missing_data_days=0, bootstrap_stats=bootstrap_stats)
    
    out_path = os.path.join(os.getcwd(), "mock_report.html")
    generate_html_report(result, out_path)
    print(f"Mock Report generated at: {out_path}")

if __name__ == "__main__":
    generate_mock_report()
