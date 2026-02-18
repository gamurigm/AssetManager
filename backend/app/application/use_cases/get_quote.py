"""
Use Case: Get Quote (SRP — Single Responsibility)
Orchestrates: Cache check → Provider cascade (with rate limiting) → Return.
Depends on abstractions only (DIP).
"""

import os
from typing import List, Optional, Dict, Any
from diskcache import Cache

from ...domain.entities.market import Quote
from ...domain.interfaces.market_provider import IMarketDataProvider
from ...core.rate_limiter import get_bucket

CACHE_DIR = os.path.join(os.path.dirname(__file__), "../../../.cache")
_cache = Cache(CACHE_DIR)
QUOTE_TTL = 60  # seconds


class GetQuoteUseCase:
    """
    Fetches a real-time quote using a prioritized list of providers.
    Uses Token Bucket rate limiting per provider.
    """

    def __init__(self, providers: List[IMarketDataProvider]):
        # Injected dependencies — never concrete classes (DIP)
        self._providers = providers

    async def execute(self, symbol: str) -> Dict[str, Any]:
        # 1. Cache check
        cache_key = f"quote_{symbol.replace('/', '_')}"
        cached = _cache.get(cache_key)
        if cached:
            return cached

        # 2. Cascade through providers
        for provider in self._providers:
            bucket = get_bucket(provider.name)
            
            # Direct request (Rate limits bypassed in rate_limiter.py)
            if not bucket.can_request():
                print(f"[GetQuote] ⛔ {provider.name} rate limited for {symbol}")
                continue

            bucket.consume()
            
            try:
                quote = await provider.get_quote(symbol)
                if quote:
                    result = quote.to_dict()
                    _cache.set(cache_key, result, expire=QUOTE_TTL)
                    return result
            except Exception as e:
                print(f"[GetQuote] ⚠️ Error with {provider.name}: {e}")
                continue

        return {"error": f"All providers exhausted or rate limited for {symbol}."}
