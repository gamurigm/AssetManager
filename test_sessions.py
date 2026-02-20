import asyncio
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from app.services.yahoo_finance_service import yahoo_finance_service
from app.agents.strategies.backtest_runner import BacktestRunner

async def main():
    res1 = await yahoo_finance_service.get_intraday("AAPL", "1m", "7d")
    res5 = await yahoo_finance_service.get_intraday("AAPL", "5m", "1mo")
    
    m1 = res1.get("candles", [])
    m5 = res5.get("candles", [])
    
    sessions = BacktestRunner._split_into_sessions(m1, m5)
    print(f"Total sessions extracted: {len(sessions)}")
    
    # print sessions that have both M1 and M5 > 0
    valid_sessions = [s for s in sessions if len(s['m1']) > 0 and len(s['m5']) > 0]
    print(f"Valid sessions: {len(valid_sessions)}")
    for s in valid_sessions:
        print(f"Session: {s['date']} | m5: {len(s['m5'])} | m1: {len(s['m1'])}")
        
if __name__ == "__main__":
    asyncio.run(main())
