
import asyncio
import os
import sys

# Add the current directory to sys.path so we can import 'app'
sys.path.append(os.getcwd())

from app.services.ibkr_service import ibkr_service

async def test_conn():
    print("Testing IBKR connection...")
    for client_id in [1, 2, 7, 99]:
        print(f"Trying Client ID: {client_id}...")
        ibkr_service.client_id = client_id
        await ibkr_service.connect()
        status = ibkr_service.get_status()
        if status["connected"]:
            print(f"✅ IBKR connected successfully with Client ID {client_id}!")
            return
        else:
            print(f"❌ Failed with Client ID {client_id}: {status['last_connection_error']}")

if __name__ == "__main__":
    asyncio.run(test_conn())
