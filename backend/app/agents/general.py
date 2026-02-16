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
        "You are a helpful financial knowledge assistant for an Asset Management platform. "
        "You provide information about financial markets, investment strategies, and platform features. "
        "Keep your answers concise and professional."
    )
)

@general_agent.tool
async def get_market_overview(ctx: RunContext[None]) -> str:
    """Get a high-level overview of the current market state."""
    # This would eventually call OpenBB
    return "Market is currently stable with a slight bullish trend in tech stocks."
