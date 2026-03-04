"""
test_multi_range.py
===================
Validates the backtest pipeline across different date ranges via HTTP API.
Calls the running backend at localhost:8282 — avoids DuckDB lock conflicts.

Run with:
    & "c:\\AssetManager\\backend\\venv\\Scripts\\python.exe" test_multi_range.py
"""

import asyncio
import sys
import time
import httpx

BACKEND = "http://localhost:8282"

# ── ANSI colours ─────────────────────────────────────────────────────────────
G   = "\033[92m"
R   = "\033[91m"
Y   = "\033[93m"
B   = "\033[94m"
W   = "\033[97m"
CY  = "\033[96m"
DIM = "\033[2m"
RST = "\033[0m"

# ── Test scenarios ─────────────────────────────────────────────────────────────
# (symbol, label, start_date, end_date)
SCENARIOS = [
    # SPY — progressively longer ranges (key: trade count must grow)
    ("SPY",  "1 week",   "2025-01-06", "2025-01-10"),
    ("SPY",  "2 weeks",  "2025-01-06", "2025-01-17"),
    ("SPY",  "1 month",  "2025-01-06", "2025-01-31"),
    ("SPY",  "3 months", "2025-01-06", "2025-03-31"),
    ("SPY",  "6 months", "2025-01-06", "2025-06-30"),
    # Multiple symbols, same 3-month range
    ("QQQ",  "3 months", "2025-01-06", "2025-03-31"),
    ("AAPL", "3 months", "2025-01-06", "2025-03-31"),
    ("MSFT", "3 months", "2025-01-06", "2025-03-31"),
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def hdr(text):
    print(f"\n{B}{'─'*72}{RST}")
    print(f"{B}  {text}{RST}")
    print(f"{B}{'─'*72}{RST}")


def bar(n, max_n=40):
    if n <= 0:
        return DIM + "(none)" + RST
    b = min(max_n, n)
    return G + "█" * b + RST + (f" +{n-max_n}" if n > max_n else "")


async def run_backtest(client: httpx.AsyncClient, symbol, start, end, iterations=500):
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
        timeout=600.0,  # Polygon paging can take a few minutes
    )
    resp.raise_for_status()
    return resp.json()


