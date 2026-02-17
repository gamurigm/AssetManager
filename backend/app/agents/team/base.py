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

        self.agent = Agent(
            self.model,
            system_prompt=(
                f"You are the {name}, a {role} in an Asset Management Team. "
                "Your expertise is STRICTLY LIMITED to financial markets, investments, trading, economics, and asset management. "
                "You are PROHIBITED from discussing or answering questions about any other topics, including but not limited to: "
                "general knowledge, entertainment, cooking, sports, personal advice, or creative writing. "
                "If a user asks about a non-financial topic, you must politely decline and state: "
                "'I am a specialized financial AI, I can only assist with investment and market-related queries.' "
                "You collaborate with other agents via a shared context. "
                "Keep responses concise and professional."
            ),
            deps_type=TeamContext
        )
        for tool in tools:
            self.agent.tool(tool)

    async def run(self, message: str, context: TeamContext) -> str:
        # Add user/orchestrator message to history handled by caller usually, 
        # but let's log the attempt if valuable.
        # context.add_message("user", message, "Orchestrator") # Caller usually does this
        
        try:
            # Run the agent with dependencies
            result = await self.agent.run(message, deps=context)
            
            # Extract output robustly across pydantic-ai versions
            output = getattr(result, 'output', getattr(result, 'data', str(result)))
            
            # Add response to history
            context.add_message("assistant", output, self.name)
            
            return output
        except Exception as e:
            error_msg = f"Error in {self.name}: {str(e)}"
            context.add_message("system", error_msg, self.name)
            return error_msg
