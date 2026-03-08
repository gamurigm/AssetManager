import asyncio
import os
import sys

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), "backend"))

from app.services.ibkr_service import ibkr_service

async def test_connection():
    print("Attempting to connect to TWS via IBKRService...")
    # Ensure the IB instance is bound to the current event loop
    ibkr_service._ensure_ib_instance()
    # IBKRService uses candidates: [7497, 4002, 7496, 4001, 4000]
    # Default ClientID is now 100
    await ibkr_service.connect()
    status = ibkr_service.get_status()
    print("Connection Status:", status["connected"])
    if status["connected"]:
        print(f"Successfully connected to active port: {status['active_port']}")
        print(f"Active ClientID: {ibkr_service.client_id}")
    else:
        print("Failed to connect.")
        print("Last error:", status.get("last_connection_error"))
    
    ibkr_service.disconnect()

if __name__ == "__main__":
    asyncio.run(test_connection())
