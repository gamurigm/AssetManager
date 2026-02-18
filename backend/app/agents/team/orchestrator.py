from .state import TeamContext
from .specialists import specialists_map
from .base import TeamAgent
from pydantic_ai import RunContext
from typing import Optional
import json

# --- Orchestrator Definition ---
# Uses GLM-5 or similar high-reasoning model for planning

ORCHESTRATOR_MODEL = "deepseek-ai/deepseek-v3.2"

import asyncio
from typing import List, Dict

# ... existing imports ...

async def delegate_task(ctx: RunContext[TeamContext], specialist_name: str, instruction: str) -> str:
    """Delegate a single subtask (Sequential)."""
    # ... existing implementation ...
    agent = specialists_map.get(specialist_name)
    if not agent:
        return f"Error: Specialist '{specialist_name}' not found."
    
    # Log delegation in context
    from app.core.logging import logger
    logger.info(f"Delegating task to {specialist_name}: {instruction[:100]}...")
    ctx.deps.add_message("system", f"Delegating to {specialist_name}: {instruction}", "Head of Strategy")
    
    result = await agent.run(instruction, ctx.deps)
    return f"Response from {specialist_name}: {result}"


async def delegate_parallel_tasks(ctx: RunContext[TeamContext], tasks: List[Dict[str, str]]) -> str:
    """
    Delegate multiple subtasks to run in PARALLEL.
    Input format: [{"specialist": "Fundamental Analyst", "instruction": "Check news..."}, ...]
    """
    from app.core.logging import logger
    
    async def run_single(task):
        spec_name = task.get("specialist")
        instr = task.get("instruction")
        agent = specialists_map.get(spec_name)
        if not agent:
            return f"{spec_name}: Specialist not found."
        
        logger.info(f"PARALLEL Delegation to {spec_name}: {instr[:50]}...")
        ctx.deps.add_message("system", f"Parallel delegation to {spec_name}: {instr}", "Head of Strategy")
        
        try:
            res = await agent.run(instr, ctx.deps)
            return f"--- Response from {spec_name} ---\n{res}"
        except Exception as e:
            return f"Error from {spec_name}: {str(e)}"

    results = await asyncio.gather(*(run_single(t) for t in tasks))
    return "\n\n".join(results)

class HeadOfStrategy(TeamAgent):
    def __init__(self):
        super().__init__(
            "Head of Strategy",
            "Orchestrator lead responsible for planning and delegating tasks",
            ORCHESTRATOR_MODEL,
            tools=[delegate_task, delegate_parallel_tasks]
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

    async def run_stream(self, user_query: str, portfolio: Optional[dict] = None):
        # Update shared context with real-time portfolio data if available
        if portfolio:
            self.context.update_scratchpad("current_portfolio", portfolio)
            # Add a hidden system message just for this turn to inform the agent
            p_info = json.dumps(portfolio, indent=2)
            self.context.add_message("system", f"REAL-TIME PORTFOLIO DATA:\n{p_info}", "System Monitor")

        # Add user message to shared context
        self.context.add_message("user", user_query, "User")
        
        try:
            async for chunk in super().run_stream(user_query, self.context):
                yield chunk
        except Exception as e:
            yield f"Orchestrator Stream Error: {str(e)}"

# Singleton instance
orchestrator = HeadOfStrategy()
