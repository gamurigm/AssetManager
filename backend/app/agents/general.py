from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from ..core.config import settings
import os

# Set environment variables for OpenAI client configuration
os.environ["OPENAI_API_KEY"] = settings.NVIDIA_NIM_API_KEY
os.environ["OPENAI_BASE_URL"] = 'https://integrate.api.nvidia.com/v1'

# Initialize NIM model (OpenAI compatible)
# pydantic-ai should pick up the environment variables
model = OpenAIModel(settings.NIM_MODEL_NAME)

general_agent = Agent(
    model,
    system_prompt=(
        "You are a specialized Financial Intelligence Assistant for an Asset Management platform. "
        "Your expertise is STRICTLY LIMITED to financial markets, investments, trading, economics, and asset management. "
        "You are PROHIBITED from discussing or answering questions about any other topics, including but not limited to: "
        "general knowledge, entertainment, cooking, sports, personal advice, or creative writing. "
        "If a user asks about a non-financial topic, you must politely decline and state: "
        "'I am a specialized financial AI, I can only assist with investment and market-related queries.' "
        "Keep your answers concise and professional."
    )
)

@general_agent.tool
async def get_market_overview(ctx: RunContext[None]) -> str:
    """Get a high-level overview of the current market state."""
    # This would eventually call OpenBB
    return "Market is currently stable with a slight bullish trend in tech stocks."
