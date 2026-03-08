import asyncio
import sys
import nest_asyncio

# Force SelectorEventLoop BEFORE any loop is created
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

nest_asyncio.apply()

import uvicorn
from app.main import sio_app

async def main():
    config = uvicorn.Config(sio_app, host="0.0.0.0", port=8282, loop="asyncio")
    server = uvicorn.Server(config)
    print(f">>> [DEBUG] Starting server on loop: {asyncio.get_running_loop()}")
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
