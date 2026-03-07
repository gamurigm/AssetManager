"""
Capital Sweep — Multi-Capital Backtest Comparison
===================================================
Runs the same backtest with different initial capitals and prints a
normalized comparison table.

Key insight:
  • pnl_r (R-multiples) and win_rate are CAPITAL-NEUTRAL → must be
    identical across all capital levels.
  • pnl_usd and final_equity scale linearly with capital.
  • net_pnl_pct (%) must also be identical — test used to verify the fix.

Position sizing formula used by ORBFVGEngine:
  lots = (account × risk_pct) / (risk_pips × pip_value)

For equities (stocks):
  pip_value = $1.00 per share   (since price is quoted in USD/share)
  lots      = number of shares to buy/sell per trade
  risk_pips = distance in $ from entry to stop-loss

Usage:
  & "c:\AssetManager\backend\venv\Scripts\python.exe" scripts\capital_sweep.py \\
        --symbol TSLA \\
        --start 2025-03-21 --end 2026-03-05 \\
        --capitals 100,1000,10000,50000 \\
        --output reports/capital_sweep.html
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.agents.strategies.backtest_runner import BacktestRunner, BacktestConfig
from app.agents.strategies.engine import ORBFVGEngine, ORBKPICalculator
from app.services.intraday_repository import intraday_repository

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os


async def run_one(symbol: str, start: str, end: str, capital: float) -> dict:
    runner = BacktestRunner(
        strategy=ORBFVGEngine(),
        repository=intraday_repository,
        kpi_calc=ORBKPICalculator(),
    )
    cfg = BacktestConfig(
        symbol=symbol,
        start_date=start,
        end_date=end,
        account_size=capital,
        strategy_name="ORB_FVG_ENGULFING",
        run_bootstrap=False,
    )
    result = await runner.run(cfg)
    s = result.summary()
    # Build equity curve (normalized to %)
    equity_pct = []
    running = capital
    for t in result.trades:
        prev = running
        running += t.pnl_usd
        equity_pct.append(round((running - capital) / capital * 100, 4))
    s["_equity_pct_curve"] = equity_pct
    s["_trade_labels"] = [f"T{i+1}" for i in range(len(result.trades))]
    return s


async def main():
    parser = argparse.ArgumentParser(description="Capital Sweep — compare backtest results across capital levels")
    parser.add_argument("--symbol", type=str, default="TSLA")
    parser.add_argument("--start", type=str, default="2025-03-21")
    parser.add_argument("--end", type=str, default="2026-03-05")
    parser.add_argument("--capitals", type=str, default="100,1000,10000,50000",
                        help="Comma-separated list of initial capitals to test")
    parser.add_argument("--output", type=str, default="reports/capital_sweep.html")
    args = parser.parse_args()

    capitals = [float(c.strip()) for c in args.capitals.split(",")]

    print(f"\n{'='*80}")
    print(f"  Capital Sweep: {args.symbol}  |  {args.start} → {args.end}")
    print(f"  Capitals: {capitals}")
    print(f"{'='*80}")
    print()

    results = []
    for cap in capitals:
        print(f"  Running with capital = ${cap:>10,.2f} ...", end=" ", flush=True)
        s = await run_one(args.symbol, args.start, args.end, cap)
        results.append(s)
        print(f"done. trades={s['total_trades']}  net_pnl_pct={s['net_pnl_pct']:.4f}%  total_R={s['total_r']:.4f}")

    # ── Print Comparison Table ──────────────────────────────────────────────
    col_w = 14
    headers = ["Capital($)", "Lots/Trade*", "Risk$/Trade", "AvgRisk(pts)", "Trades", "WinRate%", "PF", "TotalR", "NetPnL($)", "NetPnL%", "CAGR%", "Sharpe", "MaxDD%"]
    print()
    print(f"{'─'*len(headers)*col_w}")
    hdr_line = "".join(h.rjust(col_w) for h in headers)
    print(hdr_line)
    print(f"{'─'*len(headers)*col_w}")

    for s in results:
        row = [
            f"${s['account_size']:,.0f}",
            f"{s['avg_lots_per_trade']:.4f}",
            f"${s['risk_per_trade_usd']:.2f}",
            f"{s['avg_risk_pips']:.4f}",
            str(s['total_trades']),
            f"{s['win_rate']*100:.2f}%",
            f"{s['profit_factor']:.4f}",
            f"{s['total_r']:.4f}",
            f"${s['net_pnl_usd']:,.2f}",
            f"{s['net_pnl_pct']:.4f}%",
            f"{s['cagr']*100:.2f}%",
            f"{s['sharpe_ratio']:.4f}",
            f"{s['max_drawdown_pct']*100:.2f}%",
        ]
        print("".join(v.rjust(col_w) for v in row))

    print(f"{'─'*len(headers)*col_w}")
    print()
    print("* Lots/Trade = avg shares or units per trade  (equity = USD/share, pip_value=$1.00)")
    print("  NetPnL%, TotalR, WinRate, PF, CAGR, Sharpe, MaxDD% must be identical across")
    print("  all capital levels — they are CAPITAL-NEUTRAL metrics.")
    print()

    print("Explanation of position sizing:")
    print("  lots = (capital × risk_pct) / (entry_to_stop_distance × pip_value)")
    print("  For TSLA @ $250 entry, stop at $247 (risk_pips=$3.00), capital=$1000, risk_pct=0.5%:")
    ex_capital = 1000.0
    ex_risk_pct = 0.005
    ex_risk_pips = 3.0
    ex_pip_value = 1.0
    ex_lots = (ex_capital * ex_risk_pct) / (ex_risk_pips * ex_pip_value)
    print(f"    lots = ({ex_capital} × {ex_risk_pct}) / ({ex_risk_pips} × {ex_pip_value}) = {ex_lots:.2f} shares")
    print(f"    risk_amount = ${ex_capital * ex_risk_pct:.2f}  (${ex_risk_pct*100:.1f}% of capital)")
    print(f"    TP profit   = ${ex_capital * ex_risk_pct * 3:.2f}  (+3R)")
    print(f"    SL loss     = ${ex_capital * ex_risk_pct:.2f}   (-1R)")

    # ── Plotly Charts ───────────────────────────────────────────────────────
    print("\nGenerating charts...")
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            "Equity Curve (% of Capital) — all capitals must overlap",
            "Net PnL % by Capital Level",
            "Position Size (Lots) vs Capital",
            "Capital-Neutral KPIs by Level"
        )
    )

    colors = ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]
    for i, s in enumerate(results):
        cap_label = f"${s['account_size']:,.0f}"
        color = colors[i % len(colors)]
        curve = s.get("_equity_pct_curve", [])
        labels = s.get("_trade_labels", [])

        # Equity curve overlay
        fig.add_trace(go.Scatter(
            x=labels, y=curve, mode="lines",
            name=cap_label, line=dict(color=color, width=2)
        ), row=1, col=1)

        # Bar: net_pnl_pct
        fig.add_trace(go.Bar(
            x=[cap_label], y=[s["net_pnl_pct"]], name=cap_label,
            marker_color=color, showlegend=False
        ), row=1, col=2)

        # Bar: avg_lots
        fig.add_trace(go.Bar(
            x=[cap_label], y=[s["avg_lots_per_trade"]], name=cap_label,
            marker_color=color, showlegend=False
        ), row=2, col=1)

    # Capital-neutral KPIs bar chart
    kpi_names = ["win_rate", "profit_factor", "sharpe_ratio"]
    kpi_labels = ["Win Rate", "Profit Factor", "Sharpe"]
    for j, (kn, kl) in enumerate(zip(kpi_names, kpi_labels)):
        fig.add_trace(go.Bar(
            x=[f"${s['account_size']:,.0f}" for s in results],
            y=[s[kn] for s in results],
            name=kl,
        ), row=2, col=2)

    fig.update_yaxes(title_text="Equity Change (%)", row=1, col=1)
    fig.update_yaxes(title_text="Net PnL (%)", row=1, col=2)
    fig.update_yaxes(title_text="Avg Lots (shares)", row=2, col=1)

    fig.update_layout(
        height=750,
        title_text=f"Capital Sweep Analysis — {args.symbol}  |  {args.start} → {args.end}",
        barmode="group",
    )

    out_dir = Path(args.output).parent
    if not out_dir.is_absolute():
        out_dir = Path(__file__).resolve().parent.parent / out_dir
    os.makedirs(out_dir, exist_ok=True)
    out_file = out_dir / Path(args.output).name
    fig.write_html(str(out_file))

    print(f"Charts saved to: {out_file.absolute()}")


if __name__ == "__main__":
    asyncio.run(main())
