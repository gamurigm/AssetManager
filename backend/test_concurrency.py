
import asyncio
import time
from app.services.ibkr_service import ibkr_service

async def worker(id):
    print(f"Worker {id} starting")
    try:
        # Simulate what the provider does
        await ibkr_service.connect()
        status = ibkr_service.get_status()
        print(f"Worker {id} connected: {status['connected']}")
    except asyncio.CancelledError:
        print(f"Worker {id} CANCELLED")
        raise
    except Exception as e:
        print(f"Worker {id} error: {e}")

async def main():
    print("Starting stress test...")
    tasks = [asyncio.create_task(worker(i)) for i in range(10)]
    
    # Wait a tiny bit then cancel some
    await asyncio.sleep(0.1)
    print("Cancelling some workers...")
    for i in [2, 5, 8]:
        tasks[i].cancel()
        
    await asyncio.gather(*tasks, return_exceptions=True)
    
    print("\nFinal Service Status:")
    import json
    print(json.dumps(ibkr_service.get_status(), indent=2))
    
    ibkr_service.disconnect()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
