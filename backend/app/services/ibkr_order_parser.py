import shlex
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class IBKROrderRequest(BaseModel):
    symbol: str
    quantity: float = Field(..., gt=0)
    side: str
    asset_type: str = "stock"
    currency: str = "USD"
    exchange: Optional[str] = None
    primary_exchange: Optional[str] = None
    last_trade_date: Optional[str] = None
    portfolio_id: str = "main"
    record_trade: bool = True


class IBKRCommandRequest(BaseModel):
    command: str
    portfolio_id: str = "main"
    record_trade: bool = True


def parse_cli_args(parts: List[str]) -> Dict[str, Any]:
    kwargs: Dict[str, Any] = {}
    idx = 0
    while idx < len(parts):
        token = parts[idx]
        if token.startswith("--"):
            key = token[2:].replace("-", "_")
            if idx + 1 < len(parts) and not parts[idx + 1].startswith("--"):
                kwargs[key] = parts[idx + 1]
                idx += 2
            else:
                kwargs[key] = True
                idx += 1
            continue
        idx += 1
    return kwargs


def parse_ibkr_terminal_command(
    command: str,
    portfolio_id: str,
    record_trade: bool,
) -> IBKROrderRequest:
    normalized_command = command.strip()
    if not normalized_command:
        raise ValueError("command is required")

    if normalized_command.startswith(":"):
        normalized_command = normalized_command[1:].strip()

    tokens = shlex.split(normalized_command)
    if not tokens:
        raise ValueError("command is required")

    action = tokens[0].lower().lstrip("/")
    if action in {"buy", "portfolio.buy", "ibkr.buy"}:
        side = "BUY"
    elif action in {"sell", "portfolio.sell", "ibkr.sell"}:
        side = "SELL"
    else:
        raise ValueError("command must start with buy or sell")

    symbol = None
    quantity = None
    remainder: List[str] = []
    for token in tokens[1:]:
        if symbol is None and not token.startswith("--"):
            symbol = token
        elif quantity is None and not token.startswith("--"):
            quantity = token
        else:
            remainder.append(token)

    kwargs = parse_cli_args(remainder)
    symbol = kwargs.get("symbol", symbol)
    quantity = kwargs.get("quantity") or kwargs.get("qty") or kwargs.get("shares") or quantity

    if not symbol:
        raise ValueError("symbol is required")
    if quantity is None:
        raise ValueError("quantity is required")

    try:
        parsed_quantity = float(quantity)
    except ValueError as exc:
        raise ValueError("quantity must be numeric") from exc

    return IBKROrderRequest(
        symbol=str(symbol),
        quantity=parsed_quantity,
        side=side,
        asset_type=str(kwargs.get("asset_type", "stock")),
        currency=str(kwargs.get("currency", "USD")),
        exchange=kwargs.get("exchange"),
        primary_exchange=kwargs.get("primary_exchange"),
        last_trade_date=kwargs.get("last_trade_date"),
        portfolio_id=str(kwargs.get("portfolio", portfolio_id)),
        record_trade=record_trade,
    )