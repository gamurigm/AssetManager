from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.settings import ModelSettings
from pydantic_ai.providers.openai import OpenAIProvider
from openai import AsyncOpenAI
from ..core.config import settings

# Initialize NIM model (OpenAI compatible)
client = AsyncOpenAI(
    base_url='https://integrate.api.nvidia.com/v1',
    api_key=settings.NVIDIA_NIM_API_KEY
)
provider = OpenAIProvider(openai_client=client)
model = OpenAIModel(settings.NIM_MODEL_NAME, provider=provider)

general_agent = Agent(
    model,
    model_settings=ModelSettings(),
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
