import asyncio
import os
import httpx
from dotenv import load_dotenv

env_path = os.path.join(os.getcwd(), "backend", ".env")
load_dotenv(env_path)

async def test_fmp_endpoints():
    api_key = os.getenv("FMP_API_KEY")
    if not api_key:
        print("No FMP key found")
        return

    endpoints = [
        "https://financialmodelingprep.com/api/v3/stock/list",
        "https://financialmodelingprep.com/api/v3/available-traded/list",
        "https://financialmodelingprep.com/api/v3/symbol/available-nasdaq",
        "https://financialmodelingprep.com/api/v3/symbol/available-euronext"
    ]
    
    async with httpx.AsyncClient(timeout=10) as client:
        for url in endpoints:
            print(f"\nTesting {url}...")
            resp = await client.get(f"{url}?apikey={api_key}")
            print(f"Status: {resp.status_code}")
            if resp.status_code == 200:
                data = resp.json()
                print(f"Results: {len(data)}")
                if data:
                    print(f"First element: {data[0]}")
            else:
                print(f"Response: {resp.text[:200]}")

if __name__ == "__main__":
    asyncio.run(test_fmp_endpoints())
