from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
import json
import asyncio
import os
import sys
import requests
import pandas as pd
from pathlib import Path
from ...core.container import get_quote, get_historical, fmp_provider, yahoo_provider, duckdb_repo
from ...services.risk_service import risk_service
from ...services.standardizer import standardizer
from ...services.openbb_rest_service import openbb_rest
from ...services.openbb_native_service import openbb_native

router = APIRouter()

def _parse_args(parts: list[str]) -> dict:
    """Parse --key value pairs from a command string."""
    kwargs = {}
    i = 0
    while i < len(parts):
        if parts[i].startswith("--"):
            key = parts[i][2:].replace("-", "_")
            if i + 1 < len(parts) and not parts[i+1].startswith("--"):
                kwargs[key] = parts[i+1]
                i += 2
            else:
                kwargs[key] = True
                i += 1
        else:
            i += 1
    return kwargs


def _format_dict(d: dict, indent: int = 0) -> str:
    """Pretty-format a dictionary for terminal display."""
    lines = []
    prefix = "  " * indent
    for k, v in d.items():
        if isinstance(v, float):
            lines.append(f"{prefix}{k}: {v:,.4f}")
        elif isinstance(v, (int,)):
            lines.append(f"{prefix}{k}: {v:,}")
        else:
            lines.append(f"{prefix}{k}: {v}")
    return "\n".join(lines)


