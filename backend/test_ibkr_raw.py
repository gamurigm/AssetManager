
import asyncio
from ib_insync import IB

async def test_raw():
    ib = IB()
    try:
        print("Connecting to 127.0.0.1:7497...")
        await ib.connectAsync('127.0.0.1', 7497, clientId=99)
        print("✅ Connected!")
        print(f"Account: {ib.accountValues()[0] if ib.accountValues() else 'N/A'}")
        ib.disconnect()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_raw())
