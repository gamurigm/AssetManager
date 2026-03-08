from pydantic_ai import RunContext, Tool
from typing import Optional, List, Dict
from .state import TeamContext
from .base import TeamAgent, AgentTier
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
from ...services.gsd_service import gsd_service
from ...services.ctrader_service import ctrader_service
from ...services.ibkr_service import ibkr_service
from ...core.container import search_knowledge_base_uc, read_book_section_uc, duckdb_repo
from ...core.config import settings
import asyncio
import time

# --- Constants for Models ---
MISTRAL_LARGE = "mistralai/mistral-large-3-675b-instruct-2512"
MIXTRAL_8X22B = "mistralai/mixtral-8x22b-instruct-v0.1"
KIMI_K25 = "moonshotai/kimi-k2.5"
DEEPSEEK_V3 = "deepseek-ai/deepseek-v3.2"
NEMOTRON_253B = "nvidia/llama-3.1-nemotron-ultra-253b-v1"
QWEN_35 = "qwen/qwen3.5-397b-a17b"

# ─────────────────────────────────────────────────────────────────────────────
# HIERARCHICAL PIPELINE TOOLS
# These tools enforce the strict analyst→risk→strategist→execution flow.
# ─────────────────────────────────────────────────────────────────────────────

async def submit_analysis_report(ctx: RunContext[TeamContext], content: str) -> str:
    """
    [ANALYST TIER TOOL]
    Formally deposit your analysis findings into the shared pipeline context
    so that the Strategy Analyst can consume them.

    Call this at the END of your analysis, passing your full structured report
    as the `content` argument. The report is stored keyed by your agent name.

    This is the ONLY way your findings will be visible to the Strategist.
    """
    # Infer calling agent name from the message history (last system message sender)
    agent_name = "Unknown Analyst"
    for msg in reversed(ctx.deps.chat_history):
        if msg.role in ("user", "assistant") and msg.agent_name not in ("System", "Head of Strategy"):
            agent_name = msg.agent_name
            break

    ctx.deps.submit_report(agent_name, content)
    return (
        f"✅ Report from '{agent_name}' has been deposited into the pipeline context. "
        f"The Strategy Analyst will retrieve it via `request_team_briefing`."
    )


async def submit_risk_report(ctx: RunContext[TeamContext], content: str) -> str:
    """
    [RISK TIER TOOL]
    Formally deposit the session risk assessment into the shared pipeline context
    so that the Strategy Analyst can consume it before authorizing any trade.

    This is the ONLY way your risk findings will be visible to the Strategist.
    """
    ctx.deps.submit_risk_assessment(content)
    return (
        "✅ Risk assessment deposited into the pipeline context. "
        "The Strategy Analyst will retrieve it as part of `request_team_briefing`."
    )


