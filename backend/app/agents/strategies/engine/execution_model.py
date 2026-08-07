"""Deterministic OHLC trade execution for backtests.

The strategy decides *what* to trade.  This component decides *how* that
intent would have filled inside historical candles, keeping execution costs
and ambiguous intrabar outcomes out of the orchestration layer.
"""

from __future__ import annotations

from typing import List

from .models import CandleRow, ExecutionSettings, TradeRecord, TradeSignal


class OHLCExecutionModel:
    """Conservative, deterministic fill model over OHLC candles."""

    def simulate(
        self,
        signal: TradeSignal,
        remaining_candles: List[CandleRow],
        pip_value: float,
        settings: ExecutionSettings,
    ) -> TradeRecord:
        direction = signal.direction.upper()
        if direction not in {"LONG", "SHORT"}:
            raise ValueError("TradeSignal.direction must be LONG or SHORT")
        if pip_value <= 0:
            raise ValueError("pip_value must be greater than zero")

        direction_sign = 1.0 if direction == "LONG" else -1.0
        slippage = settings.slippage_price
        entry_fill = signal.entry + direction_sign * slippage
        risk_amount = (
            signal.position_size
            * abs(signal.entry - signal.stop)
            * pip_value
        )

        def close_trade(
            outcome: str,
            target_price: float,
            timestamp: str,
            note: str = "",
        ) -> TradeRecord:
            exit_fill = target_price - direction_sign * slippage
            gross_pnl = (
                (exit_fill - entry_fill)
                * direction_sign
                * signal.position_size
                * pip_value
            )
            net_pnl = gross_pnl - settings.commission_per_trade
            pnl_r = net_pnl / risk_amount if risk_amount > 0 else 0.0
            return TradeRecord(
                signal=signal,
                outcome=outcome,
                exit_price=exit_fill,
                exit_timestamp=timestamp,
                pnl_r=pnl_r,
                pnl_usd=net_pnl,
                slippage_pips=slippage,
                entry_price=entry_fill,
                gross_pnl_usd=gross_pnl,
                fees_usd=settings.commission_per_trade,
                execution_note=note,
            )

        for candle in remaining_candles:
            high = float(candle["high"])
            low = float(candle["low"])
            if direction == "LONG":
                stop_hit = low <= signal.stop
                target_hit = high >= signal.tp
            else:
                stop_hit = high >= signal.stop
                target_hit = low <= signal.tp

            if stop_hit and target_hit:
                if settings.intrabar_fill_policy == "optimistic":
                    return close_trade(
                        "win_tp",
                        signal.tp,
                        candle["timestamp"],
                        "Both SL and TP touched; optimistic TP-first policy applied.",
                    )
                return close_trade(
                    "loss_sl",
                    signal.stop,
                    candle["timestamp"],
                    "Both SL and TP touched; conservative SL-first policy applied.",
                )
            if stop_hit:
                return close_trade("loss_sl", signal.stop, candle["timestamp"])
            if target_hit:
                return close_trade("win_tp", signal.tp, candle["timestamp"])

        if remaining_candles and settings.mark_expired_to_market:
            last = remaining_candles[-1]
            return close_trade(
                "expired",
                float(last["close"]),
                last["timestamp"],
                "Position marked to market at the final available candle.",
            )

        return close_trade(
            "expired",
            signal.entry,
            "",
            "No exit candle available; closed at theoretical entry with execution costs.",
        )
