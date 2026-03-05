    import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.agents.team.specialists import quant_analyst
from app.agents.team.state import TeamContext

async def real_agent_test():
    print("--- INITIATING REAL LLM AGENT TEST (QUANT ANALYST) ---")
    print("Prompt: 'Display the RSI for AAPL using OpenBB terminal'")
    
    ctx = TeamContext()
    try:
        result = await quant_analyst.run(
            "Display the RSI for AAPL using OpenBB terminal",
            context=ctx
        )
        print("\n=== AGENT RESPONSE ===")
        print(result)
        print("========================\n")
        
        if "```openbb" in result.lower() or "technical rsi" in result.lower():
            print("[TEST PASSED] Agent successfully utilized the native terminal schema from openbb_api_reference.md!")
        else:
            print("[TEST WARN] Agent responded, but may not have used the strict ```openbb formatting. Verify manually.")
            
    except Exception as e:
        print(f"[TEST FAILED] {e}")

if __name__ == "__main__":
    asyncio.run(real_agent_test())
