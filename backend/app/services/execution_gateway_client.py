"""HTTP adapter used by the public API to reach the execution boundary."""

from __future__ import annotations

import os
from typing import Any, Optional

import httpx


class ExecutionGatewayUnavailable(RuntimeError):
    pass


class ExecutionGatewayHTTPError(RuntimeError):
    def __init__(self, status_code: int, detail: str) -> None:
        super().__init__(detail)
        self.status_code = status_code
        self.detail = detail


class ExecutionGatewayClient:
    def __init__(
        self,
        *,
        base_url: Optional[str] = None,
        timeout_seconds: Optional[float] = None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self.base_url = (
            base_url
            or os.getenv("EXECUTION_GATEWAY_URL", "http://127.0.0.1:8293")
        ).rstrip("/")
        self.timeout_seconds = timeout_seconds or float(
            os.getenv("EXECUTION_GATEWAY_TIMEOUT_SECONDS", "20")
        )
        self.transport = transport

    async def request(
        self,
        method: str,
        path: str,
        *,
        token: Optional[str] = None,
        payload: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
    ) -> Any:
        headers = {"X-MT5-Gateway-Token": token} if token else {}
        try:
            async with httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout_seconds,
                transport=self.transport,
            ) as client:
                response = await client.request(
                    method,
                    path,
                    headers=headers,
                    json=payload,
                    params=params,
                )
        except httpx.RequestError as exc:
            raise ExecutionGatewayUnavailable(
                f"Execution gateway unavailable: {exc}"
            ) from exc

        if response.is_error:
            try:
                body = response.json()
                detail = body.get("detail", response.text)
            except ValueError:
                detail = response.text or "Execution gateway request failed"
            raise ExecutionGatewayHTTPError(response.status_code, str(detail))
        if not response.content:
            return None
        return response.json()


execution_gateway_client = ExecutionGatewayClient()
