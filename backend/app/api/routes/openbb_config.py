from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
from pathlib import Path
from ...core.container import duckdb_repo
from ...services.risk_service import risk_service
from ...services.standardizer import standardizer

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

@router.get("/widgets.json")
async def get_widgets():
    """Expose widgets configuration for OpenBB Workspace."""
    path = BASE_DIR / "widgets.json"
    if not path.exists():
        return JSONResponse(content={"error": "widgets.json not found"}, status_code=404)
    with open(path, "r") as f:
        return JSONResponse(content=json.load(f))

@router.get("/apps.json")
async def get_apps():
    """Expose apps configuration for OpenBB Workspace."""
    path = BASE_DIR / "apps.json"
    if not path.exists():
        return JSONResponse(content={"error": "apps.json not found"}, status_code=404)
    with open(path, "r") as f:
        return JSONResponse(content=json.load(f))

# Helper endpoints for the widgets defined in widgets.json

@router.get("/widgets/portfolio")
async def widget_portfolio():
    """Data for the Portfolio Overview widget."""
    holdings = duckdb_repo.get_portfolio()
    # Basic math for total value (using entry prices as placeholder for live)
    total_val = sum(h['shares'] * h['entryPrice'] for h in holdings) if holdings else 0
    
    return standardizer.to_openbb_metric(
        "Current Portfolio Value",
        f"${total_val:,.2f}",
        change="+0.0%",  # Needs live price integration for real delta
        is_positive=True
    )

@router.get("/widgets/sentiment")
async def widget_sentiment():
    """Data for the Market Sentiment widget."""
    holdings = duckdb_repo.get_portfolio()
    risk_report = risk_service.get_portfolio_risk_report(holdings)
    
    if "error" in risk_report:
        body = "Sentiment analysis currently unavailable — insufficient market data."
    else:
        var = risk_report.get('mvar_95_percent', 0)
        sharpe = risk_report.get('sharpe_ratio', 0)
        status = "BULLISH" if sharpe > 1 else ("NEUTRAL" if sharpe > 0 else "CAUTIOUS")
        
        body = (
            f"**Current Stance:** {status}\n\n"
            f"**Risk Metrics:**\n"
            f"- Modified VaR (95%): {var}%\n"
            f"- Portfolio Sharpe: {sharpe}\n"
            f"- Data Coverage: {risk_report.get('coverage_percent')}%"
        )
    
    return standardizer.to_openbb_text("MMAM Neural Sentiment", body)

@router.get("/widgets/trades")
async def widget_trades():
    """Data for the Recent Trading Activity widget."""
    txs = duckdb_repo.get_transactions()
    # Sort and slice to last 10
    recent = txs[-10:] if txs else []
    
    # Capitalize keys for OpenBB table display
    formatted = []
    for t in recent:
        formatted.append({
            "Date": t.get("date"),
            "Symbol": t.get("symbol"),
            "Type": t.get("type"),
            "Quantity": t.get("shares"),
            "Price": f"${t.get('price', 0):,.2f}",
            "PnL": f"${t.get('realized_pnl', 0):,.2f}"
        })
        
    return standardizer.to_openbb_table(formatted)
