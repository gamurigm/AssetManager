import os
import asyncio
import sys
from pathlib import Path

# MANDATORY: On Windows, ProactorEventLoop often breaks ib_insync/nest_asyncio.
# We force SelectorEventLoopPolicy BEFORE any loop is created.
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



from dotenv import load_dotenv
# Load .env ASAP
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# Configuration hydration must happen before integrations such as Logfire are
# initialized so credentials saved from the UI are available after a restart.
from .core.config import settings

_logfire_disabled = os.getenv("LOGFIRE_DISABLED", "").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}
# Development and test imports must remain offline by default.  A configured
# token is not enough to opt into a network probe; enable telemetry explicitly
# with LOGFIRE_ENABLED=true (production keeps the existing token behaviour).
_environment = os.getenv("ENVIRONMENT", "development").strip().lower()
_logfire_enabled = os.getenv("LOGFIRE_ENABLED", "").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}
if _environment not in {"production", "prod"} and not _logfire_enabled:
    _logfire_disabled = True
if _logfire_disabled:
    # The secure integration store hydrates LOGFIRE_TOKEN into the process.
    # Remove it before importing Logfire so offline local startup stays offline.
    os.environ.pop("LOGFIRE_TOKEN", None)

import logfire
import socketio
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager
from http.cookies import SimpleCookie

# Configure Logfire — try cloud, fall back silently if unreachable
token = "" if _logfire_disabled else settings.LOGFIRE_TOKEN
_logfire_online = False
if token and not _logfire_disabled:
    try:
        import urllib.request, ssl
        ctx = ssl.create_default_context()
        urllib.request.urlopen("https://logfire-us.pydantic.dev", context=ctx, timeout=3)
        _logfire_online = True
    except Exception:
        pass  # SSL error, timeout, or no internet — go offline

if _logfire_disabled:
    logfire.configure(send_to_logfire="never")
    print("INFO: Logfire disabled for this process.")
elif token and _logfire_online:
    logfire.configure(token=token, send_to_logfire='always')
    logfire.info("Logfire initialized (cloud mode)")
else:
    logfire.configure(send_to_logfire='never')
    if token and not _logfire_online:
        print("INFO: Logfire cloud unreachable — running in local-only mode (no telemetry sent).")
    else:
        print("INFO: LOGFIRE_TOKEN not set — Logfire running in local-only mode.")

# logfire.instrument_pydantic() # Trace all Pydantic models (Disabled for console cleanliness)
if not _logfire_disabled:
    logfire.instrument_openai()  # Trace all NVIDIA NIM calls
try:
    # Attempt to instrument pydantic-ai if the plugin is available
    import pydantic_ai
    # Pydantic-AI often uses logfire internally or can be instrumented via the standard methods
    # but some versions have specific calls
except ImportError:
    pass

from .core.security import get_current_principal, require_roles
from .core.database import initialize_database
from .core.jwt_keys import initialize_jwt_keys
from .models.models import UserRole
from .services.auth import decode_access_token

# App setup
from .api.routes import auth, clients, portfolios, trading, mt5, agents, market_data, openbb_config, watchlist, analytics, simulation, bybit, finviz, fmp, openbb_widgets, macro_economy, open_claw, integration_settings

# Socket.IO setup
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=settings.cors_origins,
)

from .services.realtime_service import realtime_service
from .services.ctrader_service import ctrader_service
from .services.ibkr_service import ibkr_service
from .services.simulation_service import simulation_service
from .services.portfolio_policy_realtime_service import portfolio_policy_realtime_service
from .core.runtime_policy import APIRuntimePolicy
from .core.errors import AppError, RequestValidationAppError, error_from_http_status

runtime_policy = APIRuntimePolicy.from_env()
kafka_consumer_service = None

# Suppress Twisted retry noise at module load (cTrader uses Twisted internally)
import logging as _logging
_logging.getLogger("twisted").setLevel(_logging.CRITICAL)

@asynccontextmanager
async def lifespan(app: FastAPI):
    global kafka_consumer_service

    # Startup
    initialize_jwt_keys()
    if not settings.is_production:
        await initialize_database()
    realtime_service.configure_streaming(
        sio,
        broker_streaming_enabled=runtime_policy.broker_connections_enabled,
    )
    if runtime_policy.kafka_fanout_enabled:
        from .services.kafka_consumer_service import kafka_consumer_service as kafka_service

        kafka_consumer_service = kafka_service
        kafka_consumer_service.start(sio)
    portfolio_policy_realtime_service.configure(sio)
    realtime_service.add_tick_listener(portfolio_policy_realtime_service.handle_price_update)
    simulation_service.configure_realtime(sio)
    if runtime_policy.scheduler_enabled:
        from .services.scheduler_service import start_scheduler

        start_scheduler(sio)

    ibkr_connect_task = None
    if runtime_policy.broker_connections_enabled:
        ctrader_service.start()
        ibkr_connect_task = asyncio.create_task(ibkr_service.connect())
    
    yield
    # Shutdown
    if runtime_policy.broker_connections_enabled:
        ibkr_service.disconnect()
        if ibkr_connect_task and not ibkr_connect_task.done():
            ibkr_connect_task.cancel()
    if runtime_policy.kafka_fanout_enabled:
        kafka_consumer_service.stop()
    realtime_service.remove_tick_listener(portfolio_policy_realtime_service.handle_price_update)
    realtime_service.shutdown_streaming()
    if runtime_policy.scheduler_enabled:
        from .services.scheduler_service import stop_scheduler

        stop_scheduler()

