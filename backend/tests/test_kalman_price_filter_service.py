import math
import asyncio
import os
import sys

import numpy as np
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.services.kalman_price_filter_service import KalmanPriceFilterService


def _stationary_series(n: int = 140, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    alpha = 12.0
    beta = 0.82
    process_std = 1.1
    obs_std = 2.0

    latent = np.zeros(n)
    latent[0] = 95.0
    observed = np.zeros(n)
    observed[0] = latent[0] + rng.normal(0.0, obs_std)

    for idx in range(1, n):
        latent[idx] = alpha + beta * latent[idx - 1] + rng.normal(0.0, process_std)
        observed[idx] = latent[idx] + rng.normal(0.0, obs_std)

    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="D"),
        "close": observed,
    })


def _trending_series(n: int = 140, seed: int = 13) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    close = 100.0 + np.cumsum(rng.normal(0.35, 1.1, n))
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n, freq="D"),
        "close": close,
    })


def test_kalman_filter_returns_smoothed_stationary_series():
    service = KalmanPriceFilterService()
    service._mds = object()
    service._repo = object()
    df = _stationary_series()

    async def fake_fetch(symbol: str, days: int):
        return df.tail(days).reset_index(drop=True)

    service._fetch_ohlcv = fake_fetch  # type: ignore[method-assign]

    result = asyncio.run(service.get_price_filter("VIX", days=120, measurement_noise_mult=4.0))

    assert result["symbol"] == "VIX"
    assert result["model"] == "AR(1) Kalman Filter"
    assert result["n_obs"] == 120
    assert result["ou_interpretation"] is True
    assert result["calibration"]["stationary"] is True
    assert result["calibration"]["half_life_days"] is not None
    assert len(result["series"]) == 120

    observed = np.array([point["observed"] for point in result["series"]], dtype=float)
    filtered = np.array([point["filtered"] for point in result["series"]], dtype=float)
    observed_diff_std = float(np.std(np.diff(observed), ddof=1))
    filtered_diff_std = float(np.std(np.diff(filtered), ddof=1))

    assert filtered_diff_std < observed_diff_std
    assert result["diagnostics"]["smoothness_ratio"] < 1.0
    assert math.isfinite(result["diagnostics"]["rmse_filtered_vs_observed"])
    assert result["current_state"]["gain"] >= 0.0
    assert result["current_state"]["pull_signal"] in {"UP", "DOWN", "NEUTRAL"}


def test_kalman_filter_handles_high_persistence_trending_fit():
    service = KalmanPriceFilterService()
    service._mds = object()
    service._repo = object()
    df = _trending_series()

    async def fake_fetch(symbol: str, days: int):
        return df.tail(days).reset_index(drop=True)

    service._fetch_ohlcv = fake_fetch  # type: ignore[method-assign]

    result = asyncio.run(service.get_price_filter("AAPL", days=120, measurement_noise_mult=3.0))

    assert result["symbol"] == "AAPL"
    assert result["n_obs"] == 120
    assert result["calibration"]["beta"] > 0.95
    assert result["calibration"]["half_life_days"] is None or result["calibration"]["half_life_days"] > 20
    assert len(result["series"]) == 120
    assert math.isfinite(result["diagnostics"]["last_innovation_z"])