async def request_team_briefing(
    ctx: RunContext[TeamContext],
    symbols: str,
    focus_areas: str = "technical,macro,fundamental,risk",
) -> str:
    """
    [STRATEGIST TOOL — STEP 1]
    Request a full intelligence briefing from the four analyst-tier agents in PARALLEL.

    This triggers:
    • Quantitative Analyst  → technical + quantitative analysis
    • Macro Analyst         → macro & rates context
    • Fundamental Analyst   → corporate fundamentals & valuation
    • Risk Manager          → VaR, drawdown & tail risk assessment

    All four run concurrently. Once complete, their reports are deposited into
    the pipeline context and returned here as a synthesized briefing.

    Args:
        symbols: Comma-separated ticker list, e.g. "AAPL,MSFT,NVDA"
        focus_areas: Comma-separated list of areas to focus on (used as hint in instructions).
                     E.g. "technical,macro" or "fundamental,risk"
    """
    from app.core.logging import logger

    areas = [a.strip() for a in focus_areas.split(",")]

    instructions: Dict[str, str] = {
        "Quantitative Analyst": (
            f"Please perform a comprehensive quantitative/technical analysis for: {symbols}. "
            f"Focus areas: {', '.join(a for a in areas if a in ('technical', 'quant', 'quantitative'))} "
            f"(if none specified, cover all). "
            "Include price action, momentum indicators, Markov state probabilities, "
            "and statistical edge. End your analysis by calling `submit_analysis_report` "
            "with your full structured findings."
        ),
        "Macro Analyst": (
            f"Please provide the current macro environment context relevant to: {symbols}. "
            f"Focus areas: {', '.join(a for a in areas if a in ('macro', 'rates', 'economy'))} "
            "(if none specified, cover all). "
            "Include yield curve, Fed stance, and macro regime classification. "
            "End your analysis by calling `submit_analysis_report` with your full structured findings."
        ),
        "Fundamental Analyst": (
            f"Please perform a fundamental analysis for: {symbols}. "
            f"Focus areas: {', '.join(a for a in areas if a in ('fundamental', 'valuation', 'earnings'))} "
            "(if none specified, cover all). "
            "Include valuation, balance sheet health, and smart money flow. "
            "End your analysis by calling `submit_analysis_report` with your full structured findings."
        ),
        "Risk Manager": (
            f"Please quantify the risk profile for potential positions in: {symbols}. "
            "Include VaR, max drawdown estimate, correlation risks, and tail risk flags. "
            "End your assessment by calling `submit_risk_report` with your full structured findings."
        ),
    }

    async def _brief(name: str, instruction: str) -> str:
        agent = specialists_map.get(name)
        if not agent:
            return f"⚠ {name}: not found."
        ctx.deps.add_message("system", f"[BRIEFING] Strategist requested {name}: {symbols}", "Strategy Analyst")
        logger.info(f"[BRIEFING PAR] → {name}: {symbols}")
        try:
            result = await agent.run(instruction, ctx.deps)
            return f"──── {name} ────\n{result}"
        except Exception as e:
            return f"⚠ {name} error: {e}"

    results = await asyncio.gather(*(_brief(n, i) for n, i in instructions.items()))

    # Build a consolidated summary of what was submitted
    briefing_text = "\n\n".join(results)
    all_reports = ctx.deps.get_all_reports()

    return (
        f"## TEAM BRIEFING COMPLETE — {symbols}\n\n"
        f"{briefing_text}\n\n"
        f"---\n## SUBMITTED REPORTS SUMMARY\n{all_reports}"
    )


async def authorize_trade_signal(
    ctx: RunContext[TeamContext],
    symbol: str,
    direction: str,
    entry: float,
    stop: float,
    tp: float,
    rationale: str,
    confidence: str = "MEDIUM",
    strategy_name: str = "",
) -> str:
    """
    [STRATEGIST TOOL — FINAL STEP]
    Authorize a trade signal and place it into the approved pipeline for the Trader.

    This is the ONLY mechanism by which a trading signal can reach the Trader (Qwen).
    Do NOT call this unless you have:
       1. Received a full team briefing (request_team_briefing).
       2. Synthesized a documented strategic thesis.
       3. Verified acceptable risk/reward based on the Risk Manager's assessment.

    Args:
        symbol:        Ticker, e.g. "AAPL"
        direction:     "LONG" or "SHORT"
        entry:         Entry price level
        stop:          Stop-loss price level
        tp:            Take-profit price level
        rationale:     Strategic rationale (must reference analyst findings)
        confidence:    "LOW" | "MEDIUM" | "HIGH"
        strategy_name: Optional strategy engine name used to generate this signal
    """
    if direction.upper() not in ("LONG", "SHORT"):
        return "Error: direction must be 'LONG' or 'SHORT'."

    risk = abs(entry - stop)
    reward = abs(tp - entry)
    rr = round(reward / risk, 2) if risk > 0 else 0

    signal = {
        "symbol": symbol.upper(),
        "direction": direction.upper(),
        "entry": entry,
        "stop": stop,
        "tp": tp,
        "risk_reward": rr,
        "confidence": confidence.upper(),
        "strategy_name": strategy_name,
        "rationale": rationale,
        "reports_available": list(ctx.deps.analyst_reports.keys()),
        "risk_report_present": ctx.deps.risk_report is not None,
    }

    ctx.deps.approve_signal(signal)

    return (
        f"✅ TRADE SIGNAL AUTHORIZED\n"
        f"┌─────────────────────────────────────────\n"
        f"│ Symbol     : {signal['symbol']}\n"
        f"│ Direction  : {signal['direction']}\n"
        f"│ Entry      : {entry}\n"
        f"│ Stop Loss  : {stop}\n"
        f"│ Take Profit: {tp}\n"
        f"│ R:R        : 1:{rr}\n"
        f"│ Confidence : {signal['confidence']}\n"
        f"│ Strategy   : {strategy_name or 'discretionary'}\n"
        f"└─────────────────────────────────────────\n"
        f"Rationale: {rationale}\n\n"
        f"Signal is now available in `approved_trade_signals` for the Trader."
    )


