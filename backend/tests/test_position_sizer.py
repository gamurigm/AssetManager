import pytest

from app.agents.strategies.engine.position_sizer import FixedFractionPositionSizer


def test_fixed_fraction_position_size_respects_price_value():
    size = FixedFractionPositionSizer().calculate(
        account_equity=10_000,
        risk_fraction=0.01,
        risk_price_distance=2.0,
        price_value_per_unit=5.0,
    )

    assert size == pytest.approx(10.0)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("account_equity", 0.0),
        ("risk_fraction", 0.0),
        ("risk_price_distance", 0.0),
        ("price_value_per_unit", 0.0),
    ],
)
def test_fixed_fraction_position_size_rejects_invalid_inputs(field, value):
    args = {
        "account_equity": 10_000,
        "risk_fraction": 0.01,
        "risk_price_distance": 2.0,
        "price_value_per_unit": 1.0,
    }
    args[field] = value

    with pytest.raises(ValueError):
        FixedFractionPositionSizer().calculate(**args)
