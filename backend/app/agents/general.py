from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.settings import ModelSettings
from pydantic_ai.providers.openai import OpenAIProvider
from openai import AsyncOpenAI
from ..core.config import settings
from ..services.openbb_native_service import openbb_native

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
        "You have access to a suite of OpenBB tools to fetch live market data, charts, and fundamentals. "
        "If you need specific data, use the 'execute_openbb_command' tool. "
        "OpenBB command paths follow the structure 'equity/price/quote', 'crypto/price/historical', etc. "
        "Supported flags: --symbol, --start_date, --end_date, --limit, --chart. "
        "You are PROHIBITED from discussing or answering questions about any other topics."
    )
)

@general_agent.tool
async def execute_openbb_command(ctx: RunContext[None], command_path: str, symbol: str = None, chart: bool = False, limit: int = 10) -> str:
    """
    Execute a native OpenBB Platform command.
    Example command_path: 'equity/price/quote', 'equity/fundamental/income', 'crypto/price/historical'.
    Flags are passed via arguments.
    """
    kwargs = {}
    if symbol:
        kwargs["symbol"] = symbol
    if chart:
        kwargs["chart"] = True
    if limit:
        kwargs["limit"] = limit
        
    # Standardize path
    command_path = command_path.replace("/", ".")
    
    result = await openbb_native.execute(command_path, kwargs)
    if "error" in result:
        return f"Error: {result['error']}"
    return result.get("output", "Command executed.")

@general_agent.tool
async def get_market_overview(ctx: RunContext[None]) -> str:
    """Get a high-level overview of the current market state."""
    # This would eventually call OpenBB
    return "Market is currently stable with a slight bullish trend in tech stocks."
