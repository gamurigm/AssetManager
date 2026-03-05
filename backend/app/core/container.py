"""
Composition Root — Dependency Injection Container
This is the ONLY place where concrete classes are wired together.
All other modules depend on abstractions (interfaces), not implementations.

Pattern: Composition Root (replaces Service Locator anti-pattern).
"""

from ..infrastructure.providers import (
    YahooProvider, FMPProvider, TwelveDataProvider, PolygonProvider, AlphaVantageProvider,
    FinazonProvider, BybitProvider, LocalKnowledgeBaseProvider
)
from ..infrastructure.persistence import DuckDBRepository
from ..infrastructure.ai import (
    MistralLargeProvider, MixtralProvider, KimiProvider,
    DeepSeekProvider, NemotronProvider,
)
from ..application.use_cases import (
    GetQuoteUseCase, GetHistoricalUseCase,
    SearchKnowledgeBaseUseCase, ReadBookSectionUseCase,
    CalculateEquityCurveUseCase
)
from ..services.portfolio_chart_service import PortfolioChartService
from ..services.quant_models_service import QuantModelsService
from ..services.ml_models_service import MLModelsService


# --- Singletons (instantiated once) ---

# Market Data Providers (ordered by priority for cascade)
yahoo_provider = YahooProvider()
fmp_provider = FMPProvider()
twelvedata_provider = TwelveDataProvider()
polygon_provider = PolygonProvider()
alpha_vantage_provider = AlphaVantageProvider()
finazon_provider = FinazonProvider()
bybit_provider = BybitProvider()

# Finazon is omitted from the active chain due to severe Free Tier limits (only AAPL, GOOG, TSLA allowed)
_market_providers = [yahoo_provider, fmp_provider, twelvedata_provider, polygon_provider, bybit_provider]

# Persistence
duckdb_repo = DuckDBRepository()

# AI / LLM Providers
mistral_provider = MistralLargeProvider()
mixtral_provider = MixtralProvider()
kimi_provider = KimiProvider()
deepseek_provider = DeepSeekProvider()
nemotron_provider = NemotronProvider()

llm_providers = {
    "mistral": mistral_provider,
    "mixtral": mixtral_provider,
    "kimi": kimi_provider,
    "deepseek": deepseek_provider,
    "nemotron": nemotron_provider,
}

# Knowledge Base Provider
kb_provider = LocalKnowledgeBaseProvider()

# --- Use Cases (wired with dependencies) ---

get_quote = GetQuoteUseCase(providers=_market_providers)
get_historical = GetHistoricalUseCase(providers=_market_providers, repository=duckdb_repo)
search_knowledge_base_uc = SearchKnowledgeBaseUseCase(provider=kb_provider)
read_book_section_uc = ReadBookSectionUseCase(provider=kb_provider)
calculate_equity_curve_uc = CalculateEquityCurveUseCase(repository=duckdb_repo)
portfolio_charts = PortfolioChartService(repo=duckdb_repo, get_quote_use_case=get_quote)
quant_models = QuantModelsService(get_historical_uc=get_historical, yahoo_provider=yahoo_provider)
ml_models = MLModelsService()
