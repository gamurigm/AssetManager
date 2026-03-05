import duckdb
import os

DB_PATH = "c:/AssetManager/backend/data/market.duckdb"

def update_eurusd():
    if not os.path.exists(DB_PATH):
        print(f"Error: Database file not found at {DB_PATH}")
        return

    try:
        conn = duckdb.connect(DB_PATH)
        # 100,000 USD is 1 standard lot (shares = 1.0 or -1.0 depending on side)
        # Factor for EURUSD is 100,000.
        # To get 100,000 USD exposure: shares * price * factor = 100,000.
        # price approx 1.15. factor 100,000.
        # shares * 1.15 * 100,000 = 100,000  => shares = 1/1.15 approx 0.869.
        # But usually Forex is measured in units of base currency. 
        # If shares = -1.0 (1 lot short), exposure is 1.0 * 100,000 EUR = approx 115,000 USD.
        # If the user wants EXACTLY 100k USD, shares should be 100000 / (1.15 * 100000) = 0.8695
        # However, "100 mil" usually implies 1 lot. Let's aim for 1 unit if units = lots, or 
        # given the previous -10006 shares = 1.1B, then 1 share = 1 lot (100k units).
        # So for 100k USD exposure, shares should be ~0.87.
        
        # Let's check current price first to be precise
        res = conn.execute("SELECT entry_price FROM portfolio WHERE symbol = 'EURUSD=X'").fetchone()
        price = res[0] if res else 1.15
        
        # Calculation: shares * price * 100,000 = 100,000 => shares = 1 / price
        new_shares = - (1.0 / price) # Negative because "en contra" (short)
        
        conn.execute("UPDATE portfolio SET shares = ? WHERE symbol = 'EURUSD=X'", [new_shares])
        print(f"Updated EURUSD=X to {new_shares} shares (Exposure approx $100,000)")
        
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_eurusd()
