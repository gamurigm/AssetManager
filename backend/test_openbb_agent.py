import asyncio
from app.agents.team.orchestrator import orchestrator

async def main():
    print("Testing Orchestrator with OpenBB API...")
    result = await orchestrator.run("Hey, use the OpenBB API to get the current price for MSFT.", session_id='test')
    print("\nResult:\n")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