@router.post("/openbb/cli")
async def openbb_cli(body: dict = Body(...)):
    """Execute financial data commands via the terminal."""
    cmd_str = body.get("command", "").strip()
    if not cmd_str:
        return {"output": "No command provided."}

    # Strip leading : (vim-style)
    if cmd_str.startswith(":"):
        cmd_str = cmd_str[1:].strip()

    low = cmd_str.lower()
    
    # ─── Qwen AI Assistant ──────────────────────────────────────────
    if low.startswith("qwen ") or low.startswith("q "):
        prompt = cmd_str[4:].strip() if low.startswith("q ") else cmd_str[5:].strip()
        if not prompt:
            return {"output": "Usage: qwen <your question about openbb>"}
        
        nvidia_key = os.getenv("NVIDIA_NIM_API_KEY") or os.getenv("NVIDIA_API_KEY")
        if not nvidia_key:
            return {"output": "Error: NVIDIA_API_KEY environment variable not set.", "type": "error"}
            
        invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {nvidia_key}",
            "Accept": "application/json"
        }
        
        system_msg = (
            "You are an expert OpenBB Platform CLI assistant. "
            "Help the user find the right command. "
            "OpenBB commands follow a path structure like 'equity/price/quote'. "
            "Provide the command first, then a very brief explanation."
        )
        
        payload = {
            "model": "qwen/qwen3.5-397b-a17b",
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 512,
            "temperature": 0.3,
            "stream": False,
        }
        
        try:
            res = requests.post(invoke_url, headers=headers, json=payload, timeout=20)
            res.raise_for_status()
            ai_text = res.json()["choices"][0]["message"]["content"].strip()
            return {"output": f"🤖 Qwen: {ai_text}"}
        except Exception as e:
            return {"output": f"Qwen API Error: {str(e)}", "type": "error"}

    # ─── Built-in commands ──────────────────────────────────────────
    if low in ("help", "h", "?"):
        return {"output": (
            "╔════════════════════════════════════════════════════════════════════════════════════╗\n"
            "║                        🌌 MMAM INTELLIGENCE · OPENBB PLATFORM                      ║\n"
            "║                            ADVANCED CLI TERMINAL v2.5.0                            ║\n"
            "╚════════════════════════════════════════════════════════════════════════════════════╝\n\n"
            "  Welcome to the advanced command-line interface. This terminal integrates\n"
            "  high-performance direct providers and the full OpenBB Native framework capabilities.\n\n"
            "  [ SYNTAX ]\n"
            "  > command --flag value --flag2 value2\n"
            "  > :command  (Vim-style colon is optional but supported)\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━ 📊 CORE MARKET DATA (Lightning Fast) ━━━━━━━━━━━━━━━━━━━━━━\n"
            "  quote          Real-time price quote        | e.g. quote --symbol AAPL\n"
            "  historical     Price history candles        | e.g. historical --symbol TSLA --limit 50\n"
            "  profile        Company overview             | e.g. profile --symbol MSFT\n"
            "  search         Find ticker by name          | e.g. search --query \"nvidia\"\n"
            "  news           Latest market news           | e.g. news --limit 10\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━ 🏦 FUNDAMENTALS & ECONOMY (Aliases)  ━━━━━━━━━━━━━━━━━━━━━━\n"
            "  income         Income statement             | e.g. income --symbol GOOG\n"
            "  balance        Balance sheet                | e.g. balance --symbol AMZN\n"
            "  calendar       Economic calendar            | e.g. calendar\n"
            "  cpi            Consumer Price Index         | e.g. cpi\n"
            "  gdp            Nominal GDP                  | e.g. gdp\n"
            "  treasury       Government Treasury Rates    | e.g. treasury\n"
            "  options        Derivatives options chains   | e.g. options --symbol SPY\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━ ⚙️  OPENBB NATIVE ENGINE (Full API)   ━━━━━━━━━━━━━━━━━━━━━━\n"
            "  You can use ANY standard OpenBB command path.\n"
            "  The terminal routes dynamically into the OpenBB native container wrapper.\n"
            "  Paths:         equity/price/quote --symbol NVDA\n"
            "                 crypto/price/historical --symbol BTC-USD\n"
            "                 fixedincome/corporate/ice_bofa\n\n"
            "  Global Flags:  --chart True                 (Return visual charts when supported)\n"
            "                 --provider [name]            (Force specific data provider)\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━ 🤖 AI COPILOT (NVIDIA NIM)           ━━━━━━━━━━━━━━━━━━━━━━\n"
            "  qwen, q        Ask the AI assistant for command help or financial context.\n"
            "                 e.g. qwen How do I get insider trading data?\n"
            "                 e.g. q What is the command for bond yields?\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━ 🕹️  SYSTEM COMMANDS                   ━━━━━━━━━━━━━━━━━━━━━━\n"
            "  help, h, ?     Display this exhaustive help documentation.\n"
            "  clear          Clear the terminal buffer screen.\n"
        )}

    # ─── Parse command + args ───────────────────────────────────────
    parts = cmd_str.split()
    raw_cmd = parts[0].lower().lstrip("/").replace("/", ".")
    aliases = {
        "quote": "equity.price.quote",
        "price": "equity.price.quote",
        "profile": "equity.profile",
        "income": "equity.fundamental.income",
        "balance": "equity.fundamental.balance",
        "historical": "equity.price.historical",
        "search": "equity.search",
        "news": "news.world",
        "calendar": "economy.calendar",
        "cpi": "economy.cpi",
        "gdp": "economy.gdp.nominal",
        "treasury": "fixedincome.government.treasury_rates",
        "options": "derivatives.options.chains",
    }
    command = aliases.get(raw_cmd, raw_cmd)
    kwargs = _parse_args(parts[1:])

    # ─── Command execution ───────────────────────────────────────────
    try:
        # 1. Direct short-circuit for high-performance providers
        if "chart" not in kwargs:
            if command in ("quote", "price", "equity.price.quote"):
                symbol = kwargs.get("symbol")
                if not symbol: return {"output": "Usage: quote --symbol AAPL", "type": "error"}
                data = await get_quote.execute(symbol)
                if "error" in data: return {"output": f"Error: {data['error']}", "type": "error"}
                return {"output": f"┌─ {data.get('symbol', symbol)} ─────────────────────\n│  Price:    ${data.get('price', 0):,.4f}\n│  Change:   {data.get('change', 0):+,.4f} ({data.get('changePercentage', 0):+.2f}%)\n│  Volume:   {data.get('volume', 'N/A'):,}\n│  Source:   {data.get('source', 'Unknown')}\n└──────────────────────────────────"}

            if command in ("historical", "history", "equity.price.historical"):
                symbol = kwargs.get("symbol")
                if not symbol: return {"output": "Usage: historical --symbol TSLA", "type": "error"}
                limit = int(kwargs.get("limit", 20))
                data = await get_historical.execute(symbol, limit=limit)
                if "error" in data: return {"output": f"Error: {data['error']}", "type": "error"}
                df = pd.DataFrame(data.get("historical", []))
                if df.empty: return {"output": "No historical data found."}
                output = df[["date", "open", "high", "low", "close", "volume"]].tail(limit).to_string(index=False)
                return {"output": f"── {symbol} Historical ({len(df)} candles) ──\n{output}"}

            if command in ("profile", "equity.profile"):
                symbol = kwargs.get("symbol")
                if not symbol: return {"output": "Usage: profile --symbol MSFT", "type": "error"}
                data = await fmp_provider.get_profile(symbol)
                if not data: return {"output": f"Profile not found for {symbol}.", "type": "error"}
                return {"output": _format_dict(data)}

            if command in ("search", "equity.search"):
                query = kwargs.get("query", kwargs.get("symbol", ""))
                if not query: return {"output": "Usage: search --query nvidia", "type": "error"}
                results = await yahoo_provider.search(query)
                if not results: return {"output": f"No results for '{query}'."}
                lines = [f"  {r.get('symbol', '?'):>10}  │  {r.get('name', '?')}" for r in results[:15]]
                return {"output": f"── Search: \"{query}\" ({len(results)} results) ──\n" + "\n".join(lines)}

        # 2. Native OpenBB execution via subprocess container
        result = await openbb_native.execute(command, kwargs)
        if "error" in result:
            return {"output": result["error"], "type": "error"}
        return {"output": result.get("output", "Command executed.")}

    except TypeError as e:
        return {"output": f"Parameter error: {str(e)}", "type": "error"}
    except Exception as e:
        return {"output": f"Error: {str(e)}", "type": "error"}


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

