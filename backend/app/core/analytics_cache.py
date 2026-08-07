"""
Server-side TTL cache for heavy analytics computations.

Each analytics service (GARCH, Kalman, IV, Regimes) does expensive
numerical work (MLE optimisation, Newton-Raphson IV inversion, Markov
chain estimation).  Since the underlying data only changes once per
trading day, we cache the results for 10 minutes to avoid redundant
computation on repeated or rapid requests.

Usage:
    from app.core.analytics_cache import analytics_cache
    result = analytics_cache.get("arch", "AAPL")
    if result is None:
        result = await compute(...)
        analytics_cache.set("arch", "AAPL", result)
"""

from __future__ import annotations

import time
from typing import Any, Dict, Optional

_TTL_SECONDS = 600  # 10 minutes


class _CacheEntry:
    __slots__ = ("data", "ts")

    def __init__(self, data: Any) -> None:
        self.data = data
        self.ts = time.monotonic()

    def is_stale(self) -> bool:
        return (time.monotonic() - self.ts) > _TTL_SECONDS


class AnalyticsCache:
    """Simple in-process TTL cache keyed by (namespace, symbol)."""

    def __init__(self) -> None:
        self._store: Dict[str, _CacheEntry] = {}

    def _key(self, namespace: str, symbol: str) -> str:
        return f"{namespace}:{symbol.upper()}"

    def get(self, namespace: str, symbol: str) -> Optional[Any]:
        entry = self._store.get(self._key(namespace, symbol))
        if entry is None or entry.is_stale():
            return None
        return entry.data

    def set(self, namespace: str, symbol: str, data: Any) -> None:
        self._store[self._key(namespace, symbol)] = _CacheEntry(data)

    def invalidate(self, namespace: str, symbol: str) -> None:
        self._store.pop(self._key(namespace, symbol), None)

    def clear(self) -> None:
        self._store.clear()


analytics_cache = AnalyticsCache()
