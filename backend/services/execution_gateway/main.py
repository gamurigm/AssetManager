"""HTTP entry point for the MT5 execution gateway.

The gateway is intentionally separate from the public API process.  It owns
the terminal adapter, execution journal, pre-trade checks and idempotency.
"""

from __future__ import annotations

import asyncio
import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, Query, status

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

from app.services.mt5_service import (
    MT5ConfigurationError,
    MT5Error,
    MT5ExecutionBlocked,
    MT5OrderIntent,
    MT5ValidationError,
    mt5_service,
)
from services.contracts.execution import (
    ExecutionExpertSignalRequest,
    ExecutionOrderRequest,
    KillSwitchRequest,
    KillSwitchResetRequest,
)
from services.platform.health import ServiceHealth
from services.execution_gateway.supervisor import ExecutionGatewaySupervisor


def _raise_http(exc: Exception) -> None:
    if isinstance(exc, MT5ConfigurationError):
        code = status.HTTP_503_SERVICE_UNAVAILABLE
    elif isinstance(exc, (MT5ValidationError, MT5ExecutionBlocked)):
        code = status.HTTP_422_UNPROCESSABLE_ENTITY
    else:
        code = status.HTTP_502_BAD_GATEWAY
    raise HTTPException(status_code=code, detail=str(exc)) from exc


def create_app(*, execution_service: Any = mt5_service) -> FastAPI:
    health = ServiceHealth("execution-gateway")
    health.register_dependency("mt5-adapter")
    supervisor = ExecutionGatewaySupervisor(
        execution_service=execution_service,
        health=health,
        interval_seconds=float(os.getenv("MT5_RECONCILE_INTERVAL_SECONDS", "30")),
        reconciliation_limit=int(os.getenv("MT5_RECONCILE_LIMIT", "200")),
    )
    supervisor_task = None

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        nonlocal supervisor_task
        health.mark_started()
        try:
            adapter_status = execution_service.get_status(include_account=False)
            health.set_dependency(
                "mt5-adapter",
                ready=bool(adapter_status.get("package_available")),
                detail=(
                    "adapter available"
                    if adapter_status.get("package_available")
                    else "adapter package unavailable"
                ),
            )
        except Exception as exc:
            health.set_dependency("mt5-adapter", ready=False, detail=str(exc))
        supervisor_task = asyncio.create_task(
            supervisor.run(), name="mt5-reconciliation-supervisor"
        )
        yield
        supervisor.stop()
        if supervisor_task:
            try:
                await asyncio.wait_for(supervisor_task, timeout=5)
            except asyncio.TimeoutError:
                supervisor_task.cancel()
        health.mark_stopped()

    app = FastAPI(
        title="AssetManager Execution Gateway",
        version="1.0.0",
        lifespan=lifespan,
    )

    def require_token(candidate: Optional[str]) -> None:
        if not execution_service.verify_gateway_token(candidate):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing or invalid MT5 gateway token",
            )

    @app.get("/health/live")
    async def live():
        return health.liveness()

    @app.get("/health/ready")
    async def ready():
        snapshot = health.readiness()
        if snapshot["status"] != "ready":
            raise HTTPException(status_code=503, detail=snapshot)
        return snapshot

    @app.get("/v1/status")
    async def gateway_status(
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        return execution_service.get_status(
            include_account=execution_service.verify_gateway_token(gateway_token)
        )

    @app.post("/v1/connect")
    async def connect(
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        require_token(gateway_token)
        try:
            result = await execution_service.connect()
            health.set_dependency("mt5-adapter", ready=True, detail="connected")
            return result
        except MT5Error as exc:
            _raise_http(exc)

    @app.post("/v1/preview")
    async def preview(
        order: ExecutionOrderRequest,
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        require_token(gateway_token)
        try:
            return await execution_service.preview_order(
                MT5OrderIntent(**order.model_dump())
            )
        except MT5Error as exc:
            _raise_http(exc)

    @app.post("/v1/orders")
    async def execute(
        order: ExecutionOrderRequest,
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        require_token(gateway_token)
        try:
            return await execution_service.execute_order(
                MT5OrderIntent(**order.model_dump())
            )
        except MT5Error as exc:
            _raise_http(exc)

    @app.post("/v1/experts/signals")
    async def expert_signal(
        signal: ExecutionExpertSignalRequest,
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        require_token(gateway_token)
        try:
            intent = MT5OrderIntent(**signal.model_dump(exclude={"execute"}))
            if signal.execute:
                result = await execution_service.execute_order(intent)
                return {"accepted": True, "executed": True, **result}
            preview = await execution_service.preview_order(intent)
            return {"accepted": True, "executed": False, "preview": preview}
        except MT5Error as exc:
            _raise_http(exc)

    @app.get("/v1/positions")
    async def positions(
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        require_token(gateway_token)
        try:
            return {"positions": await execution_service.positions()}
        except MT5Error as exc:
            _raise_http(exc)

    @app.get("/v1/experts/orders")
    async def recent_orders(
        limit: int = Query(default=50, ge=1, le=200),
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        require_token(gateway_token)
        return {"orders": execution_service.recent_orders(limit)}

    @app.post("/v1/reconcile")
    async def reconcile(
        limit: int = Query(default=200, ge=1, le=500),
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        require_token(gateway_token)
        try:
            return await execution_service.reconcile_orders(limit)
        except MT5Error as exc:
            _raise_http(exc)

    @app.post("/v1/kill-switch")
    async def activate_kill_switch(
        request: KillSwitchRequest,
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        require_token(gateway_token)
        try:
            return execution_service.activate_kill_switch(request.reason)
        except MT5Error as exc:
            _raise_http(exc)

    @app.post("/v1/kill-switch/reset")
    async def reset_kill_switch(
        request: KillSwitchResetRequest,
        gateway_token: Optional[str] = Header(
            default=None, alias="X-MT5-Gateway-Token"
        ),
    ):
        require_token(gateway_token)
        try:
            return execution_service.reset_kill_switch(confirm=request.confirm)
        except MT5Error as exc:
            _raise_http(exc)

    return app


app = create_app()