# FastAPI app
app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)
if not _logfire_disabled:
    logfire.instrument_fastapi(app)

# Performance: Compress large JSON responses (like historical data arrays)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID", "X-MT5-Gateway-Token"],
)

# Custom Logging Middleware
from .core.logging import LoggingMiddleware, logger
app.add_middleware(LoggingMiddleware)


def _request_id(request: Request) -> str | None:
    return getattr(request.state, "request_id", None) or request.headers.get("X-Request-ID")


@app.exception_handler(AppError)
async def app_error_handler(request: Request, error: AppError):
    request_id = _request_id(request)
    logger.warning(
        "Handled app error code=%s status=%s request_id=%s detail=%s",
        error.code,
        error.status_code,
        request_id,
        error.technical_detail,
    )
    return JSONResponse(status_code=error.status_code, content=error.to_payload(request_id=request_id))


@app.exception_handler(HTTPException)
@app.exception_handler(StarletteHTTPException)
async def http_error_handler(request: Request, error: HTTPException | StarletteHTTPException):
    """Convert legacy route exceptions to the same safe response schema."""
    normalized = error_from_http_status(error.status_code, error.detail)
    request_id = _request_id(request)
    logger.warning(
        "Handled HTTP error status=%s code=%s request_id=%s detail=%s",
        error.status_code,
        normalized.code,
        request_id,
        normalized.technical_detail,
    )
    return JSONResponse(
        status_code=error.status_code,
        content=normalized.to_payload(request_id=request_id),
        headers=error.headers,
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, error: RequestValidationError):
    normalized = RequestValidationAppError(
        message="Request validation failed",
        technical_detail=str(error.errors()),
    )
    request_id = _request_id(request)
    logger.warning("Request validation failed request_id=%s detail=%s", request_id, normalized.technical_detail)
    return JSONResponse(status_code=normalized.status_code, content=normalized.to_payload(request_id=request_id))


@app.exception_handler(Exception)
async def unexpected_error_handler(request: Request, error: Exception):
    request_id = _request_id(request)
    logger.exception("Unhandled API error request_id=%s", request_id)
    normalized = AppError(message="Unhandled server error", technical_detail=str(error))
    return JSONResponse(status_code=500, content=normalized.to_payload(request_id=request_id))

# Routes
reports_path = Path(settings.REPORTS_DIR).resolve()
reports_path.mkdir(parents=True, exist_ok=True)

protected = [Depends(get_current_principal)]
manager_only = [Depends(require_roles(UserRole.MANAGER))]

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(integration_settings.router, prefix=f"{settings.API_V1_STR}/settings/integrations", tags=["settings"], dependencies=manager_only)
app.include_router(clients.router, prefix=f"{settings.API_V1_STR}/clients", tags=["clients"], dependencies=manager_only)
app.include_router(portfolios.router, prefix=f"{settings.API_V1_STR}/portfolios", tags=["portfolios"], dependencies=protected)
app.include_router(trading.router, prefix=f"{settings.API_V1_STR}/trading", tags=["trading"], dependencies=protected)
app.include_router(mt5.router, prefix=f"{settings.API_V1_STR}/trading/mt5", tags=["trading", "mt5", "experts"], dependencies=manager_only)
app.include_router(agents.router, prefix=f"{settings.API_V1_STR}/agents", tags=["agents"], dependencies=protected)
app.include_router(market_data.router, prefix=f"{settings.API_V1_STR}/market", tags=["market"])
app.include_router(watchlist.router, prefix=f"{settings.API_V1_STR}/watchlist", tags=["watchlist"], dependencies=protected)
app.include_router(analytics.router, prefix=f"{settings.API_V1_STR}/analytics", tags=["analytics"], dependencies=protected)
app.include_router(simulation.router, prefix=f"{settings.API_V1_STR}/simulation", tags=["simulation"], dependencies=protected)
app.include_router(openbb_config.router, prefix="", tags=["openbb"], dependencies=protected)
app.include_router(openbb_widgets.router, prefix="", tags=["openbb", "widgets"], dependencies=protected)
app.include_router(macro_economy.router, prefix="", tags=["macro_economy"])
app.include_router(bybit.router, prefix=f"{settings.API_V1_STR}/bybit", tags=["bybit"])
app.include_router(finviz.router, prefix=f"{settings.API_V1_STR}/finviz", tags=["finviz"], dependencies=protected)
app.include_router(fmp.router, prefix=f"{settings.API_V1_STR}/fmp", tags=["fmp"], dependencies=protected)
app.include_router(open_claw.router, prefix=f"{settings.API_V1_STR}/openclaw", tags=["open_claw"], dependencies=manager_only)


