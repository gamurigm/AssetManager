from .state import TeamContext
from .specialists import specialists_map
from .base import TeamAgent
from pydantic_ai import RunContext
from typing import Optional
import json

# --- Orchestrator Definition ---
# Uses Nemotron or similar high-reasoning model for planning

ORCHESTRATOR_MODEL = "nvidia/llama-3.1-nemotron-ultra-253b-v1"

import asyncio
from typing import List, Dict, Optional
from ...services.risk_service import risk_service

# ... existing imports ...

async def delegate_task(ctx: RunContext[TeamContext], specialist_name: str, instruction: str) -> str:
    """Delegate a single subtask (Sequential)."""
    # ... existing implementation ...
    agent = specialists_map.get(specialist_name)
    if not agent:
        return f"Error: Specialist '{specialist_name}' not found."
    
    # Log delegation in context
    from app.core.logging import logger
    logger.info(f"Delegating task to {specialist_name}: {instruction[:100]}...")
    ctx.deps.add_message("system", f"Delegating to {specialist_name}: {instruction}", "Head of Strategy")
    
    result = await agent.run(instruction, ctx.deps)
    return f"Response from {specialist_name}: {result}"


async def delegate_parallel_tasks(ctx: RunContext[TeamContext], tasks: List[Dict[str, str]]) -> str:
    """
    Delegate multiple subtasks to run in PARALLEL.
    Input format: [{"specialist": "Fundamental Analyst", "instruction": "Check news..."}, ...]
    """
    from app.core.logging import logger
    
    async def run_single(task):
        spec_name = task.get("specialist")
        instr = task.get("instruction")
        agent = specialists_map.get(spec_name)
        if not agent:
            return f"{spec_name}: Specialist not found."
        
        logger.info(f"PARALLEL Delegation to {spec_name}: {instr[:50]}...")
        ctx.deps.add_message("system", f"Parallel delegation to {spec_name}: {instr}", "Head of Strategy")
        
        try:
            res = await agent.run(instr, ctx.deps)
            return f"--- Response from {spec_name} ---\n{res}"
        except Exception as e:
            return f"Error from {spec_name}: {str(e)}"

    results = await asyncio.gather(*(run_single(t) for t in tasks))
    return "\n\n".join(results)

class HeadOfStrategy(TeamAgent):
    def __init__(self):
        super().__init__(
            "Head of Strategy",
            "Orchestrator lead responsible for planning and delegating tasks",
            ORCHESTRATOR_MODEL,
            tools=[delegate_task, delegate_parallel_tasks]
        )
        self.context = TeamContext()

    async def run(self, user_query: str) -> str:
        # Add user message to shared context
        self.context.add_message("user", user_query, "User")
        
        try:
            # Run the agent (TeamAgent.run handles internal context logging)
            result = await super().run(user_query, self.context)
            return result
        except Exception as e:
            error_msg = f"Orchestrator Error: {str(e)}"
            self.context.add_message("system", error_msg, "Head of Strategy")
            return error_msg

    async def run_stream(self, user_query: str, portfolio: Optional[dict] = None, market_regime: Optional[dict] = None):
        # Update shared context with real-time portfolio data if available
        system_context_parts = []

        if portfolio:
            self.context.update_scratchpad("current_portfolio", portfolio)
            
            # Format portfolio as a readable Markdown table for the LLM
            holdings = portfolio.get("holdings", [])
            total_val = portfolio.get("total_value", 0)
            pnl = portfolio.get("total_pnl", 0)
            pct = portfolio.get("pnl_percent", 0)
            
            table_rows = []
            for h in holdings:
                sym = h.get("symbol", "N/A")
                shares = h.get("shares", 0)
                price = h.get("price", 0)
                val = shares * price
                chg = h.get("changePercent", 0)
                table_rows.append(f"| {sym} | {shares} | ${price:,.2f} | ${val:,.2f} | {chg:+.2f}% |")

            table_str = "\n".join(table_rows)
            
            # 🛡️ RISK ANALYSIS INTEGRATION (Pfaff Logic)
            risk_report = risk_service.get_portfolio_risk_report(holdings)
            risk_str = ""
            if "error" not in risk_report:
                risk_str = f"""
## 🛡️ PORTFOLIO RISK (PFAFF METHODOLOGY)
- **Modified VaR (95%):** {risk_report.get('mvar_95_percent')}% (${risk_report.get('mvar_95_cash', 0):,.2f})
- **Modified ES (mES):** {risk_report.get('mes_95_percent')}%
- **Gaussian VaR (Ref):** {risk_report['var_95_percent']}%
- **Portfolio Skewness:** {risk_report.get('skewness', 0)}
- **Excess Kurtosis:** {risk_report.get('excess_kurtosis', 0)}
- **Annualized Sharpe:** {risk_report['sharpe_ratio']}
- **Annualized Vol:** {risk_report['annualized_volatility_percent']}%
- **Asset Risks:** {json.dumps(risk_report['asset_risks'])}
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

        if market_regime:
             self.context.update_scratchpad("market_regime", market_regime)
             r = market_regime
             symbol = r.get("symbol", "Unknown")
             analysis = r.get("regime_analysis", {})
             curr_regime = analysis.get("current_regime", "Unknown")
             
             system_context_parts.append(f"""
## 🧠 MARKET REGIME ANALYSIS ({symbol})
**Current State:** {curr_regime}
**Details:** {json.dumps(analysis, indent=2)}
""")

        if system_context_parts:
             full_context = "\n".join(system_context_parts)
             # Share with all agents via scratchpad
             self.context.update_scratchpad("formatted_realtime_context", full_context)
             # Still add as a direct message for the orchestrator's immediate turn
             self.context.add_message("system", full_context, "System Monitor")

        # Add user message to shared context
        self.context.add_message("user", user_query, "User")
        
        try:
            async for chunk in super().run_stream(user_query, self.context):
                yield chunk
        except Exception as e:
            yield f"Orchestrator Stream Error: {str(e)}"

# Singleton instance
orchestrator = HeadOfStrategy()
