import sys
from pathlib import Path

from ib_insync import Forex, Stock

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.services.ibkr_service import IBKRService


def test_build_market_data_contract_uses_forex_for_yahoo_style_pair(monkeypatch):
    monkeypatch.delenv("IBKR_PORT_CANDIDATES", raising=False)
    service = IBKRService()

    contract, app_symbol = service._build_market_data_contract("EURUSD=X")

    assert isinstance(contract, Forex)
    assert app_symbol == "EURUSD=X"


def test_build_market_data_contract_normalizes_slash_forex_pair(monkeypatch):
    monkeypatch.delenv("IBKR_PORT_CANDIDATES", raising=False)
    service = IBKRService()

    contract, app_symbol = service._build_market_data_contract("eur/usd")

    assert isinstance(contract, Forex)
    assert app_symbol == "EURUSD=X"


def test_build_market_data_contract_keeps_stock_symbols(monkeypatch):
    monkeypatch.delenv("IBKR_PORT_CANDIDATES", raising=False)
    service = IBKRService()

    contract, app_symbol = service._build_market_data_contract("AAPL")

    assert isinstance(contract, Stock)
    assert app_symbol == "AAPL"


def test_resolve_app_symbol_restores_forex_room_name(monkeypatch):
    monkeypatch.delenv("IBKR_PORT_CANDIDATES", raising=False)
    service = IBKRService()
    contract = Forex("EURUSD")
    contract.conId = 12345
    contract.localSymbol = "EUR.USD"

    service._remember_contract_symbol(contract, "EURUSD=X")

    assert service._resolve_app_symbol(contract) == "EURUSD=X"


def test_get_port_candidates_prioritizes_configured_port(monkeypatch):
    monkeypatch.setenv("IBKR_PORT", "7496")
    monkeypatch.setenv("IBKR_PORT_CANDIDATES", "4002, 7497, 4001")

    service = IBKRService()

    assert service._get_port_candidates() == [7496, 4002, 7497, 4001, 4000]