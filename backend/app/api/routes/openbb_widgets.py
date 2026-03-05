from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
import json
from pathlib import Path
from datetime import datetime, timezone

from ...core.container import duckdb_repo, calculate_equity_curve_uc
from ...services.risk_service import risk_service
from ...services.standardizer import standardizer

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

@router.get("/widgets.json")
async def get_widgets():
    path = BASE_DIR / "widgets.json"
    if not path.exists(): return JSONResponse(content={"error": "widgets.json not found"}, status_code=404)
    with open(path, "r") as f: return JSONResponse(content=json.load(f))

@router.get("/apps.json")
async def get_apps():
    path = BASE_DIR / "apps.json"
    if not path.exists(): return JSONResponse(content={"error": "apps.json not found"}, status_code=404)
    with open(path, "r") as f: return JSONResponse(content=json.load(f))

@router.get("/widgets/portfolio")
async def widget_portfolio():
    holdings = duckdb_repo.get_portfolio()
    total_val = sum(h['shares'] * h['entryPrice'] for h in holdings) if holdings else 0
    return standardizer.to_openbb_metric("Current Portfolio Value", f"${total_val:,.2f}", change="+0.0%", is_positive=True)

@router.get("/widgets/sentiment")
async def widget_sentiment():
    holdings = duckdb_repo.get_portfolio()
    risk_report = risk_service.get_portfolio_risk_report(holdings)
    if "error" in risk_report: body = "Sentiment analysis currently unavailable — insufficient market data."
    else:
        var = risk_report.get('mvar_95_percent', 0)
        sharpe = risk_report.get('sharpe_ratio', 0)
        status = "BULLISH" if sharpe > 1 else ("NEUTRAL" if sharpe > 0 else "CAUTIOUS")
        body = f"**Current Stance:** {status}\n\n**Risk Metrics:**\n- Modified VaR (95%): {var}%\n- Portfolio Sharpe: {sharpe}\n- Data Coverage: {risk_report.get('coverage_percent')}%"
    return standardizer.to_openbb_text("MMAM Neural Sentiment", body)

@router.get("/widgets/trades")
async def widget_trades():
    txs = duckdb_repo.get_transactions()
    recent = txs[-10:] if txs else []
    formatted = [{"Date": t.get("date"), "Symbol": t.get("symbol"), "Type": t.get("type"), "Quantity": t.get("shares"), "Price": f"${t.get('price', 0):,.2f}", "PnL": f"${t.get('realized_pnl', 0):,.2f}"} for t in recent]
    return standardizer.to_openbb_table(formatted)

# ─── Manager Widgets ─────────────────────────────────────────────────────────

@router.get("/widgets/aum")
async def widget_aum():
    """Manager: Total AUM metric with daily change."""
    holdings = duckdb_repo.get_portfolio()
    if not holdings:
        return standardizer.to_openbb_metric("Total AUM", "$0.00", change="0.00%", is_positive=True)

    total_cost  = sum(h["shares"] * h["entryPrice"] * h.get("factor", 1.0) for h in holdings)
    total_mkt   = sum(h["shares"] * h.get("price", h["entryPrice"]) * h.get("factor", 1.0) for h in holdings)
    total_pnl   = total_mkt - total_cost
    pct_change  = (total_pnl / total_cost * 100) if total_cost else 0

    snapshots  = calculate_equity_curve_uc.execute(days=2)
    day_change = pct_change
    if isinstance(snapshots, list) and len(snapshots) >= 2:
        prev = snapshots[-2].get("total", total_cost)
        curr = snapshots[-1].get("total", total_mkt)
        day_change = ((curr - prev) / prev * 100) if prev else 0

    return standardizer.to_openbb_metric(
        label="Total AUM",
        value=f"${total_mkt:,.2f}",
        change=f"{day_change:+.2f}%",
        is_positive=day_change >= 0,
    )

