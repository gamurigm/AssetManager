"""
Diagnostic script to find why ORB FVG Engulfing yields so few trades.
It runs the strategy on SPY over 6 months and tracks exactly which step fails each day.
"""

import asyncio
import sys
import os
from collections import Counter
from datetime import datetime

# Setup paths
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))
os.chdir(os.path.join(os.path.dirname(__file__), "backend"))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "backend", ".env"))

import logfire
logfire.configure(send_to_logfire="never")

from app.services.market_data import market_data_service
from app.agents.strategies.engine.orb_fvg_engine import ORBFVGEngine
from app.agents.strategies.engine.models import StrategyConfig
from app.agents.strategies.backtest_runner import BacktestRunner

async def run_diagnostics():
    symbol = "SPY"
    start_date = "2025-01-06"
    end_date = "2025-06-30"  # 6 months
    
    print(f"Fetching data for {symbol} from {start_date} to {end_date}...")
    
    # 1. Fetch data
    m5_data = await market_data_service.get_intraday(symbol, "5m", start=start_date, end=end_date)
    m1_data = await market_data_service.get_intraday(symbol, "1m", start=start_date, end=end_date)
    
    if "error" in m5_data or "error" in m1_data:
        print("Data fetch failed:", m5_data.get("error"), m1_data.get("error"))
        return
        
    m5_candles = m5_data["candles"]
    m1_candles = m1_data["candles"]
    print(f"Loaded {len(m5_candles)} M5 candles and {len(m1_candles)} M1 candles")
    
    # 2. Group by days (Session logic from BacktestRunner)
    # We will use the runner's grouping logic
    runner = BacktestRunner(ORBFVGEngine(), None, None)
    sessions = runner._split_into_sessions(m1_candles, m5_candles)
    print(f"Total valid trading sessions (days with 9:30-11:00 data): {len(sessions)}")
    
    # 3. Instrument the engine config
    config = StrategyConfig()
    # config.min_range_pips = 0.5 # default 1.0 (for forex, but SPY is an ETF where 1 pip = $0.01)
    # config.body_ratio_breakout = 0.5 # default 0.6
    
    # Trackers
    stats = Counter()
    
    engine = ORBFVGEngine()
    
    for session in sessions:
        date_str = session["date"]
        sess_m5 = session["m5"]
        sess_m1 = session["m1"]
        
        # We need to trace the engine execution manually to see where it stops
        # PASO 1: ORB
        orb = engine._detect_orb(sess_m5[0], config.min_range_pips)
        if not orb.valid:
            stats["Fail 1: ORB invalid (range too small)"] += 1
            # print(f"{date_str}: ORB size {orb.range_} < {config.min_range_pips}")
            continue
            
        # Run strategy engine
        signal = engine.run_session(sess_m5, sess_m1, 10000.0, config)
        
        if signal:
            stats["SUCCESS: Trade Generated"] += 1
        else:
            # For simplicity in this new version, we just count fails
            stats["Fail: No setup completed"] += 1

    print("\n--- Diagnostic Results ---")
    print(f"Total sessions analyzed: {len(sessions)}")
    for reason, count in sorted(stats.items()):
        pct = (count / len(sessions)) * 100
        print(f"{count:3d} ({pct:5.1f}%) : {reason}")

if __name__ == "__main__":
    asyncio.run(run_diagnostics())
