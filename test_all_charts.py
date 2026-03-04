"""Test all chart commands from the help text."""
import requests
import json
import sys

URL = "http://localhost:8282/openbb/cli"

commands = [
    "equity price historical --symbol AAPL --chart true",
    "equity price performance --symbol NVDA --chart true",
    "equity historical_market_cap --symbol TSLA --chart true",
    "crypto price historical --symbol BTC-USD --chart true",
    "currency price historical --symbol EURUSD=X --chart true",
    "etf historical --symbol SPY --chart true",
    "etf holdings --symbol QQQ --chart true",
    "etf price_performance --symbol IWM --chart true",
    "derivatives futures curve --symbol CL --chart true",
    "derivatives futures historical --symbol CL --chart true",
    "derivatives options surface --symbol SPY --chart true",
    "fixedincome government yield_curve --chart true",
    "index price historical --symbol ^GSPC --chart true",
    "economy fred_series --symbol GDP --chart true",
    "economy shipping chokepoint_info --chart true",
    "economy shipping port_info --chart true",
    "economy survey bls_series --symbol CES0000000001 --chart true",
    "technical macd --symbol AAPL --chart true",
    "technical rsi --symbol AAPL --chart true",
    "technical ema --symbol AAPL --length 50 --chart true",
    "technical sma --symbol AAPL --length 200 --chart true",
    "technical wma --symbol AAPL --chart true",
    "technical hma --symbol AAPL --chart true",
    "technical zlma --symbol AAPL --chart true",
    "technical adx --symbol AAPL --chart true",
    "technical aroon --symbol AAPL --chart true",
    "technical cones --symbol AAPL --chart true",
    "technical relative_rotation --symbol AAPL --benchmark ^GSPC --chart true",
    "econometrics correlation_matrix --symbol AAPL,MSFT,NVDA --chart true",
]

print(f"Testing {len(commands)} chart commands...\n")
ok = 0
fail = 0

for cmd in commands:
    try:
        r = requests.post(URL, json={"command": cmd}, timeout=120)
        data = r.json()
        if data.get("type") == "chart_window" and data.get("html"):
            print(f"  OK   | {cmd}")
            ok += 1
        elif data.get("type") == "error":
            msg = data.get("output", data.get("error", "?"))
            print(f"  FAIL | {cmd}")
            print(f"         => {msg[:200]}")
            fail += 1
        else:
            out = data.get("output", str(data))[:200]
            print(f"  WARN | {cmd}")
            print(f"         => {out}")
            fail += 1
    except Exception as e:
        print(f"  ERR  | {cmd}")
        print(f"         => {e}")
        fail += 1
    sys.stdout.flush()

print(f"\n{'='*60}")
print(f"RESULTS: {ok} OK, {fail} FAILED out of {len(commands)} total")
