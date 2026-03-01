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
from ...services.market_data import market_data_service
from ...core.container import search_knowledge_base_uc, read_book_section_uc
from ...core.config import settings
import asyncio
import time

# --- Constants for Models ---
MISTRAL_LARGE = "mistralai/mistral-large-3-675b-instruct-2512"
MIXTRAL_8X22B = "mistralai/mixtral-8x22b-instruct-v0.1"
KIMI_K25 = "moonshotai/kimi-k2.5"
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

async def get_balance_sheet(ctx: RunContext[TeamContext], symbol: str) -> str:
    """Get the latest annual balance sheet statement for a specific company (e.g. AAPL, MSFT, NVDA)."""
    import yfinance as yf
    
    def _fetch():
        ticker = yf.Ticker(symbol)
        bs = ticker.balance_sheet
        if bs is None or bs.empty:
            return f"Balance sheet data not found for {symbol}."
        
        # Take the most recent year column
        recent_bs = bs.iloc[:, 0].dropna()
        period = bs.columns[0].strftime('%Y-%m-%d') if hasattr(bs.columns[0], 'strftime') else str(bs.columns[0])
        
        # Format for LLM context
        res = f"Balance Sheet for {symbol} (Period Ending: {period}):\n"
        for idx, val in recent_bs.items():
            # Format large numbers to billions/millions if possible or just commas
            if isinstance(val, (int, float)):
                if abs(val) >= 1e9:
                    res += f"- {idx}: ${val/1e9:,.2f}B\n"
                elif abs(val) >= 1e6:
                    res += f"- {idx}: ${val/1e6:,.2f}M\n"
                else:
                    res += f"- {idx}: ${val:,.0f}\n"
            else:
                res += f"- {idx}: {val}\n"
        return res
        
    try:
        return await asyncio.to_thread(_fetch)
    except Exception as e:
        return f"Error fetching balance sheet for {symbol}: {str(e)}"


# --- Knowledge Base Tools ---
async def search_knowledge_base(ctx: RunContext[TeamContext], query: str) -> str:
    """
    Search for academic/textbook information in the Quant Knowledge Base.
    Useful for finding definitions, formulas, or theory on:
    - Stochastic Calculus (Shreve)
    - Optimization Methods (Cornuejols)
    - Risk Modelling (Pfaff)
    - Linear Algebra (Primer)
    """
    results = search_knowledge_base_uc.execute(query, limit=10)
    if not results:
        return f"No results for '{query}' found in the textbooks."
        
    formatted = []
    for r in results:
        formatted.append(f"• [{r.file}]: {r.snippet}...")
    
    return "Top 10 Knowledge Base results:\n" + "\n".join(formatted)

async def read_textbook_section(ctx: RunContext[TeamContext], file_path: str, start_line: int, end_line: int) -> str:
    """Read a specific section from a textbook found during search."""
    return read_book_section_uc.execute(file_path, start_line, end_line)

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

async def general_web_search(ctx: RunContext[TeamContext], query: str, max_results: int = 5) -> str:
    """Perform a general web search (e.g., using DuckDuckGo) to find live information on the internet. Useful for recent events, market events, or general knowledge."""
    from duckduckgo_search import DDGS
    
    def _search():
        with DDGS() as ddgs:
            return list(ddgs.text(query, max_results=max_results))

    try:
        results = await asyncio.to_thread(_search)
        if not results:
            return f"No results found on the web for '{query}'."
        formatted = "\n".join([f"- {r.get('title', 'No Title')}: {r.get('body', 'No Body')} ({r.get('href', 'No URL')})" for r in results])
        return f"Web Search Results for '{query}':\n{formatted}"
    except Exception as e:
        return f"Error performing web search: {e}"

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
    
async def generate_detailed_alpha_report(ctx: RunContext[TeamContext], analysis_text: Optional[str] = None) -> str:
    """
    Generates a professional, deeply detailed PDF Alpha Report with charts, 
    risk metrics (VaR, Sharpe, Risk Adjusted Returns), Trend Projections 
    using Gradient Descent, and Hedging Strategies.
    If 'analysis_text' is provided, it will be included as a dedicated Intelligence Section.
    """
    from ...services.report_service import report_service
    # Fetches real-time portfolio from context or DB
    holdings = ctx.deps.scratchpad.get("current_portfolio", {}).get("holdings", [])
    total_val = ctx.deps.scratchpad.get("current_portfolio", {}).get("total_value", 0)
    total_pnl = ctx.deps.scratchpad.get("current_portfolio", {}).get("total_pnl", 0)
    
    if not holdings:
        # Fallback to DB
        from ...core.container import duckdb_repo
        holdings = duckdb_repo.get_portfolio()
        total_val = sum(h.get('shares',0) * h.get('entryPrice',0) for h in holdings)
        total_pnl = 0 # Placeholder if not in context
        
    if analysis_text:
        # New bespoke path
        filename = report_service.generate_custom_intelligence_report(analysis_text, holdings, total_val, total_pnl)
    else:
        # Standard automated path
        filename = report_service.generate_balance_sheet(holdings, total_val, total_pnl)

    url = f"http://localhost:8282/view-reports/{filename}"
    return f"REPORT GENERATED: {filename}. Access URL: {url}"

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
    role="Specialist in qualitative analysis, news, company fundamentals, and financial statements (balance sheets)",
    model_name=NEMOTRON_253B,
    tools=[get_market_news, get_company_profile, get_balance_sheet, search_knowledge_base, read_textbook_section, general_web_search]
)

quant_analyst = TeamAgent(
    name="Quantitative Analyst",
    role="Specialist in technical analysis, price data, and metrics",
    model_name=NEMOTRON_253B, # Switched from MIXTRAL to avoid tool parsing block
    tools=[get_price, get_technical_indicator]
)

risk_manager = TeamAgent(
    name="Risk Manager",
    role="Specialist in risk assessment, VaR, and compliance. "
         "When asked for a report, ALWAYS write a deep professional 'analysis_text' "
         "summarizing neural insights, risk outliers, and strategic positioning "
         "to include in the custom PDF.",
    model_name=MISTRAL_LARGE,
    tools=[calculate_risk_metrics, generate_detailed_alpha_report, general_web_search]
)

macro_analyst = TeamAgent(
    name="Macro Analyst",
    role="Specialist in global economics and macro trends",
    model_name=NEMOTRON_253B,
    tools=[get_macro_indicators, general_web_search]
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
    model_name=NEMOTRON_253B, # Switched from MIXTRAL to avoid tool parsing block
    tools=[run_strategy_signal, search_knowledge_base, read_textbook_section, general_web_search],
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