async def main():
    # Check backend is alive
    try:
        async with httpx.AsyncClient() as probe:
            r = await probe.get(f"{BACKEND}/", timeout=5)
            r.raise_for_status()
    except Exception:
        print(f"{R}ERROR: Backend is not running at {BACKEND}{RST}")
        print(f"  Start it with: .\\run_app.ps1")
        sys.exit(1)

    hdr(f"AssetManager — Multi-Range Backtest Validation ({len(SCENARIOS)} scenarios)")
    print(f"  {DIM}Backend: {BACKEND} | Bootstrap: 500 iter (fast mode){RST}\n")

    results = []
    prev_symbol = None
    prev_label  = None
    prev_trades = None

    async with httpx.AsyncClient() as client:
        for (symbol, label, start, end) in SCENARIOS:

            # Symbol section header
            if symbol != prev_symbol:
                hdr(f"Symbol: {symbol}")
                prev_symbol = symbol
                prev_label  = None
                prev_trades = None

            print(f"  {DIM}→ {symbol} {label:10s}  [{start} → {end}]  requesting...{RST}", end="", flush=True)
            t0 = time.perf_counter()

            try:
                data    = await run_backtest(client, symbol, start, end)
                elapsed = time.perf_counter() - t0

                kpis = data.get("kpis", {})
                bs   = data.get("bootstrap") or {}

                trades  = kpis.get("total_trades", 0)
                wins    = kpis.get("wins", 0)
                losses  = kpis.get("losses", 0)
                wr      = kpis.get("win_rate", 0.0)
                pf      = kpis.get("profit_factor")
                pf_str  = f"{pf:.2f}" if pf is not None else "∞"
                dd      = kpis.get("max_drawdown_pct", 0.0)
                ci_p    = bs.get("net_profit_95_ci", [None, None])
                ci_d    = bs.get("max_drawdown_95_ci_pct", [None, None])
                iters   = bs.get("iterations", 0)

                # Status colour
                trade_col = G if trades >= 10 else (Y if trades >= 3 else DIM)
                ci_str = (f"{G}${ci_p[0]:+.1f}{RST}→{G}${ci_p[1]:+.1f}{RST}"
                          if ci_p[0] is not None and ci_p[1] is not None
                          else DIM + "N/A" + RST)
                print(f"\r  {G}OK{RST}  {W}{symbol:5s}{RST} {label:10s} | "
                      f"Trades: {trade_col}{trades:3d}{RST} ({wins}W/{losses}L) | "
                      f"WR: {wr*100:.1f}% | PF: {pf_str} | "
                      f"DD: {dd*100:.3f}% | "
                      f"CI₉₅: {ci_str}"
                      f" | {DIM}{elapsed:.1f}s{RST}")

                # Bootstrap details if available
                if iters:
                    sample_size = bs.get("sample_size", 0)
                    ci_d_str = (f"{ci_d[0]:.2f}%→{ci_d[1]:.2f}%" 
                                if ci_d[0] is not None and ci_d[1] is not None else "N/A")
                    print(f"      {DIM}Bootstrap: {iters} iter, {sample_size} trades sampled | "
                          f"MaxDD 95CI: {ci_d_str}{RST}")

                # Trade bar chart
                print(f"      {bar(trades)}")

                # ── Assertions ──────────────────────────────────────────────
                fails = []

                # 1. Longer range ≥ shorter range (same symbol)
                if prev_trades is not None:
                    if trades < prev_trades:
                        fails.append(
                            f"Trade count REGRESSION: {label}({trades}) < {prev_label}({prev_trades}) "
                            f"— longer range should have ≥ trades"
                        )

                # 2. KPI sanity
                if not 0.0 <= wr <= 1.0:
                    fails.append(f"Win rate out of [0,1]: {wr}")
                if pf is not None and pf < 0:
                    fails.append(f"Negative profit factor: {pf}")
                if dd < 0:
                    fails.append(f"Negative drawdown: {dd}")
                if ci_p[0] is not None and ci_p[1] is not None and ci_p[0] > ci_p[1]:
                    fails.append(f"CI inverted: {ci_p}")

                for f in fails:
                    print(f"    {R}  ⚠  {f}{RST}")

                results.append({
                    "symbol": symbol, "label": label,
                    "trades": trades, "elapsed": elapsed, "fails": fails,
                })

                prev_label  = label
                prev_trades = trades

            except httpx.HTTPStatusError as e:
                elapsed = time.perf_counter() - t0
                print(f"\r  {R}FAIL{RST} {symbol} {label:10s} → HTTP {e.response.status_code}: {e.response.text[:120]}  ({elapsed:.1f}s)")
                results.append({"symbol": symbol, "label": label, "trades": -1, "elapsed": elapsed, "fails": [str(e)]})

            except Exception as e:
                elapsed = time.perf_counter() - t0
                print(f"\r  {R}CRASH{RST} {symbol} {label:10s} → {e}  ({elapsed:.1f}s)")
                results.append({"symbol": symbol, "label": label, "trades": -1, "elapsed": elapsed, "fails": [str(e)]})

    # ── Final summary ──────────────────────────────────────────────────────────
    hdr("Final Summary")
    total   = len(results)
    crashes = sum(1 for r in results if r["trades"] < 0)
    warns   = sum(1 for r in results if r["fails"] and r["trades"] >= 0)
    ok      = total - crashes - warns

    print(f"  Total scenarios : {total}")
    print(f"  {G}✓ OK            : {ok}{RST}")
    print(f"  {Y}⚠ Warnings      : {warns}{RST}")
    print(f"  {R}✗ Crashes       : {crashes}{RST}")

    # SPY progression table
    spy_res = [r for r in results if r["symbol"] == "SPY"]
    if spy_res:
        print(f"\n  {CY}SPY trade count by range:{RST}")
        for r in spy_res:
            status = G+"✓"+RST if not r["fails"] else R+"⚠"+RST
            print(f"    {status} {r['label']:12s} : {r['trades']:3d} trades  {bar(r['trades'])}")

    if crashes == 0 and warns == 0:
        print(f"\n  {G}✅ All scenarios passed. Pipeline is range-agnostic and healthy.{RST}")
    else:
        print(f"\n  {Y}⚠  Some issues detected. Review lines above.{RST}")
    print()


if __name__ == "__main__":
    asyncio.run(main())
