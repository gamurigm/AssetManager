import asyncio
import os
import sys
import time
import unittest
from collections import namedtuple
from pathlib import Path
from unittest.mock import patch

from pydantic import ValidationError

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.services.mt5_gateway_journal import MT5GatewayJournal
from app.services.mt5_service import MT5ExecutionBlocked, MT5OrderIntent, MT5Service
from app.api.routes.mt5 import MT5OrderRequest


Account = namedtuple(
    "Account",
    "login server currency trade_mode balance equity margin_free trade_allowed trade_expert",
)
Terminal = namedtuple(
    "Terminal",
    "name build connected trade_allowed tradeapi_disabled",
)
Symbol = namedtuple(
    "Symbol",
    "visible volume_min volume_max volume_step point trade_stops_level",
)
Tick = namedtuple("Tick", "ask bid time time_msc")
Check = namedtuple("Check", "retcode comment request")
Result = namedtuple("Result", "retcode comment order deal volume price")
Position = namedtuple("Position", "symbol volume sl type price_open")
HistoryOrder = namedtuple("HistoryOrder", "ticket state")


class FakeMT5:
    ACCOUNT_TRADE_MODE_DEMO = 0
    ACCOUNT_TRADE_MODE_CONTEST = 1
    ACCOUNT_TRADE_MODE_REAL = 2
    TRADE_ACTION_DEAL = 1
    ORDER_TYPE_BUY = 0
    ORDER_TYPE_SELL = 1
    ORDER_TIME_GTC = 0
    ORDER_FILLING_FOK = 0
    ORDER_FILLING_IOC = 1
    ORDER_FILLING_RETURN = 2
    TRADE_RETCODE_PLACED = 10008
    TRADE_RETCODE_DONE = 10009
    TRADE_RETCODE_DONE_PARTIAL = 10010
    POSITION_TYPE_BUY = 0
    POSITION_TYPE_SELL = 1
    ORDER_STATE_CANCELED = 2
    ORDER_STATE_REJECTED = 3
    ORDER_STATE_FILLED = 4
    ORDER_STATE_EXPIRED = 6

    def __init__(self, trade_mode=0):
        self.trade_mode = trade_mode
        self.terminal_trade_allowed = True
        self.sent = []
        self.initialized = False
        self.positions = []
        self.active_orders = []
        self.history_orders = []
        self.send_retcode = self.TRADE_RETCODE_DONE

    def initialize(self, *args, **kwargs):
        self.initialized = True
        return True

    def shutdown(self):
        self.initialized = False

    def last_error(self):
        return (0, "ok")

    def account_info(self):
        if not self.initialized:
            return None
        return Account(12345678, "Demo-Server", "USD", self.trade_mode, 10_000, 10_050, 9_500, True, True)

    def terminal_info(self):
        if not self.initialized:
            return None
        return Terminal("MetaTrader 5", 5000, True, self.terminal_trade_allowed, False)

    def symbol_info(self, symbol):
        return Symbol(True, 0.01, 100.0, 0.01, 0.00001, 20)

    def symbol_select(self, symbol, selected):
        return True

    def symbol_info_tick(self, symbol):
        now = time.time()
        return Tick(1.10020, 1.10000, int(now), int(now * 1000))

    def order_check(self, request):
        return Check(0, "Done", request)

    def order_calc_margin(self, order_type, symbol, volume, price):
        return 50.0

    def order_calc_profit(self, order_type, symbol, volume, price_open, price_close):
        return -25.0

    def order_send(self, request):
        self.sent.append(request)
        deal = 202 if self.send_retcode == self.TRADE_RETCODE_DONE else 0
        return Result(self.send_retcode, "Done", 101, deal, request["volume"], request["price"])

    def positions_get(self):
        return self.positions

    def orders_get(self, ticket=None):
        if ticket is None:
            return self.active_orders
        return [order for order in self.active_orders if order.ticket == ticket]

    def history_orders_get(self, *args, ticket=None):
        if ticket is None:
            return self.history_orders
        return [order for order in self.history_orders if order.ticket == ticket]

    def history_deals_get(self, *args, ticket=None):
        return []


