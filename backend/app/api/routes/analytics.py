from fastapi import APIRouter, HTTPException, Query
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from ...core.container import get_historical, duckdb_repo
from ...analytics.models.hmm import MarketRegimeModel
from ...services.math_core import math_core
from ...services.asset_classification_service import classify_assets
from ...services.markov_vol_service import markov_vol_service
from ...services.implied_vol_service import implied_vol_service
from ...services.arch_vol_service import arch_vol_service
from ...services.kalman_price_filter_service import kalman_price_filter_service

router = APIRouter()


@router.get("/factor-analysis")
async def get_factor_analysis(
    tickers: str = Query(..., description="Comma-separated list of asset symbols, e.g. AAPL,MSFT,NVDA"),
    benchmark: str = Query("SPY", description="Market proxy symbol for CAPM regression"),
    days: int = Query(252, description="Historical lookback in calendar days"),
):
    """
    Runs CAPM regression, Idiosyncratic Risk decomposition, Covariance Matrix,
    and PCA spectral decomposition for the given portfolio assets.
    """
    symbols = [t.strip().upper() for t in tickers.split(",") if t.strip()]
    if not symbols:
        raise HTTPException(status_code=400, detail="No valid tickers provided")

    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    conn = duckdb_repo._connect(read_only=True)
    try:
        all_returns: dict[str, np.ndarray] = {}
        symbols_to_load = list(set(symbols + [benchmark]))

        for sym in symbols_to_load:
            df = conn.execute(
                "SELECT date, close FROM ohlcv WHERE symbol = ? AND date >= ? ORDER BY date ASC",
                [sym, start_date.date()],
            ).df()
            if not df.empty and len(df) > 10:
                df["returns"] = df["close"].pct_change().fillna(0)
                all_returns[sym] = df["returns"].values

    finally:
        conn.close()

    if benchmark not in all_returns:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for benchmark '{benchmark}'. Pre-populate it in DuckDB first.",
        )

    valid_tickers = [t for t in symbols if t in all_returns]
    if not valid_tickers:
        raise HTTPException(status_code=404, detail="No historical data found for any of the requested tickers")

    asset_classifications = await classify_assets(valid_tickers, benchmark=benchmark)

    market_returns = all_returns[benchmark]
    returns_dict = {t: all_returns[t] for t in valid_tickers}

    # ── Per-asset CAPM + Idiosyncratic Risk ────────────────────────────
    asset_metrics = []
    for t in valid_tickers:
        asset_ret = all_returns[t]
        min_len = min(len(asset_ret), len(market_returns))
        a = asset_ret[-min_len:]
        m = market_returns[-min_len:]

        beta, alpha, exp_ret = math_core.calculate_capm(a, m)
        idio_risk = math_core.calculate_idiosyncratic_risk(a, m)
        total_vol = float(np.std(a, ddof=1) * np.sqrt(252))

        # Systematic risk (portion explained by market)
        systematic_risk = abs(beta) * float(np.std(m, ddof=1) * np.sqrt(252))

        asset_metrics.append({
            "ticker": t,
            "beta": round(beta, 4),
            "alpha_daily": round(alpha, 6),
            "expected_return_pct": round(exp_ret * 100, 2),
            "idiosyncratic_risk_pct": round(idio_risk * 100, 2),
            "systematic_risk_pct": round(systematic_risk * 100, 2),
            "total_volatility_pct": round(total_vol * 100, 2),
            # For CAPM scatter plot — pairs of (market_return, asset_return)
            "scatter": [
                {"x": round(float(mx), 5), "y": round(float(ay), 5)}
                for mx, ay in zip(m[::3], a[::3])  # Subsample every 3rd point for chart performance
            ],
            # Best-fit line: y = alpha + beta * x  (for 2 points defining the line)
            "fit_line": [
                {"x": round(float(np.percentile(m, 5)), 5), "y": round(float(alpha + beta * np.percentile(m, 5)), 5)},
                {"x": round(float(np.percentile(m, 95)), 5), "y": round(float(alpha + beta * np.percentile(m, 95)), 5)},
            ],
        })

    # ── Sector Correlations ────────────────────────────────────────────
    # For each portfolio ticker, find its sector ETF and compute correlation
    needed_sector_etfs = {asset_classifications[t]["sector_etf"] for t in valid_tickers}

    # Load sector ETF returns — try DuckDB first, fall back to yfinance
    sector_returns: dict[str, np.ndarray] = {}
    missing_etfs: list[str] = []

    conn2 = duckdb_repo._connect(read_only=True)
    try:
        for etf in needed_sector_etfs:
            if etf in all_returns:
                sector_returns[etf] = all_returns[etf]
                continue
            df_etf = conn2.execute(
                "SELECT date, close FROM ohlcv WHERE symbol = ? AND date >= ? ORDER BY date ASC",
                [etf, start_date.date()],
            ).df()
            if not df_etf.empty and len(df_etf) > 10:
                df_etf["returns"] = df_etf["close"].pct_change().fillna(0)
                sector_returns[etf] = df_etf["returns"].values
            else:
                missing_etfs.append(etf)
    finally:
        conn2.close()

    # Fetch missing ETFs from yfinance on-the-fly
    if missing_etfs:
        try:
            import yfinance as yf
            for etf in missing_etfs:
                hist = yf.download(
                    etf,
                    start=start_date.strftime("%Y-%m-%d"),
                    end=end_date.strftime("%Y-%m-%d"),
                    progress=False,
                    auto_adjust=True,
                )
                if not hist.empty and len(hist) > 10:
                    closes = hist["Close"].squeeze()
                    rets = closes.pct_change().fillna(0).values
                    sector_returns[etf] = rets
        except Exception:
            pass  # If yfinance fails, we'll fallback to SPY for that ETF

    sector_correlations = []
    for t in valid_tickers:
        classification = asset_classifications[t]
        sector_etf = classification["sector_etf"]
        # Fallback: if we couldn't load the specific sector ETF, use benchmark
        etf_rets = sector_returns.get(sector_etf)
        if etf_rets is None:
            etf_rets = all_returns.get(benchmark)
        asset_ret = all_returns[t]

        if etf_rets is None:
            corr = None
            r2 = None
        else:
            min_len = min(len(asset_ret), len(etf_rets))
            a = asset_ret[-min_len:]
            e = etf_rets[-min_len:]
            try:
                corr = float(np.corrcoef(a, e)[0, 1])
                r2 = corr ** 2
            except Exception:
                corr, r2 = None, None

        used_etf = sector_etf if sector_etf in sector_returns else benchmark
        sector_correlations.append({
            "ticker": t,
            "sector_etf": used_etf,
            "sector_name": classification["sector"],
            "industry_group": classification["industry_group"],
            "industry": classification["industry"],
            "sub_industry": classification["sub_industry"],
            "correlation": round(corr, 4) if corr is not None else None,
            "r_squared": round(r2, 4) if r2 is not None else None,
        })

    # ── Correlation Matrix ─────────────────────────────────────────────
    _, cov_matrix = math_core.calculate_covariance_matrix(returns_dict)
    stds = np.sqrt(np.diag(cov_matrix))
    stds[stds == 0] = 1.0
    corr_matrix = cov_matrix / np.outer(stds, stds)

    correlation_matrix = []
    for i, t1 in enumerate(valid_tickers):
        row_dict = {"ticker": t1}
        for j, t2 in enumerate(valid_tickers):
            row_dict[t2] = round(float(corr_matrix[i, j]), 4)
        correlation_matrix.append(row_dict)

    # ── PCA ────────────────────────────────────────────────────────────
    pca = math_core.calculate_pca(returns_dict)

    return {
        "tickers": valid_tickers,
        "benchmark": benchmark,
        "lookback_days": days,
        "asset_metrics": asset_metrics,
        "correlation_matrix": correlation_matrix,
        "sector_correlations": sector_correlations,
        "pca": {
            "eigenvalues": [round(v, 4) for v in pca.get("eigenvalues", [])],
            "explained_variance_pct": [round(v * 100, 2) for v in pca.get("explained_variance", [])],
            "cumulative_variance_pct": [round(v * 100, 2) for v in pca.get("cumulative_variance", [])],
            "components_labels": [f"PC{i+1}" for i in range(len(pca.get("eigenvalues", [])))],
        },
    }

