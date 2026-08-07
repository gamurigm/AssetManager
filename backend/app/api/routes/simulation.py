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

from datetime import date
import re

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from typing import Literal, Optional, List
import logfire

from ...agents.strategies.backtest_runner import BacktestConfig
from ...agents.strategies.engine import StrategyFactory
from ...services.simulation_service import simulation_service

router = APIRouter()


# --------------------------------------------------------------------------- #
#  Request / Response Schemas                                                  #
# --------------------------------------------------------------------------- #

class StrategyParamsRequest(BaseModel):
    """Optional override for any strategy parameter. All are optional."""
    model_config = ConfigDict(extra="forbid")

    min_range_pips: Optional[float] = Field(default=None, ge=0)
    vol_ruptura_ratio: Optional[float] = Field(default=None, gt=0, le=10)
    body_ratio_breakout: Optional[float] = Field(default=None, ge=0, le=1)
    min_fvg_size_atr: Optional[float] = Field(default=None, ge=0, le=10)
    wait_fvg_max_m1: Optional[int] = Field(default=None, ge=1, le=240)
    k1_atr_fcr: Optional[float] = Field(default=None, ge=0, le=10)
    k2_body_ratio: Optional[float] = Field(default=None, ge=0, le=1)
    k3_vol_ratio_fcr: Optional[float] = Field(default=None, ge=0, le=10)
    p_cuerpo_min: Optional[float] = Field(default=None, ge=0, le=10)
    p_vol_min: Optional[float] = Field(default=None, ge=0, le=10)
    wait_retest_max_m1: Optional[int] = Field(default=None, ge=1, le=240)
    rr_target: Optional[float] = Field(default=None, gt=0, le=20)
    buffer_sl_factor: Optional[float] = Field(default=None, ge=0, le=5)
    max_spread: Optional[float] = Field(default=None, ge=0)
    swing_lookback: Optional[int] = Field(default=None, ge=1, le=240)
    risk_per_trade: Optional[float] = Field(default=None, gt=0, le=0.05)
    max_trades_per_day: Optional[int] = Field(default=None, ge=1, le=20)
    max_concurrent_trades: Optional[int] = Field(default=None, ge=1, le=1)
    max_daily_losses: Optional[int] = Field(default=None, ge=1, le=20)
    max_daily_drawdown_pct: Optional[float] = Field(default=None, gt=0, le=1)
    max_monthly_drawdown_pct: Optional[float] = Field(default=None, gt=0, le=1)

    def to_dict(self) -> dict:
        return {k: v for k, v in self.model_dump().items() if v is not None}


class SimulationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    symbol: str = Field(..., examples=["AAPL"])
    start_date: str = Field(..., examples=["2025-11-01"])
    end_date: str = Field(..., examples=["2025-11-30"])
    account_size: float = Field(default=10_000.0, gt=0)
    strategy_name: str = Field(default="ORB_FVG_ENGULFING")
    strategy_params: Optional[StrategyParamsRequest] = None
    pip_value: float = Field(default=1.0, gt=0)
    fixed_slippage_price: float = Field(default=0.0, ge=0)
    commission_per_trade: float = Field(default=0.0, ge=0)
    intrabar_fill_policy: Literal["conservative", "optimistic"] = "conservative"
    mark_expired_to_market: bool = True
    run_bootstrap: bool = Field(default=False)
    bootstrap_iterations: int = Field(default=1000, gt=0, le=100_000)
    debug_lookbehind_guard: bool = Field(default=False)
    use_atr_slippage: bool = Field(default=False)
    atr_slippage_factor: float = Field(default=0.20, ge=0, le=5)

    @field_validator("symbol")
    @classmethod
    def normalize_symbol(cls, value: str) -> str:
        normalized = value.strip().upper()
        if not re.fullmatch(r"[A-Z0-9._=-]{1,32}", normalized):
            raise ValueError("symbol contains unsupported characters")
        return normalized

    @field_validator("strategy_name")
    @classmethod
    def normalize_strategy_name(cls, value: str) -> str:
        normalized = value.strip().upper()
        if not re.fullmatch(r"[A-Z0-9_]{2,64}", normalized):
            raise ValueError("strategy_name contains unsupported characters")
        return normalized

    @model_validator(mode="after")
    def validate_date_range(self):
        try:
            start = date.fromisoformat(self.start_date)
            end = date.fromisoformat(self.end_date)
        except ValueError as exc:
            raise ValueError("start_date and end_date must use YYYY-MM-DD") from exc
        if start >= end:
            raise ValueError("start_date must be before end_date")
        return self


class TradeRecordResponse(BaseModel):
    signal_id: str
    timestamp: str
    direction: str
    entry: float
    stop: float
    tp: float
    exit_price: Optional[float] = None
    exit_timestamp: Optional[str] = None
    outcome: str
    pnl_r: float
    pnl_usd: float
    gross_pnl_usd: float
    fees_usd: float
    entry_price: Optional[float] = None
    execution_note: str = ""


