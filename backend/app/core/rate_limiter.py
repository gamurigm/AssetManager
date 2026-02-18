"""
Rate Limiter Module - Token Bucket Algorithm
Tracks API usage per provider and prevents exceeding free-tier limits.
Uses diskcache for persistence across restarts.
"""

import time
import os
from diskcache import Cache

CACHE_DIR = os.path.join(os.path.dirname(__file__), "../../.rate_limit_cache")
_rl_cache = Cache(CACHE_DIR)

# Provider limits (requests per minute for free tiers)
PROVIDER_LIMITS = {
    "fmp":        {"rpm": 5,   "daily": 250},
    "twelvedata": {"rpm": 8,   "daily": 800},
    "polygon":    {"rpm": 5,   "daily": 500},
    "yahoo":      {"rpm": 60,  "daily": 99999},  # Effectively unlimited for basic use
    "alphavantage":{"rpm": 5,  "daily": 25},
}


class TokenBucket:
    """
    Token Bucket rate limiter backed by diskcache.
    Each provider gets its own bucket that refills over time.
    """

    def __init__(self, provider: str):
        self.provider = provider
        limits = PROVIDER_LIMITS.get(provider, {"rpm": 5, "daily": 500})
        self.max_tokens_per_min = limits["rpm"]
        self.max_daily = limits["daily"]
        self._minute_key = f"rl_min_{provider}"
        self._daily_key = f"rl_day_{provider}"
        self._last_refill_key = f"rl_refill_{provider}"
        self._daily_reset_key = f"rl_daily_reset_{provider}"

    def _refill(self):
        """Refill tokens based on elapsed time."""
        now = time.time()
        last_refill = _rl_cache.get(self._last_refill_key, now)
        elapsed = now - last_refill

        if elapsed >= 60:
            # Full minute elapsed, reset minute tokens
            _rl_cache.set(self._minute_key, self.max_tokens_per_min)
            _rl_cache.set(self._last_refill_key, now)
        elif elapsed > 0:
            # Proportional refill
            current = _rl_cache.get(self._minute_key, self.max_tokens_per_min)
            refill_rate = self.max_tokens_per_min / 60.0
            new_tokens = min(self.max_tokens_per_min, current + (elapsed * refill_rate))
            _rl_cache.set(self._minute_key, new_tokens)
            _rl_cache.set(self._last_refill_key, now)

        # Daily reset check
        last_daily_reset = _rl_cache.get(self._daily_reset_key, 0)
        if now - last_daily_reset > 86400:  # 24 hours
            _rl_cache.set(self._daily_key, self.max_daily)
            _rl_cache.set(self._daily_reset_key, now)

    def can_request(self) -> bool:
        """Check if we have tokens available (both minute and daily)."""
        self._refill()
        minute_tokens = _rl_cache.get(self._minute_key, self.max_tokens_per_min)
        daily_tokens = _rl_cache.get(self._daily_key, self.max_daily)
        return minute_tokens >= 1 and daily_tokens >= 1

    def consume(self) -> bool:
        """
        Try to consume a token. Returns True if successful, False if rate limited.
        """
        self._refill()
        minute_tokens = _rl_cache.get(self._minute_key, self.max_tokens_per_min)
        daily_tokens = _rl_cache.get(self._daily_key, self.max_daily)

        if minute_tokens < 1 or daily_tokens < 1:
            print(f"[RateLimiter] ⛔ {self.provider} BLOCKED (min:{minute_tokens:.1f}, day:{daily_tokens})")
            return False

        _rl_cache.set(self._minute_key, minute_tokens - 1)
        _rl_cache.set(self._daily_key, daily_tokens - 1)
        return True

    def get_status(self) -> dict:
        """Get current rate limit status for monitoring."""
        self._refill()
        return {
            "provider": self.provider,
            "minute_remaining": round(_rl_cache.get(self._minute_key, self.max_tokens_per_min), 1),
            "minute_max": self.max_tokens_per_min,
            "daily_remaining": _rl_cache.get(self._daily_key, self.max_daily),
            "daily_max": self.max_daily,
        }


# Pre-instantiated buckets for each provider
buckets = {
    name: TokenBucket(name) for name in PROVIDER_LIMITS
}


def get_bucket(provider: str) -> TokenBucket:
    """Get the rate limiter bucket for a provider."""
    if provider not in buckets:
        buckets[provider] = TokenBucket(provider)
    return buckets[provider]


def get_all_statuses() -> list:
    """Get rate limit status for all providers (for dashboard monitoring)."""
    return [b.get_status() for b in buckets.values()]