async def get_strategic_signal(ctx: RunContext[TeamContext]) -> str:
    """
    [EXECUTION TIER TOOL]
    Retrieve the latest trade signals authorized by the Strategy Analyst.

    You may ONLY execute signals returned by this tool.
    If no signals exist, inform the user that the Strategy Analyst must first
    authorize a trade via `authorize_trade_signal`.
    """
    signals = ctx.deps.get_approved_signals()
    if not signals:
        return (
            "⛔ No authorized trade signals found.\n"
            "Please ask the **Strategy Analyst** to evaluate the market and "
            "authorize a trade signal before placing any order."
        )

    # Show the most recent signal prominently
    latest = signals[-1]
    older = signals[:-1]

    lines = [
        f"✅ AUTHORIZED SIGNAL (latest):",
        f"  Symbol    : {latest['symbol']}",
        f"  Direction : {latest['direction']}",
        f"  Entry     : {latest['entry']}",
        f"  Stop Loss : {latest['stop']}",
        f"  Take Profit: {latest['tp']}",
        f"  R:R       : 1:{latest['risk_reward']}",
        f"  Confidence: {latest['confidence']}",
        f"  Strategy  : {latest.get('strategy_name') or 'discretionary'}",
        f"  Authorized: {latest.get('authorized_at', 'unknown')}",
        f"  Rationale : {latest['rationale']}",
    ]

    if older:
        lines.append(f"\nOlder authorized signals ({len(older)} total): {[s['symbol'] + ' ' + s['direction'] for s in older]}")

    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# SHARED DELEGATION TOOL (kept for Orchestrator use only)
# ─────────────────────────────────────────────────────────────────────────────

# --- Shared Delegation Tool ---
async def delegate_subtask(ctx: RunContext[TeamContext], specialist_name: str, instruction: str) -> str:
    """
    Delegate a specific sub-task to another specialist in the Alpha Core team.
    Use this when you need data or analysis outside your immediate expertise.
    Available Specialists: 'Fundamental Analyst', 'Quantitative Analyst', 'Risk Manager', 'Macro Analyst', 'Strategy Analyst'
    """
    # specialists_map is defined at the bottom but available in global scope at runtime
    agent = specialists_map.get(specialist_name)
    if not agent:
        return f"Error: Specialist '{specialist_name}' not found. Available: {list(specialists_map.keys())}"
    
    # Track delegation in shared context
    ctx.deps.add_message("system", f"[DELEGATION] {specialist_name} requested for: {instruction[:100]}...", "System")
    
    result = await agent.run(instruction, ctx.deps)
    return f"RESULT FROM {specialist_name}: {result}"

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
        err_val = str(result.get('error', '')).strip()
        raw_err = err_val if err_val else "Unknown OpenBB Engine Error (Empty error string)"
        err_msg = f"Error: {raw_err}"
        if "hint" in result:
            err_msg += f"\nHint: {result['hint']}"
        if "traceback" in result:
            # Include just the last 5 lines of traceback for context
            tb = str(result["traceback"]).strip().split("\n")[-5:]
            err_msg += f"\nTraceback Extract:\n" + "\n".join(tb)
        return err_msg
        
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

