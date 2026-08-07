from __future__ import annotations

import asyncio

import httpx

from app.services.execution_gateway_client import (
    ExecutionGatewayClient,
    ExecutionGatewayHTTPError,
)


def test_client_forwards_token_payload_and_query_parameters() -> None:
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(200, json={"state": "previewed"})

    client = ExecutionGatewayClient(
        base_url="http://execution-gateway:8293",
        transport=httpx.MockTransport(handler),
    )

    result = asyncio.run(
        client.request(
            "POST",
            "/v1/preview",
            token="gateway-token",
            payload={"signal_id": "signal-001"},
            params={"limit": 10},
        )
    )

    request = captured["request"]
    assert result == {"state": "previewed"}
    assert request.url == "http://execution-gateway:8293/v1/preview?limit=10"
    assert request.headers["X-MT5-Gateway-Token"] == "gateway-token"
    assert request.read() == b'{"signal_id":"signal-001"}'


def test_client_preserves_gateway_error_status_and_detail() -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(422, json={"detail": "risk limit exceeded"})

    client = ExecutionGatewayClient(
        base_url="http://execution-gateway:8293",
        transport=httpx.MockTransport(handler),
    )

    try:
        asyncio.run(client.request("POST", "/v1/orders"))
    except ExecutionGatewayHTTPError as exc:
        assert exc.status_code == 422
        assert exc.detail == "risk limit exceeded"
    else:
        raise AssertionError("gateway HTTP failures must be surfaced")
