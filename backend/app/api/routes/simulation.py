"""
Simulation Routes (simulation.py)
===================================
FastAPI router for backtest and live signal endpoints.

Follows the same style as analytics.py and market_data.py:
  - APIRouter with prefix registered in main.py.
  - Pydantic models for request/response validation.
  - HTTPException for clean error handling.
  - All heavy lifting delegated to SimulationService (Façade).
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List
import logfire

from ...services.simulation_service import simulation_service

router = APIRouter()


# --------------------------------------------------------------------------- #
#  Request / Response Schemas                                                  #
# --------------------------------------------------------------------------- #

class StrategyParamsRequest(BaseModel):
    """Optional override for any strategy parameter. All are optional."""
    min_range_pips: Optional[float] = None
    vol_ruptura_ratio: Optional[float] = None
    p_cuerpo_min: Optional[float] = None
    p_vol_min: Optional[float] = None
    min_fvg_size_atr: Optional[float] = None
    wait_retest_max_m1: Optional[int] = None
    rr_target: Optional[float] = None
    buffer_sl_factor: Optional[float] = None
    risk_per_trade: Optional[float] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.model_dump().items() if v is not None}


class SimulationRequest(BaseModel):
    symbol: str = Field(..., example="AAPL")
    start_date: str = Field(..., example="2025-11-01")
    end_date: str = Field(..., example="2025-11-30")
    account_size: float = Field(default=10_000.0, gt=0)
    strategy_name: str = Field(default="ORB_FVG_ENGULFING")
    strategy_params: Optional[StrategyParamsRequest] = None
    pip_value: float = Field(default=1.0, gt=0)
    run_bootstrap: bool = Field(default=False)
    bootstrap_iterations: int = Field(default=1000, gt=0)


class TradeRecordResponse(BaseModel):
    signal_id: str
    timestamp: str
    direction: str
    entry: float
    stop: float
    tp: float
    outcome: str
    pnl_r: float
    pnl_usd: float


class SimulationRunResponse(BaseModel):
    sim_id: str
    symbol: str
    strategy: str
    kpis: dict
    trading_days: int
    total_trades: int
    bootstrap: Optional[dict] = None
    report_url: Optional[str] = None


class SimulationDetailResponse(BaseModel):
    sim_id: str
    summary: dict
    trades: List[TradeRecordResponse]


# --------------------------------------------------------------------------- #
#  Endpoints                                                                   #
# --------------------------------------------------------------------------- #

@router.post("/run", response_model=SimulationRunResponse, status_code=202)
async def run_simulation(request: SimulationRequest):
    """
    Run a full backtest simulation for a given symbol and date range.

    - Downloads M1 + M5 intraday candles (cached in DuckDB after first run).
    - Applies the ORB FVG Engulfing strategy session by session.
    - Returns KPIs: win_rate, expectancy, profit_factor, max_drawdown, sharpe, CAGR.
    """
    if request.start_date >= request.end_date:
        raise HTTPException(status_code=400, detail="start_date must be before end_date")

    params = request.strategy_params.to_dict() if request.strategy_params else {}

    try:
        sim_id, result = await simulation_service.run_backtest(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            account_size=request.account_size,
            strategy_name=request.strategy_name,
            strategy_params=params,
            pip_value=request.pip_value,
            run_bootstrap=request.run_bootstrap,
            bootstrap_iterations=request.bootstrap_iterations,
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logfire.error(f"Simulation failed: {e}")
        raise HTTPException(status_code=500, detail=f"Simulation error: {str(e)}")

    report_url = None
    if result.report_path:
        report_url = f"http://localhost:8282/view-reports/{result.report_path}"

    return SimulationRunResponse(
        sim_id=sim_id,
        symbol=request.symbol,
        strategy=request.strategy_name,
        kpis=result.kpis.as_dict(),
        trading_days=result.trading_days,
        total_trades=result.kpis.total_trades,
        bootstrap=result.bootstrap_stats if result.bootstrap_stats else None,
        report_url=report_url
    )


@router.get("/results/{sim_id}", response_model=SimulationDetailResponse)
async def get_simulation_result(sim_id: str):
    """
    Retrieve the full result of a previously executed backtest, including trade-level detail.
    """
    result = simulation_service.get_result(sim_id)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Simulation '{sim_id}' not found.")

    trades_out = [
        TradeRecordResponse(
            signal_id=t.signal.signal_id,
            timestamp=t.signal.timestamp,
            direction=t.signal.direction,
            entry=t.signal.entry,
            stop=t.signal.stop,
            tp=t.signal.tp,
            outcome=t.outcome,
            pnl_r=t.pnl_r,
            pnl_usd=t.pnl_usd,
        )
        for t in result.trades
    ]

    return SimulationDetailResponse(
        sim_id=sim_id,
        summary=result.summary(),
        trades=trades_out,
    )


@router.get("/results")
async def list_simulations():
    """List all simulation runs stored in the current session."""
    return simulation_service.list_simulations()


@router.get("/signal/live")
async def get_live_signal(
    symbol: str = Query(..., example="AAPL"),
    strategy: str = Query(default="ORB_FVG_ENGULFING"),
    account_size: float = Query(default=10_000.0, gt=0),
):
    """
    Run the strategy engine on today's live intraday candles.
    Returns a TradeSignal if a valid setup is detected, or reason for no signal.

    Note: M1 data from Yahoo Finance is only available for the last 7 days.
    """
    try:
        result = await simulation_service.get_live_signal(
            symbol=symbol,
            strategy_name=strategy,
            account_size=account_size,
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logfire.error(f"Live signal error: {e}")
        raise HTTPException(status_code=500, detail=f"Live signal error: {str(e)}")


@router.get("/strategies")
async def list_strategies():
    """Return all registered strategy names (for frontend dropdown)."""
    from ...agents.strategies.engine import StrategyFactory
    return {"strategies": StrategyFactory.available()}