@app.get("/view-reports/{filename}", include_in_schema=False)
async def view_report(
    filename: str,
    principal=Depends(get_current_principal),
):
    from fastapi.responses import Response
    from app.services.artifact_service import read_report
    from app.infrastructure.artifacts.store import ArtifactTooLarge

    try:
        artifact = await read_report(filename, principal)
    except (FileNotFoundError, PermissionError):
        raise HTTPException(status_code=404, detail="Report not found")
    except ArtifactTooLarge:
        raise HTTPException(status_code=413, detail="Report exceeds configured size limit")
    return Response(artifact.content, media_type=artifact.content_type, headers={
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Cache-Control": "private, no-store",
        "X-Content-Type-Options": "nosniff",
    })

@app.get("/")
async def root():
    logfire.info("Root endpoint accessed via diagnostic check")
    return {"message": "MMAM Intelligence Core Running", "version": "1.0.0", "logging": "enabled"}


@app.get("/health/live")
async def health_live():
    return {"service": "api-bff", "status": "alive"}


@app.get("/health/ready")
async def health_ready():
    kafka_running = bool(kafka_consumer_service and kafka_consumer_service.is_running)
    kafka_error = kafka_consumer_service.last_error if kafka_consumer_service else None
    dependencies = {
        "kafka_fanout": {
            "enabled": runtime_policy.kafka_fanout_enabled,
            "running": kafka_running,
            "error": kafka_error,
        },
        "embedded_scheduler": runtime_policy.scheduler_enabled,
        "embedded_brokers": runtime_policy.broker_connections_enabled,
    }
    kafka_ready = (
        not runtime_policy.kafka_fanout_enabled
        or (
            kafka_running
            and kafka_error is None
        )
    )
    snapshot = {
        "service": "api-bff",
        "status": "ready" if kafka_ready else "not_ready",
        "dependencies": dependencies,
    }
    if not kafka_ready:
        raise HTTPException(status_code=503, detail=snapshot)
    return snapshot

# Socket.IO events

def _socket_token(environ, auth) -> str | None:
    if isinstance(auth, dict) and auth.get("token"):
        return str(auth["token"])
    raw_cookie = environ.get("HTTP_COOKIE", "")
    if raw_cookie:
        cookie = SimpleCookie()
        cookie.load(raw_cookie)
        value = cookie.get(settings.AUTH_COOKIE_NAME)
        if value:
            return value.value
    return None


@sio.event
async def connect(sid, environ, auth=None):
    owner_id = 0
    if settings.AUTH_REQUIRED:
        token = _socket_token(environ, auth)
        if not token:
            return False
        try:
            payload = decode_access_token(token)
            owner_id = int(payload["uid"])
        except (KeyError, TypeError, ValueError):
            return False
    await sio.enter_room(sid, f"user:{owner_id}")
    logger.info(f"Socket Client connected: {sid}")

@sio.event
async def disconnect(sid):
    logger.info(f"Socket Client disconnected: {sid}")
    realtime_service.clear_client(sid)
    portfolio_policy_realtime_service.clear_client(sid)

@sio.on("join_symbol")
async def join_symbol(sid, symbol: str):
    try:
        normalized_symbol = symbol.upper()
        logger.info(f"[Socket] Client {sid} joining room: {normalized_symbol}")
        await sio.enter_room(sid, normalized_symbol)
        realtime_service.subscribe(sid, normalized_symbol)
    except (KeyError, ValueError):
        # A reconnect can race a queued join event.  It is harmless and should
        # not surface as an unhandled Socket.IO task exception.
        logger.debug(f"[Socket] Ignored join for disconnected client: {sid}")

@sio.on("leave_symbol")
async def leave_symbol(sid, symbol: str):
    try:
        normalized_symbol = symbol.upper()
        logger.info(f"[Socket] Client {sid} leaving room: {normalized_symbol}")
        await sio.leave_room(sid, normalized_symbol)
        realtime_service.unsubscribe(sid, normalized_symbol)
    except (KeyError, ValueError):
        logger.debug(f"[Socket] Ignored leave for disconnected client: {sid}")


@sio.on("subscribe_portfolio_policy")
async def subscribe_portfolio_policy(sid, payload=None):
    await portfolio_policy_realtime_service.subscribe(sid, payload or {})


@sio.on("unsubscribe_portfolio_policy")
async def unsubscribe_portfolio_policy(sid):
    await portfolio_policy_realtime_service.unsubscribe(sid)

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
        workers=1,
        loop="auto",
        http="auto",
        log_level="info"
    )