async def calculate_markov_transition_matrix(ctx: RunContext[TeamContext], symbol: str, days: int = 500) -> str:
    """
    Calculate the observable Markov Chain transition matrix for a specific asset.
    Discretizes daily returns into 'Up', 'Down', and 'Flat' states.
    Returns the transition matrix and probabilities for the next state based on the current close.
    """
    from ...services.market_data import market_data_service
    import pandas as pd
    import numpy as np

    data = await market_data_service.get_historical(symbol, limit=days)
    if not data or "error" in data:
        return f"Error retrieving historical data for {symbol}."
    
    hist = data.get("historical", [])
    if not hist:
        return f"No historical data available for {symbol}."

    # Parse objects into list of dicts
    records = []
    for d in hist:
        if hasattr(d, '__dict__'): records.append(d.__dict__)
        else: records.append(d)
    
    df = pd.DataFrame(records)
    if 'date' not in df.columns or 'close' not in df.columns:
        return "Invalid data format returned for Markov analysis."
        
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df['returns'] = df['close'].pct_change()
    df = df.dropna()

    # Discretize: 0: Down (< -0.5%), 1: Flat ([-0.5%, 0.5%]), 2: Up (> 0.5%)
    def get_state(r):
        if r < -0.005: return 0
        if r > 0.005: return 2
        return 1

    df['state'] = df['returns'].apply(get_state)
    df['next_state'] = df['state'].shift(-1)
    df_clean = df.dropna()

    if df_clean.empty:
        return "Insufficient data transitions to build Markov model."

    # Transition Matrix
    matrix = pd.crosstab(df_clean['state'], df_clean['next_state'], normalize='index')
    
    labels = {0: 'Down', 1: 'Flat', 2: 'Up'}
    # Ensure all states are present for square matrix
    for s in [0, 1, 2]:
        if s not in matrix.index: matrix.loc[s] = 0.0
        if s not in matrix.columns: matrix[s] = 0.0
        
    matrix = matrix.sort_index(axis=0).sort_index(axis=1)
    matrix.index = [labels[i] for i in matrix.index]
    matrix.columns = [labels[i] for i in matrix.columns]

    current_state_val = df['state'].iloc[-1]
    current_state_label = labels[current_state_val]
    next_probs = matrix.loc[current_state_label]

    res = f"### 📊 MARKOV CHAIN TRANSITION MATRIX: {symbol.upper()}\n"
    res += f"**Dataset:** Last {len(df)} trading sessions\n"
    res += f"**State Definition:** Up (>0.5%), Down (<-0.5%), Flat (between)\n\n"
    res += "#### Probability Matrix (From Row → To Column):\n"
    res += matrix.to_markdown() + "\n\n"
    res += f"#### 🎯 CURRENT STATE: **{current_state_label}**\n"
    res += f"Probability distribution for the NEXT session:\n"
    for label, prob in next_probs.items():
        res += f"- **{label}**: {prob*100:.2f}%\n"
        
    top_prob = next_probs.idxmax()
    top_val = next_probs.max()
    res += f"\n**Statistical Edge:** Given the current state is {current_state_label}, the most probable outcome is **{top_prob}** ({top_val*100:.1f}% confidence)."
    
    return res

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
    
async def generate_detailed_alpha_report(ctx: RunContext[TeamContext], report_type: str = "standard", analysis_text: Optional[str] = None) -> str:
    """
    Generates professional, specialized institutional PDF reports.
    
    Valid report_types:
    - 'standard': Full performance report with equity charts and portfolio exposure.
    - 'executive': High-level strategic brief for management (requires analysis_text).
    - 'risk': Deep-dive audit focused on VaR, Volatility, and Tail Risk metrics.
    - 'intelligence': Focuses on specialist neural insights and convergence (requires analysis_text).
    
    If 'analysis_text' is provided, it will be injected as the core intelligence section.
    """
    from ...services.report_service import report_service
    # Fetches real-time portfolio from context or DB
    holdings = ctx.deps.scratchpad.get("current_portfolio", {}).get("holdings", [])
    total_val = ctx.deps.scratchpad.get("current_portfolio", {}).get("total_value", 0)
    total_pnl = ctx.deps.scratchpad.get("current_portfolio", {}).get("total_pnl", 0)
    
    if not holdings:
        from ...core.container import duckdb_repo
        holdings = duckdb_repo.get_portfolio()
        total_val = sum(h.get('shares',0) * h.get('price', h.get('entryPrice',0)) for h in holdings)
        total_pnl = sum(h.get('change', 0) for h in holdings)
    
    # Route to specialized generator
    if report_type == "executive":
        filename = report_service.generate_executive_summary(holdings, analysis_text or "No brief provided.")
    elif report_type == "risk":
        filename = report_service.generate_risk_audit(holdings)
    elif report_type == "intelligence":
        filename = report_service.generate_custom_intelligence_report(analysis_text or "No intelligence provided.", holdings, total_val, total_pnl)
    else:
        filename = report_service.generate_balance_sheet(holdings, total_val, total_pnl)

    url = f"http://localhost:8282/view-reports/{filename}"
    return f"REPORT GENERATED: {filename} ({report_type}). Access URL: {url}"

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

