
import numpy as np
import sys
# Ensure we can import from the app
sys.path.append('c:\\AssetManager\\backend')

from app.agents.strategies.engine import indicators
import jesse_rust

def test_wma_rust():
    print(f"Jesse Rust Version (module check): {jesse_rust.__file__}")
    
    # Create sample data: price increasing by 1 each time
    # [timestamp, open, close, high, low, volume]
    candles = []
    for i in range(50):
        # Close price = i + 1
        candles.append({
            "timestamp": i * 60,
            "open": 100,
            "high": 110,
            "low": 90,
            "close": float(i + 1), 
            "volume": 500
        })
    
    # Calculate WMA 10
    # WMA(10) of sequence 1..50
    # Expected: WMA puts more weight on recent values.
    # WMA is sum(price[i] * weight[i]) / sum(weights)
    
    wma_val = indicators.wma(candles, period=10)
    print(f"WMA(10) calculated: {wma_val}")
    
    # Manual verification for last 10 candles (prices 41 to 50)
    # Weights 1..10
    prices = np.arange(41, 51)
    weights = np.arange(1, 11)
    expected = np.dot(prices, weights) / weights.sum()
    print(f"Expected manually: {expected}")
    
    assert abs(wma_val - expected) < 0.0001, "WMA calculation mismatch!"
    print("SUCCESS: WMA matches expected value.")

if __name__ == "__main__":
    try:
        test_wma_rust()
    except Exception as e:
        print(f"FAILED: {e}")
        import traceback
        traceback.print_exc()
