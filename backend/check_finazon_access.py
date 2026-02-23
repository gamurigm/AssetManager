import asyncio
import httpx
import json

async def check_access():
    api_key = "777a94a9379343a1b487c3a8bdaeadcacg"
    
    # Try api_usage endpoint, which often requires authentication and shows what is allowed
    url = "https://api.finazon.io/latest/finazon/us_stocks_essential/api_usage"
    
    async with httpx.AsyncClient() as client:
        rsp = await client.get(url, params={"apikey": api_key})
        print("--- API Usage Endpoint ---")
        print(f"Status: {rsp.status_code}")
        try:
            print(json.dumps(rsp.json(), indent=2))
        except:
            print(rsp.text)

if __name__ == "__main__":
    asyncio.run(check_access())