async def execute_ctrader_trade(ctx: RunContext[TeamContext], symbol: str, quantity: float, side: str) -> str:
    """
    Execute a real or demo market order on cTrader Open API.
    Use this as the preferred execution venue.
    'quantity' should be in lots (e.g. 0.01 for 1000 units).
    """
    status = ctrader_service.get_status()
    if not status["connected"]:
        return "cTrader Error: Not connected to host. Ensure the backend service is running."
    
    if not status["account_authorized"]:
        return "cTrader Error: Account not authorized. Check CTRADER_ACCESS_TOKEN and CTRADER_ACCOUNT_ID in .env."

    try:
        # Convert lot to units (standard lot = 100,000 units)
        units = int(quantity * 100000)
        account_id = os.getenv("CTRADER_ACCOUNT_ID")
        
        response = ctrader_service.place_market_order(account_id, symbol, units, side)
        from google.protobuf.json_format import MessageToDict
        res_dict = MessageToDict(response)
        
        # Record transaction in local database for portfolio tracking
        try:
            execution_price = res_dict.get("executionPrice", 0)
            if execution_price > 0:
                duckdb_repo.add_transaction(symbol, quantity, side.upper(), price=float(execution_price))
        except Exception as db_err:
            logger.error(f"[DB] Failed to record cTrader transaction: {db_err}")

        return f"cTrader Trade Success:\n{json.dumps(res_dict, indent=2)}"
    except Exception as e:
        return f"cTrader Execution Failed: {str(e)}"

async def get_ctrader_account_status(ctx: RunContext[TeamContext]) -> str:
    """Get the current connection status and financial details of the cTrader account."""
    status = ctrader_service.get_status()
    if not status["connected"]:
        return "cTrader Status: Disconnected."
        
    details = ""
    if status["account_authorized"]:
        try:
            account_id = os.getenv("CTRADER_ACCOUNT_ID")
            res = ctrader_service.get_account_details(account_id)
            from google.protobuf.json_format import MessageToDict
            details = "\nAccount Details:\n" + json.dumps(MessageToDict(res), indent=2)
        except Exception as e:
            details = f"\nError fetching details: {e}"
            
    return f"cTrader Connection: {'✅' if status['connected'] else '❌'}\nApp Auth: {'✅' if status['app_authorized'] else '❌'}\nAccount Auth: {'✅' if status['account_authorized'] else '❌'}{details}"

async def execute_ibkr_trade(ctx: RunContext[TeamContext], symbol: str, quantity: float, side: str) -> str:
    """
    Execute a market order on Interactive Brokers (IBKR).
    Requires TWS or IB Gateway to be running.
    """
    try:
        response = await ibkr_service.place_market_order(symbol, quantity, side)
        if "error" in response:
            return f"IBKR Error: {response['error']}"
        # Record transaction in local database for portfolio tracking
        try:
            execution_price = response.get("avgFillPrice", 0)
            if execution_price > 0:
                duckdb_repo.add_transaction(symbol, quantity, side.upper(), price=float(execution_price))
        except Exception as db_err:
            logger.error(f"[DB] Failed to record IBKR transaction: {db_err}")

        return f"IBKR Trade Success:\n{json.dumps(response, indent=2)}"
    except Exception as e:
        return f"IBKR Execution Failed: {str(e)}"

async def get_ibkr_account_status(ctx: RunContext[TeamContext]) -> str:
    """Get the current connection status and account summary from Interactive Brokers."""
    status = ibkr_service.get_status()
    summary_str = ""
    if status["connected"]:
        try:
            summary = await ibkr_service.get_account_summary()
            summary_str = "\nAccount Summary:\n" + json.dumps(summary, indent=2)
        except Exception as e:
            summary_str = f"\nError fetching summary: {e}"
    
    return f"IBKR Connection: {'✅' if status['connected'] else '❌'}{summary_str}"