@router.get("/widgets/allocation")
async def widget_allocation():
    """Manager: Portfolio allocation table grouped by sector."""
    holdings = duckdb_repo.get_portfolio()
    if not holdings:
        return standardizer.to_openbb_table([])

    total_mkt = sum(
        h["shares"] * h.get("price", h["entryPrice"]) * h.get("factor", 1.0)
        for h in holdings
    ) or 1.0

    sector_map: dict[str, dict] = {}
    for h in holdings:
        sector  = h.get("sector", "Other")
        mkt_val = h["shares"] * h.get("price", h["entryPrice"]) * h.get("factor", 1.0)
        cost    = h["shares"] * h["entryPrice"] * h.get("factor", 1.0)
        if sector not in sector_map:
            sector_map[sector] = {"market_value": 0.0, "cost": 0.0, "count": 0}
        sector_map[sector]["market_value"] += mkt_val
        sector_map[sector]["cost"]         += cost
        sector_map[sector]["count"]        += 1

    rows = []
    for sector, data in sorted(sector_map.items(), key=lambda x: -x[1]["market_value"]):
        pnl  = data["market_value"] - data["cost"]
        pct  = data["market_value"] / total_mkt * 100
        rows.append({
            "Sector":      sector,
            "Positions":   data["count"],
            "Market Value": f"${data['market_value']:,.2f}",
            "Allocation":  f"{pct:.1f}%",
            "P&L":         f"${pnl:+,.2f}",
        })
    return standardizer.to_openbb_table(rows)

@router.get("/widgets/risk")
async def widget_risk():
    """Manager: Risk dashboard — VaR, CVaR, Sharpe, max drawdown."""
    holdings = duckdb_repo.get_portfolio()
    if not holdings:
        return standardizer.to_openbb_text("Risk Dashboard", "_No holdings to analyze._")

    report = risk_service.get_portfolio_risk_report(holdings)
    if "error" in report:
        return standardizer.to_openbb_text("Risk Dashboard", f"⚠️ {report['error']}")

    var     = report.get("mvar_95_percent", report.get("var_95_percent", 0))
    cvar    = report.get("cvar_95_percent", 0)
    sharpe  = report.get("sharpe_ratio", 0)
    cov     = report.get("coverage_percent", 0)

    snapshots = calculate_equity_curve_uc.execute(days=365)
    max_dd    = 0.0
    if isinstance(snapshots, list) and snapshots:
        equities = [s.get("total", 0) for s in snapshots]
        peak     = equities[0]
        for e in equities:
            peak   = max(peak, e)
            dd     = (peak - e) / peak * 100 if peak else 0
            max_dd = max(max_dd, dd)

    stance = "🟢 BULLISH" if sharpe > 1 else ("🟡 NEUTRAL" if sharpe > 0 else "🔴 CAUTIOUS")

    body = (
        f"**Stance:** {stance}  |  **Data Coverage:** {cov:.0f}%\n\n"
        f"| Metric | Value |\n"
        f"|--------|-------|\n"
        f"| Modified VaR (95%) | {var:.2f}% |\n"
        f"| CVaR / Expected Shortfall | {cvar:.2f}% |\n"
        f"| Sharpe Ratio | {sharpe:.3f} |\n"
        f"| Max Drawdown (1Y) | -{max_dd:.2f}% |\n"
    )
    return standardizer.to_openbb_text("Portfolio Risk Report", body)

@router.get("/widgets/equity-curve")
async def widget_equity_curve():
    """Manager: Equity curve history as a table (total vs realized)."""
    snapshots = calculate_equity_curve_uc.execute(days=365)
    if not isinstance(snapshots, list) or not snapshots:
        return standardizer.to_openbb_table([])

    rows = [
        {
            "Date":         datetime.fromtimestamp(s["time"], tz=timezone.utc).strftime("%Y-%m-%d"),
            "Total Equity": f"${s.get('total', 0):,.2f}",
            "Realized":     f"${s.get('realized', 0):,.2f}",
        }
        for s in snapshots[-90:]  # last 90 data points
    ]
    return standardizer.to_openbb_table(rows)

