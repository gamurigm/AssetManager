# AssetManager MetaTrader 5 Expert Gateway

This integration keeps strategy generation inside an MQL5 Expert Advisor while
all execution passes through the AssetManager risk gateway.

## Safety model

- `MT5_EXECUTION_MODE=disabled` accepts previews but never sends an order.
- `paper` only sends to MT5 demo or contest accounts.
- `live` requires a real account, `MT5_LIVE_TRADING_ENABLED=true`, and the EA
  must send `confirm_live=true`.
- Expert IDs and symbols must be explicitly allowlisted.
- Every signal has a unique `signal_id`; duplicates are blocked durably in
  `backend/data/mt5_gateway.sqlite3`.
- Quote age, signal age, spread, volume, margin, stops, and `order_check` are
  validated before `order_send`.
- Open positions are evaluated as one account-wide exposure: position count,
  pending orders, total/symbol volume, aggregate stop risk, and unprotected
  positions can all block a new Expert signal.
- A durable rate limit blocks bot bursts across all Experts.
- Algo Trading must be enabled, and projected stop-loss risk must remain under
  the configured percentage of account equity.
- Live execution also requires `MT5_LIVE_ARMED_UNTIL_EPOCH` to be in the
  future. Use a short window so the gateway disarms itself automatically.
- Unresolved `submitted`, `partial`, and `unknown` journal records can be
  reconciled against the terminal's active orders and history.

## Setup

1. Copy the variables from `backend/mt5.env.example` into `backend/.env` and
   replace the token and account values. Start with `disabled`.
2. In MetaTrader 5 open **Tools → Options → Expert Advisors** and add
   `http://127.0.0.1:8282` to the allowed WebRequest URLs.
3. Copy `Include/AssetManagerBridge.mqh` to `MQL5/Include/` and the files under
   `Experts/` to `MQL5/Experts/`, then compile in MetaEditor.
4. Attach `AssetManagerEmaCrossEA` to a demo chart. Keep `ExecuteSignals=false`
   until previews appear in the AssetManager Experts panel.
5. Change the backend to `MT5_EXECUTION_MODE=paper`, restart it, and only then
   enable `ExecuteSignals` in the EA.

For live, keep the window short. In PowerShell, a 15-minute arm timestamp is:

```powershell
[DateTimeOffset]::UtcNow.AddMinutes(15).ToUnixTimeSeconds()
```

Put that value in `MT5_LIVE_ARMED_UNTIL_EPOCH`, restart the backend, verify the
real account and limits in the UI, then set `ConfirmLive=true` on the intended
EA only.

MT5 `WebRequest` is synchronous and unavailable in Strategy Tester. Backtest
the EA's signal logic natively in MT5; use the gateway for forward/demo and live
execution only.

## API contract

- `GET /api/v1/trading/mt5/status`
- `POST /api/v1/trading/mt5/connect`
- `POST /api/v1/trading/mt5/preview`
- `POST /api/v1/trading/mt5/orders`
- `POST /api/v1/trading/mt5/experts/signals`
- `GET /api/v1/trading/mt5/experts/orders`
- `GET /api/v1/trading/mt5/positions`
- `POST /api/v1/trading/mt5/reconcile`

All endpoints except sanitized status require `X-MT5-Gateway-Token`.
