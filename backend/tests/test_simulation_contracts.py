import pytest
from pydantic import ValidationError

from app.agents.strategies.backtest_runner import BacktestConfig
from app.agents.strategies.engine.models import StrategyConfig
from app.api.routes.simulation import SimulationRequest, StrategyParamsRequest


def valid_request(**overrides) -> dict:
    payload = {
        "symbol": " aapl ",
        "start_date": "2026-01-01",
        "end_date": "2026-02-01",
        "strategy_name": "orb_fvg_engulfing",
    }
    payload.update(overrides)
    return payload


def test_simulation_request_normalizes_boundary_identifiers():
    request = SimulationRequest(**valid_request())

    assert request.symbol == "AAPL"
    assert request.strategy_name == "ORB_FVG_ENGULFING"


@pytest.mark.parametrize(
    "overrides",
    [
        {"start_date": "not-a-date"},
        {"start_date": "2026-02-01", "end_date": "2026-01-01"},
        {"symbol": "AAPL;DROP"},
        {"bootstrap_iterations": 100_001},
    ],
)
def test_simulation_request_rejects_unsafe_or_unbounded_inputs(overrides):
    with pytest.raises(ValidationError):
        SimulationRequest(**valid_request(**overrides))


def test_strategy_parameter_contract_forbids_silent_typos():
    with pytest.raises(ValidationError):
        StrategyParamsRequest(risk_per_trdae=0.005)


def test_unsupported_concurrent_position_model_is_rejected():
    with pytest.raises(ValidationError):
        StrategyParamsRequest(max_concurrent_trades=2)


def test_domain_config_forbids_unknown_parameters_outside_http_too():
    with pytest.raises(ValueError, match="Unknown strategy parameters"):
        StrategyConfig.from_dict({"risk_per_trdae": 0.005})


def test_backtest_config_owns_core_invariants():
    with pytest.raises(ValueError, match="start_date must be before end_date"):
        BacktestConfig(
            symbol="AAPL",
            start_date="2026-02-01",
            end_date="2026-01-01",
        )
