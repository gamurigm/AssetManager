from fastapi import APIRouter, Body, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from ...services.report_service import report_service
from ...services.risk_service import risk_service
from ...services.portfolio_backtest_service import portfolio_backtest_service
from ...services.portfolio_policy_service import portfolio_policy_service
from ...services.portfolio_rebalance_service import portfolio_rebalance_service

from ...core.container import duckdb_repo, calculate_equity_curve_uc

INITIAL_HOLDINGS = [
    { "symbol": "^N225", "name": "Nikkei 225 Index", "shares": 0.1, "entryPrice": 29600, "price": 0, "factor": 0.4166, "change": 0, "changePercent": 0, "source": "Live", "sector": "Indices", "type": "cfd", "purchaseDate": "2023-05-15" },
    { "symbol": "AAPL", "name": "Apple Inc CFD", "shares": 10, "entryPrice": 188.50, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Technology", "type": "cfd", "purchaseDate": "2024-02-10" },
    { "symbol": "PLTR", "name": "Palantir Technologies CFD", "shares": 10, "entryPrice": 24.19, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Technology", "type": "cfd", "purchaseDate": "2024-03-01" },
    { "symbol": "GC=F", "name": "Gold Futures", "shares": 0.1, "entryPrice": 1980.30, "price": 0, "factor": 84.397, "change": 0, "changePercent": 0, "source": "Live", "sector": "Commodities", "type": "cfd", "purchaseDate": "2023-11-20" },
    { "symbol": "JPM", "name": "JPMorgan Chase & Co", "shares": 1.536, "entryPrice": 122.81, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Financials", "type": "stock", "purchaseDate": "2022-08-14" },
    { "symbol": "COIN", "name": "Coinbase Global Inc", "shares": 2.724, "entryPrice": 34.93, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Digital Assets", "type": "stock", "purchaseDate": "2023-01-05" },
    { "symbol": "GS", "name": "Goldman Sachs Group Inc", "shares": 0.164, "entryPrice": 345.54, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Financials", "type": "stock", "purchaseDate": "2023-12-12" },
    { "symbol": "LMT", "name": "Lockheed Martin Corp", "shares": 0.214, "entryPrice": 425.70, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Industrials", "type": "stock", "purchaseDate": "2022-06-30" },
    { "symbol": "NVDA", "name": "NVIDIA Corp", "shares": 0.54, "entryPrice": 58.15, "price": 0, "factor": 1.0, "change": 0, "changePercent": 0, "source": "Live", "sector": "Technology", "type": "stock", "purchaseDate": "2024-01-20" },
    { "symbol": "CHFJPY=X", "name": "CHF/JPY", "shares": 0.5, "entryPrice": 172.071, "price": 0, "factor": 615.66, "change": 0, "changePercent": 0, "source": "Live", "sector": "Forex", "type": "cfd", "purchaseDate": "2024-05-02" },
    { "symbol": "ZT=F", "name": "US 2 Year T-Note", "shares": 0.1, "entryPrice": 101.57, "price": 0, "factor": 114.285, "change": 0, "changePercent": 0, "source": "Live", "sector": "Bonds", "type": "cfd", "purchaseDate": "2024-04-15" },
    { "symbol": "EURUSD=X", "name": "EUR/USD", "shares": -1.2, "entryPrice": 1.12519, "price": 0, "factor": 100000, "change": 0, "changePercent": 0, "source": "Live", "sector": "Forex", "type": "cfd", "purchaseDate": "2024-06-10" },
]

router = APIRouter()


class PortfolioBacktestAssetRequest(BaseModel):
    symbol: str = Field(..., examples=["AAPL"])
    weight: Optional[float] = Field(default=None, ge=0)
    factor: float = Field(default=1.0, gt=0)
    name: Optional[str] = Field(default=None)


class PortfolioBacktestRequest(BaseModel):
    start_date: str = Field(..., examples=["2024-01-02"])
    end_date: str = Field(..., examples=["2024-12-31"])
    initial_cash: float = Field(default=10_000.0, gt=0)
    portfolio_id: Optional[str] = Field(default=None, examples=["main"])
    assets: List[PortfolioBacktestAssetRequest] = Field(default_factory=list)
    rebalance_frequency: str = Field(default="none", examples=["none", "monthly"])
    fee_bps: float = Field(default=0.0, ge=0, le=500)
    execution_mode: str = Field(default="auto", examples=["auto", "remote", "cpp", "python"])


class PortfolioPolicyHoldingRequest(BaseModel):
    symbol: str = Field(..., examples=["AAPL"])
    name: Optional[str] = Field(default=None)
    shares: float = Field(...)
    price: float = Field(default=0.0)
    entryPrice: float = Field(default=0.0)
    factor: float = Field(default=1.0, gt=0)
    sector: Optional[str] = Field(default=None)
    type: Optional[str] = Field(default=None)
    purchaseDate: Optional[str] = Field(default=None)


class PortfolioPolicyRequest(BaseModel):
    portfolio_id: str = Field(default="main", examples=["main"])
    holdings: Optional[List[PortfolioPolicyHoldingRequest]] = Field(default=None)
    benchmark: str = Field(default="SPY", examples=["SPY"])
    lookback_days: int = Field(default=252, ge=30, le=756)
    risk_aversion: float = Field(default=0.35, ge=0, le=3)
    turnover_penalty: float = Field(default=0.08, ge=0, le=1)
    max_weight: float = Field(default=0.35, gt=0, le=1)
    gross_limit: float = Field(default=1.0, gt=0, le=2)


class PortfolioPolicyAllocationRequest(BaseModel):
    symbol: str = Field(..., examples=["AAPL"])
    price: float = Field(default=0.0)
    factor: float = Field(default=1.0, gt=0)
    delta_shares: float = Field(default=0.0)
    target_notional: Optional[float] = Field(default=None)
    action: Optional[str] = Field(default=None)


class PortfolioPolicyApplyRequest(BaseModel):
    portfolio_id: str = Field(default="main", examples=["main"])
    holdings: Optional[List[PortfolioPolicyHoldingRequest]] = Field(default=None)
    allocations: List[PortfolioPolicyAllocationRequest] = Field(default_factory=list)
    symbols: Optional[List[str]] = Field(default=None)
    trade_date: Optional[str] = Field(default=None)

@router.get("/")
def get_portfolios(portfolio_id: str = Query("main", description="Target portfolio to load")):
    """Load persisted portfolio from DuckDB. Fallback to INITIAL_HOLDINGS if empty and no history."""
    data = duckdb_repo.get_portfolio(portfolio_id)
    if not data:
        # Check if the user has trading history for this portfolio. If they do, they legitimately liquidated all positions.
        history = duckdb_repo.get_transactions(portfolio_id)
        if history and len(history) > 0:
            return [] # Legitimate empty portfolio
            
        # Optional: Seed main portfolio only
        if portfolio_id == "main":
            duckdb_repo.save_portfolio(INITIAL_HOLDINGS, portfolio_id)
            return INITIAL_HOLDINGS
        return []
    return data

@router.post("/save")
def save_portfolio(
    holdings: List[Dict[str, Any]] = Body(...),
    portfolio_id: str = Query("main", description="Target portfolio to save")
):
    """Persist current holdings to DuckDB."""
    success = duckdb_repo.save_portfolio(holdings, portfolio_id)
    return {"status": "success" if success else "failed"}


@router.post("/backtest")
async def run_portfolio_backtest(request: PortfolioBacktestRequest):
    """
    Buy a weighted basket on the first available trading day in the range and backtest it.

    Input can come either from:
      - `assets`: manual weighted basket
      - `portfolio_id`: current persisted holdings converted to long-only weights
    """
    if request.start_date >= request.end_date:
        raise HTTPException(status_code=400, detail="start_date must be before end_date")

    result = await portfolio_backtest_service.run_backtest(
        start_date=request.start_date,
        end_date=request.end_date,
        initial_cash=request.initial_cash,
        assets=[asset.model_dump(exclude_none=True) for asset in request.assets],
        portfolio_id=request.portfolio_id,
        rebalance_frequency=request.rebalance_frequency,
        fee_bps=request.fee_bps,
        execution_mode=request.execution_mode,
    )
    if "error" in result:
        detail = str(result["error"])
        status = 404 if "historical data" in detail.lower() else 422
        raise HTTPException(status_code=status, detail=detail)
    return result


@router.get("/backtest/engines")
async def get_portfolio_backtest_engines():
    """Describe which portfolio backtest execution engines are currently available."""
    return await portfolio_backtest_service.describe_execution_engines()


@router.post("/policy")
async def get_portfolio_policy(request: PortfolioPolicyRequest):
    """Continuous EV-maximizing policy snapshot for the live portfolio state."""
    snapshot = portfolio_policy_service.build_policy_snapshot(
        portfolio_id=request.portfolio_id,
        holdings=[holding.model_dump(exclude_none=True) for holding in request.holdings] if request.holdings else None,
        benchmark=request.benchmark,
        lookback_days=request.lookback_days,
        risk_aversion=request.risk_aversion,
        turnover_penalty=request.turnover_penalty,
        max_weight=request.max_weight,
        gross_limit=request.gross_limit,
    )
    if "error" in snapshot:
        detail = str(snapshot["error"])
        status = 404 if "history" in detail.lower() or "holdings" in detail.lower() else 422
        raise HTTPException(status_code=status, detail=detail)
    return snapshot


@router.post("/policy/apply")
async def apply_portfolio_policy(request: PortfolioPolicyApplyRequest):
    """Apply one or more live portfolio policy allocations to the persisted portfolio and record transactions."""
    result = portfolio_rebalance_service.apply_policy_rebalance(
        portfolio_id=request.portfolio_id,
        holdings=[holding.model_dump(exclude_none=True) for holding in request.holdings] if request.holdings else None,
        allocations=[allocation.model_dump(exclude_none=True) for allocation in request.allocations],
        symbols=request.symbols,
        trade_date=request.trade_date,
    )
    if "error" in result:
        raise HTTPException(status_code=422, detail=str(result["error"]))
    return result

@router.get("/risk")
def get_portfolio_risk(portfolio_id: str = Query("main", description="Target portfolio")):
    """Live portfolio risk metrics: VaR, Volatility, Sharpe, Drawdown, etc."""
    holdings = duckdb_repo.get_portfolio(portfolio_id)
    if not holdings:
        return {"error": "No holdings"}

    report = risk_service.get_portfolio_risk_report(holdings)
    if "error" in report:
        return report

    # Calculate max drawdown from equity snapshots
    max_dd = 0.0
    try:
        snapshots = calculate_equity_curve_uc.execute(days=365, portfolio_id=portfolio_id)
        if isinstance(snapshots, list) and snapshots:
            equities = [s.get("total", 0) for s in snapshots]
            peak = equities[0]
            for e in equities:
                peak = max(peak, e)
                dd = (peak - e) / peak * 100 if peak else 0
                max_dd = max(max_dd, dd)
    except Exception:
        pass

    report["max_drawdown"] = round(max_dd, 2)
    return report

@router.post("/report")
async def generate_portfolio_report(
    holdings: List[Dict[str, Any]] = Body(...),
    total_value: float = Body(0),
    total_pnl: float = Body(0),
    type: str = Body("standard"),
    intelligence_text: str = Body("")
):
    """
    Generate different types of institutional reports.
    Types: 'standard', 'executive', 'risk', 'intelligence'
    """
    if type == "executive":
        filename = report_service.generate_executive_summary(holdings, intelligence_text)
    elif type == "risk":
        filename = report_service.generate_risk_audit(holdings)
    elif type == "intelligence":
        filename = report_service.generate_custom_intelligence_report(intelligence_text, holdings, total_value, total_pnl)
    else:
        filename = report_service.generate_balance_sheet(holdings, total_value, total_pnl)
        
    report_url = f"http://localhost:8282/view-reports/{filename}"
    return {"url": report_url, "filename": filename, "type": type}

@router.post("/snapshot-equity")
def snapshot_equity(
    total_value: float = Body(..., embed=True),
    portfolio_id: str = Query("main", description="Target portfolio")
):
    """Record current total balance and realized balance."""
    success = duckdb_repo.record_equity_snapshot(total_value, portfolio_id)
    return {"status": "success" if success else "failed"}

@router.get("/history")
def get_equity_history(portfolio_id: str = Query("main", description="Target portfolio")):
    """Retrieve dynamic equity history (realized vs total) for charts."""
    return calculate_equity_curve_uc.execute(days=730, portfolio_id=portfolio_id)

