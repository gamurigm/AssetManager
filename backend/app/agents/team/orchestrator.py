from .state import TeamContext
from .specialists import specialists_map
from .base import TeamAgent
from pydantic_ai import RunContext
from typing import Optional

# --- Orchestrator Definition ---
# Uses GLM-5 or similar high-reasoning model for planning

ORCHESTRATOR_MODEL = "z-ai/glm5"

async def delegate_task(ctx: RunContext[TeamContext], specialist_name: str, instruction: str) -> str:
    """
    Delegate a subtask to a specialist agent.
    Available Specialists:
    - "Fundamental Analyst": Use for news, company profiles, qualitative data.
    - "Quantitative Analyst": Use for price data, technical analysis.
    - "Macro Analyst": Use for global economic news and broad market trends.
    - "Risk Manager": Use for compliance and risk metrics (VaR, Sharpe).
    - "Trader": Use for executing orders and calculating fees.
    """
    agent = specialists_map.get(specialist_name)
    if not agent:
        return f"Error: Specialist '{specialist_name}' not found."
    
    # Log delegation in context
    ctx.deps.add_message("system", f"Delegating to {specialist_name}: {instruction}", "Head of Strategy")
    
    # Run the specialist
    # Note: agent.run returns the output string directly because TeamAgent wraps it
    result = await agent.run(instruction, ctx.deps)
    
    return f"Response from {specialist_name}: {result}"

class HeadOfStrategy(TeamAgent):
    def __init__(self):
        super().__init__(
            "Head of Strategy",
            "Orchestrator lead responsible for planning and delegating tasks",
            ORCHESTRATOR_MODEL,
            tools=[delegate_task]
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

    async def run_stream(self, user_query: str):
        # Add user message to shared context
        self.context.add_message("user", user_query, "User")
        
        try:
            async for chunk in super().run_stream(user_query, self.context):
                yield chunk
        except Exception as e:
            yield f"Orchestrator Stream Error: {str(e)}"

# Singleton instance
orchestrator = HeadOfStrategy()
