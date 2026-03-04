import asyncio
from app.infrastructure.providers.finazon_provider import FinazonProvider

async def main():
    provider = FinazonProvider()
    print(f"Testing {provider.name} provider...")
    
    quote = await provider.get_quote("AAPL")
    print("\nQuote AAPL:")
    if quote:
        print(quote.__dict__)
    else:
        print("Failed to get quote")
        
    hist = await provider.get_historical("AAPL", limit=5)
    print("\nHistorical AAPL (Last 5 days):")
    if hist:
        for c in hist:
            print(c.__dict__)
    else:
        print("Failed to get historical")

if __name__ == "__main__":
    asyncio.run(main())
