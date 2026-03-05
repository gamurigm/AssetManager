"""
FMP API Routes — Financial Modeling Prep fundamentals & analytics endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from ...services.fmp_service import fmp_service

router = APIRouter()


@router.get("/income-statement/{symbol}")
async def get_income_statement(
    symbol: str,
    period: str = Query("annual", description="annual or quarter"),
    limit: int = Query(5, description="Number of periods"),
):
    """Get income statements for a company."""
    data = await fmp_service.get_income_statement(symbol, period, limit)
    if not data:
        raise HTTPException(status_code=404, detail=f"No income statement data for {symbol}")
    return data


@router.get("/balance-sheet/{symbol}")
async def get_balance_sheet(
    symbol: str,
    period: str = Query("annual", description="annual or quarter"),
    limit: int = Query(5, description="Number of periods"),
):
    """Get balance sheet statements for a company."""
    data = await fmp_service.get_balance_sheet(symbol, period, limit)
    if not data:
        raise HTTPException(status_code=404, detail=f"No balance sheet data for {symbol}")
    return data


@router.get("/key-metrics/{symbol}")
async def get_key_metrics(
    symbol: str,
    period: str = Query("annual", description="annual or quarter"),
    limit: int = Query(5, description="Number of periods"),
):
    """Get key financial metrics (PE, EV/EBITDA, ROE, etc.)."""
    data = await fmp_service.get_key_metrics(symbol, period, limit)
    if not data:
        raise HTTPException(status_code=404, detail=f"No key metrics for {symbol}")
    return data


@router.get("/ratios/{symbol}")
async def get_financial_ratios(
    symbol: str,
    period: str = Query("annual", description="annual or quarter"),
    limit: int = Query(5, description="Number of periods"),
):
    """Get financial ratios (profitability, liquidity, solvency)."""
    data = await fmp_service.get_financial_ratios(symbol, period, limit)
    if not data:
        raise HTTPException(status_code=404, detail=f"No financial ratios for {symbol}")
    return data
