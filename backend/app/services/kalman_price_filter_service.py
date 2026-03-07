"""
KalmanPriceFilterService
========================
AR(1) state-space Kalman filter for daily close series.

State equation:
    x_t = alpha + beta * x_{t-1} + w_t,   w_t ~ N(0, Q)

Observation equation:
    z_t = x_t + v_t,                      v_t ~ N(0, R)

When 0 < beta < 1 the state dynamics admit an Ornstein-Uhlenbeck /
mean-reversion interpretation. For trending assets the service still runs as
an AR(1) state filter, but the OU diagnostics are left nullable.

Usage
-----
    from app.services.kalman_price_filter_service import kalman_price_filter_service
    result = await kalman_price_filter_service.get_price_filter("VIX", days=300)
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd


def _fit_ar1_levels(prices: np.ndarray) -> Dict[str, Optional[float]]:
    """Estimate alpha / beta for the level AR(1) process by OLS."""
    if len(prices) < 20:
        raise ValueError("Need at least 20 prices to calibrate the AR(1) model")

    x_prev = prices[:-1]
    y_cur = prices[1:]
    design = np.column_stack([np.ones(len(x_prev)), x_prev])
    coeffs, _, _, _ = np.linalg.lstsq(design, y_cur, rcond=None)

    alpha = float(coeffs[0])
    beta = float(coeffs[1])
    fitted = alpha + beta * x_prev
    resid = y_cur - fitted

    resid_var = float(np.var(resid, ddof=1)) if len(resid) > 1 else 0.0
    diff_var = float(np.var(np.diff(prices), ddof=1)) if len(prices) > 2 else 0.0
    process_noise_q = max(resid_var, diff_var * 1e-4, 1e-8)
    resid_std = math.sqrt(process_noise_q)

    stationary = 0.0 < beta < 0.999
    long_run_mean = float(alpha / (1.0 - beta)) if stationary else None
    half_life_days = (
        float(math.log(0.5) / math.log(beta))
        if stationary and beta > 0.0
        else None
    )

    return {
        "alpha": alpha,
        "beta": beta,
        "residual_std": resid_std,
        "process_noise_q": process_noise_q,
        "stationary": stationary,
        "long_run_mean": long_run_mean,
        "half_life_days": half_life_days,
    }


def _run_kalman_filter(
    dates: List[str],
    prices: np.ndarray,
    alpha: float,
    beta: float,
    process_noise_q: float,
    measurement_noise_r: float,
    long_run_mean: Optional[float],
) -> Dict[str, Any]:
    """Run the one-factor AR(1) Kalman filter over the observed close series."""
    if len(prices) != len(dates):
        raise ValueError("dates and prices must have the same length")
    if len(prices) == 0:
        raise ValueError("prices must contain at least one observation")

    q = max(float(process_noise_q), 1e-8)
    r = max(float(measurement_noise_r), 1e-8)

    series: List[Dict[str, float | str | None]] = []
    innovations: List[float] = []
    gains: List[float] = []
    obs_vs_filtered: List[float] = []

    x = float(prices[0])
    p = max(q, r)
    sigma = math.sqrt(p)
    initial_mean_gap_pct = (
        ((long_run_mean - x) / x) * 100.0
        if long_run_mean is not None and x != 0.0
        else None
    )
    series.append({
        "date": dates[0],
        "observed": round(float(prices[0]), 6),
        "predicted": round(float(prices[0]), 6),
        "filtered": round(x, 6),
        "innovation": 0.0,
        "innovation_z": 0.0,
        "gain": 0.0,
        "variance": round(p, 6),
        "lower_1sigma": round(x - sigma, 6),
        "upper_1sigma": round(x + sigma, 6),
        "mean_gap_pct": round(initial_mean_gap_pct, 4) if initial_mean_gap_pct is not None else None,
    })
    obs_vs_filtered.append(float(prices[0]) - x)

    for idx in range(1, len(prices)):
        observed = float(prices[idx])

        x_pred = alpha + beta * x
        p_pred = (beta ** 2) * p + q

        innovation = observed - x_pred
        innovation_var = max(p_pred + r, 1e-8)
        gain = p_pred / innovation_var

        x = x_pred + gain * innovation
        p = max((1.0 - gain) * p_pred, 1e-8)

        innovation_z = innovation / math.sqrt(innovation_var)
        sigma = math.sqrt(p)
        mean_gap_pct = (
            ((long_run_mean - observed) / observed) * 100.0
            if long_run_mean is not None and observed != 0.0
            else None
        )

        series.append({
            "date": dates[idx],
            "observed": round(observed, 6),
            "predicted": round(x_pred, 6),
            "filtered": round(x, 6),
            "innovation": round(innovation, 6),
            "innovation_z": round(innovation_z, 6),
            "gain": round(gain, 6),
            "variance": round(p, 6),
            "lower_1sigma": round(x - sigma, 6),
            "upper_1sigma": round(x + sigma, 6),
            "mean_gap_pct": round(mean_gap_pct, 4) if mean_gap_pct is not None else None,
        })

        innovations.append(innovation)
        gains.append(gain)
        obs_vs_filtered.append(observed - x)

    observed_arr = np.asarray(prices, dtype=float)
    filtered_arr = np.asarray([float(point["filtered"]) for point in series], dtype=float)
    observed_diff_std = float(np.std(np.diff(observed_arr), ddof=1)) if len(observed_arr) > 2 else 0.0
    filtered_diff_std = float(np.std(np.diff(filtered_arr), ddof=1)) if len(filtered_arr) > 2 else 0.0
    smoothness_ratio = (
        filtered_diff_std / observed_diff_std
        if observed_diff_std > 1e-12
        else 0.0
    )

    rmse = float(math.sqrt(np.mean(np.square(np.asarray(obs_vs_filtered, dtype=float)))))
    mean_abs_innovation = float(np.mean(np.abs(np.asarray(innovations, dtype=float)))) if innovations else 0.0
    avg_gain = float(np.mean(np.asarray(gains, dtype=float))) if gains else 0.0
    last = series[-1]

    spread_pct = (
        ((float(last["filtered"]) - float(last["observed"])) / float(last["observed"])) * 100.0
        if float(last["observed"]) != 0.0
        else 0.0
    )
    if abs(spread_pct) < 0.25 and abs(float(last["innovation_z"])) < 0.75:
        pull_signal = "NEUTRAL"
    elif spread_pct > 0.0:
        pull_signal = "UP"
    else:
        pull_signal = "DOWN"

    return {
        "series": series,
        "diagnostics": {
            "rmse_filtered_vs_observed": round(rmse, 6),
            "mean_abs_innovation": round(mean_abs_innovation, 6),
            "avg_gain": round(avg_gain, 6),
            "last_gain": round(float(last["gain"]), 6),
            "last_innovation_z": round(float(last["innovation_z"]), 6),
            "smoothness_ratio": round(smoothness_ratio, 6),
        },
        "current_state": {
            "observed": round(float(last["observed"]), 6),
            "predicted": round(float(last["predicted"]), 6),
            "filtered": round(float(last["filtered"]), 6),
            "innovation": round(float(last["innovation"]), 6),
            "innovation_z": round(float(last["innovation_z"]), 6),
            "gain": round(float(last["gain"]), 6),
            "variance": round(float(last["variance"]), 6),
            "lower_1sigma": round(float(last["lower_1sigma"]), 6),
            "upper_1sigma": round(float(last["upper_1sigma"]), 6),
            "spread_pct": round(spread_pct, 4),
            "pull_signal": pull_signal,
            "mean_gap_pct": last["mean_gap_pct"],
        },
    }


class KalmanPriceFilterService:
    """AR(1) state-space filter backed by historical OHLCV closes."""

    def __init__(self) -> None:
        self._mds = None
        self._repo = None

    def _get_deps(self):
        if self._mds is None:
            from .market_data import market_data_service
            from .duckdb_store import duckdb_repo

            self._mds = market_data_service
            self._repo = duckdb_repo

    async def get_price_filter(
        self,
        symbol: str,
        days: int = 300,
        measurement_noise_mult: float = 4.0,
    ) -> Dict[str, Any]:
        """
        Estimate an AR(1) model on closes, then run a 1D Kalman filter.

        measurement_noise_mult controls the observation uncertainty via:
            R = measurement_noise_mult * Q
        """
        self._get_deps()

        if measurement_noise_mult <= 0:
            return {"error": "measurement_noise_mult must be > 0"}

        df = await self._fetch_ohlcv(symbol, days)
        if df is None or len(df) < 40:
            return {"error": f"Insufficient data for {symbol} (need >=40 rows)"}

        df = df.sort_values("date").reset_index(drop=True)
        df["close"] = pd.to_numeric(df["close"], errors="coerce")
        df = df.dropna(subset=["close"]).reset_index(drop=True)
        if len(df) < 40:
            return {"error": f"Insufficient clean close data for {symbol}"}

        prices = df["close"].values.astype(float)
        dates = [str(value)[:10] for value in df["date"]]

        fit = _fit_ar1_levels(prices)
        process_noise_q = float(fit["process_noise_q"] or 1e-8)
        measurement_noise_r = max(process_noise_q * float(measurement_noise_mult), 1e-8)
        long_run_mean = float(fit["long_run_mean"]) if fit["long_run_mean"] is not None else None

        filter_result = _run_kalman_filter(
            dates=dates,
            prices=prices,
            alpha=float(fit["alpha"] or 0.0),
            beta=float(fit["beta"] or 0.0),
            process_noise_q=process_noise_q,
            measurement_noise_r=measurement_noise_r,
            long_run_mean=long_run_mean,
        )

        calibration = {
            "alpha": round(float(fit["alpha"] or 0.0), 6),
            "beta": round(float(fit["beta"] or 0.0), 6),
            "residual_std": round(float(fit["residual_std"] or 0.0), 6),
            "process_noise_q": round(process_noise_q, 6),
            "measurement_noise_r": round(measurement_noise_r, 6),
            "measurement_noise_mult": round(float(measurement_noise_mult), 4),
            "stationary": bool(fit["stationary"]),
            "long_run_mean": round(long_run_mean, 6) if long_run_mean is not None else None,
            "half_life_days": round(float(fit["half_life_days"]), 4) if fit["half_life_days"] is not None else None,
        }

        return {
            "symbol": symbol.upper(),
            "n_obs": len(df),
            "model": "AR(1) Kalman Filter",
            "ou_interpretation": bool(fit["stationary"]),
            "calibration": calibration,
            "diagnostics": filter_result["diagnostics"],
            "current_state": filter_result["current_state"],
            "series": filter_result["series"],
        }

    async def _fetch_ohlcv(self, symbol: str, days: int) -> pd.DataFrame | None:
        """Try DuckDB first, then fall back to market_data_service."""
        try:
            conn = self._repo._connect(read_only=True)
            try:
                df = conn.execute(
                    "SELECT date, close FROM ohlcv WHERE symbol = ? ORDER BY date ASC",
                    [symbol.upper()],
                ).df()
            finally:
                conn.close()

            if len(df) >= max(40, days // 2):
                df["date"] = pd.to_datetime(df["date"])
                return df.tail(days).reset_index(drop=True)
        except Exception:
            pass

        try:
            data = await self._mds.get_historical(symbol, limit=days)
            hist = data.get("historical", []) if data else []
            if not hist:
                return None
            records = [(item.__dict__ if hasattr(item, "__dict__") else item) for item in hist]
            df = pd.DataFrame(records)
            df["date"] = pd.to_datetime(df["date"])
            df["close"] = pd.to_numeric(df["close"], errors="coerce")
            return df.dropna(subset=["close"]).sort_values("date").reset_index(drop=True)
        except Exception:
            return None


kalman_price_filter_service = KalmanPriceFilterService()