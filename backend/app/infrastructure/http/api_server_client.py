"""API_Server transport. Upstream keys never travel to the gateway.

Only explicit relative routes and configured provider slugs are accepted.
There are no automatic retries or fallback to a direct provider: quota and
authentication failures remain visible to callers.
"""

from __future__ import annotations

import re
from urllib.parse import urlsplit

import httpx

from app.core.config import settings
from app.core.errors import ExternalProviderError


class ApiServerError(ExternalProviderError):
    code = "api_server_error"
    user_message = "API_Server no pudo completar la consulta. Revisa la integración."

    def __init__(self, status: int, *, request_id: str = "", retry_after: str = ""):
        super().__init__(
            provider="api_server",
            message=f"API_Server HTTP {status}",
            retryable=status in {429, 502, 503, 504},
            metadata={"upstream_status": status, "gateway_request_id": request_id,
                      "retry_after": retry_after},
        )
        # A failed application credential must not log the AssetManager user out.
        self.status_code = status if status in {429, 502, 503, 504} else 503


class ApiServerClient:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    def _url(self, route: str) -> str:
        base = settings.API_SERVER_BASE_URL.rstrip("/")
        parsed = urlsplit(base)
        if (parsed.scheme not in {"http", "https"} or not parsed.hostname
                or parsed.username or parsed.password or parsed.query or parsed.fragment
                or parsed.path not in {"", "/"}):
            raise ApiServerError(503)
        if settings.is_production and parsed.scheme != "https":
            raise ApiServerError(503)
        if not settings.API_SERVER_API_KEY:
            raise ApiServerError(503)
        return base + route

    async def _get(self, route: str, params: dict | None = None) -> httpx.Response:
        try:
            response = await self.client.get(
                self._url(route), params=params,
                headers={"Authorization": f"Bearer {settings.API_SERVER_API_KEY}",
                         "Accept": "application/json"},
                timeout=settings.API_SERVER_TIMEOUT_SECONDS,
                follow_redirects=False,
            )
        except httpx.TimeoutException:
            raise ApiServerError(504) from None
        except httpx.RequestError:
            raise ApiServerError(502) from None
        if not 200 <= response.status_code < 300:
            raise ApiServerError(
                response.status_code,
                request_id=response.headers.get("X-Gateway-Request-Id", "")[:128],
                retry_after=response.headers.get("Retry-After", "")[:64],
            )
        return response

    async def providers(self) -> httpx.Response:
        return await self._get("/api/v1/providers")

    async def get(self, slug: str, path: str, params: dict) -> httpx.Response:
        if (not re.fullmatch(r"[a-zA-Z0-9_-]+", slug)
                or not re.fullmatch(r"[a-zA-Z0-9_/-]+", path)
                or path.startswith("/") or "//" in path):
            raise ValueError("Invalid gateway provider or relative path")
        clean = {k: v for k, v in params.items()
                 if k.lower() not in {"apikey", "api_key", "token", "access_token"}}
        return await self._get(f"/api/v1/gateway/{slug}/{path}", clean)


async def provider_get(client, provider: str, path: str, params: dict):
    """Shared boundary used by both legacy services and domain providers."""
    prefix = {"fmp": "FMP", "twelvedata": "TWELVE_DATA"}[provider]
    if settings.is_production and getattr(settings, f"{prefix}_TRANSPORT") != "gateway":
        raise ApiServerError(503)
    if getattr(settings, f"{prefix}_TRANSPORT") == "gateway":
        return await ApiServerClient(client).get(
            getattr(settings, f"{prefix}_GATEWAY_SLUG"), path, params,
        )
    return await client.get(
        f"{getattr(settings, f'{prefix}_BASE_URL').rstrip('/')}/{path}", params=params,
    )
