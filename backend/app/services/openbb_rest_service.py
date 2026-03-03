"""
OpenBB REST API Service
──────────────────────────────────────────────────────────────

Connects to the OpenBB Platform FastAPI server running on port 6900.
This is the PREFERRED execution path: zero subprocess overhead,
connection-pooled HTTP, and native chart support.

The OpenBB server is started alongside the backend via run_app.ps1:
    uvicorn openbb_core.api.router:app --host 0.0.0.0 --port 6900
"""

import httpx
import logging
import pandas as pd
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)

# Base URL for the OpenBB REST API server
OPENBB_API_BASE = "http://127.0.0.1:6900"


class OpenBBRestService:
    """
    High-performance client for the OpenBB REST API.
    Uses a persistent httpx.AsyncClient with connection pooling.
    """

    def __init__(self, base_url: str = OPENBB_API_BASE):
        self.base_url = base_url
        self._client: httpx.AsyncClient | None = None

    def _get_client(self) -> httpx.AsyncClient:
        """Lazily create a persistent, connection-pooled HTTP client."""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=30.0,
                limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
            )
        return self._client

    async def health_check(self) -> bool:
        """Check if the OpenBB API server is reachable."""
        try:
            client = self._get_client()
            resp = await client.get("/")
            return resp.status_code == 200
        except Exception:
            return False

    async def execute(self, command_path: str, kwargs: dict) -> dict:
        """
        Execute an OpenBB command via the REST API.

        Args:
            command_path: Dot-separated command path, e.g. "equity.price.quote"
            kwargs: Parameters dict, e.g. {"symbol": "AAPL", "provider": "yfinance"}

        Returns:
            dict with "output" (formatted text) or "error" key.
        """
        # Convert dot path → REST endpoint: equity.price.quote → /api/v1/equity/price/quote
        endpoint = "/api/v1/" + command_path.replace(".", "/")

        # Separate chart flag
        want_chart = kwargs.pop("chart", None)

        # Clean params: remove None values
        params = {k: v for k, v in kwargs.items() if v is not None}

        if want_chart:
            params["chart"] = "true"

        try:
            client = self._get_client()
            resp = await client.get(endpoint, params=params)

            if resp.status_code == 404:
                return {"error": f"Endpoint not found: {endpoint}. Check 'help' for available commands.", "type": "error"}

            resp.raise_for_status()
            data = resp.json()

            return self._format_response(data, command_path)

        except httpx.ConnectError:
            return {
                "error": "OpenBB API server is not running.\n"
                         "Start it with: run_app.ps1 or manually via:\n"
                         "  cd external_repos/OpenBB/OpenBB\n"
                         "  .venv/Scripts/python -m uvicorn openbb_core.api.rest_api:app --port 6900",
                "type": "error"
            }
        except httpx.HTTPStatusError as exc:
            body = exc.response.text[:500]
            return {"error": f"HTTP {exc.response.status_code}: {body}", "type": "error"}
        except Exception as e:
            return {"error": f"OpenBB API Error: {str(e)}", "type": "error"}

    def _format_response(self, data: dict, command_path: str) -> dict:
        """Format the raw API JSON response into readable terminal text."""
        # OpenBB API responses typically have a "results" key
        results = data.get("results")

        if results is None:
            # Some endpoints return data directly
            if isinstance(data, dict) and "error" in data:
                return {"error": data["error"], "type": "error"}
            return {"output": str(data)}

        # List of dicts → table format
        if isinstance(results, list):
            if len(results) == 0:
                return {"output": "Query returned no results."}

            try:
                df = pd.DataFrame(results)
                if df.empty:
                    return {"output": "Query returned no data."}

                # Trim wide DataFrames
                display_df = df.head(25)
                text = display_df.to_string(index=False)
                if len(df) > 25:
                    text += f"\n... Showing 25 of {len(df)} rows"
                return {"output": f"── {command_path} ──\n{text}"}
            except Exception:
                # Fallback: just stringify
                lines = [str(r) for r in results[:20]]
                text = "\n".join(lines)
                if len(results) > 20:
                    text += f"\n... Showing 20 of {len(results)} results"
                return {"output": text}

        # Single dict result
        if isinstance(results, dict):
            return {"output": self._format_dict(results)}

        return {"output": str(results)}

    @staticmethod
    def _format_dict(d: dict, indent: int = 0) -> str:
        """Pretty-format a dictionary for terminal display."""
        lines = []
        prefix = "  " * indent
        for k, v in d.items():
            if isinstance(v, float):
                lines.append(f"{prefix}{k}: {v:,.4f}")
            elif isinstance(v, int):
                lines.append(f"{prefix}{k}: {v:,}")
            else:
                lines.append(f"{prefix}{k}: {v}")
        return "\n".join(lines)

    async def fetch(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Generic HTTP GET for custom endpoints."""
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        try:
            client = self._get_client()
            response = await client.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.ConnectError:
            return {"error": "OpenBB API server offline", "detail": "Start the server on port 6900"}
        except httpx.HTTPStatusError as exc:
            return {"error": f"HTTP {exc.response.status_code}", "detail": exc.response.text}
        except Exception as e:
            return {"error": "Unexpected error", "detail": str(e)}

    async def post(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Generic HTTP POST for custom endpoints."""
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        try:
            client = self._get_client()
            response = await client.post(endpoint, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            return {"error": f"HTTP {exc.response.status_code}", "detail": exc.response.text}
        except Exception as e:
            return {"error": "Connection error", "detail": str(e)}


openbb_rest = OpenBBRestService()

