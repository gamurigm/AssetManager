from pydantic_ai import Agent, RunContext
from pydantic_ai.settings import ModelSettings
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from typing import Optional, Dict, Any, List, Union
from enum import Enum
from .state import TeamContext
from ...core.config import settings
from openai import AsyncOpenAI
import json
from datetime import datetime
from pathlib import Path
import os


class AgentTier(str, Enum):
    """Defines the role tier of each agent in the hierarchical pipeline.

    Pipeline order (strict):
      ANALYST → RISK → STRATEGIST → EXECUTION

    Rules enforced via prompt injection:
    • ANALYST  : Can only produce analysis reports (submit_analysis_report).
                 Cannot write strategies or authorize trade signals.
    • RISK     : Can only produce risk assessments (submit_risk_report).
                 Cannot write strategies or authorize trade signals.
    • STRATEGIST: SOLE authority to synthesize reports, write strategy engines,
                  and authorize trade signals (authorize_trade_signal).
    • EXECUTION : Can ONLY execute trade signals that have been authorized
                  by the STRATEGIST and placed in approved_trade_signals.
    • ORCHESTRATOR: Meta-level coordination; delegates to any tier.
    """
    ANALYST      = "ANALYST"
    RISK         = "RISK"
    STRATEGIST   = "STRATEGIST"
    EXECUTION    = "EXECUTION"
    ORCHESTRATOR = "ORCHESTRATOR"


# Human-readable constraint text injected into every agent's system prompt.
_TIER_CONSTRAINTS: Dict[AgentTier, str] = {
    AgentTier.ANALYST: (
        "## 🏛️ YOUR TIER: ANALYST\n"
        "You are an **Analyst-tier** agent. Your role is strictly limited to research and analysis.\n\n"
        "**YOU MAY:**\n"
        "- Gather market data, run technical/fundamental/macro analysis.\n"
        "- Call `submit_analysis_report` to formally deposit your findings for the Strategist.\n\n"
        "**YOU MAY NOT:**\n"
        "- Write or modify trading strategy code.\n"
        "- Authorize, suggest, or initiate trade signals.\n"
        "- Instruct the Trader or any execution-tier agent directly.\n\n"
        "Your output feeds the **Strategy Analyst** who decides what to do with it."
    ),
    AgentTier.RISK: (
        "## 🏛️ YOUR TIER: RISK\n"
        "You are a **Risk-tier** agent. Your role is strictly portfolio and position risk assessment.\n\n"
        "**YOU MAY:**\n"
        "- Quantify VaR, drawdown, correlation, and tail risk.\n"
        "- Call `submit_risk_report` to formally deposit your risk assessment for the Strategist.\n\n"
        "**YOU MAY NOT:**\n"
        "- Write or modify trading strategy code.\n"
        "- Authorize, suggest, or initiate trade signals.\n"
        "- Instruct the Trader or any execution-tier agent directly.\n\n"
        "Your risk assessment is consumed by the **Strategy Analyst** before any trade is authorized."
    ),
    AgentTier.STRATEGIST: (
        "## 🏛️ YOUR TIER: STRATEGIST (GATEKEEPER)\n"
        "You are the **sole authority** at the top of the investment pipeline.\n\n"
        "**YOU MAY:**\n"
        "- Call `request_team_briefing` to collect all analyst and risk reports in parallel.\n"
        "- Write trading strategies with `create_or_edit_strategy_engine` — **you are the ONLY agent that may do this**.\n"
        "- Authorize trade signals with `authorize_trade_signal` — **you are the ONLY agent that may do this**.\n"
        "- Run backtests to validate strategies before authorizing a live signal.\n\n"
        "**YOU MAY NOT:**\n"
        "- Skip the briefing step — always read analyst and risk reports before synthesizing.\n"
        "- Authorize a signal without a documented rationale backed by analyst findings.\n\n"
        "**MANDATORY WORKFLOW:**\n"
        "1. `request_team_briefing(symbols, focus_areas)` → collect Quant + Macro + Fundamental + Risk reports.\n"
        "2. Synthesize the multi-dimensional view into a **Strategic Thesis**.\n"
        "3. Optionally: `create_or_edit_strategy_engine` to codify the thesis.\n"
        "4. `authorize_trade_signal(...)` to formally pass a signal to the Trader.\n"
    ),
    AgentTier.EXECUTION: (
        "## 🏛️ YOUR TIER: EXECUTION\n"
        "You are an **Execution-tier** agent. Your job is fast, accurate order placement.\n\n"
        "**YOU MAY:**\n"
        "- Call `get_strategic_signal` to retrieve signals authorized by the Strategy Analyst.\n"
        "- Place orders via cTrader/IBKR for signals that appear in `approved_trade_signals`.\n"
        "- Check account status and confirm execution details.\n\n"
        "**YOU MAY NOT:**\n"
        "- Make investment decisions — you execute, you do NOT decide.\n"
        "- Place any order that does NOT appear in `approved_trade_signals`.\n"
        "- Request analysis from analyst-tier agents — that is the Strategist's job.\n\n"
        "If you receive a buy/sell request that is NOT backed by an approved signal, reply:\n"
        "> 'No authorized signal found. Please ask the Strategy Analyst to evaluate and authorize a trade first.'"
    ),
    AgentTier.ORCHESTRATOR: (
        "## 🏛️ YOUR TIER: ORCHESTRATOR\n"
        "You coordinate the full Alpha Core team. You may delegate to any tier."
    ),
}

