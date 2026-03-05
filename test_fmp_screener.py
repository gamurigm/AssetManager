import asyncio
import os
import httpx
from dotenv import load_dotenv

env_path = os.path.join(os.getcwd(), "backend", ".env")
load_dotenv(env_path)

async def test_screener():
    api_key = os.getenv("FMP_API_KEY")
    url = f"https://financialmodelingprep.com/api/v3/stock-screener?limit=100&apikey={api_key}"
    
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(url)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"Results: {len(data)}")
            if data:
                print(f"First element: {data[0]}")

if __name__ == "__main__":
    asyncio.run(test_screener())