# ─── Client Widgets ───────────────────────────────────────────────────────────

@router.get("/widgets/client/portfolio")
async def widget_client_portfolio(client_id: str = Query(default="default")):
    """Client: Open positions table with live P&L per holding."""
    holdings = duckdb_repo.get_portfolio()
    if not holdings:
        return standardizer.to_openbb_table([])

    rows = []
    for h in holdings:
        cost    = h["shares"] * h["entryPrice"] * h.get("factor", 1.0)
        mkt_val = h["shares"] * h.get("price", h["entryPrice"]) * h.get("factor", 1.0)
        pnl     = mkt_val - cost
        pnl_pct = (pnl / cost * 100) if cost else 0
        rows.append({
            "Symbol":       h["symbol"],
            "Name":         h.get("name", ""),
            "Sector":       h.get("sector", ""),
            "Shares":       f"{h['shares']:,.4f}",
            "Entry Price":  f"${h['entryPrice']:,.4f}",
            "Market Value": f"${mkt_val:,.2f}",
            "P&L":          f"${pnl:+,.2f}",
            "P&L %":        f"{pnl_pct:+.2f}%",
            "Type":         h.get("type", ""),
        })
    return standardizer.to_openbb_table(rows)

@router.get("/widgets/client/pnl")
async def widget_client_pnl(client_id: str = Query(default="default")):
    """Client: Realized P&L history from transactions."""
    txs = duckdb_repo.get_transactions()
    if not txs:
        return standardizer.to_openbb_table([])

    rows = [
        {
            "Date":      t.get("date", ""),
            "Time":      t.get("time", ""),
            "Symbol":    t.get("symbol", ""),
            "Side":      t.get("type", "").upper(),
            "Qty":       f"{t.get('shares', 0):,.4f}",
            "Price":     f"${t.get('price', 0):,.2f}",
            "Realized P&L": f"${t.get('realized_pnl', 0):+,.2f}",
        }
        for t in reversed(txs[-50:])
    ]
    return standardizer.to_openbb_table(rows)

@router.get("/widgets/client/summary")
async def widget_client_summary(client_id: str = Query(default="default")):
    """Client: Portfolio summary metrics: total value, unrealized PnL, top holding."""
    holdings = duckdb_repo.get_portfolio()
    if not holdings:
        return standardizer.to_openbb_text("Portfolio Summary", "_No holdings found._")

    total_cost = sum(h["shares"] * h["entryPrice"] * h.get("factor", 1.0) for h in holdings)
    total_mkt  = sum(h["shares"] * h.get("price", h["entryPrice"]) * h.get("factor", 1.0) for h in holdings)
    unrealized = total_mkt - total_cost
    pct        = (unrealized / total_cost * 100) if total_cost else 0

    top = max(holdings, key=lambda h: h["shares"] * h.get("price", h["entryPrice"]) * h.get("factor", 1.0))
    top_val = top["shares"] * top.get("price", top["entryPrice"]) * top.get("factor", 1.0)
    top_pct = (top_val / total_mkt * 100) if total_mkt else 0

    txs       = duckdb_repo.get_transactions()
    realized  = sum(t.get("realized_pnl", 0) for t in txs)

    body = (
        f"| | |\n|---|---|\n"
        f"| **Portfolio Value** | ${total_mkt:,.2f} |\n"
        f"| **Unrealized P&L** | ${unrealized:+,.2f} ({pct:+.2f}%) |\n"
        f"| **Realized P&L** | ${realized:+,.2f} |\n"
        f"| **Open Positions** | {len(holdings)} |\n"
        f"| **Largest Position** | {top['symbol']} ({top_pct:.1f}%) |\n"
    )
    return standardizer.to_openbb_text("Portfolio Summary", body)