def _load_project_file(filename: str) -> str:
    """Load a file from the project root."""
    root_dir = Path(__file__).parent.parent.parent.parent.parent
    filepath = root_dir / filename
    try:
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read().strip()
        return ""
    except Exception:
        return ""

def _load_prompt(filename: str) -> str:
    """Load Markdown prompt from the prompts directory."""
    prompt_dir = Path(__file__).parent / "prompts"
    filepath = prompt_dir / filename
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        return f"Error loading {filename}: {str(e)}"

class TeamAgent:
    def __init__(self, name: str, role: str, model_name: str, tools: List[callable] = [], tier: AgentTier = AgentTier.ANALYST):
        self.name = name
        self.role = role
        self.tier = tier
        
        if isinstance(model_name, str):
            client = AsyncOpenAI(
                base_url='https://integrate.api.nvidia.com/v1',
                api_key=settings.NVIDIA_NIM_API_KEY
            )
            provider = OpenAIProvider(openai_client=client)
            self.model = OpenAIModel(model_name, provider=provider)
        else:
            self.model = model_name

        self.agent = Agent(
            self.model, 
            deps_type=TeamContext,
            model_settings=ModelSettings()
        )

        _tier = tier  # capture for closure

        @self.agent.system_prompt
        def dynamic_system_prompt(ctx: RunContext[TeamContext]) -> str:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Use pre-formatted context if available (provided by Orchestrator)
            realtime_info = ctx.deps.scratchpad.get("formatted_realtime_context", "")
            
            # Fallback to local formatting if not pre-formatted
            if not realtime_info:
                if "current_portfolio" in ctx.deps.scratchpad:
                    p = ctx.deps.scratchpad["current_portfolio"]
                    holdings = p.get('holdings', [])
                    realtime_info += f"\n\n[REAL-TIME PORTFOLIO SNAPSHOT]\nReference Time: {now}\nTotal Value: ${p.get('total_value', 0):,.2f}\nTotal P&L: ${p.get('total_pnl', 0):,.2f} ({p.get('pnl_percent', 0):.2f}%)\nAssets: {json.dumps(holdings)}"

                if "market_regime" in ctx.deps.scratchpad:
                    r = ctx.deps.scratchpad["market_regime"]
                    realtime_info += f"\n\n[MARKET REGIME DATA]\nSymbol: {r.get('symbol')}\nAnalysis: {json.dumps(r.get('regime_analysis'))}"

            # GSD Context Injection
            gsd_roadmap = _load_project_file("ROADMAP.md")
            gsd_state = _load_project_file("STATE.md")
            
            gsd_context = ""
            if gsd_roadmap:
                gsd_context += f"\n\n## 🗺️ PROJECT ROADMAP (GSD)\n{gsd_roadmap}"
            if gsd_state:
                gsd_context += f"\n\n## 📊 PROJECT STATE (GSD)\n{gsd_state}"

            # Tier constraint injection
            tier_block = _TIER_CONSTRAINTS.get(_tier, "")

            template = _load_prompt("agent_base.md")
            base_prompt = template.format(name=name, role=role)
            return f"{base_prompt}\n\n{tier_block}\n\nCurrent Time: {now}\n{realtime_info}{gsd_context}"
        for tool in tools:
            self.agent.tool(tool)

    async def run(self, message: str, context: TeamContext) -> str:
        import logfire
        from .specialists import discover_openbb_endpoints, get_openbb_endpoint_details

        max_retries = 5
        current_attempt = 0
        last_error = None
        seen_commands = set()
        
        while current_attempt < max_retries:
            with logfire.span(f"{self.name} processing (Attempt {current_attempt + 1}): {message[:50]}...", agent=self.name, role=self.role):
                try:
                    # Run the agent with dependencies
                    result = await self.agent.run(message, deps=context)
                    
                    # Extract output robustly
                    output = getattr(result, 'output', getattr(result, 'data', str(result)))
                    
                    # DETECTION: If the output looks like an error from our tools
                    is_error = False
                    if isinstance(output, str):
                        lower_output = output.lower()
                        # Broad markers for any kind of failure
                        error_markers = ["error", "http 4", "http 5", "failed", "not found", "traceback", "exception", "validation error"]
                        if any(marker in lower_output for marker in error_markers):
                            is_error = True
                    
                    if is_error:
                        current_attempt += 1
                        last_error = output
                        
                        # ANTI-LOOP: Check if the agent is repeating the exact same command
                        # We try to extract the last command from the history or output
                        # For now, let's just warn about repeating the same error message
                        error_fingerprint = f"{output[:100]}"
                        
                        warning = ""
                        if error_fingerprint in seen_commands:
                            warning = "\nALERTA: Estás repitiendo un comando que YA FALLÓ con el mismo resultado. CAMBIA los parámetros (ej. tickers, proveedores) o usa 'discover_openbb_endpoints'. No repitas lo mismo."
                        
                        seen_commands.add(error_fingerprint)
                        
                        # INJECT Correction Prompt for the NEXT iteration of the loop
                        message = f"""
[COMMAND EXECUTION FAILED]
Attempt {current_attempt} of {max_retries} failed with the following feedback: {warning}
---
{output}
---

INSTRUCTION:
1. ANALYZE why it failed. 
2. If ticker data is missing (e.g. DJI), it is usually because the ticker is WRONG for the provider (yfinance needs '^DJI').
3. DO NOT repeat the exact same command. Try a variation or a different tool.
4. FIX and RETRY now.
"""
                        logfire.info(f"{self.name} detected error, retrying...", attempt=current_attempt, error_preview=output[:100])
                        continue # Retry the loop with the new message
                    
                    # Success path
                    context.add_message("assistant", output, self.name)
                    logfire.info(f"{self.name} response completed", character_count=len(output))
                    return output
                    
                except Exception as e:
                    current_attempt += 1
                    error_msg = f"Error in {self.name}: {str(e)}"
                    logfire.error(f"Agent {self.name} failed", error=str(e))
                    
                    if current_attempt >= max_retries:
                        context.add_message("system", error_msg, self.name)
                        return error_msg
                    
                    message = f"The system encountered an internal execution error: {str(e)}. Please try an alternative approach or fix the command parameters."
                    continue

        return f"Failed after {max_retries} correction attempts. Last error: {last_error}"

    async def run_stream(self, message: str, context: TeamContext):
        """Streams the response from the agent."""
        import logfire
        with logfire.span(f"{self.name} streaming: {message[:50]}...", agent=self.name):
            try:
                async with self.agent.run_stream(message, deps=context) as result:
                    async for message_chunk in result.stream_text(delta=True):
                        yield message_chunk
            except Exception as e:
                logfire.error(f"Agent {self.name} stream failed", error=str(e))
                yield f"Error in {self.name} stream: {str(e)}"
