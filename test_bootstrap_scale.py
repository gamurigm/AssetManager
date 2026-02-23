import asyncio
import sys
import time
import httpx

BACKEND = "http://localhost:8282"

async def run_iterations(client, iterations):
    symbol = "SPY"
    start = "2025-01-06"
    end = "2025-06-30"
    
    print(f"\n--- Testing Bootstrap with {iterations} iterations ---")
    t0 = time.time()
    
    resp = await client.post(
        f"{BACKEND}/api/v1/simulation/run",
        json={
            "symbol": symbol,
            "start_date": start,
            "end_date": end,
            "account_size": 10000.0,
            "run_bootstrap": True,
            "bootstrap_iterations": iterations,
        },
        timeout=600.0,
    )
    
    t1 = time.time()
    
    if resp.status_code in [200, 202]:
        data = resp.json()
        kpis = data.get("kpis", {})
        trades = data.get("trades", [])
        if "total_trades" in data and not trades:
            trades_count = data["total_trades"]
        else:
            trades_count = len(trades)
        
        boot = data.get("bootstrap", {})
        
        print(f"Time Taken: {t1 - t0:.2f} seconds")
        print(f"Trades Count: {trades_count}")
        print(f"Win Rate: {kpis.get('win_rate', 0)*100:.1f}%")
        
        if boot:
            ci_d = boot.get("max_drawdown_95_ci_pct", [None, None])
            ci_p = boot.get("net_profit_95_ci", [None, None])
            print(f"Bootstrap MaxDD 95% CI: {ci_d[0]*100 if ci_d[0] else 'N/A':.2f}% -> {ci_d[1]*100 if ci_d[1] else 'N/A':.2f}%")
            print(f"Bootstrap Net Profit 95% CI: {ci_p[0] if ci_p[0] else 'N/A':.2f} -> {ci_p[1] if ci_p[1] else 'N/A':.2f}")
        else:
            print("Bootstrap stats missing!")
    else:
        print(f"Error {resp.status_code}: {resp.text[:200]}")

async def main():
    try:
        async with httpx.AsyncClient() as probe:
            r = await probe.get(f"{BACKEND}/", timeout=5)
            r.raise_for_status()
    except Exception:
        print("Backend is not running at http://localhost:8282")
        sys.exit(1)

    iters = [1000, 5000, 10000]
    async with httpx.AsyncClient() as client:
        for i in iters:
            await run_iterations(client, i)

if __name__ == "__main__":
    asyncio.run(main())
