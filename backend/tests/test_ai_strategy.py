import asyncio
import httpx

async def run_ai_strategy_gen():
    print("Asking AI Strategy Analyst to generate a strategy via API...")
    prompt = "Create a very simple Moving Average Crossover strategy (SMA_CROSSOVER) using 20 and 50 periods. Output the Python code implementing the IStrategyEngine interface. Save it using your create_or_edit_strategy_engine tool."
    
    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(
            "http://localhost:8282/api/v1/chat/chat",
            json={"message": prompt}
        )
        print("\n--- AI Result ---")
        print(response.json())

if __name__ == "__main__":
    asyncio.run(run_ai_strategy_gen())
