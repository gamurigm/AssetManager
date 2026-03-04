"""
OpenBB API Catalog — Dynamic Endpoint Discovery
═══════════════════════════════════════════════════════════════
Fetches the full OpenAPI spec from the OpenBB Platform server
and builds a searchable catalog of all available endpoints.
Agents use this to understand exactly what data they can fetch.
"""

import httpx
import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger("MMAM")

OPENBB_API_BASE = "http://127.0.0.1:6900"


class EndpointInfo:
    """Represents a single OpenBB API endpoint."""
    __slots__ = ("path", "method", "operation_id", "summary", "description",
                 "tags", "parameters", "has_chart", "examples")

    def __init__(self, path: str, method: str, op: dict):
        self.path = path
        self.method = method.upper()
        self.operation_id = op.get("operationId", "")
        self.summary = op.get("summary", "")
        self.description = (op.get("description") or "")[:300]
        self.tags = op.get("tags", [])
        self.has_chart = any(
            p.get("name") == "chart" for p in op.get("parameters", [])
        )
        # Extract parameter names, types, required
        self.parameters: List[dict] = []
        for p in op.get("parameters", []):
            schema = p.get("schema", {})
            self.parameters.append({
                "name": p["name"],
                "required": p.get("required", False),
                "type": schema.get("type", "string"),
                "description": (p.get("description") or "")[:120],
            })
        # Extract examples
        self.examples: List[dict] = op.get("examples", [])

    def matches(self, query: str) -> bool:
        """Case-insensitive match against path, operation_id, summary, tags, description."""
        q = query.lower()
        return (
            q in self.path.lower()
            or q in self.operation_id.lower()
            or q in self.summary.lower()
            or q in self.description.lower()
            or any(q in t.lower() for t in self.tags)
        )

    def to_compact_str(self) -> str:
        """Compact representation for LLM context."""
        params_str = ", ".join(
            f"{p['name']}{'*' if p['required'] else ''}:{p['type']}"
            for p in self.parameters
            if p['name'] not in ('provider', 'chart')
        )
        chart_flag = " 📊" if self.has_chart else ""
        return f"{self.method} {self.path}{chart_flag}\n   {self.summary}\n   Params: [{params_str}]"

    def to_detailed_str(self) -> str:
        """Detailed representation with description and examples."""
        lines = [
            f"{'─' * 60}",
            f"{self.method} {self.path}",
            f"  Summary: {self.summary}",
            f"  Tags: {', '.join(self.tags)}",
            f"  Chart Support: {'Yes' if self.has_chart else 'No'}",
            f"  Description: {self.description}",
            f"  Parameters:",
        ]
        for p in self.parameters:
            req = " [REQUIRED]" if p["required"] else ""
            lines.append(f"    - {p['name']}: {p['type']}{req} — {p['description'][:80]}")
        if self.examples:
            lines.append("  Examples:")
            for ex in self.examples[:2]:
                if "parameters" in ex:
                    lines.append(f"    {ex.get('description', '')}: {ex['parameters']}")
        return "\n".join(lines)


class OpenBBAPICatalog:
    """
    Fetches and indexes the complete OpenBB OpenAPI specification.
    Provides search and listing capabilities for agents.
    """

    def __init__(self, base_url: str = OPENBB_API_BASE):
        self.base_url = base_url
        self._endpoints: List[EndpointInfo] = []
        self._categories: Dict[str, List[EndpointInfo]] = {}
        self._loaded = False

    async def load(self) -> bool:
        """Fetch and parse the OpenAPI spec. Returns True if successful."""
        if self._loaded:
            return True
        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                resp = await client.get(f"{self.base_url}/openapi.json")
                resp.raise_for_status()
                spec = resp.json()

            paths = spec.get("paths", {})
            for path, methods in paths.items():
                for method, operation in methods.items():
                    if method.lower() in ("get", "post", "put", "delete"):
                        ep = EndpointInfo(path, method, operation)
                        self._endpoints.append(ep)
                        for tag in ep.tags:
                            self._categories.setdefault(tag, []).append(ep)

            self._loaded = True
            logger.info(f"[OpenBB Catalog] Loaded {len(self._endpoints)} endpoints across {len(self._categories)} categories")
            return True
        except Exception as e:
            logger.warning(f"[OpenBB Catalog] Failed to load: {e}")
            return False

    @property
    def is_loaded(self) -> bool:
        return self._loaded

    def list_categories(self) -> List[str]:
        """List all available API categories (equity, crypto, economy, etc.)."""
        return sorted(self._categories.keys())

    def list_endpoints_by_category(self, category: str) -> List[EndpointInfo]:
        """List all endpoints in a category."""
        return self._categories.get(category, [])

    def search(self, query: str, limit: int = 15) -> List[EndpointInfo]:
        """Search endpoints by keyword."""
        matches = [ep for ep in self._endpoints if ep.matches(query)]
        return matches[:limit]

    def get_endpoint(self, path: str) -> Optional[EndpointInfo]:
        """Get details for a specific endpoint path."""
        for ep in self._endpoints:
            if ep.path == path:
                return ep
        return None

    def get_full_reference(self) -> str:
        """
        Generate a comprehensive, categorized reference of ALL endpoints.
        Used for injecting into agent system prompts.
        """
        lines = ["# OpenBB Platform API — Complete Endpoint Reference\n"]
        for cat in sorted(self._categories.keys()):
            endpoints = self._categories[cat]
            lines.append(f"\n## {cat.upper()} ({len(endpoints)} endpoints)")
            for ep in endpoints:
                lines.append(ep.to_compact_str())
        return "\n".join(lines)

    def get_category_reference(self, category: str) -> str:
        """Get detailed reference for a single category."""
        endpoints = self._categories.get(category, [])
        if not endpoints:
            return f"No endpoints found for category '{category}'. Available: {', '.join(self.list_categories())}"
        lines = [f"# OpenBB {category.upper()} Endpoints ({len(endpoints)} total)\n"]
        for ep in endpoints:
            lines.append(ep.to_detailed_str())
        return "\n".join(lines)


# Singleton instance
openbb_catalog = OpenBBAPICatalog()
