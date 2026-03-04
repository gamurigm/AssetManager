from .state import TeamContext
from .specialists import specialists_map
from .base import TeamAgent
from pydantic_ai import RunContext
from typing import Optional, List, Dict
import json
import asyncio
import uuid

from ...services.risk_service import risk_service

# --- Orchestrator Definition ---
ORCHESTRATOR_MODEL = "nvidia/llama-3.1-nemotron-ultra-253b-v1"


# ── Tools available to the Orchestrator LLM ─────────────────────────

async def delegate_task(ctx: RunContext[TeamContext], specialist_name: str, instruction: str) -> str:
    """Delegate a single subtask to one specialist (sequential)."""
    agent = specialists_map.get(specialist_name)
    if not agent:
        return f"Error: Specialist '{specialist_name}' not found. Available: {list(specialists_map.keys())}"

    from app.core.logging import logger
    logger.info(f"[SEQ] -> {specialist_name}: {instruction[:80]}...")
    ctx.deps.add_message("system", f"Delegating to {specialist_name}: {instruction}", "Head of Strategy")

    result = await agent.run(instruction, ctx.deps)
    return f"Response from {specialist_name}: {result}"


async def delegate_parallel_tasks(ctx: RunContext[TeamContext], tasks: List[Dict[str, str]]) -> str:
    """
    Delegate multiple subtasks in PARALLEL.
    Each element: {"specialist": "Risk Manager", "instruction": "…"}
    All run concurrently via asyncio.gather.
    """
    from app.core.logging import logger

    async def _run(task: dict) -> str:
        name = task.get("specialist", "")
        instr = task.get("instruction", "")
        agent = specialists_map.get(name)
        if not agent:
            return f"⚠ {name}: not found."

        logger.info(f"[PAR] -> {name}: {instr[:60]}...")
        ctx.deps.add_message("system", f"Parallel -> {name}: {instr}", "Head of Strategy")

        try:
            res = await agent.run(instr, ctx.deps)
            return f"──── {name} ────\n{res}"
        except Exception as e:
            return f"⚠ {name} error: {e}"

    results = await asyncio.gather(*(_run(t) for t in tasks))
    return "\n\n".join(results)


# ── Orchestrator class ──────────────────────────────────────────────

from .specialists import query_openbb_api, execute_openbb_terminal_command