@router.get("/regime/{symbol}")
async def get_market_regime(symbol: str):
    """
    Analyzes historical data to detect the current market regime using a Hidden Markov Model (HMM).
    Returns: Current regime (Bullish/Bearish/Neutral) and transition probabilities.
    """
    # 1. Fetch Historical Data (Last 500 candles for solid regime detection)
    # Using existing UseCase to leverage cache/provider fallback
    data = await get_historical.execute(symbol, limit=500)
    
    if not data or "error" in data:
        raise HTTPException(status_code=404, detail=data.get("error", "Data not found"))
        
    candles = data.get("historical", [])
    if not candles:
        raise HTTPException(status_code=404, detail="No historical data found for HMM analysis")
        
    # 2. Convert to DataFrame for Analysis
    try:
        df = pd.DataFrame(candles)
        
        # 3. Predict Regime
        # Instantiate fresh model for this asset to learn its specific volatility patterns
        model = MarketRegimeModel()
        result = model.fit_predict(df)
        
        if result.get("error"):
            raise HTTPException(status_code=422, detail=result["error"])

        return {
            "symbol": symbol,
            "regime_analysis": result,
            "data_source": data.get("source", "Unknown"),
            "data_points_analyzed": len(df)
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@router.get("/volatility-regimes/{symbol}")
async def get_volatility_regimes(
    symbol: str,
    days:   int = Query(500, description="Lookback window in trading sessions"),
    window: int = Query(20,  description="Rolling volatility window (days)"),
):
    """
    3-state Markov volatility model (percentile-based, observable states).

    States:
      0 = Low Volatility  — rolling vol in bottom 33rd pct  (green)
      1 = Med Volatility  — rolling vol in 33rd–66th pct    (yellow)
      2 = High Volatility — rolling vol above 66th pct      (red)

    Returns state sequence, 3×3 transition matrix, per-state return
    distributions and the most probable next state.
    """
    result = await markov_vol_service.get_volatility_regimes(
        symbol.upper(), days=days, window=window
    )
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/implied-vol/{symbol}")
async def get_implied_volatility(
    symbol: str,
    rf: float = Query(0.045, description="Risk-free rate (decimal, e.g. 0.045 = 4.5%)"),
):
    """
    Black-Scholes IV inversion: for each contract in the options chain,
    solves C_BS(S, K, T, r, σ) = C_market for σ using Newton-Raphson
    (fallback: Brentq bracketed solver).

    Returns the full IV smile (IV vs Strike) per expiration date.
    Mid-price (bid+ask)/2 is used as the market price; lastPrice is the
    fallback when bid/ask are zero.
    """
    result = await implied_vol_service.get_iv_smile(symbol.upper(), rf=rf)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/arch-vol/{symbol}")
async def get_arch_volatility(
    symbol: str,
    days: int = Query(500, description="Lookback window in trading sessions"),
):
    """
    Fits GARCH(1,1) to log-returns:
        σ²_t = ω + α·ε²_{t-1} + β·σ²_{t-1}

    Returns the full conditional-volatility time series plus model parameters,
    multi-horizon vol forecasts (1d / 5d / 21d), parametric VaR, and the
    Engle LM test for remaining ARCH effects in the standardised residuals.
    """
    result = await arch_vol_service.get_garch(symbol.upper(), days=days)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/kalman-filter/{symbol}")
async def get_kalman_filter(
    symbol: str,
    days: int = Query(300, description="Lookback window in trading sessions"),
    measurement_noise_mult: float = Query(
        4.0,
        gt=0.0,
        description="Observation-noise multiplier, with R = measurement_noise_mult × Q",
    ),
):
    """
    Fits an AR(1) state model on closes:
        x_t = alpha + beta·x_(t-1) + w_t
        z_t = x_t + v_t

    Then runs the 1D Kalman filter to estimate the latent state x_t.
    When 0 < beta < 1 the dynamics admit an OU / mean-reversion interpretation.

    Returns the filtered series, innovation diagnostics, current gain / spread,
    and the offline AR(1) calibration used as the transition model.
    """
    result = await kalman_price_filter_service.get_price_filter(
        symbol.upper(),
        days=days,
        measurement_noise_mult=measurement_noise_mult,
    )
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

