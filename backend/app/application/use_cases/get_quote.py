"""
Use Case: Get Quote (SRP — Single Responsibility)
Orchestrates: Cache check → Parallel provider race → Return.
Depends on abstractions only (DIP).

PERFORMANCE: Providers are queried in parallel (first-wins race).
"""

import asyncio
import os
from typing import List, Optional, Dict, Any
from diskcache import Cache

from ...domain.entities.market import Quote
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...core.rate_limiter import get_bucket

CACHE_DIR = os.path.join(os.path.dirname(__file__), "../../../.cache")
_cache = Cache(CACHE_DIR)
QUOTE_TTL = 1  # 1 second for real-time accuracy


class GetQuoteUseCase:
    """
    Fetches a real-time quote using a parallel-race of providers.
    The first provider to return valid data wins; the rest are cancelled.
    """

    def __init__(self, providers: List[IMarketDataProvider]):
        self._providers = providers

    async def _try_provider(self, provider, symbol: str) -> Optional[Dict[str, Any]]:
        """Attempt a single provider; returns dict on success, None on failure."""
        bucket = get_bucket(provider.name)
        if not bucket.can_request():
            return None
        bucket.consume()
        try:
            quote = await provider.get_quote(symbol)
            if quote:
                return quote.to_dict()
        except Exception as e:
            print(f"[GetQuote] ⚠️ {provider.name}: {e}")
        return None

    async def execute(self, symbol: str) -> Dict[str, Any]:
        # 1. Cache check (instant)
        cache_key = f"quote_{symbol.replace('/', '_')}"
        cached = _cache.get(cache_key)
        if cached:
            return cached

        # 2. Race first N providers in parallel (first-wins)
        RACE_SIZE = min(3, len(self._providers))
        race_providers = self._providers[:RACE_SIZE]
        tasks = [asyncio.create_task(self._try_provider(p, symbol)) for p in race_providers]

        # As each task completes, check if we have a winner
        for coro in asyncio.as_completed(tasks):
            result = await coro
            if result:
                # Cancel remaining tasks
                for t in tasks:
                    t.cancel()
                result["source"] = result.get("source", "parallel-race")
                _cache.set(cache_key, result, expire=QUOTE_TTL)
                return result

        # 3. Fallback: try remaining providers sequentially
        for provider in self._providers[RACE_SIZE:]:
            result = await self._try_provider(provider, symbol)
            if result:
                _cache.set(cache_key, result, expire=QUOTE_TTL)
                return result

        return {"error": f"All providers exhausted or rate limited for {symbol}."}