@router.get("/widgets.json")
async def get_widgets():
    path = BASE_DIR / "widgets.json"
    if not path.exists(): return JSONResponse(content={"error": "widgets.json not found"}, status_code=404)
    with open(path, "r") as f: return JSONResponse(content=json.load(f))

@router.get("/apps.json")
async def get_apps():
    path = BASE_DIR / "apps.json"
    if not path.exists(): return JSONResponse(content={"error": "apps.json not found"}, status_code=404)
    with open(path, "r") as f: return JSONResponse(content=json.load(f))

@router.get("/widgets/portfolio")
async def widget_portfolio():
    holdings = duckdb_repo.get_portfolio()
    total_val = sum(h['shares'] * h['entryPrice'] for h in holdings) if holdings else 0
    return standardizer.to_openbb_metric("Current Portfolio Value", f"${total_val:,.2f}", change="+0.0%", is_positive=True)

@router.get("/widgets/sentiment")
async def widget_sentiment():
    holdings = duckdb_repo.get_portfolio()
    risk_report = risk_service.get_portfolio_risk_report(holdings)
    if "error" in risk_report: body = "Sentiment analysis currently unavailable — insufficient market data."
    else:
        var = risk_report.get('mvar_95_percent', 0)
        sharpe = risk_report.get('sharpe_ratio', 0)
        status = "BULLISH" if sharpe > 1 else ("NEUTRAL" if sharpe > 0 else "CAUTIOUS")
        body = f"**Current Stance:** {status}\n\n**Risk Metrics:**\n- Modified VaR (95%): {var}%\n- Portfolio Sharpe: {sharpe}\n- Data Coverage: {risk_report.get('coverage_percent')}%"
    return standardizer.to_openbb_text("MMAM Neural Sentiment", body)

@router.get("/widgets/trades")
async def widget_trades():
    txs = duckdb_repo.get_transactions()
    recent = txs[-10:] if txs else []
    formatted = [{"Date": t.get("date"), "Symbol": t.get("symbol"), "Type": t.get("type"), "Quantity": t.get("shares"), "Price": f"${t.get('price', 0):,.2f}", "PnL": f"${t.get('realized_pnl', 0):,.2f}"} for t in recent]
    return standardizer.to_openbb_table(formatted)