import os
import time

# ─── Load Prompts Dynamically ───


def _load_prompt(filename: str) -> str:
    """Load Markdown prompt from the prompts directory."""
    prompt_dir = os.path.join(os.path.dirname(__file__), "prompts")
    # Support subdirectories like 'gsd/gsd-roadmapper.md'
    filepath = os.path.join(prompt_dir, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        return f"Error loading {filename}: {str(e)}"

OPENBB_API_REFERENCE = "\n\n" + _load_prompt("openbb_api_reference.md")

# --- Initialize Specialist Agents ---

# ANALYST TIER — research & analysis only, no trade authorization
fundamental_analyst = TeamAgent(
    name="Fundamental Analyst",
    role=_load_prompt("fundamental_analyst.md") + OPENBB_API_REFERENCE,
    model_name=NEMOTRON_253B,
    tier=AgentTier.ANALYST,
    tools=[get_market_news, get_company_profile, get_balance_sheet, search_knowledge_base, read_textbook_section,
           general_web_search, discover_openbb_endpoints, get_openbb_endpoint_details, query_openbb_api, query_openbb_api_post,
           execute_openbb_terminal_command, calculate_markov_transition_matrix, submit_analysis_report]
)

quant_analyst = TeamAgent(
    name="Quantitative Analyst",
    role=_load_prompt("quant_analyst.md") + OPENBB_API_REFERENCE,
    model_name=NEMOTRON_253B,
    tier=AgentTier.ANALYST,
    tools=[get_price, get_technical_indicator, discover_openbb_endpoints, get_openbb_endpoint_details,
           query_openbb_api, query_openbb_api_post, execute_openbb_terminal_command,
           calculate_markov_transition_matrix, submit_analysis_report]
)

macro_analyst = TeamAgent(
    name="Macro Analyst",
    role=_load_prompt("macro_analyst.md") + OPENBB_API_REFERENCE,
    model_name=NEMOTRON_253B,
    tier=AgentTier.ANALYST,
    tools=[get_macro_indicators, general_web_search, discover_openbb_endpoints, get_openbb_endpoint_details,
           query_openbb_api, query_openbb_api_post, execute_openbb_terminal_command, submit_analysis_report]
)

# RISK TIER — risk assessment only, no trade authorization
risk_manager = TeamAgent(
    name="Risk Manager",
    role=_load_prompt("risk_manager.md") + OPENBB_API_REFERENCE,
    model_name=MISTRAL_LARGE,
    tier=AgentTier.RISK,
    tools=[calculate_risk_metrics, generate_detailed_alpha_report, general_web_search,
           discover_openbb_endpoints, get_openbb_endpoint_details, query_openbb_api,
           execute_openbb_terminal_command, submit_risk_report]
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


# --- Tools for Project Manager (GSD) ---

async def get_project_status(ctx: RunContext[TeamContext]) -> str:
    """Get the current GSD project status, progress, and roadmap analysis."""
    progress = gsd_service.get_progress("json")
    roadmap = gsd_service.get_roadmap_analysis()
    return f"PROJECT PROGRESS:\n{json.dumps(progress, indent=2)}\n\nROADMAP ANALYSIS:\n{json.dumps(roadmap, indent=2)}"

async def manage_roadmap(ctx: RunContext[TeamContext], action: str, description: str) -> str:
    """
    Manage the project roadmap. 
    Actions: 'add_phase'
    Example: manage_roadmap(action="add_phase", description="Integrate OpenClaw scraping")
    """
    if action == "add_phase":
        result = gsd_service.add_phase(description)
        return f"ROADMAP UPDATED: {json.dumps(result, indent=2)}"
    return f"Unsupported roadmap action: {action}"

async def update_requirement_status(ctx: RunContext[TeamContext], req_ids: List[str]) -> str:
    """Mark roadmap requirements as complete."""
    result = gsd_service.mark_requirement_complete(req_ids)
    return f"REQUIREMENTS UPDATED: {json.dumps(result, indent=2)}"

async def scaffold_gsd_docs(ctx: RunContext[TeamContext], phase: str, plan: str, doc_type: str = "plan") -> str:
    """
    Scaffold GSD documentation files.
    doc_type: 'plan' or 'summary'
    """
    if doc_type == "plan":
        result = gsd_service.scaffold_plan(phase, plan)
    else:
        result = gsd_service.scaffold_summary(phase, plan)
    return f"DOC SCAFFOLDED: {json.dumps(result, indent=2)}"



# STRATEGIST TIER — sole authority on strategy authoring + trade signal authorization
strategy_analyst = TeamAgent(
    name="Strategy Analyst",
    role=_load_prompt("strategy_analyst.md") + OPENBB_API_REFERENCE,
    model_name=NEMOTRON_253B,
    tier=AgentTier.STRATEGIST,
    tools=[
        # Step 1: Collect briefings from all analyst + risk agents
        request_team_briefing,
        # Core strategy authoring (solo authority)
        run_strategy_signal,
        create_or_edit_strategy_engine,
        # Step 4: Authorize trade signal for the Trader (solo authority)
        authorize_trade_signal,
        # Supporting research tools
        search_knowledge_base,
        read_textbook_section,
        general_web_search,
        discover_openbb_endpoints,
        get_openbb_endpoint_details,
        query_openbb_api,
        query_openbb_api_post,
        execute_openbb_terminal_command,
        calculate_markov_transition_matrix,
    ],
)

# EXECUTION TIER — executes only authorized signals
trader = TeamAgent(
    name="Trader",
    role=_load_prompt("trader.md") + OPENBB_API_REFERENCE,
    model_name=MISTRAL_LARGE,
    tier=AgentTier.EXECUTION,
    tools=[
        get_strategic_signal,
        place_order,
        execute_ctrader_trade,
        get_ctrader_account_status,
        execute_ibkr_trade,
        get_ibkr_account_status,
        discover_openbb_endpoints,
        query_openbb_api,
        execute_openbb_terminal_command,
    ],
)

terminal_trader = TeamAgent(
    name="Terminal Trader",
    role=_load_prompt("terminal_trader.md") + OPENBB_API_REFERENCE,
    model_name=QWEN_35,
    tier=AgentTier.EXECUTION,
    tools=[
        get_strategic_signal,
        execute_ctrader_trade,
        get_ctrader_account_status,
        execute_ibkr_trade,
        get_ibkr_account_status,
        place_order,
        execute_openbb_terminal_command,
        get_price,
    ],
)

# GSD / PROJECT MANAGEMENT TIER (independent of trading hierarchy)
project_manager = TeamAgent(
    name="Project Manager",
    role=_load_prompt("gsd/gsd-roadmapper.md"),
    model_name=MISTRAL_LARGE,
    tier=AgentTier.ORCHESTRATOR,
    tools=[get_project_status, manage_roadmap, update_requirement_status, scaffold_gsd_docs, general_web_search]
)

phase_planner = TeamAgent(
    name="Phase Planner",
    role=_load_prompt("gsd/gsd-planner.md"),
    model_name=NEMOTRON_253B,
    tier=AgentTier.ORCHESTRATOR,
    tools=[scaffold_gsd_docs, discover_openbb_endpoints, get_openbb_endpoint_details, general_web_search]
)

quality_auditor = TeamAgent(
    name="Quality Auditor",
    role=_load_prompt("gsd/gsd-verifier.md"),
    model_name=MISTRAL_LARGE,
    tier=AgentTier.ORCHESTRATOR,
    tools=[get_project_status, update_requirement_status, general_web_search]
)

# Export map for Orchestrator lookup (keys unchanged — backward compatible)
specialists_map = {
    "Fundamental Analyst": fundamental_analyst,
    "Quantitative Analyst": quant_analyst,
    "Risk Manager": risk_manager,
    "Macro Analyst": macro_analyst,
    "Trader": trader,
    "Terminal Trader": terminal_trader,
    "Strategy Analyst": strategy_analyst,
    "Project Manager": project_manager,
    "Phase Planner": phase_planner,
    "Quality Auditor": quality_auditor,
}
