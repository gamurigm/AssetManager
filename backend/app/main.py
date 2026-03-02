import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env FIRST before anything else
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

import logfire
import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager

# Configure Logfire — try cloud, fall back silently if unreachable
token = os.getenv("LOGFIRE_TOKEN")
_logfire_online = False
if token:
    try:
        import urllib.request, ssl
        ctx = ssl.create_default_context()
        urllib.request.urlopen("https://logfire-us.pydantic.dev", context=ctx, timeout=3)
        _logfire_online = True
    except Exception:
        pass  # SSL error, timeout, or no internet — go offline

if token and _logfire_online:
    logfire.configure(token=token, send_to_logfire='always')
    logfire.info("Logfire initialized (cloud mode)")
else:
    logfire.configure(send_to_logfire='never')
    if token and not _logfire_online:
        print("INFO: Logfire cloud unreachable — running in local-only mode (no telemetry sent).")
    else:
        print("INFO: LOGFIRE_TOKEN not set — Logfire running in local-only mode.")

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
from .api.routes import auth, clients, portfolios, trading, agents, market_data, openbb_config, watchlist, analytics, simulation, bybit, finviz

# Socket.IO setup
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

from .services.scheduler_service import start_scheduler, stop_scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    start_scheduler()
    yield
    # Shutdown
    stop_scheduler()

# FastAPI app
app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)
logfire.instrument_fastapi(app)

# Performance: Compress large JSON responses (like historical data arrays)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3309", 
        "http://127.0.0.1:3309",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8282", # For self-referencing if needed
        "*" # Temporary for debugging if necessary, but we'll stick to specific ones + regex below
    ],
    allow_origin_regex="http://(localhost|127\.0\.0\.1):[0-9]+",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Logging Middleware
from .core.logging import LoggingMiddleware
app.add_middleware(LoggingMiddleware)

# Routes
from fastapi.staticfiles import StaticFiles
reports_path = os.path.join(os.getcwd(), "reports")
os.makedirs(reports_path, exist_ok=True)
app.mount("/view-reports", StaticFiles(directory=reports_path), name="reports")

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(clients.router, prefix=f"{settings.API_V1_STR}/clients", tags=["clients"])
app.include_router(portfolios.router, prefix=f"{settings.API_V1_STR}/portfolios", tags=["portfolios"])
app.include_router(trading.router, prefix=f"{settings.API_V1_STR}/trading", tags=["trading"])
app.include_router(agents.router, prefix=f"{settings.API_V1_STR}/agents", tags=["agents"])
app.include_router(market_data.router, prefix=f"{settings.API_V1_STR}/market", tags=["market"])
app.include_router(watchlist.router, prefix=f"{settings.API_V1_STR}/watchlist", tags=["watchlist"])
app.include_router(analytics.router, prefix=f"{settings.API_V1_STR}/analytics", tags=["analytics"])
app.include_router(simulation.router, prefix=f"{settings.API_V1_STR}/simulation", tags=["simulation"])
app.include_router(openbb_config.router, prefix="", tags=["openbb"])
app.include_router(bybit.router, prefix=f"{settings.API_V1_STR}/bybit", tags=["bybit"])
app.include_router(finviz.router, prefix=f"{settings.API_V1_STR}/finviz", tags=["finviz"])

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
    logger.info("Starting MMAM Backend on http://0.0.0.0:8282")
    # PERFORMANCE: Disable reload for production-like runs to reduce overhead
    # using workers=4 and optimized loop/http implementations
    uvicorn.run(
        "app.main:sio_app", 
        host="0.0.0.0", 
        port=8282, 
        reload=False, 
        workers=4,
        loop="auto",
        http="auto",
        log_level="info"
    )
