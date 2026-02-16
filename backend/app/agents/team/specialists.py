from pydantic_ai import RunContext, Tool
from typing import Optional, List
from .state import TeamContext
from .base import TeamAgent
from ...services.openbb_service import openbb_service
from ...services.fmp_service import fmp_service
from ...services.market_data import market_data_service
from ...core.config import settings
import asyncio

# --- Constants for Models ---
MISTRAL_LARGE = "mistralai/mistral-large-3-675b-instruct-2512"
MIXTRAL_8X22B = "mistralai/mixtral-8x22b-instruct-v0.1"
GLM5 = "z-ai/glm5"

# --- Tools for Fundamental Analyst ---
async def get_market_news(ctx: RunContext[TeamContext], limit: int = 5) -> str:
    """Get latest market news headlines regarding a specific topic or general market."""
    news = await openbb_service.get_market_news(limit) 
    formatted = "\n".join([f"- {n.get('title', 'No Title')} ({n.get('date', 'Unknown Date')})" for n in news])
    return formatted if formatted else "No news found."

async def get_company_profile(ctx: RunContext[TeamContext], symbol: str) -> str:
    """Get company profile/description (sector, industry, business summary)."""
    profile = await fmp_service.get_profile(symbol)
    if not profile or "error" in profile: return "Company not found."
    description = profile.get('description', 'No description available')
    return f"{profile.get('companyName')} ({profile.get('sector')}): {description[:500]}..."

# --- Tools for Quantitative Analyst ---
async def get_price(ctx: RunContext[TeamContext], symbol: str) -> str:
    """
    Get real-time OR historical price data.
    Supports Stocks (AAPL), Crypto (BTC/USD), and Forex (EUR/USD).
    Automatically selects the best data source (FMP, TwelveData, or Polygon).
    """
    data = await market_data_service.get_price(symbol)
    if not data or "error" in data:
        return f"Error retrieving data for {symbol}: {data.get('error', 'Unknown error')}"
    
    price = data.get('price')
    source = data.get('source', 'Unknown')
    change = data.get('change', 'N/A')
    
    return f"Symbol: {symbol}\nPrice: ${price}\nSource: {source}\nChange: {change}"

async def get_technical_indicator(ctx: RunContext[TeamContext], symbol: str, indicator: str) -> str:
    """
    Get technical indicators (RSI, MACD, SMA, EMA).
    Uses Alpha Vantage for calculation.
    """
    data = await market_data_service.get_technical_indicator(symbol, indicator)
    if not data or "error" in data:
        return f"Error retrieving {indicator} for {symbol}."
        
    return f"{indicator} for {symbol}: {data.get('value')} (Source: {data.get('source')})"

# --- Tools for Risk Manager ---
async def check_compliance(ctx: RunContext[TeamContext], trade_details: str) -> str:
    """Validate if a trade complies with risk management policies."""
    # Mock compliance rules
    details_lower = trade_details.lower()
    if "speculative" in details_lower or "crypto" in details_lower:
        return "RISK WARNING: Trade flagged as high risk. Explicit approval required."
    
    # Store approval in context
    ctx.deps.update_scratchpad("RISK_APPROVED", True)
    return "RISK APPROVED: Trade complies with standard policy."

# --- Tools for Trader ---
async def place_order(ctx: RunContext[TeamContext], symbol: str, quantity: int, side: str, order_type: str = "market") -> str:
    """Execute a trade order (Buy/Sell). Requires Risk Manager approval."""
    # Check context for approval
    if not ctx.deps.scratchpad.get("RISK_APPROVED"):
        return "REJECTED: Risk Manager approval required before trading."
    
    # Mock execution logic
    order_id = f"ORD-{symbol}-{quantity}-{side.upper()}-{asyncio.get_event_loop().time()}"
    return f"ORDER EXECUTED: {side.upper()} {quantity} {symbol} @ {order_type.upper()}. ID: {order_id}"

# --- Initialize Specialist Agents ---

fundamental_analyst = TeamAgent(
    name="Fundamental Analyst",
    role="Specialist in qualitative analysis, news, and company fundamentals",
    model_name=MISTRAL_LARGE,
    tools=[get_market_news, get_company_profile]
)

quant_analyst = TeamAgent(
    name="Quantitative Analyst",
    role="Specialist in technical analysis, price data, and metrics",
    model_name=MIXTRAL_8X22B, # Use faster/larger context model for data
    tools=[get_price, get_technical_indicator]
)

risk_manager = TeamAgent(
    name="Risk Manager",
    role="Compliance officer responsible for validating all trades",
    model_name=MISTRAL_LARGE,
    tools=[check_compliance]
)

trader = TeamAgent(
    name="Trader",
    role="Execution specialist responsible for placing orders",
    model_name=MISTRAL_LARGE, # Use reliable model for tool calling
    tools=[place_order]
)

# Export map for Orchestrator lookup
specialists_map = {
    "Fundamental Analyst": fundamental_analyst,
    "Quantitative Analyst": quant_analyst,
    "Risk Manager": risk_manager,
    "Trader": trader
}
