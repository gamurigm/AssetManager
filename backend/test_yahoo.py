import yfinance as yf
import asyncio

def test_sync():
    print("--- Testing yfinance (Synchronous) ---")
    try:
        ticker = yf.Ticker("AAPL")
        hist = ticker.history(period="5d")
        print(f"History Type: {type(hist)}")
        print(f"History Empty: {hist.empty}")
        if not hist.empty:
            print(f"Latest Close: {hist['Close'].iloc[-1]}")
        else:
            print("❌ History is empty!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_sync()
