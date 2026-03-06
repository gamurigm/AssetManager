from fastapi import APIRouter, Body, Query
from fastapi.responses import JSONResponse
import json
import asyncio
import os
import sys
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

def _load_prompt(filename: str) -> str:
    """Load Markdown prompt from the prompts directory."""
    prompt_path = Path(__file__).parent.parent.parent / "agents" / "team" / "prompts" / filename
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error loading prompt {filename}: {e}")
        return ""

from ...core.container import get_quote, get_historical, fmp_provider, yahoo_provider, duckdb_repo, calculate_equity_curve_uc, portfolio_charts, quant_models, ml_models
from ...services.risk_service import risk_service
from ...services.standardizer import standardizer
from ...services.openbb_rest_service import openbb_rest
from ...services.openbb_native_service import openbb_native, get_chart_html

router = APIRouter()

def _parse_args(parts: list[str]) -> dict:
    """Parse --key value pairs from a command string."""
    kwargs = {}
    i = 0
    while i < len(parts):
        if parts[i].startswith("--"):
            key = parts[i][2:].replace("-", "_")
            if i + 1 < len(parts) and not parts[i+1].startswith("--"):
                val = parts[i+1]
                if val.lower() == "true":
                    val = True
                elif val.lower() == "false":
                    val = False
                kwargs[key] = val
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
    if low.startswith("qwen ") or low.startswith("q ") or low.startswith("/qwen "):
        prompt = cmd_str
        if low.startswith("/qwen "):
            prompt = cmd_str[6:].strip()
        elif low.startswith("qwen "):
            prompt = cmd_str[5:].strip()
        else:
            prompt = cmd_str[2:].strip()
            
        if not prompt:
            return {"output": "Usage: /qwen <your instruction>"}
        
        nvidia_key = os.getenv("NVIDIA_NIM_API_KEY") or os.getenv("NVIDIA_API_KEY")
        if not nvidia_key:
            return {"output": "Error: NVIDIA_API_KEY environment variable not set.", "type": "error"}
            
        invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {nvidia_key}",
            "Accept": "application/json"
        }
        
        system_msg = _load_prompt("terminal_qwen.md")
        if not system_msg:
            system_msg = "You are Qwen, the expert Terminal Executor for the MMAM investment app." # Fallback
        
        payload = {
            "model": "qwen/qwen3.5-397b-a17b",
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 512,
            "temperature": 0.1,
            "stream": False,
        }
        
        models_to_try = [
            ("qwen/qwen3.5-397b-a17b", 25),
            ("meta/llama3-70b-instruct", 35),
            ("mistralai/mixtral-8x22b-instruct-v0.1", 45)
        ]
        
        last_error = None
        for model_id, timeout_sec in models_to_try:
            payload["model"] = model_id
            try:
                res = requests.post(invoke_url, headers=headers, json=payload, timeout=timeout_sec)
                res.raise_for_status()
                ai_text = res.json()["choices"][0]["message"]["content"].strip()
                
                if "<execute>" in ai_text and "</execute>" in ai_text:
                    cmd_to_run = ai_text.split("<execute>")[1].split("</execute>")[0].strip()
                    # Run the command recursively
                    inner_res = await openbb_cli({"command": cmd_to_run})
                    inner_output = inner_res.get("output", "Done")
                    model_name = model_id.split('/')[1].split('-')[0].upper()
                    return {"output": f"🤖 [{model_name} EXECUTOR]: Entendido. Preparando ejecución...\n⚡ Ejecutando: {cmd_to_run}\n\n{inner_output}"}
                
                model_name = model_id.split('/')[1].split('-')[0].capitalize()
                return {"output": f"🤖 {model_name}: {ai_text}"}
                
            except Exception as e:
                last_error = e
                print(f"[LLM Failover] {model_id} failed: {e}. Trying next...")
                continue
                
        return {"output": f"LLM Connectivity Error (Failover exhausted). Last Error: {str(last_error)}", "type": "error"}

    # ─── Built-in commands ──────────────────────────────────────────
    if low in ("help", "h", "?"):
        return {"output": _load_prompt("terminal_help.md")}

    # ─── Parse command + args ───────────────────────────────────────
    parts = cmd_str.split()

    # Consume all leading non-flag tokens as the command path
    # e.g. "index price historical --symbol ^NDX" → path="index.price.historical", rest=[--symbol, ^NDX]
    path_tokens = []
    rest_tokens = []
    for i, tok in enumerate(parts):
        if tok.startswith("--") or tok.startswith("-"):
            rest_tokens = parts[i:]
            break
        path_tokens.append(tok)
    else:
        # No flags found at all
        rest_tokens = []

    if not path_tokens:
        return {"output": "Empty command.", "type": "error"}

    raw_cmd = ".".join(t.lower().lstrip("/").replace("/", ".") for t in path_tokens)

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
        "ratio": "models.ratio",
        "bs": "models.blackscholes",
        "hmm": "ml.hmm",
        "mc": "ml.montecarlo",
        "buy": "portfolio.buy",
        "sell": "portfolio.sell",
        "modify": "portfolio.modify",
        "positions": "portfolio.positions",
        "assets": "equity.search_all",
        "cash": "equity.fundamental.cash",
        "dividends": "equity.fundamental.dividends",
        "earnings": "equity.calendar.earnings",
        "estimates": "equity.estimates.price_target",
        "insiders": "equity.ownership.insider_trading",
        "institutional": "equity.ownership.institutional",
        "short": "equity.short.interest",
        "yieldcurve": "fixedincome.government.yield_curve",
        "unemployment": "economy.unemployment",
        "fedfunds": "economy.fed_funds",
        "etf_holdings": "etf.holdings",
        "index_members": "index.constituents",
        "gainers": "equity.discovery.gainers",
        "losers": "equity.discovery.losers",
        "active": "equity.discovery.active",
    }
    # Only apply alias if it's a single-token shortcut OR starts with an alias
    command = aliases.get(raw_cmd, raw_cmd)
    kwargs = {}
    
    # Handle aliases with positional arguments (e.g. "ratio AAPL MSFT")
    if "." in raw_cmd:
        base = raw_cmd.split(".")[0]
        if base in aliases:
            command = aliases[base]
            # Put the rest of the tokens into placeholders if needed
            extra_tokens = path_tokens[1:]
            if base == "ratio" and len(extra_tokens) >= 2:
                kwargs["symbol1"] = extra_tokens[0].upper()
                kwargs["symbol2"] = extra_tokens[1].upper()
            elif base in ("bs", "hmm", "mc", "positions", "quote", "price", "historical", "history", "profile", "income", "balance", "cash", "dividends", "earnings", "estimates", "insiders", "institutional", "short", "etf_holdings", "index_members", "gainers", "losers", "active") and len(extra_tokens) >= 1:
                kwargs["symbol"] = extra_tokens[0].upper()
            elif base in ("buy", "sell") and len(extra_tokens) >= 2:
                kwargs["symbol"] = extra_tokens[0].upper()
                val = extra_tokens[1].lower()
                if val.endswith('$') or val.startswith('$'):
                    kwargs["usd"] = val.replace('$', '')
                else:
                    kwargs["shares"] = val
            elif base == "modify" and len(extra_tokens) >= 1:
                kwargs["symbol"] = extra_tokens[0].upper()
        

    kwargs.update(_parse_args(rest_tokens))

    # ─── Smart Default Providers ────────────────────────────────────
    if "provider" not in kwargs:
        if command in ("index.constituents", "etf.holdings") or command.startswith("equity.discovery."):
            kwargs["provider"] = "fmp"
        elif command.startswith(("equity.", "derivatives.", "etf.", "index.", "crypto.")):
            kwargs["provider"] = "yfinance"
        elif command.startswith("economy.") or command.startswith("fixedincome."):
            kwargs["provider"] = "bls" if "bls" in command else "fred"

    # Strip '^' for FMP indices if needed (symbol normalization)
    if kwargs.get("provider") == "fmp" and "symbol" in kwargs:
        kwargs["symbol"] = str(kwargs["symbol"]).lstrip("^")

    # ─── Portfolio Liquidator ───────────────────────────────────────
    if command == "portfolio.liquidate":
        portfolio_id = str(kwargs.get("portfolio", "main")).lower()
        holdings = duckdb_repo.get_portfolio(portfolio_id)
        if not holdings:
            return {"output": "No active holdings found in portfolio to liquidate."}
            
        liquidated_symbols = []
        keep_holdings = []
        is_all = kwargs.get("all") or kwargs.get("all") is True
        is_losers = kwargs.get("losers") or kwargs.get("losers") is True
        target_symbol = str(kwargs.get("symbol")).upper() if kwargs.get("symbol") else None
        
        for h in holdings:
            sym = h.get("symbol", "")
            # --- FETCH CURRENT PRICE FOR ACCURATE PNL ---
            current_price = h.get("price", 0)
            if not current_price or current_price == 0:
                try:
                    # FIX: get_quote is an instance of GetQuoteUseCase, must call .execute() and await it
                    quote_data = await get_quote.execute(sym)
                    current_price = float(quote_data.get("price", quote_data.get("last_price", h.get("entryPrice", 0))))
                except Exception as e:
                    print(f"[Liquidation] Price fetch error for {sym}: {e}")
                    current_price = h.get("entryPrice", 0)
            
            entry_price = h.get("entryPrice", 0)
            factor = h.get("factor", 1)
            shares = h.get("shares", 0)
            
            # Recalculate PnL based on fresh (or best available) price
            pnl = (current_price - entry_price) * shares * factor
            pnl_pct = ((current_price - entry_price) / entry_price * 100) if entry_price != 0 else 0
            
            should_sell = False
            if is_all:
                should_sell = True
            elif is_losers and (pnl < 0 or pnl_pct < 0):
                should_sell = True
            elif target_symbol and sym == target_symbol:
                should_sell = True
                
            if should_sell:
                # Add to liquidated list with detailed PnL
                liquidated_symbols.append(f"{sym} ({'+' if pnl >= 0 else ''}${pnl:,.2f})")
                duckdb_repo.add_transaction(
                    type_str="SELL",
                    symbol=sym,
                    shares=shares,
                    price=current_price,
                    realized_pnl=pnl,
                    portfolio_id=portfolio_id
                )
            else:
                keep_holdings.append(h)
                
        if not liquidated_symbols:
            criteria = "TODO" if is_all else ("EN ROJO" if is_losers else (f"SYMBOL {target_symbol}" if target_symbol else "N/A"))
            return {"output": f"⚠️ No se encontraron activos que cumplan el criterio: [{criteria}].\n\nSi quieres vender TODO independientemente del PnL, usa: 'portfolio liquidate --all' o dile a Qwen 'vende absolutamente todo'."}
            
        success = duckdb_repo.save_portfolio(keep_holdings, portfolio_id)
        if success:
            total_realized = sum(float(s.split('($')[1].split(')')[0].replace(',','')) for s in liquidated_symbols if '($' in s)
            return {"output": (
                f"🚨 LIQUIDATION COMPLETE 🚨\n"
                f"Total Positions Sold: {len(liquidated_symbols)}\n"
                f"Details: {', '.join(liquidated_symbols)}\n"
                f"PROFIT/LOSS REALIZED THIS RUN: {'+' if total_realized >= 0 else ''}${total_realized:,.2f}\n\n"
                f"✅ Cash updated in balance sheets."
            )}
        else:
            return {"output": "Error: Database failed to persist the liquidation.", "type": "error"}

    # ─── New Trading Commands ───────────────────────────────────────
    if command == "portfolio.buy":
        symbol = kwargs.get("symbol")
        shares = float(kwargs.get("shares", 0))
        usd_val = str(kwargs.get("usd", "0")).lower()
        if not symbol or (shares <= 0 and usd_val == "0"):
            return {"output": "Usage: buy --symbol AAPL --shares 10 (OR --usd 5000) [--price 150] [--sl 140] [--tp 180]", "type": "error"}
        
        symbol = symbol.upper()
        price_str = str(kwargs.get("price", "0")).lower()
        # Simple handling for 'k' notation
        if price_str.endswith('k'): price = float(price_str[:-1]) * 1000
        else:
            try: price = float(price_str)
            except ValueError: price = 0
        
        if price <= 0:
            quote = await get_quote.execute(symbol)
            if "error" in quote: return {"output": f"Error fetching price: {quote['error']}", "type": "error"}
            price = float(quote.get("price", 0))

        # Calculate shares from USD if provided
        if usd_val != "0":
            total_usd = float(usd_val[:-1]) * 1000 if usd_val.endswith('k') else float(usd_val)
            shares = total_usd / price

        portfolio_id = str(kwargs.get("portfolio", "main")).lower()

        # Add Transaction
        duckdb_repo.add_transaction("BUY", symbol, shares, price, portfolio_id=portfolio_id)
        
        # Reconcile Portfolio
        holdings = duckdb_repo.get_portfolio(portfolio_id)
        existing = next((h for h in holdings if h['symbol'] == symbol), None)
        
        if existing:
            # Weighted average entry
            old_total = existing['shares'] * existing['entryPrice']
            new_total = shares * price
            existing['shares'] += shares
            existing['entryPrice'] = (old_total + new_total) / existing['shares']
            if kwargs.get("sl"): existing['sl'] = float(kwargs.get("sl"))
            if kwargs.get("tp"): existing['tp'] = float(kwargs.get("tp"))
        else:
            holdings.append({
                "symbol": symbol,
                "name": symbol,
                "shares": shares,
                "entryPrice": price,
                "factor": 1.0,
                "sector": "Other",
                "type": "stock",
                "purchaseDate": datetime.now().strftime("%Y-%m-%d"),
                "sl": float(kwargs.get("sl")) if kwargs.get("sl") else None,
                "tp": float(kwargs.get("tp")) if kwargs.get("tp") else None
            })
        
        duckdb_repo.save_portfolio(holdings, portfolio_id)
        return {"output": f"✅ BUY ORDER EXECUTED [{portfolio_id.upper()}]\nSymbol: {symbol}\nShares: {shares}\nPrice:  ${price:,.4f}\nTotal:  ${(shares*price):,.2f}\nSL:     {kwargs.get('sl') or 'None'} | TP: {kwargs.get('tp') or 'None'}"}

    if command == "portfolio.sell":
        symbol = kwargs.get("symbol")
        shares = float(kwargs.get("shares", 0))
        usd_val = str(kwargs.get("usd", "0")).lower()
        if not symbol or (shares <= 0 and usd_val == "0"):
            return {"output": "Usage: sell --symbol AAPL --shares 5 (OR --usd 1000) [--price 160]", "type": "error"}
        
        symbol = symbol.upper()
        portfolio_id = str(kwargs.get("portfolio", "main")).lower()
        holdings = duckdb_repo.get_portfolio(portfolio_id)
        existing = next((h for h in holdings if h['symbol'] == symbol), None)
        if not existing:
            return {"output": f"❌ No position found for {symbol}", "type": "error"}

        price_str = str(kwargs.get("price", "0")).lower()
        if price_str.endswith('k'): price = float(price_str[:-1]) * 1000
        else:
            try: price = float(price_str)
            except ValueError: price = 0

        if price <= 0:
            quote = await get_quote.execute(symbol)
            price = float(quote.get("price", existing['entryPrice']))

        # Calculate shares from USD if provided
        if usd_val != "0":
            total_usd = float(usd_val[:-1]) * 1000 if usd_val.endswith('k') else float(usd_val)
            shares = total_usd / price

        if existing['shares'] < shares:
            return {"output": f"❌ Insufficient shares for {symbol}. Available: {existing['shares']:.4f} ($ {existing['shares']*price:,.2f})", "type": "error"}

        # Calculate PnL
        pnl = (price - existing['entryPrice']) * shares
        duckdb_repo.add_transaction("SELL", symbol, shares, price, realized_pnl=pnl, portfolio_id=portfolio_id)

        # Update Portfolio
        existing['shares'] -= shares
        if existing['shares'] <= 0.0001: # handle floating point
            holdings = [h for h in holdings if h['symbol'] != symbol]
        
        duckdb_repo.save_portfolio(holdings, portfolio_id)
        return {"output": f"✅ SELL ORDER EXECUTED [{portfolio_id.upper()}]\nSymbol: {symbol}\nShares: {shares}\nPrice:  ${price:,.4f}\nTotal:  ${(shares*price):,.2f}\nRealized PnL: {'+' if pnl >= 0 else ''}${pnl:,.2f}"}

    if command == "portfolio.modify":
        symbol = kwargs.get("symbol")
        portfolio_id = str(kwargs.get("portfolio", "main")).lower()
        if not symbol: return {"output": "Usage: modify --symbol AAPL --sl 140 --tp 180", "type": "error"}
        symbol = symbol.upper()
        holdings = duckdb_repo.get_portfolio(portfolio_id)
        existing = next((h for h in holdings if h['symbol'] == symbol), None)
        if not existing: return {"output": f"❌ No position found for {symbol}", "type": "error"}

        if kwargs.get("sl"): existing['sl'] = float(kwargs.get("sl"))
        if kwargs.get("tp"): existing['tp'] = float(kwargs.get("tp"))
        
        duckdb_repo.save_portfolio(holdings, portfolio_id)
        return {"output": f"✅ POSITION MODIFIED: {symbol}\nStop Loss:  {existing.get('sl', 'None')}\nTake Profit: {existing.get('tp', 'None')}"}

    if command == "portfolio.positions":
        portfolio_id = str(kwargs.get("portfolio", "main")).lower()
        holdings = duckdb_repo.get_portfolio(portfolio_id)
        if not holdings:
            return {"output": f"No open positions in [{portfolio_id.upper()}]."}
        
        lines = [f"{'SYMBOL':<8} │ {'SHARES':>10} │ {'ENTRY':>10} │ {'S/L':>10} │ {'T/P':>10}"]
        lines.append("─" * 60)
        for h in holdings:
            sl = f"{h.get('sl'):.2f}" if h.get('sl') else "n/a"
            tp = f"{h.get('tp'):.2f}" if h.get('tp') else "n/a"
            lines.append(f"{h['symbol']:<8} │ {h['shares']:>10.4f} │ {h['entryPrice']:>10.2f} │ {sl:>10} │ {tp:>10}")
        
        return {"output": "── Open Positions ──\n" + "\n".join(lines)}

    # ─── Portfolio Dynamic Charts ───────────────────────────────────
    if command == "portfolio.pie":
        html = await portfolio_charts.get_allocation_pie()
        return {"type": "chart_window", "html": html}
        
    if command == "portfolio.risk":
        html = await portfolio_charts.get_risk_analysis()
        return {"type": "chart_window", "html": html}
        
    if command == "portfolio.performance":
        html = await portfolio_charts.get_pnl_performance()
        return {"type": "chart_window", "html": html}

    if command == "portfolio.equity":
        html = await portfolio_charts.get_equity_curve()
        return {"type": "chart_window", "html": html}

    if command == "portfolio.3d":
        html = await portfolio_charts.get_3d_risk_return()
        return {"type": "chart_window", "html": html}

    if command == "portfolio.distribution":
        html = await portfolio_charts.get_returns_distribution()
        return {"type": "chart_window", "html": html}

    # ─── Quantitative 3D Models ──────────────────────────────────────
    if command == "models.options.surface":
        symbol = kwargs.get("symbol", "SPY")
        html = await quant_models.get_volatility_surface(symbol)
        return {"type": "chart_window", "html": html}

    if command == "models.yield.surface":
        html = await quant_models.get_yield_surface()
        return {"type": "chart_window", "html": html}

    if command == "models.pca.clusters":
        symbols = kwargs.get("symbols", kwargs.get("symbol", "AAPL,MSFT,NVDA,TSLA,META,AMZN,GOOGL,JPM,V,JNJ"))
        html = await quant_models.get_pca_clusters(symbols)
        return {"type": "chart_window", "html": html}

    if command == "models.blackscholes":
        symbol = kwargs.get("symbol", "SPY")
        rf = float(kwargs.get("rf", 0.045))  # Default risk free rate 4.5%
        html = await quant_models.get_black_scholes(symbol, risk_free_rate=rf)
        return {"type": "chart_window", "html": html}

    if command == "models.ratio":
        # Supports --symbol1 AAPL --symbol2 MSFT or generic --symbol AAPL,MSFT
        s1 = kwargs.get("symbol1")
        s2 = kwargs.get("symbol2")
        if not s1 or not s2:
            syms = kwargs.get("symbol", "NVDA,INTC").split(',')
            s1 = syms[0] if len(syms) > 0 else "NVDA"
            s2 = syms[1] if len(syms) > 1 else "INTC"
        html = await quant_models.get_relative_strength(s1, s2)
        return {"type": "chart_window", "html": html}

    # ─── Machine Learning Models ─────────────────────────────────────
    if command == "ml.hmm":
        symbol = kwargs.get("symbol", "SPY")
        html = await ml_models.get_hmm_regimes(symbol)
        return {"type": "chart_window", "html": html}

    if command == "ml.montecarlo":
        symbol = kwargs.get("symbol", "SPY")
        days = int(kwargs.get("days", 60))
        sims = int(kwargs.get("sims", 500))
        html = await ml_models.get_monte_carlo(symbol, days=days, sims=sims)
        return {"type": "chart_window", "html": html}

    if command == "ml.clusters":
        symbols = kwargs.get("symbols", kwargs.get("symbol", "AAPL,MSFT,NVDA,TSLA,META,AMZN,GOOGL,JPM,V,JNJ,XOM,PFE,KO,DIS,NFLX"))
        n_clusters = int(kwargs.get("clusters", 4))
        html = await ml_models.get_kmeans_clusters(symbols, n_clusters=n_clusters)
        return {"type": "chart_window", "html": html}

    if command == "ml.bootstrap":
        symbol = kwargs.get("symbol", "SPY")
        n_resamples = int(kwargs.get("samples", kwargs.get("resamples", 1000)))
        block_size = int(kwargs.get("block", kwargs.get("block_size", 5)))
        horizon = int(kwargs.get("horizon", kwargs.get("days", 60)))
        confidence = float(kwargs.get("confidence", 95.0))
        html = await ml_models.get_bootstrap(symbol, n_resamples=n_resamples, block_size=block_size, horizon=horizon, confidence=confidence)
        return {"type": "chart_window", "html": html}

    if command == "ml.intraday":
        symbol = kwargs.get("symbol", "AAPL")
        html = await ml_models.get_intraday_anomaly(symbol)
        return {"type": "chart_window", "html": html}

    # ─── Command execution ───────────────────────────────────────────
    try:
        # 0. Charts — run via native OpenBB, return full HTML to open in new browser window
        if kwargs.get("chart"):
            native_result = await openbb_native.execute(command, kwargs)
            if native_result.get("type") == "chart_window" and "html" in native_result:
                return {"type": "chart_window", "html": native_result["html"]}
            err_msg = native_result.get("error") or "Chart generation failed"
            return {"output": err_msg, "type": "error"}

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
                results = await yahoo_provider.search_ticker(query)
                if not results: return {"output": f"No results for '{query}'."}
                lines = [f"  {r.get('symbol', '?'):>10}  │  {r.get('name', '?')}" for r in results[:15]]
                return {"output": f"── Search: \"{query}\" ({len(results)} results) ──\n" + "\n".join(lines)}

            if command == "equity.search_all":
                query = kwargs.get("query", "")
                limit = int(kwargs.get("limit", 20))
                
                if query:
                    # Broad search via FMP or Yahoo
                    results = await fmp_provider.search_ticker(query, limit=limit)
                    if not results: results = await yahoo_provider.search_ticker(query, limit=limit)
                    title = f"Search: \"{query}\""
                else:
                    # Return global list from FMP
                    results = await fmp_provider.get_stock_list()
                    if not results:
                        # Fallback: A diverse mix of global assets if the list fails
                        fallback_queries = ["AAPL", "BTC-USD", "EURUSD=X", "^GSPC", "TSLA", "NVDA", "GC=F", "CL=F", "MSFT", "ETH-USD"]
                        results = []
                        for sym in fallback_queries[:limit]:
                            results.append({"symbol": sym, "name": sym, "stockExchange": "GLOBAL", "exchangeShortName": "MKT"})
                        title = "Global Market Pulse (Mix)"
                    else:
                        title = "Global Asset List (First 20)"
                
                if not results: return {"output": "No se encontraron activos. Intenta con una búsqueda específica: 'assets --query AAPL'"}
                
                lines = [f"  {r.get('symbol', r.get('ticker', '?')):<10} │ {r.get('name', '?')[:40]:<40} │ {r.get('exchangeShortName', r.get('exchange', r.get('stockExchange', 'N/A')))}" for r in results[:limit]]
                header = f"{'SYMBOL':<10} │ {'NAME':<40} │ {'EXCHANGE'}"
                return {"output": f"── {title} ──\n{header}\n" + ("─" * 70) + "\n" + "\n".join(lines)}

        # 2. OpenBB REST API (primary — fast, no subprocess overhead)
        rest_result = await openbb_rest.execute(command, kwargs)
        if "error" not in rest_result:
            return {"output": rest_result.get("output", "Command executed.")}

        # 3. Fallback to native subprocess if REST server is offline
        if "not running" in rest_result.get("error", "").lower() or "offline" in rest_result.get("error", "").lower():
            native_result = await openbb_native.execute(command, kwargs)
            if "error" in native_result:
                return {"output": native_result["error"], "type": "error"}
            return {"output": native_result.get("output", "Command executed.")}

        # REST returned an error (but server was reachable)
        return {"output": rest_result.get("error", "Unknown error"), "type": "error"}

    except TypeError as e:
        return {"output": f"Parameter error: {str(e)}", "type": "error"}
    except Exception as e:
        return {"output": f"Error: {str(e)}", "type": "error"}


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

