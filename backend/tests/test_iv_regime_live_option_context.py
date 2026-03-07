import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.services.implied_vol_service import ImpliedVolService
from app.services.iv_regime_strategy_service import IVRegimeParams, _build_live_option_context


def test_build_live_option_context_long_bias() -> None:
    params = IVRegimeParams(use_markov_filter=True, allow_short=True)
    current_signal = {
        "regime": "Low",
        "momentum_pct": 2.4,
        "realized_vol_ann_pct": 24.0,
    }
    snapshot = {
        "exp_date": "2025-01-17",
        "dte": 21,
        "strike": 100.0,
        "atm_iv": 21.0,
        "atm_call_iv": 20.0,
        "atm_put_iv": 22.0,
        "skew_pct": 2.0,
        "call_price": 2.5,
        "put_price": 2.9,
        "source": "live_options_chain_bs",
        "as_of": "2024-01-01 10:30",
    }

    context = _build_live_option_context(current_signal, snapshot, params)

    assert context["available"] is True
    assert context["direction_bias"] == "LONG"
    assert context["iv_realized_ratio"] == 0.875
    assert context["iv_realized_spread_pct"] == -3.0


def test_build_live_option_context_short_bias() -> None:
    params = IVRegimeParams(use_markov_filter=True, allow_short=True)
    current_signal = {
        "regime": "High",
        "momentum_pct": -1.8,
        "realized_vol_ann_pct": 20.0,
    }
    snapshot = {
        "exp_date": "2025-01-17",
        "dte": 14,
        "strike": 100.0,
        "atm_iv": 25.0,
        "atm_call_iv": 24.0,
        "atm_put_iv": 26.0,
        "skew_pct": 2.0,
        "call_price": 2.1,
        "put_price": 3.0,
        "source": "live_options_chain_bs",
        "as_of": "2024-01-01 10:30",
    }

    context = _build_live_option_context(current_signal, snapshot, params)

    assert context["available"] is True
    assert context["direction_bias"] == "SHORT"
    assert context["iv_realized_ratio"] == 1.25
    assert context["iv_realized_spread_pct"] == 5.0


def test_get_atm_iv_snapshot_selects_nearest_expiry() -> None:
    service = ImpliedVolService()

    async def fake_get_iv_smile(symbol: str, rf: float = 0.045):
        return {
            "symbol": symbol,
            "spot": 100.0,
            "rf": rf,
            "as_of": "2024-01-01 10:30",
            "expirations": [
                {
                    "exp_date": "2025-02-21",
                    "dte": 45,
                    "smile": [
                        {"type": "CALL", "strike": 100.0, "iv_pct": 24.0, "market_price": 4.2},
                        {"type": "PUT", "strike": 100.0, "iv_pct": 26.0, "market_price": 4.5},
                    ],
                },
                {
                    "exp_date": "2025-01-17",
                    "dte": 10,
                    "smile": [
                        {"type": "CALL", "strike": 100.0, "iv_pct": 20.0, "market_price": 2.3},
                        {"type": "PUT", "strike": 100.0, "iv_pct": 22.0, "market_price": 2.8},
                    ],
                },
            ],
        }

    service.get_iv_smile = fake_get_iv_smile  # type: ignore[method-assign]

    snapshot = asyncio.run(service.get_atm_iv_snapshot("SPY"))

    assert snapshot["exp_date"] == "2025-01-17"
    assert snapshot["dte"] == 10
    assert snapshot["atm_iv"] == 21.0
    assert snapshot["skew_pct"] == 2.0