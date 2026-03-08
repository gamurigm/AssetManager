import asyncio
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from app.api.routes import openbb_config


def _patch_portfolio_storage(monkeypatch):
    monkeypatch.setattr(openbb_config.duckdb_repo, "add_transaction", lambda *args, **kwargs: True)
    monkeypatch.setattr(openbb_config.duckdb_repo, "get_portfolio", lambda portfolio_id="main": [])
    monkeypatch.setattr(openbb_config.duckdb_repo, "save_portfolio", lambda holdings, portfolio_id="main": True)
    monkeypatch.setattr(openbb_config.ibkr_service, "_to_app_symbol", lambda symbol: symbol.upper())


def test_openbb_cli_buy_accepts_positional_symbol_with_flagged_shares(monkeypatch):
    _patch_portfolio_storage(monkeypatch)

    async def fake_quote(symbol):
        return {"price": 200.0}

    monkeypatch.setattr(openbb_config.get_quote, "execute", fake_quote)
    monkeypatch.setattr(openbb_config.ibkr_service, "_ib_connected", lambda: False)
    monkeypatch.setattr(openbb_config.ctrader_service, "get_status", lambda: {"connected": False})

    result = asyncio.run(openbb_config.openbb_cli({"command": "buy AAPL --shares 1 --venue sim"}))

    assert result.get("type") != "error"
    assert "Symbol: AAPL" in result["output"]
    assert "Shares: 1.0000" in result["output"]


def test_openbb_cli_buy_ibkr_with_explicit_shares_skips_quote_lookup(monkeypatch):
    _patch_portfolio_storage(monkeypatch)

    async def should_not_run(_symbol):
        raise AssertionError("quote lookup should not be called for explicit-share IBKR orders")

    async def fake_ibkr_order(symbol, quantity, side, **kwargs):
        return {
            "symbol": symbol,
            "asset_type": kwargs.get("asset_type", "stock"),
            "avgFillPrice": 123.45,
            "orderId": 1,
            "status": "Filled",
            "filled": quantity,
            "remaining": 0,
        }

    monkeypatch.setattr(openbb_config.get_quote, "execute", should_not_run)
    monkeypatch.setattr(openbb_config.ibkr_service, "_ib_connected", lambda: True)
    monkeypatch.setattr(openbb_config.ibkr_service, "place_market_order", fake_ibkr_order)

    result = asyncio.run(openbb_config.openbb_cli({"command": "buy AAPL --shares 1 --venue ibkr"}))

    assert result.get("type") != "error"
    assert "ORDER EXECUTED LIVE" in result["output"]
    assert "Price:  $123.4500" in result["output"]