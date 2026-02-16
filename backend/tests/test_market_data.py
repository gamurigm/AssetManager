import asyncio
import os
import sys

# Add backend directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.market_data import market_data_service

async def run_tests():
    print("=== Starting Market Data Cascade Tests ===\n")

    # 1. Test US Stock (Should route to FMP)
    print("Testing US Stock: AAPL (Expected: FMP)")
    stock_data = await market_data_service.get_price("AAPL")
    print(f"Result: {stock_data}\n")

    # 2. Test Crypto (Should route to TwelveData)
    print("Testing Crypto: BTC/USD (Expected: TwelveData)")
    crypto_data = await market_data_service.get_price("BTC/USD")
    print(f"Result: {crypto_data}\n")

    # 3. Test Forex (Should route to TwelveData)
    print("Testing Forex: EUR/USD (Expected: TwelveData)")
    forex_data = await market_data_service.get_price("EUR/USD")
    print(f"Result: {forex_data}\n")

    # 4. Test Technical Indicator (Expected: Alpha Vantage)
    print("Testing Technical Indicator: RSI for AAPL (Expected: Alpha Vantage)")
    rsi_data = await market_data_service.get_technical_indicator("AAPL", "RSI")
    print(f"Result: {rsi_data}\n")

    # 5. Test Fallback (Polygon)
    # We can simulate this by putting a fake symbol or if we know FMP doesn't have it but Polygon might,
    # but for a simple test, let's just see if we can trigger the cascade.
    print("Testing Fallback/Specific Endpoint: MSFT (Primary FMP)")
    fallback_data = await market_data_service.get_price("MSFT")
    print(f"Result: {fallback_data}\n")

    print("=== Tests Completed ===")

if __name__ == "__main__":
    asyncio.run(run_tests())
