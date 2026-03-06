import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.agents.team.specialists import quant_analyst
from app.agents.team.state import TeamContext

async def test_self_correction():
    print("--- TESTING AGENT SELF-CORRECTION (FORCED TYPO) ---")
    print("Instruction: 'Use the OpenBB terminal to get historical prices for AAPL, but intentionaly use the wrong path: equity.price.historial'")
    
    ctx = TeamContext()
    try:
        # We explicitly tell the agent to use a wrong path to trigger the fuzzy matcher and retry loop
        result = await quant_analyst.run(
            "Execute the OpenBB terminal command 'equity.price.historial' for symbol AAPL. "
            "I know it has a typo, I want to see you fix it using the fuzzy matching feedback.",
            context=ctx
        )
        print("\n=== FINAL AGENT RESPONSE ===")
        print(result)
        print("============================\n")
        
        # Check if the successful output is present (from the corrected command)
        if "close" in result.lower() or "open" in result.lower() or "volume" in result.lower():
            print("[TEST PASSED] Agent successfully corrected the typo and fetched the data!")
        else:
            print("[TEST FAILED] Agent did not return the expected data. Check logs for retry attempts.")
            
    except Exception as e:
        print(f"[TEST ERROR] {e}")

if __name__ == "__main__":
    asyncio.run(test_self_correction())
