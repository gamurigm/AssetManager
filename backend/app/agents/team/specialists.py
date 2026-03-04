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
from ...services.openbb_rest_service import openbb_rest
from ...services.openbb_native_service import openbb_native
from ...services.openbb_api_catalog import openbb_catalog
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

async def discover_openbb_endpoints(ctx: RunContext[TeamContext], query: str) -> str:
    """
    Search the OpenBB Platform API for available endpoints matching a keyword.
    Use this FIRST to discover what data is available before calling query_openbb_api.
    
    Examples:
      - discover_openbb_endpoints(query="equity price") → finds stock price endpoints  
      - discover_openbb_endpoints(query="options") → finds options/derivatives endpoints
      - discover_openbb_endpoints(query="gdp") → finds GDP/economy endpoints
      - discover_openbb_endpoints(query="treasury") → finds fixed income endpoints
      - discover_openbb_endpoints(query="crypto") → finds crypto endpoints
      - discover_openbb_endpoints(query="technical") → finds all technical indicators
      - discover_openbb_endpoints(query="futures") → finds futures endpoints
    """
    await openbb_catalog.load()
    
    if query.lower() in ("categories", "all", "list", "help"):
        cats = openbb_catalog.list_categories()
        return f"Available OpenBB API categories: {', '.join(cats)}\nUse a category name or keyword to search for specific endpoints."
    
    results = openbb_catalog.search(query, limit=12)
    if not results:
        cats = openbb_catalog.list_categories()
        return f"No endpoints found for '{query}'. Try broader terms.\nAvailable categories: {', '.join(cats)}"
    
    lines = [f"Found {len(results)} OpenBB endpoints matching '{query}':"]
    for ep in results:
        lines.append(ep.to_compact_str())
    return "\n".join(lines)


async def get_openbb_endpoint_details(ctx: RunContext[TeamContext], endpoint_path: str) -> str:
    """
    Get full parameter details for a specific OpenBB API endpoint.
    Use the exact path from discover_openbb_endpoints.
    Example: get_openbb_endpoint_details(endpoint_path="/api/v1/equity/price/historical")
    """
    await openbb_catalog.load()
    ep = openbb_catalog.get_endpoint(endpoint_path)
    if not ep:
        return f"Endpoint '{endpoint_path}' not found. Use discover_openbb_endpoints to search first."
    return ep.to_detailed_str()


async def query_openbb_api(ctx: RunContext[TeamContext], endpoint: str, params: dict = None) -> str:
    """
    Fetch data from the OpenBB REST API (HTTP GET).
    The endpoint MUST start with `/api/v1/`. Parameters are query params.
    
    Examples:
      query_openbb_api(endpoint="/api/v1/equity/price/historical", params={"symbol": "AAPL", "provider": "yfinance"})
      query_openbb_api(endpoint="/api/v1/equity/fundamental/income", params={"symbol": "AAPL", "provider": "fmp", "limit": 4})
      query_openbb_api(endpoint="/api/v1/economy/fred_series", params={"symbol": "GDP"})
      query_openbb_api(endpoint="/api/v1/derivatives/options/chains", params={"symbol": "AAPL", "provider": "cboe"})
      query_openbb_api(endpoint="/api/v1/crypto/price/historical", params={"symbol": "BTCUSD", "provider": "yfinance"})
    """
    if params is None:
        params = {}
    
    result = await openbb_rest.fetch(endpoint, params)
    
    if "error" in result:
         return f"OpenBB API Error on {endpoint}: {result.get('error')} - {result.get('detail', '')}\nEnsure OpenBB is running on port 6900."
         
    import json
    res_str = json.dumps(result, indent=2)
    return res_str[:5000] + ("...\n[Truncated]" if len(res_str) > 5000 else "")


async def query_openbb_api_post(ctx: RunContext[TeamContext], endpoint: str, payload: dict) -> str:
    """
    Send data to OpenBB REST API via HTTP POST. Required for econometrics endpoints.
    
    Examples:
      query_openbb_api_post(endpoint="/api/v1/econometrics/correlation_matrix", payload=[{"date": "...", "open": ..., "close": ...}])
      query_openbb_api_post(endpoint="/api/v1/econometrics/ols_regression", payload={"data": [...], "y_column": "close", "x_columns": ["open", "high"]})
    """
    result = await openbb_rest.post(endpoint, payload)
    
    if "error" in result:
        return f"OpenBB POST Error on {endpoint}: {result.get('error')} - {result.get('detail', '')}"
    
    import json
    res_str = json.dumps(result, indent=2)
    return res_str[:5000] + ("...\n[Truncated]" if len(res_str) > 5000 else "")


async def execute_openbb_terminal_command(ctx: RunContext[TeamContext], command_path: str, symbol: str = None, chart: bool = False, limit: int = 10, **extra_kwargs) -> str:
    """
    Execute a native OpenBB Platform command via the persistent worker process.
    This supports ANY OpenBB command path and returns formatted text or opens charts.
    
    Examples:
      execute_openbb_terminal_command(command_path="equity.price.quote", symbol="AAPL")
      execute_openbb_terminal_command(command_path="equity.fundamental.income", symbol="AAPL")
      execute_openbb_terminal_command(command_path="technical.rsi", symbol="AAPL", chart=True)
      execute_openbb_terminal_command(command_path="economy.fred_series", symbol="GDP", chart=True)
      execute_openbb_terminal_command(command_path="derivatives.options.chains", symbol="AAPL")
      execute_openbb_terminal_command(command_path="crypto.price.historical", symbol="BTCUSD")
      execute_openbb_terminal_command(command_path="currency.price.historical", symbol="EURUSD")
      execute_openbb_terminal_command(command_path="fixedincome.government.treasury_rates", chart=True)
    """
    kwargs = {}
    if symbol:
        kwargs["symbol"] = symbol
    if chart:
        kwargs["chart"] = True
    if limit:
        kwargs["limit"] = limit
    kwargs.update(extra_kwargs)
        
    command_path = command_path.replace("/", ".")
    
    result = await openbb_native.execute(command_path, kwargs)
    if "error" in result:
        return f"Error: {result['error']}"
    return result.get("output", "Command executed.")

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

