import asyncio
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from app.services.yahoo_finance_service import yahoo_finance_service

async def main():
    res = await yahoo_finance_service.get_intraday("AAPL", "5m", "7d")
    print(res["source"])
    if "candles" in res:
        print(f"Total candles: {len(res['candles'])}")
        for c in res["candles"][:5]:
            print(f"Candle: {c['timestamp']} - {c['close']}")
    else:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())