class MT5ServiceTests(unittest.TestCase):
    def setUp(self):
        self.db_path = Path(__file__).resolve().parents[1] / "data" / "_test_mt5_gateway.sqlite3"
        self._remove_test_db()
        self.journal = MT5GatewayJournal(self.db_path)
        self.fake = FakeMT5()
        self.service = MT5Service(mt5_module=self.fake, journal=self.journal)
        self.env = patch.dict(
            os.environ,
            {
                "MT5_TERMINAL_PATH": "",
                "MT5_GATEWAY_TOKEN": "unit-test-token",
                "MT5_EXECUTION_MODE": "disabled",
                "MT5_ALLOWED_EXPERTS": "EMA-CROSS-V1",
                "MT5_ALLOWED_SYMBOLS": "EURUSD",
                "MT5_MAX_VOLUME_PER_ORDER": "0.10",
                "MT5_MAX_MARGIN_PER_ORDER": "500",
                "MT5_MAX_RISK_PER_ORDER_PCT": "0.5",
                "MT5_MAX_SPREAD_POINTS": "30",
                "MT5_MAX_TICK_AGE_SECONDS": "5",
                "MT5_MAX_SIGNAL_AGE_SECONDS": "10",
                "MT5_MAX_OPEN_POSITIONS": "3",
                "MT5_MAX_PENDING_ORDERS": "3",
                "MT5_MAX_TOTAL_VOLUME": "0.30",
                "MT5_MAX_SYMBOL_VOLUME": "0.20",
                "MT5_MAX_AGGREGATE_RISK_PCT": "2.0",
                "MT5_MAX_ORDERS_PER_MINUTE": "3",
                "MT5_MAX_ORDERS_PER_DAY": "20",
            },
        )
        self.env.start()

    def tearDown(self):
        self.env.stop()
        self._remove_test_db()

    def _remove_test_db(self):
        for suffix in ("", "-wal", "-shm"):
            candidate = Path(f"{self.db_path}{suffix}")
            if candidate.exists():
                candidate.unlink()

    def intent(self, signal_id="ema-cross-v1:EURUSD:1:BUY"):
        return MT5OrderIntent(
            signal_id=signal_id,
            expert_id="ema-cross-v1",
            symbol="EURUSD",
            side="BUY",
            volume=0.01,
            observed_at_epoch=int(time.time()),
            sl=1.0970,
            tp=1.1040,
        )

    def test_preview_runs_pretrade_checks_without_sending(self):
        preview = asyncio.run(self.service.preview_order(self.intent()))

        self.assertEqual(preview["symbol"], "EURUSD")
        self.assertEqual(preview["account_mode"], "demo")
        self.assertEqual(preview["margin_required"], 50.0)
        self.assertEqual(preview["stop_risk_amount"], 25.0)
        self.assertEqual(self.fake.sent, [])

    def test_disabled_mode_blocks_execution(self):
        with self.assertRaisesRegex(MT5ExecutionBlocked, "disabled"):
            asyncio.run(self.service.execute_order(self.intent()))
        self.assertEqual(self.fake.sent, [])

    def test_paper_mode_executes_once_and_blocks_duplicate_signal(self):
        os.environ["MT5_EXECUTION_MODE"] = "paper"
        result = asyncio.run(self.service.execute_order(self.intent()))

        self.assertEqual(result["state"], "filled")
        self.assertEqual(len(self.fake.sent), 1)
        with self.assertRaisesRegex(MT5ExecutionBlocked, "Duplicate signal_id"):
            asyncio.run(self.service.execute_order(self.intent()))
        self.assertEqual(len(self.fake.sent), 1)

    def test_paper_mode_refuses_real_account(self):
        os.environ["MT5_EXECUTION_MODE"] = "paper"
        self.fake.trade_mode = self.fake.ACCOUNT_TRADE_MODE_REAL

        with self.assertRaisesRegex(MT5ExecutionBlocked, "real MT5 account"):
            asyncio.run(self.service.execute_order(self.intent()))
        self.assertEqual(self.fake.sent, [])

    def test_paper_mode_requires_terminal_algo_trading(self):
        os.environ["MT5_EXECUTION_MODE"] = "paper"
        self.fake.terminal_trade_allowed = False

        with self.assertRaisesRegex(MT5ExecutionBlocked, "Algo Trading"):
            asyncio.run(self.service.execute_order(self.intent()))
        self.assertEqual(self.fake.sent, [])

    def test_status_masks_account_login(self):
        status = asyncio.run(self.service.connect())
        self.assertEqual(status["account"]["login_masked"], "***5678")
        self.assertNotIn("password", str(status).lower())
        self.assertIsNone(self.service.get_status()["account"])

    def test_live_mode_requires_both_server_and_signal_opt_in(self):
        os.environ["MT5_EXECUTION_MODE"] = "live"
        self.fake.trade_mode = self.fake.ACCOUNT_TRADE_MODE_REAL
        live_intent = self.intent()
        live_intent = MT5OrderIntent(**{**live_intent.__dict__, "confirm_live": True})

        with self.assertRaisesRegex(MT5ExecutionBlocked, "server opt-in"):
            asyncio.run(self.service.execute_order(live_intent))
        self.assertEqual(self.fake.sent, [])

    def test_preview_blocks_excess_stop_loss_risk(self):
        os.environ["MT5_MAX_RISK_PER_ORDER_PCT"] = "0.1"

        with self.assertRaisesRegex(MT5ExecutionBlocked, "Stop-loss risk"):
            asyncio.run(self.service.preview_order(self.intent()))
        self.assertEqual(self.fake.sent, [])

    def test_preview_blocks_aggregate_volume_across_bots(self):
        self.fake.positions = [
            Position("EURUSD", 0.15, 1.0950, self.fake.POSITION_TYPE_BUY, 1.1000)
        ]
        os.environ["MT5_MAX_TOTAL_VOLUME"] = "0.15"

        with self.assertRaisesRegex(MT5ExecutionBlocked, "Aggregate volume"):
            asyncio.run(self.service.preview_order(self.intent()))

    def test_unprotected_existing_position_blocks_new_execution(self):
        self.fake.positions = [
            Position("GBPUSD", 0.01, 0.0, self.fake.POSITION_TYPE_BUY, 1.2500)
        ]

        with self.assertRaisesRegex(MT5ExecutionBlocked, "Unprotected"):
            asyncio.run(self.service.preview_order(self.intent()))

    def test_order_rate_limit_is_account_wide(self):
        os.environ["MT5_EXECUTION_MODE"] = "paper"
        os.environ["MT5_MAX_ORDERS_PER_MINUTE"] = "1"
        asyncio.run(self.service.execute_order(self.intent("signal-rate-0001")))

        with self.assertRaisesRegex(MT5ExecutionBlocked, "rate limit"):
            asyncio.run(self.service.execute_order(self.intent("signal-rate-0002")))

    def test_daily_order_limit_is_account_wide(self):
        os.environ["MT5_EXECUTION_MODE"] = "paper"
        os.environ["MT5_MAX_ORDERS_PER_MINUTE"] = "0"
        os.environ["MT5_MAX_ORDERS_PER_DAY"] = "1"
        asyncio.run(self.service.execute_order(self.intent("signal-day-0001")))

        with self.assertRaisesRegex(MT5ExecutionBlocked, "daily order limit"):
            asyncio.run(self.service.execute_order(self.intent("signal-day-0002")))

    def test_live_window_must_be_armed_and_unexpired(self):
        os.environ["MT5_EXECUTION_MODE"] = "live"
        os.environ["MT5_LIVE_TRADING_ENABLED"] = "true"
        self.fake.trade_mode = self.fake.ACCOUNT_TRADE_MODE_REAL
        live_intent = MT5OrderIntent(
            **{**self.intent("signal-live-0001").__dict__, "confirm_live": True}
        )

        with self.assertRaisesRegex(MT5ExecutionBlocked, "expired"):
            asyncio.run(self.service.execute_order(live_intent))

    def test_durable_kill_switch_blocks_orders_until_explicit_reset(self):
        os.environ["MT5_EXECUTION_MODE"] = "paper"

        activated = self.service.activate_kill_switch("unit-test emergency stop")

        self.assertTrue(activated["active"])
        self.assertTrue(self.service.get_status()["kill_switch"]["active"])
        with self.assertRaisesRegex(MT5ExecutionBlocked, "kill switch"):
            asyncio.run(self.service.execute_order(self.intent("signal-kill-0001")))
        self.assertEqual(self.fake.sent, [])

        reset = self.service.reset_kill_switch(confirm="RESET")
        self.assertFalse(reset["active"])
        result = asyncio.run(
            self.service.execute_order(self.intent("signal-kill-0002"))
        )
        self.assertEqual(result["state"], "filled")

    def test_reconciliation_resolves_submitted_order_from_history(self):
        os.environ["MT5_EXECUTION_MODE"] = "paper"
        self.fake.send_retcode = self.fake.TRADE_RETCODE_PLACED
        result = asyncio.run(
            self.service.execute_order(self.intent("signal-reconcile-0001"))
        )
        self.assertEqual(result["state"], "submitted")
        self.fake.history_orders = [
            HistoryOrder(101, self.fake.ORDER_STATE_FILLED)
        ]

        reconciliation = asyncio.run(self.service.reconcile_orders())

        self.assertEqual(reconciliation["changed"], 1)
        entry = self.journal.get("signal-reconcile-0001")
        self.assertEqual(entry["state"], "filled")
        self.assertEqual(
            entry["result"]["reconciliation"]["source"],
            "history_order",
        )

    def test_http_contract_forbids_unknown_execution_fields(self):
        payload = {
            **self.intent("signal-contract-0001").__dict__,
            "bypass_risk": True,
        }
        with self.assertRaises(ValidationError):
            MT5OrderRequest(**payload)


if __name__ == "__main__":
    unittest.main()