import os
import time

# ─── Load Prompts Dynamically ───

def _load_prompt(filename: str) -> str:
    """Load Markdown prompt from the prompts directory."""
    prompt_dir = os.path.join(os.path.dirname(__file__), "prompts")
    filepath = os.path.join(prompt_dir, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        return f"Error loading {filename}: {str(e)}"

OPENBB_API_REFERENCE = "\n\n" + _load_prompt("openbb_api_reference.md")

# --- Initialize Specialist Agents ---

fundamental_analyst = TeamAgent(
    name="Fundamental Analyst",
    role=_load_prompt("fundamental_analyst.md") + OPENBB_API_REFERENCE,
    model_name=NEMOTRON_253B,
    tools=[get_market_news, get_company_profile, get_balance_sheet, search_knowledge_base, read_textbook_section,
           general_web_search, discover_openbb_endpoints, get_openbb_endpoint_details, query_openbb_api, query_openbb_api_post,
           execute_openbb_terminal_command]
)

quant_analyst = TeamAgent(
    name="Quantitative Analyst",
    role=_load_prompt("quant_analyst.md") + OPENBB_API_REFERENCE,
    model_name=NEMOTRON_253B,
    tools=[get_price, get_technical_indicator, discover_openbb_endpoints, get_openbb_endpoint_details,
           query_openbb_api, query_openbb_api_post, execute_openbb_terminal_command]
)

risk_manager = TeamAgent(
    name="Risk Manager",
    role=_load_prompt("risk_manager.md") + OPENBB_API_REFERENCE,
    model_name=MISTRAL_LARGE,
    tools=[calculate_risk_metrics, generate_detailed_alpha_report, general_web_search,
           discover_openbb_endpoints, get_openbb_endpoint_details, query_openbb_api, execute_openbb_terminal_command]
)

macro_analyst = TeamAgent(
    name="Macro Analyst",
    role=_load_prompt("macro_analyst.md") + OPENBB_API_REFERENCE,
    model_name=NEMOTRON_253B,
    tools=[get_macro_indicators, general_web_search, discover_openbb_endpoints, get_openbb_endpoint_details,
           query_openbb_api, query_openbb_api_post, execute_openbb_terminal_command]
)

trader = TeamAgent(
    name="Trader",
    role=_load_prompt("trader.md") + OPENBB_API_REFERENCE,
    model_name=MISTRAL_LARGE,
    tools=[place_order, discover_openbb_endpoints, query_openbb_api, execute_openbb_terminal_command]
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

async def create_or_edit_strategy_engine(ctx: RunContext[TeamContext], strategy_name: str, code: str, description: str) -> str:
    """
    Creates or updates a Python strategy engine based on theoretical textbooks or user ideas.
    
    CRITICAL INSTRUCTIONS FOR THE CODE PARAMETER:
    1. You MUST import the interface: `from app.agents.strategies.engine.interfaces import IStrategyEngine`
    2. You MUST import models: `from app.agents.strategies.engine.models import StrategyConfig, TradeSignal`
    3. You MUST import typing: `from typing import List, Optional, Dict`
    4. Your class MUST inherit from `IStrategyEngine`.
    5. Your class MUST implement: 
       `def run_session(self, m5_candles: List[dict], m1_candles: List[dict], account_size: float, config: StrategyConfig) -> Optional[TradeSignal]:`
    6. Return a `TradeSignal` if criteria met, else `None`.
    
    This tool dynamically loads the code, registers it in the StrategyFactory, 
    and saves the file to disk so it can be backtested immediately.
    """
    import os
    from ...agents.strategies.engine.strategy_factory import StrategyFactory
    
    # Clean the code string (remove markdown blocks if present)
    if code.startswith("```python"):
        code = code[9:]
    elif code.startswith("```"):
        code = code[3:]
    if code.endswith("```"):
        code = code[:-3]
    code = code.strip()
    
    try:
        # Dynamically load and register
        StrategyFactory.load_from_code(strategy_name, code)
        
        # Save to disk for persistence
        file_name = f"{strategy_name.lower().replace(' ', '_')}.py"
        engine_dir = os.path.join(os.path.dirname(__file__), "..", "strategies", "engine")
        os.makedirs(engine_dir, exist_ok=True)
        
        file_path = os.path.join(engine_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
            
        return f"SUCCESS: Strategy '{strategy_name}' was verified, generated, and registered successfully. It is now available for Backtesting or live tracking. File saved at: {file_name}\nDescription: {description}"
        
    except Exception as e:
        return f"FAILED to create strategy: {str(e)}\nPlease review your Python code for syntax errors or missing required methods (run_session)."


strategy_analyst = TeamAgent(
    name="Strategy Analyst",
    role=_load_prompt("strategy_analyst.md") + OPENBB_API_REFERENCE,
    model_name=NEMOTRON_253B,
    tools=[run_strategy_signal, create_or_edit_strategy_engine, search_knowledge_base, read_textbook_section,
           general_web_search, discover_openbb_endpoints, get_openbb_endpoint_details, query_openbb_api,
           query_openbb_api_post, execute_openbb_terminal_command],
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
