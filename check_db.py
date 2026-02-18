import duckdb
import os

db_path = "backend/data/market.duckdb"
if os.path.exists(db_path):
    conn = duckdb.connect(db_path)
    res = conn.execute("SELECT symbol, COUNT(*), MIN(date), MAX(date) FROM ohlcv GROUP BY symbol").fetchall()
    for row in res:
        print(f"Symbol: {row[0]}, Count: {row[1]}, Min: {row[2]}, Max: {row[3]}")
    conn.close()
else:
    print("Database not found")
