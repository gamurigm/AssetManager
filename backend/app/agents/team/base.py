from pydantic_ai import Agent, RunContext
from pydantic_ai.settings import ModelSettings
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from typing import Optional, Dict, Any, List, Union
from .state import TeamContext
from ...core.config import settings
from openai import AsyncOpenAI
import json
from datetime import datetime
from pathlib import Path
import os

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
    def __init__(self, name: str, role: str, model_name: str, tools: List[callable] = []):
        self.name = name
        self.role = role
        
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

            template = _load_prompt("agent_base.md")
            base_prompt = template.format(name=name, role=role)
            return f"{base_prompt}\n\nCurrent Time: {now}\n{realtime_info}{gsd_context}"
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
