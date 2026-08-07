"""Public BFF routes proxying the isolated execution gateway."""

from __future__ import annotations

from typing import Any, Optional

from fastapi import APIRouter, Header, HTTPException, Query, status

from services.contracts.execution import (
    ExecutionExpertSignalRequest,
    ExecutionOrderRequest,
    KillSwitchRequest,
    KillSwitchResetRequest,
)

from ...services.execution_gateway_client import (
    ExecutionGatewayHTTPError,
    ExecutionGatewayUnavailable,
    execution_gateway_client,
)


router = APIRouter()

# Compatibility names used by existing callers and contract tests.
MT5OrderRequest = ExecutionOrderRequest
MT5ExpertSignalRequest = ExecutionExpertSignalRequest


async def _proxy(
    method: str,
    path: str,
    *,
    token: Optional[str] = None,
    payload: Optional[dict[str, Any]] = None,
    params: Optional[dict[str, Any]] = None,
):
    try:
        return await execution_gateway_client.request(
            method,
            path,
            token=token,
            payload=payload,
            params=params,
        )
    except ExecutionGatewayHTTPError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail) from exc
    except ExecutionGatewayUnavailable as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc


@router.get("/status")
async def get_mt5_status(
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy("GET", "/v1/status", token=gateway_token)


@router.post("/connect")
async def connect_mt5(
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy("POST", "/v1/connect", token=gateway_token)


@router.post("/preview")
async def preview_mt5_order(
    order: MT5OrderRequest,
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy(
        "POST", "/v1/preview", token=gateway_token, payload=order.model_dump()
    )


@router.post("/orders")
async def execute_mt5_order(
    order: MT5OrderRequest,
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy(
        "POST", "/v1/orders", token=gateway_token, payload=order.model_dump()
    )


@router.post("/experts/signals")
async def receive_expert_signal(
    signal: MT5ExpertSignalRequest,
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy(
        "POST",
        "/v1/experts/signals",
        token=gateway_token,
        payload=signal.model_dump(),
    )


@router.get("/positions")
async def get_mt5_positions(
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy("GET", "/v1/positions", token=gateway_token)


@router.get("/experts/orders")
async def get_mt5_expert_orders(
    limit: int = Query(default=50, ge=1, le=200),
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy(
        "GET",
        "/v1/experts/orders",
        token=gateway_token,
        params={"limit": limit},
    )


@router.post("/reconcile")
async def reconcile_mt5_orders(
    limit: int = Query(default=200, ge=1, le=500),
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy(
        "POST",
        "/v1/reconcile",
        token=gateway_token,
        params={"limit": limit},
    )


@router.post("/kill-switch")
async def activate_mt5_kill_switch(
    request: KillSwitchRequest,
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy(
        "POST",
        "/v1/kill-switch",
        token=gateway_token,
        payload=request.model_dump(),
    )


@router.post("/kill-switch/reset")
async def reset_mt5_kill_switch(
    request: KillSwitchResetRequest,
    gateway_token: Optional[str] = Header(default=None, alias="X-MT5-Gateway-Token"),
):
    return await _proxy(
        "POST",
        "/v1/kill-switch/reset",
        token=gateway_token,
        payload=request.model_dump(),
    )
