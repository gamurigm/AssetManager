import duckdb
import os

DB_PATH = "c:/AssetManager/backend/data/market.duckdb"

def check_portfolio():
    if not os.path.exists(DB_PATH):
        print(f"Error: Database file not found at {DB_PATH}")
        return

    try:
        conn = duckdb.connect(DB_PATH)
        df = conn.execute("SELECT symbol, shares, entry_price, factor FROM portfolio").df()
        print("--- PORTFOLIO ---")
        print(df.to_string())
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_portfolio()
