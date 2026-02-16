import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env FIRST before anything else
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

import logfire
import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Configure Logfire (after .env is loaded)
logfire.configure(
    token=os.getenv("LOGFIRE_TOKEN"),
    send_to_logfire='if-token-present'
)

# App setup
from .core.config import settings
from .api.routes import auth, clients, portfolios, trading, agents, market_data, openbb_config

# Socket.IO setup
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

# FastAPI app
app = FastAPI(title=settings.PROJECT_NAME)
logfire.instrument_fastapi(app)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "https://pro.openbb.co"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(clients.router, prefix=f"{settings.API_V1_STR}/clients", tags=["clients"])
app.include_router(portfolios.router, prefix=f"{settings.API_V1_STR}/portfolios", tags=["portfolios"])
app.include_router(trading.router, prefix=f"{settings.API_V1_STR}/trading", tags=["trading"])
app.include_router(agents.router, prefix=f"{settings.API_V1_STR}/agents", tags=["agents"])
app.include_router(market_data.router, prefix=f"{settings.API_V1_STR}/market", tags=["market"])
app.include_router(openbb_config.router, prefix="", tags=["openbb"]) # OpenBB Workspace expects root or specific paths for config

@app.get("/")
async def root():
    return {"message": "AI Asset Manager Backend Running", "version": "1.0.0"}

# Socket.IO events
@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

# Store sio reference for use in routes
app.state.sio = sio

# Mount Socket.IO ASGI wrapper (positional args only)
sio_app = socketio.ASGIApp(sio, app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:sio_app", host="0.0.0.0", port=8000, reload=True)
