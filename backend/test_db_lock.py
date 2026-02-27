import duckdb
import os

db_path = "C:/AssetManager/data/market.duckdb"
print(f"Testing connection to {db_path}...")
try:
    conn = duckdb.connect(db_path, read_only=False)
    print("SUCCESS: Connected with write access")
    conn.close()
except Exception as e:
    print(f"FAILED (Write): {e}")

try:
    conn = duckdb.connect(db_path, read_only=True)
    print("SUCCESS: Connected with read-only access")
    conn.close()
except Exception as e:
    print(f"FAILED (Read): {e}")
