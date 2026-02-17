    from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import json
from pathlib import Path
from typing import List, Dict, Any

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
    return {
        "metric": "Current Portfolio Value",
        "value": "$1,245,670.00",
        "change": "+2.4%",
        "isPositive": True
    }

@router.get("/widgets/sentiment")
async def widget_sentiment():
    """Data for the Market Sentiment widget."""
    return {
        "markdown": "## Market Analysis\n\n**Current Stance:** Bullish/Neutral\n\n**Key Factors:**\n- Tech sector continues to show resilience.\n- Fed rate cut expectations are priced in.\n- NVIDIA performance is driving AI-related stocks.\n\n*Last updated by Fundamental Agent at 14:30*"
    }

@router.get("/widgets/trades")
async def widget_trades():
    """Data for the Recent Trading Activity widget."""
    return [
        {"Symbol": "AAPL", "Type": "BUY", "Quantity": 100, "Price": "$178.50", "Status": "Success"},
        {"Symbol": "NVDA", "Type": "BUY", "Quantity": 50, "Price": "$870.20", "Status": "Success"},
        {"Symbol": "TSLA", "Type": "SELL", "Quantity": 20, "Price": "$245.10", "Status": "Success"},
        {"Symbol": "MSFT", "Type": "BUY", "Quantity": 30, "Price": "$410.00", "Status": "Pending"}
    ]
