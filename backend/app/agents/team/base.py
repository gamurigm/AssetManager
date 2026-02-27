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

            return (
                f"You are the {name}, a {role} in an Asset Management Team. "
                f"Current Time: {now}. "
                "You are part of the MMAM Alpha Core Institutional Team. "
                "Your expertise is STRICTLY LIMITED to financial markets, investments, trading, economics, and asset management. "
                "You have access to advanced quantitative metrics: \n"
                "- Expected Value ($E[x]$) of trades.\n"
                "- Risk Adjusted Returns.\n"
                "- Momentum via Gradient Descent / Linear Regression.\n"
                "- Algorithmic Hedging Strategies.\n"
                "If a user asks about a non-financial topic, you must politely decline. "
                "You collaborate with other agents via a shared context. "
                "\n\n[FORMATTING DIRECTIVE]:\n"
                "- Use LaTeX for ALL mathematical formulas and complex expressions.\n"
                "- Use block math with '$$' for significant calculations or derivations.\n"
                "- Use inline math with '$' for simple numbers or variables within text.\n"
                "- Format calculations step-by-step to show your logic, using LaTeX alignment if possible.\n"
                "- Ensure your output is highly professional and aesthetically structured.\n"
                "\nIMPORTANT: If the information requested (like prices or values) is already available in the [REAL-TIME] blocks provided below, use it directly instead of calling tools."
                f"{realtime_info}"
            )
        for tool in tools:
            self.agent.tool(tool)

    async def run(self, message: str, context: TeamContext) -> str:
        import logfire
        with logfire.span(f"{self.name} processing: {message[:50]}...", agent=self.name, role=self.role):
            try:
                # Run the agent with dependencies
                result = await self.agent.run(message, deps=context)
                
                # Extract output robustly
                output = getattr(result, 'output', getattr(result, 'data', str(result)))
                
                # Add response to history
                context.add_message("assistant", output, self.name)
                
                logfire.info(f"{self.name} response completed", character_count=len(output))
                return output
            except Exception as e:
                error_msg = f"Error in {self.name}: {str(e)}"
                logfire.error(f"Agent {self.name} failed", error=str(e))
                context.add_message("system", error_msg, self.name)
                return error_msg

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
