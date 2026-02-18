import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env FIRST before anything else
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

import logfire
import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Configure Logfire
token = os.getenv("LOGFIRE_TOKEN")
if token:
    logfire.configure(
        token=token,
        send_to_logfire='always' # Be explicit to ensure it sends
    )
    logfire.info("Logfire initialized successfully for MMAM")
else:
    logfire.configure(send_to_logfire='never')
    print("WARNING: LOGFIRE_TOKEN not found in environment.")

# logfire.instrument_pydantic() # Trace all Pydantic models (Disabled for console cleanliness)
logfire.instrument_openai()   # Trace all NVIDIA NIM calls
try:
    # Attempt to instrument pydantic-ai if the plugin is available
    import pydantic_ai
    # Pydantic-AI often uses logfire internally or can be instrumented via the standard methods
    # but some versions have specific calls
except ImportError:
    pass

# App setup
from .core.config import settings
from .api.routes import auth, clients, portfolios, trading, agents, market_data, openbb_config, watchlist, analytics

# Socket.IO setup
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

# FastAPI app
app = FastAPI(title=settings.PROJECT_NAME)
logfire.instrument_fastapi(app)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3309", 
        "http://127.0.0.1:3309",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Logging Middleware
from .core.logging import LoggingMiddleware
app.add_middleware(LoggingMiddleware)

# Routes
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(clients.router, prefix=f"{settings.API_V1_STR}/clients", tags=["clients"])
app.include_router(portfolios.router, prefix=f"{settings.API_V1_STR}/portfolios", tags=["portfolios"])
app.include_router(trading.router, prefix=f"{settings.API_V1_STR}/trading", tags=["trading"])
app.include_router(agents.router, prefix=f"{settings.API_V1_STR}/agents", tags=["agents"])
app.include_router(market_data.router, prefix=f"{settings.API_V1_STR}/market", tags=["market"])
app.include_router(watchlist.router, prefix=f"{settings.API_V1_STR}/watchlist", tags=["watchlist"])
app.include_router(analytics.router, prefix=f"{settings.API_V1_STR}/analytics", tags=["analytics"])
app.include_router(openbb_config.router, prefix="", tags=["openbb"])

@app.get("/")
async def root():
    logfire.info("Root endpoint accessed via diagnostic check")
    return {"message": "MMAM Intelligence Core Running", "version": "1.0.0", "logging": "enabled"}

# Socket.IO events
from .core.logging import logger

@sio.event
async def connect(sid, environ):
    logger.info(f"Socket Client connected: {sid}")

@sio.event
async def disconnect(sid):
    logger.info(f"Socket Client disconnected: {sid}")

# Store sio reference for use in routes
app.state.sio = sio

# Mount Socket.IO ASGI wrapper (positional args only)
sio_app = socketio.ASGIApp(sio, app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:sio_app", host="0.0.0.0", port=8282, reload=True)