class SimulationRunResponse(BaseModel):
    sim_id: str
    symbol: str
    strategy: str
    status: str
    kpis: Optional[dict] = None
    trading_days: Optional[int] = None
    total_trades: Optional[int] = None
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
    try:
        if request.strategy_name not in StrategyFactory.available():
            raise ValueError(
                f"Strategy '{request.strategy_name}' is not registered"
            )
        params = request.strategy_params.to_dict() if request.strategy_params else {}
        config = BacktestConfig(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            account_size=request.account_size,
            strategy_name=request.strategy_name,
            strategy_params=params,
            pip_value=request.pip_value,
            fixed_slippage_price=request.fixed_slippage_price,
            commission_per_trade=request.commission_per_trade,
            intrabar_fill_policy=request.intrabar_fill_policy,
            mark_expired_to_market=request.mark_expired_to_market,
            run_bootstrap=request.run_bootstrap,
            bootstrap_iterations=request.bootstrap_iterations,
            debug_lookbehind_guard=request.debug_lookbehind_guard,
            use_atr_slippage=request.use_atr_slippage,
            atr_slippage_factor=request.atr_slippage_factor,
        )
        sim_id = simulation_service.start_background(config)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logfire.error(f"Simulation failed: {e}")
        raise HTTPException(status_code=500, detail=f"Simulation error: {str(e)}")

    return SimulationRunResponse(
        sim_id=sim_id,
        symbol=request.symbol,
        strategy=request.strategy_name,
        status="queued",
    )


@router.get("/results/{sim_id}", response_model=SimulationDetailResponse)
async def get_simulation_result(sim_id: str):
    """
    Retrieve the full result of a previously executed backtest, including trade-level detail.
    """
    job = simulation_service.get_job(sim_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Simulation '{sim_id}' not found.")
    if job["status"] in {"queued", "running"}:
        raise HTTPException(status_code=202, detail=f"Simulation '{sim_id}' is still running.")
    if job["status"] == "failed":
        raise HTTPException(
            status_code=422,
            detail={
                "message": f"Simulation '{sim_id}' failed.",
                "error": job.get("error"),
            },
        )

    result = simulation_service.get_result(sim_id)
    if result is None:
        raise HTTPException(status_code=500, detail=f"Simulation '{sim_id}' has no result.")

    trades_out = [
        TradeRecordResponse(
            signal_id=t.signal.signal_id,
            timestamp=t.signal.timestamp,
            direction=t.signal.direction,
            entry=t.signal.entry,
            stop=t.signal.stop,
            tp=t.signal.tp,
            exit_price=t.exit_price,
            exit_timestamp=t.exit_timestamp,
            outcome=t.outcome,
            pnl_r=t.pnl_r,
            pnl_usd=t.pnl_usd,
            gross_pnl_usd=t.gross_pnl_usd,
            fees_usd=t.fees_usd,
            entry_price=t.entry_price,
            execution_note=t.execution_note,
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
    symbol: str = Query(..., examples=["AAPL"]),
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
    return {"strategies": StrategyFactory.available() + ["IV_REGIME"]}


# ── IV Regime Strategy ─────────────────────────────────────────────────────────

class IVRegimeRequest(BaseModel):
    symbol:            str   = Field(..., examples=["AAPL"])
    start_date:        str   = Field(..., examples=["2023-01-01"])
    end_date:          str   = Field(..., examples=["2024-01-01"])
    account_size:      float = Field(default=10_000.0, gt=0)
    iv_rank_low:       float = Field(default=30.0, ge=0, le=100)
    iv_rank_high:      float = Field(default=70.0, ge=0, le=100)
    momentum_window:   int   = Field(default=5, ge=1, le=60)
    vol_window:        int   = Field(default=20, ge=5, le=60)
    hold_days:         int   = Field(default=5, ge=1, le=60)
    sl_vol_mult:       float = Field(default=2.0, ge=0.5, le=10.0)
    rr_target:         float = Field(default=2.0, ge=0.5, le=10.0)
    risk_pct:          float = Field(default=0.01, ge=0.001, le=0.25)
    use_markov_filter: bool  = Field(default=True)
    allow_short:       bool  = Field(default=True)


@router.post("/iv-regime")
async def run_iv_regime(request: IVRegimeRequest):
    """
    Run the IV Regime daily strategy backtest.

    Uses rolling realised volatility percentile (IV Rank proxy) combined with
    Markov volatility state and N-day price momentum to generate long/short signals.

    Unlike /run (intraday ORB/ICT), this endpoint is synchronous and operates on
    daily OHLCV data — it returns the full result in a single response.
    """
    if request.start_date >= request.end_date:
        raise HTTPException(status_code=400, detail="start_date must be before end_date")

    from ...services.iv_regime_strategy_service import IVRegimeParams, iv_regime_service

    params = IVRegimeParams(
        iv_rank_low       = request.iv_rank_low,
        iv_rank_high      = request.iv_rank_high,
        momentum_window   = request.momentum_window,
        vol_window        = request.vol_window,
        hold_days         = request.hold_days,
        sl_vol_mult       = request.sl_vol_mult,
        rr_target         = request.rr_target,
        risk_pct          = request.risk_pct,
        use_markov_filter = request.use_markov_filter,
        allow_short       = request.allow_short,
    )

    try:
        result = await iv_regime_service.run_backtest(
            symbol       = request.symbol,
            start_date   = request.start_date,
            end_date     = request.end_date,
            account_size = request.account_size,
            params       = params,
        )
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logfire.error(f"IV Regime backtest error: {e}")
        raise HTTPException(status_code=500, detail=f"IV Regime error: {str(e)}")
