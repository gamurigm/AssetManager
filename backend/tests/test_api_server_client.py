from __future__ import annotations

import asyncio

import httpx
import pytest

from app.core.config import settings
from app.infrastructure.http.api_server_client import ApiServerClient, ApiServerError
from app.infrastructure.providers.fmp_provider import FMPProvider


@pytest.fixture
def gateway_settings(monkeypatch):
    monkeypatch.setattr(settings, "API_SERVER_BASE_URL", "http://gateway.test")
    monkeypatch.setattr(settings, "API_SERVER_API_KEY", "gateway-test-key")
    monkeypatch.setattr(settings, "FMP_TRANSPORT", "gateway")
    monkeypatch.setattr(settings, "FMP_GATEWAY_SLUG", "fmp")
    monkeypatch.setattr(settings, "FMP_API_KEY", "upstream-key-must-not-travel")


def test_provider_uses_gateway_and_keeps_original_parser(gateway_settings, monkeypatch):
    requests = []

    def respond(request):
        requests.append(request)
        assert request.url.path == "/api/v1/gateway/fmp/quote"
        assert dict(request.url.params) == {"symbol": "AAPL"}
        assert request.headers["Authorization"] == "Bearer gateway-test-key"
        return httpx.Response(200, json=[{"price": 123.5, "previousClose": 120}])

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as client:
            monkeypatch.setattr(FMPProvider, "_shared_client", client)
            quote = await FMPProvider().get_quote("AAPL")
            assert quote.price == 123.5
    asyncio.run(run())
    assert len(requests) == 1


@pytest.mark.parametrize("status", [301, 401, 403, 429, 502, 504])
def test_gateway_failure_never_retries_or_calls_direct(gateway_settings, monkeypatch, status):
    requests = []

    def respond(request):
        requests.append(request)
        return httpx.Response(status, headers={"X-Gateway-Request-Id": "correlation-1",
                                               "Retry-After": "10", "Location": "https://other.test"},
                              json={"error": {"message": "private provider details"}})

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as client:
            monkeypatch.setattr(FMPProvider, "_shared_client", client)
            with pytest.raises(ApiServerError) as failure:
                await FMPProvider().get_quote("AAPL")
            assert failure.value.metadata["gateway_request_id"] == "correlation-1"
            assert "private provider details" not in str(failure.value)
    asyncio.run(run())
    assert len(requests) == 1


@pytest.mark.parametrize("path", ["https://evil.test", "../quote", "/quote", "quote?apikey=x", "a//b"])
def test_rejects_non_relative_routes(gateway_settings, path):
    async def run():
        async with httpx.AsyncClient() as client:
            with pytest.raises(ValueError):
                await ApiServerClient(client).get("fmp", path, {})
    asyncio.run(run())


def test_missing_gateway_key_fails_before_network(gateway_settings, monkeypatch):
    monkeypatch.setattr(settings, "API_SERVER_API_KEY", "")
    async def run():
        async with httpx.AsyncClient() as client:
            with pytest.raises(ApiServerError):
                await ApiServerClient(client).providers()
    asyncio.run(run())
