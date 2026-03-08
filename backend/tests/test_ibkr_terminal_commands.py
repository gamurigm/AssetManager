import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from app.services.ibkr_order_parser import parse_ibkr_terminal_command
from app.services.ibkr_service import IBKRService


def test_parse_ibkr_terminal_command_stock_defaults():
    order = parse_ibkr_terminal_command(
        "buy AAPL 10",
        portfolio_id="main",
        record_trade=True,
    )

    assert order.symbol == "AAPL"
    assert order.quantity == 10
    assert order.side == "BUY"
    assert order.asset_type == "stock"
    assert order.currency == "USD"
    assert order.portfolio_id == "main"
    assert order.record_trade is True


def test_parse_ibkr_terminal_command_forex_options():
    order = parse_ibkr_terminal_command(
        "buy EUR/USD 25000 --asset-type forex --exchange IDEALPRO --portfolio fx_live",
        portfolio_id="main",
        record_trade=False,
    )

    assert order.symbol == "EUR/USD"
    assert order.quantity == 25000
    assert order.side == "BUY"
    assert order.asset_type == "forex"
    assert order.exchange == "IDEALPRO"
    assert order.portfolio_id == "fx_live"
    assert order.record_trade is False


def test_build_order_contract_for_forex():
    service = IBKRService()
    contract, app_symbol, asset_type = service._build_order_contract(
        "EUR/USD",
        asset_type="forex",
        exchange="IDEALPRO",
    )

    assert app_symbol == "EURUSD=X"
    assert asset_type == "forex"
    assert contract.secType == "CASH"
    assert contract.exchange == "IDEALPRO"