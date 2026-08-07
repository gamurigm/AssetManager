"""Data access boundary used by the portfolio risk engine."""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Protocol

import pandas as pd

from ..core.container import duckdb_repo


class IRiskDataSource(Protocol):
    def load_close_prices(
        self,
        symbols: List[str],
        start_date: datetime,
    ) -> Dict[str, pd.Series]:
        ...

    def get_transactions(self) -> List[dict]:
        ...


class DuckDBRiskDataSource:
    """Keep DuckDB-specific SQL outside the calculation service."""

    def __init__(self, repository=duckdb_repo) -> None:
        self._repository = repository

    def load_close_prices(
        self,
        symbols: List[str],
        start_date: datetime,
    ) -> Dict[str, pd.Series]:
        prices: Dict[str, pd.Series] = {}
        conn = self._repository._connect(read_only=True)
        try:
            for symbol in dict.fromkeys(symbols):
                frame = conn.execute(
                    "SELECT date, close FROM ohlcv "
                    "WHERE symbol = ? AND date >= ? ORDER BY date ASC",
                    [symbol, start_date.date()],
                ).df()
                if frame.empty:
                    continue
                frame["date"] = pd.to_datetime(frame["date"])
                frame = frame.drop_duplicates("date", keep="last").sort_values("date")
                prices[symbol] = frame.set_index("date")["close"].astype(float)
        finally:
            conn.close()
        return prices

    def get_transactions(self) -> List[dict]:
        return self._repository.get_transactions()