@router.post("/openbb/chart")
async def openbb_chart(body: dict = Body(...)):
    """
    Execute an OpenBB command and return the Plotly figure as JSON for inline rendering.
    The frontend renders it with Plotly.js embedded in the terminal panel.

    Body: { "command": "equity.price.historical --symbol AAPL --provider yfinance" }
    Returns: Plotly JSON figure or { "error": "..." }
    """
    cmd_str = body.get("command", "").strip()
    if not cmd_str:
        return JSONResponse({"error": "No command provided."}, status_code=400)

    parts   = cmd_str.split()
    raw_cmd = parts[0].lower().lstrip("/").replace("/", ".")
    aliases = {
        "historical": "equity.price.historical",
        "history":    "equity.price.historical",
        "quote":      "equity.price.quote",
        "price":      "equity.price.quote",
        "options":    "derivatives.options.chains",
        "cpi":        "economy.cpi",
        "gdp":        "economy.gdp.nominal",
        "treasury":   "fixedincome.government.treasury_rates",
    }
    command = aliases.get(raw_cmd, raw_cmd)
    kwargs  = _parse_args(parts[1:])
    kwargs.pop("chart", None)  # managed here

    if "provider" not in kwargs:
        if command.startswith("equity.") or command.startswith("derivatives."):
            kwargs["provider"] = "yfinance"
        elif command.startswith("economy.") or command.startswith("fixedincome."):
            kwargs["provider"] = "bls" if "bls" in command else "fred"

    result = await get_chart_html(command, kwargs)

    if result.get("type") == "chart_window" and "html" in result:
        from fastapi.responses import HTMLResponse
        return HTMLResponse(content=result["html"])
    err = result.get("error", "Chart generation failed")
    return JSONResponse({"error": err}, status_code=422)


