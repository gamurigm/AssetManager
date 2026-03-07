from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional

from ..core.container import duckdb_repo


class PortfolioRebalanceService:
    def __init__(self, repo: Any | None = None) -> None:
        self._repo = repo or duckdb_repo

    def apply_policy_rebalance(
        self,
        portfolio_id: str,
        holdings: Optional[List[Dict[str, Any]]],
        allocations: List[Dict[str, Any]],
        symbols: Optional[Iterable[str]] = None,
        trade_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        current_holdings = self._normalize_holdings(holdings if holdings is not None else self._repo.get_portfolio(portfolio_id))
        holdings_map = {holding["symbol"]: holding for holding in current_holdings}
        allocation_map = {
            str(allocation.get("symbol") or "").upper(): allocation
            for allocation in allocations
            if allocation.get("symbol")
        }
        requested_symbols = {
            str(symbol).upper()
            for symbol in (symbols or allocation_map.keys())
            if str(symbol).strip()
        }
        if not requested_symbols:
            return {"error": "No symbols selected for rebalance"}

        effective_date = trade_date or datetime.now().strftime("%Y-%m-%d")
        plan: List[Dict[str, Any]] = []

        for symbol in requested_symbols:
            allocation = allocation_map.get(symbol)
            if not allocation:
                continue

            current_holding = holdings_map.get(symbol)
            current_shares = float(current_holding.get("shares", 0.0) if current_holding else 0.0)
            price = float(allocation.get("price") or (current_holding or {}).get("price") or (current_holding or {}).get("entryPrice") or 0.0)
            factor = float(allocation.get("factor") or (current_holding or {}).get("factor") or 1.0)
            target_shares = self._target_shares(current_shares, allocation, price, factor)

            if abs(target_shares - current_shares) < 1e-6:
                continue

            plan.append(
                {
                    "symbol": symbol,
                    "allocation": allocation,
                    "current": current_holding,
                    "current_shares": current_shares,
                    "target_shares": target_shares,
                    "price": price,
                    "factor": factor,
                }
            )

        if not plan:
            return {"error": "Policy deltas are already in sync with the live portfolio"}

        transactions: List[Dict[str, Any]] = []
        for item in plan:
            transactions.extend(self._build_transactions(item, effective_date))

        for tx in transactions:
            success = self._repo.add_transaction(
                type_str=tx["type"],
                symbol=tx["symbol"],
                shares=tx["shares"],
                price=tx["price"],
                realized_pnl=tx["realized_pnl"],
                custom_date=tx["date"],
                portfolio_id=portfolio_id,
            )
            if not success:
                return {"error": f"Failed to record rebalance transaction for {tx['symbol']}"}

        for item in plan:
            updated_holding = self._updated_holding(item, effective_date)
            if updated_holding is None:
                holdings_map.pop(item["symbol"], None)
            else:
                holdings_map[item["symbol"]] = updated_holding

        updated_holdings = list(holdings_map.values())
        updated_holdings.sort(key=lambda holding: holding["symbol"])
        if not self._repo.save_portfolio(updated_holdings, portfolio_id):
            return {"error": "Failed to persist rebalanced portfolio state"}

        return {
            "status": "success",
            "portfolio_id": portfolio_id,
            "applied_symbols": sorted({item["symbol"] for item in plan}),
            "transaction_count": len(transactions),
            "transactions": transactions,
            "updated_holdings": updated_holdings,
        }

    def _normalize_holdings(self, holdings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        normalized: List[Dict[str, Any]] = []
        for raw_holding in holdings:
            symbol = str(raw_holding.get("symbol") or "").strip().upper()
            shares = float(raw_holding.get("shares", 0) or 0)
            if not symbol or shares == 0:
                continue

            normalized.append(
                {
                    "symbol": symbol,
                    "name": str(raw_holding.get("name") or symbol),
                    "shares": shares,
                    "price": float(raw_holding.get("price") or raw_holding.get("entryPrice") or 0),
                    "entryPrice": float(raw_holding.get("entryPrice") or raw_holding.get("price") or 0),
                    "factor": float(raw_holding.get("factor") or 1.0),
                    "sector": str(raw_holding.get("sector") or "Other"),
                    "type": str(raw_holding.get("type") or "stock"),
                    "purchaseDate": raw_holding.get("purchaseDate") or datetime.now().strftime("%Y-%m-%d"),
                    "source": raw_holding.get("source", "Live"),
                    "change": float(raw_holding.get("change") or 0),
                    "changePercent": float(raw_holding.get("changePercent") or 0),
                    "sl": raw_holding.get("sl"),
                    "tp": raw_holding.get("tp"),
                }
            )
        return normalized

    def _target_shares(self, current_shares: float, allocation: Dict[str, Any], price: float, factor: float) -> float:
        target_notional = allocation.get("target_notional")
        if target_notional is not None and price > 0 and factor > 0:
            return float(target_notional) / (price * factor)
        delta_shares = float(allocation.get("delta_shares", 0.0) or 0.0)
        return current_shares + delta_shares

    def _build_transactions(self, item: Dict[str, Any], trade_date: str) -> List[Dict[str, Any]]:
        symbol = item["symbol"]
        current = item["current"]
        current_shares = float(item["current_shares"])
        target_shares = float(item["target_shares"])
        price = float(item["price"])
        factor = float(item["factor"])
        entry_price = float((current or {}).get("entryPrice") or price or 0.0)
        transactions: List[Dict[str, Any]] = []

        if current_shares != 0 and target_shares != 0 and self._sign(current_shares) != self._sign(target_shares):
            close_qty = abs(current_shares)
            close_side = "SELL" if current_shares > 0 else "BUY"
            transactions.append(
                {
                    "type": close_side,
                    "symbol": symbol,
                    "shares": close_qty,
                    "price": price,
                    "realized_pnl": self._realized_pnl(entry_price, price, close_qty, factor, current_shares),
                    "date": trade_date,
                }
            )
            open_qty = abs(target_shares)
            open_side = "BUY" if target_shares > 0 else "SELL"
            transactions.append(
                {
                    "type": open_side,
                    "symbol": symbol,
                    "shares": open_qty,
                    "price": price,
                    "realized_pnl": 0.0,
                    "date": trade_date,
                }
            )
            return transactions

        delta = target_shares - current_shares
        if delta == 0:
            return transactions

        tx_type = "BUY" if delta > 0 else "SELL"
        tx_qty = abs(delta)
        realized_pnl = 0.0

        if current_shares > 0 and delta < 0:
            realized_pnl = self._realized_pnl(entry_price, price, tx_qty, factor, current_shares)
        elif current_shares < 0 and delta > 0:
            realized_pnl = self._realized_pnl(entry_price, price, tx_qty, factor, current_shares)

        transactions.append(
            {
                "type": tx_type,
                "symbol": symbol,
                "shares": tx_qty,
                "price": price,
                "realized_pnl": realized_pnl,
                "date": trade_date,
            }
        )
        return transactions

    def _updated_holding(self, item: Dict[str, Any], trade_date: str) -> Optional[Dict[str, Any]]:
        current = item["current"]
        target_shares = float(item["target_shares"])
        price = float(item["price"])
        factor = float(item["factor"])
        allocation = item["allocation"]
        current_shares = float(item["current_shares"])

        if abs(target_shares) < 1e-6:
            return None

        base = current or {
            "symbol": item["symbol"],
            "name": allocation.get("name") or item["symbol"],
            "sector": allocation.get("sector") or "Other",
            "type": allocation.get("type") or "stock",
            "purchaseDate": trade_date,
            "sl": None,
            "tp": None,
        }

        if current_shares == 0 or self._sign(current_shares) != self._sign(target_shares):
            entry_price = price
            purchase_date = trade_date
        elif abs(target_shares) > abs(current_shares):
            added = abs(target_shares) - abs(current_shares)
            previous_notional = abs(current_shares) * float(base.get("entryPrice") or price)
            entry_price = (previous_notional + added * price) / abs(target_shares)
            purchase_date = base.get("purchaseDate") or trade_date
        else:
            entry_price = float(base.get("entryPrice") or price)
            purchase_date = base.get("purchaseDate") or trade_date

        return {
            "symbol": item["symbol"],
            "name": base.get("name") or item["symbol"],
            "shares": round(target_shares, 6),
            "entryPrice": round(entry_price, 6),
            "factor": factor,
            "sector": base.get("sector") or allocation.get("sector") or "Other",
            "type": base.get("type") or allocation.get("type") or "stock",
            "purchaseDate": purchase_date,
            "sl": base.get("sl"),
            "tp": base.get("tp"),
        }

    def _realized_pnl(self, entry_price: float, exit_price: float, quantity: float, factor: float, current_shares: float) -> float:
        if current_shares > 0:
            return round((exit_price - entry_price) * quantity * factor, 2)
        return round((entry_price - exit_price) * quantity * factor, 2)

    def _sign(self, value: float) -> int:
        if value > 0:
            return 1
        if value < 0:
            return -1
        return 0


portfolio_rebalance_service = PortfolioRebalanceService()