class HeadOfStrategy(TeamAgent):
    """
    Multi-conversation orchestrator.
    Each conversation is identified by a `session_id` and gets its own
    TeamContext so parallel chats don't leak into each other.
    """

    def __init__(self):
        super().__init__(
            "Head of Strategy",
            "Orchestrator lead responsible for planning and delegating tasks. "
            "IMPORTANT: When the user asks for a comprehensive analysis, a full report, "
            "or multi-ticker research, ALWAYS use 'delegate_parallel_tasks' to trigger "
            "specialists (Fundamental Analyst, Quantitative Analyst, Risk Manager, "
            "Macro Analyst, Strategy Analyst) simultaneously to maximise efficiency. "
            "You also have direct access to the OpenBB Terminal to fetch rapid quantitative or macro data natively and open charts. "
            "\n\n## TERMINAL BRIDGE (CRITICAL)\n"
            "You can send commands directly to the user's embedded OpenBB CLI terminal. "
            "To do this, wrap the command in a fenced code block with language 'openbb'. Example:\n"
            "```openbb\n"
            "equity price historical --symbol AAPL --chart true\n"
            "```\n"
            "When you include this in your response, the command will AUTOMATICALLY execute in the user's terminal and "
            "the chart/data will appear there. Use this whenever:\n"
            "- The user asks to see data, charts, or run terminal commands\n"
            "- The user says 'usa la terminal', 'muéstrame en la terminal', 'run in terminal', 'use the terminal', etc.\n"
            "- The user asks for price quotes, historical data, fundamentals, or any data visualization\n"
            "- You want to show live market data\n\n"
            "PREFER using ```openbb blocks over internal API tools when the user explicitly mentions the terminal. "
            "You can include multiple ```openbb blocks and they will execute in sequence (1.5s apart). "
            "\n### COMMAND REFERENCE (use these inside ```openbb blocks):\n\n"
            "★ EQUITY / PRICE:\n"
            "- `equity price historical --symbol AAPL --chart true` (stock price chart)\n"
            "- `equity price quote --symbol NVDA` (real-time quote)\n"
            "- `equity price performance --symbol AAPL,MSFT,NVDA --chart true` (comparative perf)\n\n"
            "★ TECHNICAL ANALYSIS:\n"
            "- `technical rsi --symbol MSFT --chart true` (RSI indicator)\n"
            "- `technical macd --symbol AAPL --chart true` (MACD)\n"
            "- `technical sma --symbol TSLA --chart true` (Simple Moving Average)\n"
            "- `technical ema --symbol NVDA --chart true` (Exponential Moving Average)\n"
            "- `technical bbands --symbol AAPL --chart true` (Bollinger Bands)\n"
            "- `technical adx --symbol MSFT --chart true` (Average Directional Index)\n"
            "- `technical aroon --symbol AAPL --chart true` (Aroon Indicator)\n"
            "- `technical stoch --symbol TSLA --chart true` (Stochastic Oscillator)\n"
            "- `technical cg --symbol AAPL --chart true` (Center of Gravity)\n"
            "- `technical relative_rotation --symbol AAPL,MSFT,GOOGL,AMZN,NVDA --benchmark ^GSPC --chart true` (RRG chart — relative strength vs benchmark)\n\n"
            "★ ECONOMETRICS:\n"
            "- `econometrics correlation_matrix --symbol AAPL,MSFT,NVDA,GOOGL,AMZN --chart true` (correlation heatmap)\n"
            "- `econometrics cointegration --symbol AAPL,MSFT` (Engle-Granger cointegration test)\n"
            "- `econometrics granger --symbol AAPL,MSFT` (Granger causality test)\n"
            "- `econometrics residuals --symbol AAPL --chart true` (residual analysis)\n"
            "- `econometrics unitroot --symbol AAPL` (ADF unit root / stationarity test)\n"
            "- `econometrics ols --symbol AAPL --dependent close --independent volume` (OLS regression)\n\n"
            "★ CRYPTO:\n"
            "- `crypto price historical --symbol BTC-USD --chart true` (Bitcoin chart)\n"
            "- `crypto price quote --symbol ETH-USD` (Ethereum quote)\n\n"
            "★ ECONOMY / MACRO:\n"
            "- `economy fred_series --symbol GDP --chart true` (US GDP)\n"
            "- `economy fred_series --symbol CPIAUCSL --chart true` (CPI inflation)\n"
            "- `economy fred_series --symbol UNRATE --chart true` (unemployment rate)\n"
            "- `economy fred_series --symbol DFF --chart true` (Fed Funds Rate)\n"
            "- `economy calendar` (economic calendar)\n\n"
            "★ FIXED INCOME:\n"
            "- `fixedincome government yield_curve --chart true` (US Treasury yield curve)\n"
            "- `fixedincome spreads --chart true` (credit spreads)\n\n"
            "★ FUNDAMENTAL:\n"
            "- `equity fundamental income --symbol AAPL` (income statement)\n"
            "- `equity fundamental balance --symbol MSFT` (balance sheet)\n"
            "- `equity fundamental ratios --symbol NVDA` (financial ratios)\n"
            "- `equity fundamental dividends --symbol AAPL --chart true` (dividend history)\n\n"
            "★ FOREX:\n"
            "- `forex price historical --symbol EURUSD --chart true` (EUR/USD chart)\n"
            "- `forex price quote --symbol USDJPY` (USD/JPY quote)\n\n"
            "Always explain what each command does alongside the block. "
            "When the user asks for technical or econometric analysis, PREFER sending multiple relevant ```openbb blocks.",
            ORCHESTRATOR_MODEL,
            tools=[delegate_task, delegate_parallel_tasks, query_openbb_api, execute_openbb_terminal_command],
        )
        # session_id → TeamContext (multi-conversation support)
        self._sessions: Dict[str, TeamContext] = {}

    def _get_context(self, session_id: str) -> TeamContext:
        if session_id not in self._sessions:
            self._sessions[session_id] = TeamContext()
        return self._sessions[session_id]

    def reset_session(self, session_id: str):
        self._sessions.pop(session_id, None)

    # ── Non-streaming run ───────────────────────────────────────────
    async def run(self, user_query: str, session_id: str = "default") -> str:
        ctx = self._get_context(session_id)
        ctx.add_message("user", user_query, "User")
        try:
            result = await super().run(user_query, ctx)
            return result
        except Exception as e:
            err = f"Orchestrator Error: {e}"
            ctx.add_message("system", err, "Head of Strategy")
            return err

    # ── Streaming run ───────────────────────────────────────────────
    async def run_stream(
        self,
        user_query: str,
        portfolio: Optional[dict] = None,
        market_regime: Optional[dict] = None,
        session_id: str = "default",
    ):
        ctx = self._get_context(session_id)
        system_context_parts: list[str] = []

        # ── inject live portfolio into shared context ───────────────
        if portfolio:
            ctx.update_scratchpad("current_portfolio", portfolio)

            holdings  = portfolio.get("holdings", [])
            total_val = portfolio.get("total_value", 0)
            pnl       = portfolio.get("total_pnl", 0)
            pct       = portfolio.get("pnl_percent", 0)

            rows = []
            for h in holdings:
                sym = h.get("symbol", "N/A")
                shares = h.get("shares", 0)
                price  = h.get("price", 0)
                val    = shares * price
                chg    = h.get("changePercent", 0)
                rows.append(f"| {sym} | {shares} | ${price:,.2f} | ${val:,.2f} | {chg:+.2f}% |")

            table_str = "\n".join(rows)

            # risk metrics
            risk_report = risk_service.get_portfolio_risk_report(holdings)
            if "error" not in risk_report:
                risk_str = f"""
## 🛡️ INSTITUTIONAL RISK ANALYSIS (MMAM ALPHA CORE)
- **Modified VaR (95%):** {risk_report.get('mvar_95_percent')}%
- **Sharpe Ratio:** {risk_report.get('sharpe_ratio')}
- **Expected Value E[x]:** ${risk_report.get('expected_value_trade', 0):,.2f}
- **Risk Adjusted Return:** {risk_report.get('risk_adjusted_return', 'N/A')}
- **Annualized Volatility:** {risk_report.get('annualized_volatility')}%
- **Skewness:** {risk_report.get('skewness', 0)}
- **Kurtosis:** {risk_report.get('excess_kurtosis', 0)}

### 📉 MOMENTUM (Gradient Descent Linear Regression)
{json.dumps(risk_report.get('momentum', {}), indent=2)}

### 🛡️ HEDGING STRATEGY
- **Action:** {risk_report.get('hedging_strategy', {}).get('action')}
- **Strategy:** {risk_report.get('hedging_strategy', {}).get('recommended_strategy')}
- **Target:** {risk_report.get('hedging_strategy', {}).get('primary_hedge_target')}
- **Ratio:** {risk_report.get('hedging_strategy', {}).get('hedge_ratio')}
"""
            else:
                risk_str = f"\n[Risk Analysis Unavailable: {risk_report.get('error')}]\n"

            system_context_parts.append(f"""
## 📊 REAL-TIME PORTFOLIO SNAPSHOT
**Total AUM:** ${total_val:,.2f}
**Total PnL:** ${pnl:,.2f} ({pct:+.2f}%)

| Asset | Shares | Price | Value | Change |
| :--- | :--- | :--- | :--- | :--- |
{table_str}

{risk_str}
""")

        # ── inject market regime ────────────────────────────────────
        if market_regime:
            ctx.update_scratchpad("market_regime", market_regime)
            r = market_regime
            symbol   = r.get("symbol", "Unknown")
            analysis = r.get("regime_analysis", {})
            curr     = analysis.get("current_regime", "Unknown")
            system_context_parts.append(f"""
## 🧠 MARKET REGIME ANALYSIS ({symbol})
**Current State:** {curr}
**Details:** {json.dumps(analysis, indent=2)}
""")

        if system_context_parts:
            full = "\n".join(system_context_parts)
            ctx.update_scratchpad("formatted_realtime_context", full)
            ctx.add_message("system", full, "System Monitor")

        ctx.add_message("user", user_query, "User")

        try:
            async for chunk in super().run_stream(user_query, ctx):
                yield chunk
        except Exception as e:
            yield f"Orchestrator Stream Error: {e}"


# Singleton
orchestrator = HeadOfStrategy()
