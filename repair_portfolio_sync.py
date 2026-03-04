import duckdb
import os
from datetime import datetime

DB_PATH = "backend/data/market.duckdb"

# Metadata mapping for known symbols
METADATA = {
    "^N225": {"name": "Nikkei 225 Index", "sector": "Indices", "type": "cfd", "factor": 0.4166},
    "AAPL": {"name": "Apple Inc", "sector": "Technology", "type": "stock", "factor": 1.0},
    "PLTR": {"name": "Palantir Technologies", "sector": "Technology", "type": "stock", "factor": 1.0},
    "GC=F": {"name": "Gold Futures", "sector": "Commodities", "type": "cfd", "factor": 84.397},
    "JPM": {"name": "JPMorgan Chase & Co", "sector": "Financials", "type": "stock", "factor": 1.0},
    "COIN": {"name": "Coinbase Global Inc", "sector": "Digital Assets", "type": "stock", "factor": 1.0},
    "GS": {"name": "Goldman Sachs Group Inc", "sector": "Financials", "type": "stock", "factor": 1.0},
    "LMT": {"name": "Lockheed Martin Corp", "sector": "Industrials", "type": "stock", "factor": 1.0},
    "NVDA": {"name": "NVIDIA Corp", "sector": "Technology", "type": "stock", "factor": 1.0},
    "CHFJPY=X": {"name": "CHF/JPY", "sector": "Forex", "type": "cfd", "factor": 615.66},
    "ZT=F": {"name": "US 2 Year T-Note", "sector": "Bonds", "type": "cfd", "factor": 114.285},
    "EURUSD=X": {"name": "EUR/USD", "sector": "Forex", "type": "cfd", "factor": 100000},
    "DX-Y.NYB": {"name": "US Dollar Index", "sector": "Forex", "type": "cfd", "factor": 100.0},
}

def repair():
    if not os.path.exists(DB_PATH):
        print(f"DB not found at {DB_PATH}")
        return

    conn = duckdb.connect(DB_PATH)
    
    # Get current transaction summary
    # NOTE: Entry price for simplified reconciliation is the average price of all transactions for that symbol
    # (Or just the last price for simplicity in this repair)
    rows = conn.execute("""
        SELECT symbol, SUM(shares) as total_shares, AVG(price) as avg_price, MAX(date) as last_date
        FROM transactions
        GROUP BY symbol
        HAVING SUM(shares) != 0
    """).fetchall()

    print(f"Reconciling {len(rows)} symbols...")
    
    # Clear and rebuild portfolio
    conn.execute("DELETE FROM portfolio")
    
    for r in rows:
        symbol, shares, entry_price, last_date = r
        meta = METADATA.get(symbol, {"name": symbol, "sector": "Unknown", "type": "stock", "factor": 1.0})
        
        conn.execute("""
            INSERT INTO portfolio (symbol, name, shares, entry_price, factor, sector, asset_type, purchase_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [symbol, meta["name"], shares, entry_price, meta["factor"], meta["sector"], meta["type"], last_date])
        print(f"Sync: {symbol} -> {shares} shares @ ${entry_price:.2f}")

    conn.close()
    print("Repair complete.")

if __name__ == "__main__":
    repair()
