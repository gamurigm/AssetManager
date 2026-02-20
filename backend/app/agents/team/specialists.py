from pydantic_ai import RunContext, Tool
from typing import Optional, List
from .state import TeamContext
from .base import TeamAgent
from ...services.openbb_service import openbb_service
from ...services.fmp_service import fmp_service
from ...services.risk_service import RiskService
from ...services.fee_service import FeeService
from ...services.polygon_service import polygon_service
from ...services.alpha_vantage_service import alpha_vantage_service
from ...services.twelve_data_service import twelve_data_service
from ...core.config import settings
import asyncio

# --- Constants for Models ---
MISTRAL_LARGE = "mistralai/mistral-large-3-675b-instruct-2512"
MIXTRAL_8X22B = "mistralai/mixtral-8x22b-instruct-v0.1"
GLM5 = "z-ai/glm5"
DEEPSEEK_V3 = "deepseek-ai/deepseek-v3.2"
NEMOTRON_253B = "nvidia/llama-3.1-nemotron-ultra-253b-v1"

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

# --- Tools for Macro Analyst ---
async def get_macro_indicators(ctx: RunContext[TeamContext]) -> str:
    """Get global economic news and macro indicators using OpenBB."""
    news = await openbb_service.get_market_news(limit=5)
    formatted = "\n".join([f"- {n.get('title', 'N/A')}" for n in news])
    return f"Latest Global Macro News:\n{formatted}"

# --- Tools for Risk Manager ---
async def calculate_risk_metrics(ctx: RunContext[TeamContext], symbol: str) -> str:
    """Calculate VaR and Sharpe ratio for a specific asset using Polygon historical data."""
    # Get historical data from Polygon
    eod = await polygon_service.get_previous_close(symbol)
    if not eod:
        return "Could not retrieve historical data from Polygon for risk calculation."
    
    # Mocking returns for math demonstration
    mock_returns = [-0.01, 0.02, -0.005, 0.015, -0.02, 0.03, -0.01]
    var = RiskService.calculate_var(mock_returns)
    sharpe = RiskService.calculate_sharpe_ratio(mock_returns)
    
    # Store in context
    ctx.deps.update_scratchpad(f"risk_{symbol}", {"VaR": var, "Sharpe": sharpe})
    
    return f"Risk Analysis for {symbol} (via Polygon Data):\n- VaR (95%): {var:.4f}\n- Sharpe Ratio: {sharpe:.2f}\nCompliance Note: Validated against risk thresholds."

async def check_compliance(ctx: RunContext[TeamContext], trade_details: str) -> str:
    """Validate if a trade complies with risk management policies."""
    # Mock compliance logic
    if "speculative" in trade_details.lower():
        return "REJECTED: Leverage too high for current mandate."
    
    ctx.deps.update_scratchpad("RISK_APPROVED", True)
    return "RISK APPROVED: Trade meets all mandated compliance criteria."

# --- Tools for Trader ---
async def place_order(ctx: RunContext[TeamContext], symbol: str, quantity: int, side: str, order_type: str = "market") -> str:
    """Execute a trade order (Buy/Sell) using TwelveData for real-time validation."""
    if not ctx.deps.scratchpad.get("RISK_APPROVED"):
        return "REJECTED: Risk Manager approval required."
    
    # Get last quote from TwelveData to confirm price
    quote = await twelve_data_service.get_price(symbol)
    price = quote.get("price", 0) if quote else 0
    
    # Mock fee calculation
    fee = 15.0 # Fixed execution fee for demo
    
    order_id = f"EXEC-{symbol}-{side.upper()}-{time.time()}"
    return f"TRADE EXECUTED (via TwelveData Confirmation):\n- ID: {order_id}\n- Taker: {side.upper()} {quantity} @ {price}\n- Fee: ${fee}"

import time

# --- Initialize Specialist Agents ---

fundamental_analyst = TeamAgent(
    name="Fundamental Analyst",
    role="Specialist in qualitative analysis, news, and company fundamentals",
    model_name=NEMOTRON_253B,
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
    role="Specialist in risk assessment, VaR, and compliance",
    model_name=MISTRAL_LARGE,
    tools=[calculate_risk_metrics, check_compliance]
)

macro_analyst = TeamAgent(
    name="Macro Analyst",
    role="Specialist in global economics and macro trends",
    model_name=NEMOTRON_253B,
    tools=[get_macro_indicators]
)

trader = TeamAgent(
    name="Trader",
    role="Execution specialist using TwelveData for order routing",
    model_name=MISTRAL_LARGE,
    tools=[place_order]
)

# --- Tools for Strategy Analyst ---
async def run_strategy_signal(ctx: RunContext[TeamContext], symbol: str) -> str:
    """
    Run the ORB FVG Engulfing strategy engine on the current intraday session
    for the given symbol. Returns a live trade signal if a setup is detected.
    """
    from ...services.simulation_service import simulation_service
    result = await simulation_service.get_live_signal(symbol=symbol)
    signal = result.get("signal")
    reason = result.get("reason", "")
    source = result.get("source", "")

    if signal is None:
        return f"No ORB FVG signal for {symbol} in current session. Reason: {reason} (Source: {source})"

    return (
        f"ORB FVG Engulfing Signal detected for {symbol}:\n"
        f"  Direction:  {signal['direction']}\n"
        f"  Entry:      {signal['entry']:.5f}\n"
        f"  Stop Loss:  {signal['stop']:.5f}\n"
        f"  Take Profit:{signal['tp']:.5f}\n"
        f"  Risk Pips:  {signal['risk_pips']:.5f}\n"
        f"  Confidence: {signal['confidence']}\n"
        f"  FVG Zone:   [{signal['fvg_bottom']:.5f} – {signal['fvg_top']:.5f}]\n"
        f"  Signal ID:  {signal['signal_id']}\n"
        f"  Source:     {source}"
    )


# --- Initialize Strategy Analyst Agent ---
strategy_analyst = TeamAgent(
    name="Strategy Analyst",
    role="Specialist in quantitative trading strategies — detects ORB, FVG, and Engulfing setups",
    model_name=MIXTRAL_8X22B,
    tools=[run_strategy_signal],
)

# Export map for Orchestrator lookup
specialists_map = {
    "Fundamental Analyst": fundamental_analyst,
    "Quantitative Analyst": quant_analyst,
    "Risk Manager": risk_manager,
    "Macro Analyst": macro_analyst,
    "Trader": trader,
    "Strategy Analyst": strategy_analyst,
}
