"""
Composition Root — Dependency Injection Container
This is the ONLY place where concrete classes are wired together.
All other modules depend on abstractions (interfaces), not implementations.

Pattern: Composition Root (replaces Service Locator anti-pattern).
"""

from ..infrastructure.providers import (
    YahooProvider, FMPProvider, TwelveDataProvider, PolygonProvider, AlphaVantageProvider,
)
from ..infrastructure.persistence import DuckDBRepository
from ..infrastructure.ai import (
    MistralLargeProvider, MixtralProvider, GLM5Provider,
    DeepSeekProvider, NemotronProvider,
)
from ..application.use_cases import GetQuoteUseCase, GetHistoricalUseCase


# --- Singletons (instantiated once) ---

# Market Data Providers (ordered by priority for cascade)
yahoo_provider = YahooProvider()
fmp_provider = FMPProvider()
twelvedata_provider = TwelveDataProvider()
polygon_provider = PolygonProvider()
alpha_vantage_provider = AlphaVantageProvider()

_market_providers = [yahoo_provider, fmp_provider, twelvedata_provider, polygon_provider]

# Persistence
duckdb_repo = DuckDBRepository()

# AI / LLM Providers
mistral_provider = MistralLargeProvider()
mixtral_provider = MixtralProvider()
glm5_provider = GLM5Provider()
deepseek_provider = DeepSeekProvider()
nemotron_provider = NemotronProvider()

llm_providers = {
    "mistral": mistral_provider,
    "mixtral": mixtral_provider,
    "glm5": glm5_provider,
    "deepseek": deepseek_provider,
    "nemotron": nemotron_provider,
}

# --- Use Cases (wired with dependencies) ---

get_quote = GetQuoteUseCase(providers=_market_providers)
get_historical = GetHistoricalUseCase(providers=_market_providers, repository=duckdb_repo)
