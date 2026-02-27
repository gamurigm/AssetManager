import asyncio
import httpx

async def main():
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": "apple", "quotesCount": 5, "newsCount": 0}
    headers = {"User-Agent": "Mozilla/5.0"}
    async with httpx.AsyncClient() as client:
        res = await client.get(url, params=params, headers=headers)
        print(res.json())

if __name__ == "__main__":
    asyncio.run(main())
