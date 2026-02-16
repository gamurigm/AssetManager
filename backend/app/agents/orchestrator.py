from pydantic_ai import Agent, RunContext
from .general import general_agent
from pydantic import BaseModel

class AgentResponse(BaseModel):
    response: str
    agent_id: str

# In a more complex Agentic Architecture, the orchestrator might use 
# another LLM to decide which agent to call.
# For now, we can simple routing or a main agent that delegates.
from .team.orchestrator import orchestrator

async def route_query(query: str, user_id: int) -> AgentResponse:
    # Use the new Head of Strategy Team Orchestrator
    response_text = await orchestrator.run(query)
    # The team orchestrator returns a string (final answer)
    return AgentResponse(response=response_text, agent_id="head-of-strategy")
