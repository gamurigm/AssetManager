from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from typing import Optional, Dict, Any, List, Union
from .state import TeamContext
import os
from ...core.config import settings

# Force OpenAI global settings for NVIDIA NIM if not already set
os.environ["OPENAI_API_KEY"] = settings.NVIDIA_NIM_API_KEY
os.environ["OPENAI_BASE_URL"] = 'https://integrate.api.nvidia.com/v1'

class TeamAgent:
    def __init__(self, name: str, role: str, model_name: str, tools: List[callable] = []):
        self.name = name
        self.role = role
        
        # Explicitly use OpenAIModel for NVIDIA NIM compatibility
        # Check if model_name is already an OpenAIModel instance (unlikely here but good practice)
        if isinstance(model_name, str):
            self.model = OpenAIModel(model_name)
        else:
            self.model = model_name

        self.agent = Agent(self.model, deps_type=TeamContext)

        @self.agent.system_prompt
        def dynamic_system_prompt(ctx: RunContext[TeamContext]) -> str:
            portfolio_info = ""
            if "current_portfolio" in ctx.deps.scratchpad:
                p = ctx.deps.scratchpad["current_portfolio"]
                portfolio_info = f"\n\n[REAL-TIME PORTFOLIO DATA]\nTotal Value: ${p.get('total_value', 0):,.2f}\nTotal P&L: ${p.get('total_pnl', 0):,.2f} ({p.get('pnl_percent', 0):.2f}%)\nAssets: {p.get('holdings', [])}"

            return (
                f"You are the {name}, a {role} in an Asset Management Team. "
                "Your expertise is STRICTLY LIMITED to financial markets, investments, trading, economics, and asset management. "
                "You are PROHIBITED from discussing or answering questions about any other topics. "
                "If a user asks about a non-financial topic, you must politely decline. "
                "You collaborate with other agents via a shared context. "
                "Keep responses concise and professional."
                f"{portfolio_info}"
            )
        for tool in tools:
            self.agent.tool(tool)

    async def run(self, message: str, context: TeamContext) -> str:
        try:
            # Run the agent with dependencies
            result = await self.agent.run(message, deps=context)
            
            # Extract output robustly
            output = getattr(result, 'output', getattr(result, 'data', str(result)))
            
            # Add response to history
            context.add_message("assistant", output, self.name)
            
            return output
        except Exception as e:
            error_msg = f"Error in {self.name}: {str(e)}"
            context.add_message("system", error_msg, self.name)
            return error_msg

    async def run_stream(self, message: str, context: TeamContext):
        """Streams the response from the agent."""
        try:
            async with self.agent.run_stream(message, deps=context) as result:
                async for message_chunk in result.stream_text(delta=True):
                    yield message_chunk
                
                # After streaming is done, log the full message to context
                full_message = result.get_data() if hasattr(result, 'get_data') else ""
                if not full_message and hasattr(result, 'formatted_messages'):
                    # Fallback to extract from messages if needed
                    pass
                
                # Note: Handling final context update might need more care with run_stream
        except Exception as e:
            yield f"Error in {self.name} stream: {str(e)}"
