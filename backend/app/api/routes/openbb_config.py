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
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ...services.asset_classification_service import classify_assets

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
from ...services.ibkr_service import ibkr_service
from ...services.ctrader_service import ctrader_service

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


def _apply_alias_positionals(base: str, extra_tokens: list[str], kwargs: dict) -> None:
    """Map positional terminal arguments onto alias kwargs before flag parsing."""
    if not extra_tokens:
        return

    if base == "ratio" and len(extra_tokens) >= 2:
        kwargs["symbol1"] = extra_tokens[0].upper()
        kwargs["symbol2"] = extra_tokens[1].upper()
        return

    if base in {
        "bs", "fft", "hmm", "mc", "positions", "quote", "price",
        "historical", "history", "profile", "income", "balance", "cash",
        "dividends", "earnings", "estimates", "insiders", "institutional",
        "short", "etf_holdings", "index_members", "gainers", "losers",
        "active", "modify",
    }:
        kwargs["symbol"] = extra_tokens[0].upper()
        return

    if base in {"buy", "sell"}:
        kwargs["symbol"] = extra_tokens[0].upper()
        if len(extra_tokens) >= 2:
            value = extra_tokens[1].lower()
            if value.endswith('$') or value.startswith('$'):
                kwargs["usd"] = value.replace('$', '')
            else:
                kwargs["shares"] = value


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


# ─── Factor Analysis / Sector Correlation chart builder ───────────────────────
async def _generate_factor_html(tickers_str: str, benchmark: str = "SPY", days: int = 252) -> str:
    """Fetch data, compute CAPM + PCA + sector correlations, return Plotly full-HTML."""
    from ...services.math_core import math_core  # local import to avoid circular

    tickers = [t.strip().upper() for t in tickers_str.split(",") if t.strip()]
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    asset_classifications = await classify_assets(tickers, benchmark=benchmark)

    # ── Fetch returns from DuckDB ───────────────────────────────────
    needed_sector_etfs = {asset_classifications[t]["sector_etf"] for t in tickers if t in asset_classifications}
    symbols_to_load = list(set(tickers + [benchmark] + list(needed_sector_etfs)))

    all_returns: dict[str, np.ndarray] = {}
    conn = duckdb_repo._connect(read_only=True)
    try:
        for sym in symbols_to_load:
            df = conn.execute(
                "SELECT date, close FROM ohlcv WHERE symbol = ? AND date >= ? ORDER BY date ASC",
                [sym, start_date.date()],
            ).df()
            if not df.empty and len(df) > 10:
                df["returns"] = df["close"].pct_change().fillna(0)
                all_returns[sym] = df["returns"].values
    finally:
        conn.close()

    # Fetch missing sector ETFs from yfinance
    missing_etfs = [e for e in needed_sector_etfs if e not in all_returns]
    if missing_etfs:
        try:
            import yfinance as yf
            for etf in missing_etfs:
                hist = yf.download(etf, start=start_date.strftime("%Y-%m-%d"),
                                   end=end_date.strftime("%Y-%m-%d"), progress=False, auto_adjust=True)
                if not hist.empty and len(hist) > 10:
                    all_returns[etf] = hist["Close"].squeeze().pct_change().fillna(0).values
        except Exception:
            pass

    valid_tickers = [t for t in tickers if t in all_returns]
    if not valid_tickers or benchmark not in all_returns:
        return "<html><body style='background:#0f172a;color:#ef4444;font-family:monospace;padding:40px'>" \
               "<h2>⚠ No data available</h2><p>Make sure tickers are in DuckDB and benchmark is cached.</p></body></html>"

    market_returns = all_returns[benchmark]
    returns_dict = {t: all_returns[t] for t in valid_tickers}

    # ── CAPM + Idiosyncratic Risk ───────────────────────────────────
    asset_metrics: list[dict] = []
    for t in valid_tickers:
        a = all_returns[t]
        min_len = min(len(a), len(market_returns))
        av, mv = a[-min_len:], market_returns[-min_len:]
        beta, alpha, exp_ret = math_core.calculate_capm(av, mv)
        idio = math_core.calculate_idiosyncratic_risk(av, mv)
        total_vol = float(np.std(av, ddof=1) * np.sqrt(252))
        sys_risk = abs(beta) * float(np.std(mv, ddof=1) * np.sqrt(252))
        asset_metrics.append(dict(
            ticker=t, beta=beta, alpha=alpha,
            exp_ret_pct=exp_ret * 100, idio_pct=idio * 100,
            sys_pct=sys_risk * 100, vol_pct=total_vol * 100,
            a_ret=av, m_ret=mv,
        ))

    # ── PCA ─────────────────────────────────────────────────────────
    pca = math_core.calculate_pca(returns_dict)

    # ── Sector Correlations ──────────────────────────────────────────
    sector_corrs = []
    for t in valid_tickers:
        classification = asset_classifications.get(t, {})
        etf = classification.get("sector_etf", benchmark)
        etf_used = etf if etf in all_returns else benchmark
        a = all_returns[t]; e = all_returns[etf_used]
        min_len = min(len(a), len(e))
        try:
            corr = float(np.corrcoef(a[-min_len:], e[-min_len:])[0, 1])
        except Exception:
            corr = 0.0
        sector_corrs.append(dict(
            ticker=t, etf=etf_used,
            sector=classification.get("sector", "Unclassified"),
            industry_group=classification.get("industry_group", "Unclassified"),
            industry=classification.get("industry", "Unclassified"),
            sub_industry=classification.get("sub_industry", "Unclassified"),
            corr=corr, r2=corr ** 2,
        ))
    sector_corrs.sort(key=lambda x: (x["sector"], x["industry_group"], -x["corr"]))

    # ── PLOT ─────────────────────────────────────────────────────────
    PALETTE = ["#22d3ee","#a78bfa","#34d399","#f59e0b","#f87171",
               "#60a5fa","#e879f9","#4ade80","#fb923c","#94a3b8","#fde68a","#6ee7b7"]
    DARK_BG   = "#0a0f1a"
    CARD_BG   = "#111827"
    GRID_CLR  = "rgba(255,255,255,0.055)"
    TEXT_CLR  = "#9ca3af"
    TITLE_CLR = "#e5e7eb"

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[
            f"Sector Correlation (ρ) vs SPDR ETF  ·  {days}d",
            "PCA Scree — Variance Explained",
            f"CAPM Regression  ·  Benchmark: {benchmark}",
            "Risk / Return Profile (CAPM)",
        ],
        vertical_spacing=0.14,
        horizontal_spacing=0.10,
        specs=[[{"type": "bar"}, {"type": "xy"}],
               [{"type": "xy"}, {"type": "xy"}]],
    )

    # Panel 1 — Sector Correlation horizontal bars
    for i, sc in enumerate(sector_corrs):
        color = PALETTE[i % len(PALETTE)]
        corr_val = sc["corr"]
        fig.add_trace(go.Bar(
            name=sc["ticker"],
            y=[sc["ticker"]],
            x=[round(corr_val, 4)],
            orientation="h",
            marker_color=color,
            text=[f"ρ={corr_val:.3f}  R²={sc['r2']:.3f}  [{sc['etf']}]"],
            textposition="outside",
            textfont=dict(size=9, color=TEXT_CLR),
            hovertemplate=(
                f"<b>{sc['ticker']}</b><br>"
                f"Sector: {sc['sector']}<br>"
                f"Group: {sc['industry_group']}<br>"
                f"Industry: {sc['industry']}<br>"
                f"Sub-Industry: {sc['sub_industry']}<br>"
                f"ETF: {sc['etf']}<br>"
                f"ρ = {corr_val:.4f}<br>"
                "<extra></extra>"
            ),
            showlegend=False,
        ), row=1, col=1)
    fig.add_vline(x=0.7, line_dash="dot", line_color="rgba(255,255,255,0.15)",
                  annotation_text="ρ=0.7", annotation_font_size=8,
                  annotation_font_color=TEXT_CLR, row=1, col=1)

    # Panel 2 — PCA Scree
    pc_labels = [f"PC{i+1}" for i in range(len(pca["eigenvalues"]))]
    expl_pct  = [v * 100 for v in pca["explained_variance"]]
    cum_pct   = [v * 100 for v in pca["cumulative_variance"]]
    fig.add_trace(go.Bar(
        x=pc_labels, y=expl_pct, name="Explained %",
        marker_color="#22d3ee", opacity=0.7, showlegend=False,
        hovertemplate="%{x}: %{y:.2f}%<extra></extra>",
    ), row=1, col=2)
    fig.add_trace(go.Scatter(
        x=pc_labels, y=cum_pct, name="Cumulative %",
        mode="lines+markers", line=dict(color="#a78bfa", width=2),
        marker=dict(size=6, symbol="circle"), showlegend=False,
        hovertemplate="%{x} cum: %{y:.2f}%<extra></extra>",
    ), row=1, col=2)

    # Panel 3 — CAPM scatter (all assets, colour per asset)
    for i, m in enumerate(asset_metrics):
        color = PALETTE[i % len(PALETTE)]
        # subsample for perf
        step = max(1, len(m["m_ret"]) // 120)
        fig.add_trace(go.Scatter(
            x=m["m_ret"][::step], y=m["a_ret"][::step],
            mode="markers", name=m["ticker"],
            marker=dict(color=color, size=3, opacity=0.4),
            showlegend=True,
            hovertemplate=f"{m['ticker']}<extra></extra>",
        ), row=2, col=1)
        # best-fit line
        x_fit = np.array([np.percentile(m["m_ret"], 3), np.percentile(m["m_ret"], 97)])
        y_fit = m["alpha"] + m["beta"] * x_fit
        fig.add_trace(go.Scatter(
            x=x_fit, y=y_fit, mode="lines",
            line=dict(color=color, width=1.5, dash="dot"),
            showlegend=False,
        ), row=2, col=1)

    # Panel 4 — Risk / Return bubble
    for i, m in enumerate(asset_metrics):
        fig.add_trace(go.Scatter(
            x=[m["beta"]], y=[m["exp_ret_pct"]],
            mode="markers+text",
            name=m["ticker"],
            text=[m["ticker"]],
            textposition="top center",
            textfont=dict(size=9, color=PALETTE[i % len(PALETTE)]),
            marker=dict(
                size=max(10, m["idio_pct"] * 1.2),
                color=PALETTE[i % len(PALETTE)],
                opacity=0.75,
                line=dict(width=1, color="rgba(255,255,255,0.3)"),
            ),
            showlegend=False,
            hovertemplate=(
                f"<b>{m['ticker']}</b><br>"
                f"β = {m['beta']:.4f}<br>"
                f"CAPM Ret = {m['exp_ret_pct']:.2f}%<br>"
                f"Idio Risk = {m['idio_pct']:.2f}%<br>"
                f"Total Vol = {m['vol_pct']:.2f}%<br>"
                "<extra></extra>"
            ),
        ), row=2, col=2)
    # Reference lines: β=1 and y=0
    fig.add_vline(x=1, line_dash="dash", line_color="rgba(255,255,255,0.12)",
                  annotation_text="β=1", annotation_font_size=8,
                  annotation_font_color=TEXT_CLR, row=2, col=2)
    fig.add_hline(y=0, line_dash="dash", line_color="rgba(255,255,255,0.12)", row=2, col=2)

    # ── Global layout ────────────────────────────────────────────────
    fig.update_layout(
        height=820,
        title=dict(
            text=f"Factor & Sector Analysis  ·  {', '.join(valid_tickers)}  ·  {days}d lookback",
            font=dict(size=14, color=TITLE_CLR, family="monospace"),
            x=0.5,
        ),
        paper_bgcolor=DARK_BG,
        plot_bgcolor=CARD_BG,
        font=dict(color=TEXT_CLR, size=10, family="monospace"),
        margin=dict(t=80, b=40, l=60, r=40),
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.12, xanchor="center", x=0.5,
            font=dict(size=9), bgcolor="rgba(0,0,0,0)",
        ),
    )
    # Style all axes
    for row in (1, 2):
        for col in (1, 2):
            fig.update_xaxes(gridcolor=GRID_CLR, zeroline=False,
                             tickfont=dict(size=8), row=row, col=col)
            fig.update_yaxes(gridcolor=GRID_CLR, zeroline=False,
                             tickfont=dict(size=8), row=row, col=col)
    # Axis labels
    fig.update_xaxes(title_text="Correlation (ρ)", range=[0, 1.05], row=1, col=1)
    fig.update_xaxes(title_text="Principal Component", row=1, col=2)
    fig.update_yaxes(title_text="Variance Explained (%)", row=1, col=2)
    fig.update_xaxes(title_text=f"{benchmark} Daily Return", row=2, col=1)
    fig.update_yaxes(title_text="Asset Daily Return", row=2, col=1)
    fig.update_xaxes(title_text="Beta (β)", row=2, col=2)
    fig.update_yaxes(title_text="CAPM Expected Return (%/yr)", row=2, col=2)

    # Style subplot titles
    for ann in fig.layout.annotations:
        ann.font.color = TITLE_CLR
        ann.font.size  = 11

    return fig.to_html(full_html=True, include_plotlyjs="cdn")


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
        "factor": "analytics.factor",
        "sector": "analytics.sector",
        "fft": "models.options.fft",
    }
    # Only apply alias if it's a single-token shortcut OR starts with an alias
    command = aliases.get(raw_cmd, raw_cmd)
    kwargs = {}
    
    # Handle aliases with positional arguments (e.g. "ratio AAPL MSFT")
    if "." in raw_cmd:
        base = raw_cmd.split(".")[0]
        if base in aliases:
            command = aliases[base]
            _apply_alias_positionals(base, path_tokens[1:], kwargs)
        

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
                # --- REAL BROKER EXECUTION ---
                venue = kwargs.get("venue", "ibkr")
                execution_confirmed = False
                
                if venue == "ibkr" and ibkr_service._ib_connected():
                    try:
                        res = await ibkr_service.place_market_order(sym, shares, "SELL")
                        if "error" not in res:
                            current_price = float(res.get("avgFillPrice", current_price))
                            execution_confirmed = True
                    except Exception as e:
                        print(f"[Liquidation] Broker error for {sym}: {e}")

                # Add to liquidated list with detailed PnL
                liquidated_symbols.append(f"{sym} ({'+' if pnl >= 0 else ''}${pnl:,.2f}){' 🚀' if execution_confirmed else ''}")
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
            
        success = duckdb_repo.add_transaction_batch_update_portfolio(keep_holdings, portfolio_id) # Using a safer batch update if available
        # Fallback to save_portfolio if batch not found
        if not hasattr(duckdb_repo, "add_transaction_batch_update_portfolio"):
            success = duckdb_repo.save_portfolio(keep_holdings, portfolio_id)

        if success:
            total_realized = 0.0
            for s in liquidated_symbols:
                if '($' in s:
                    try:
                        # Extract value between ($ and )
                        val_str = s.split('($')[1].split(')')[0].replace(',','')
                        total_realized += float(val_str)
                    except: pass

            broker_msg = "\n🚀 Real broker orders transmitted for positions marked with 🚀." if any("🚀" in s for s in liquidated_symbols) else ""
            return {"output": (
                f"🚨 LIQUIDATION COMPLETE 🚨\n"
                f"Total Positions Sold: {len(liquidated_symbols)}\n"
                f"Details: {', '.join(liquidated_symbols)}\n"
                f"PROFIT/LOSS REALIZED THIS RUN: {'+' if total_realized >= 0 else ''}${total_realized:,.2f}\n"
                f"{broker_msg}\n\n"
                f"✅ Local database updated."
            )}
        else:
            return {"output": "Error: Database failed to persist the liquidation.", "type": "error"}

    # ─── New Trading Commands ───────────────────────────────────────
    if command == "portfolio.buy":
        symbol = kwargs.get("symbol")
        shares = float(kwargs.get("shares", 0))
        usd_val = str(kwargs.get("usd", "0")).lower()
        # Accept symbol as positional or flag (robust)
        if not symbol:
            # Try to recover from positional argument
            if "symbol" not in kwargs and len(path_tokens) > 1:
                symbol = path_tokens[1].upper()
            # Also try from extra_tokens (for cases like ': buy AAPL ...')
            if not symbol and len(rest_tokens) == 0 and len(path_tokens) > 1:
                symbol = path_tokens[1].upper()
        # Final fallback: if still missing, try from kwargs
        if not symbol and "symbol" in kwargs:
            symbol = kwargs["symbol"].upper()
        if not symbol or (shares <= 0 and usd_val == "0"):
            return {"output": "Usage: buy AAPL --shares 10 --venue ibkr\n   o\nUsage: buy --symbol AAPL --shares 10 --venue ibkr [--asset-type stock|forex|future|crypto] [--exchange SMART] [--currency USD] [--last-trade-date 202506]", "type": "error"}
        
        asset_type = str(kwargs.get("asset_type", "stock")).lower()
        venue = str(kwargs.get("venue", "ibkr")).lower()
        symbol = ibkr_service._to_app_symbol(symbol) if asset_type in {"forex", "fx", "cash"} else symbol.upper()
        price_str = str(kwargs.get("price", "0")).lower()
        # Simple handling for 'k' notation
        if price_str.endswith('k'): price = float(price_str[:-1]) * 1000
        else:
            try: price = float(price_str)
            except ValueError: price = 0
        
        if price <= 0 and (usd_val != "0" or venue != "ibkr"):
            quote = await get_quote.execute(symbol)
            if "error" in quote:
                return {"output": f"Error fetching price for {symbol}: {quote['error']}", "type": "error"}
            price = float(quote.get("price", 0))

        # Calculate shares from USD if provided
        if usd_val != "0":
            if price <= 0:
                return {"output": f"Error fetching price for {symbol}: unable to size order from USD amount.", "type": "error"}
            total_usd = float(usd_val[:-1]) * 1000 if usd_val.endswith('k') else float(usd_val)
            shares = total_usd / price

        portfolio_id = str(kwargs.get("portfolio", "main")).lower()
        execution_msg = ""
        
        # --- REAL BROKER EXECUTION ---
        if venue == "ibkr":
            try:
                # place_market_order will internally call connect() if needed.
                # However, for UX clarity we can log a small info here if we suspect it might take time.
                pass
            except Exception:
                pass
            try:
                res = await ibkr_service.place_market_order(
                    symbol,
                    shares,
                    "BUY",
                    asset_type=asset_type,
                    currency=str(kwargs.get("currency", "USD")),
                    exchange=kwargs.get("exchange"),
                    primary_exchange=kwargs.get("primary_exchange"),
                    last_trade_date=kwargs.get("last_trade_date"),
                )
                if "error" in res:
                    return {"output": f"❌ IBKR Order Failed: {res['error']}", "type": "error"}
                symbol = str(res.get("symbol", symbol)).upper()
                price = float(res.get("avgFillPrice", price))
                execution_msg = f"🚀 [IBKR] ORDER EXECUTED LIVE ({res.get('asset_type', asset_type)})"
            except Exception as e:
                return {"output": f"❌ IBKR System Error: {str(e)}", "type": "error"}
        elif venue == "ctrader" and ctrader_service.get_status()["connected"]:
            try:
                # cTrader uses units, not lots here in the CLI for simplicity
                units = int(shares) # Or use lot conversion if specified
                res = ctrader_service.place_market_order(os.getenv("CTRADER_ACCOUNT_ID"), symbol, units, "BUY")
                execution_msg = "🚀 [cTrader] ORDER EXECUTED LIVE"
                # Price update would require parsing response
            except Exception as e:
                return {"output": f"❌ cTrader System Error: {str(e)}", "type": "error"}
        else:
            execution_msg = "✅ [SIMULATION] ORDER EXECUTED"

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
                "type": asset_type,
                "purchaseDate": datetime.now().strftime("%Y-%m-%d"),
                "sl": float(kwargs.get("sl")) if kwargs.get("sl") else None,
                "tp": float(kwargs.get("tp")) if kwargs.get("tp") else None
            })
        
        duckdb_repo.save_portfolio(holdings, portfolio_id)
        return {"output": f"{execution_msg}\nSymbol: {symbol}\nShares: {shares:.4f}\nPrice:  ${price:,.4f}\nTotal:  ${(shares*price):,.2f}\nSL:     {kwargs.get('sl') or 'None'} | TP: {kwargs.get('tp') or 'None'}"}

    if command == "portfolio.sell":
        symbol = kwargs.get("symbol")
        shares = float(kwargs.get("shares", 0))
        usd_val = str(kwargs.get("usd", "0")).lower()
        if not symbol or (shares <= 0 and usd_val == "0"):
            return {"output": "Usage: sell --symbol AAPL --shares 5 [--venue ibkr] [--asset-type stock|forex|future|crypto] [--exchange SMART] [--currency USD] [--last-trade-date 202506]", "type": "error"}
        
        asset_type = str(kwargs.get("asset_type", "stock")).lower()
        venue = str(kwargs.get("venue", "ibkr")).lower()
        symbol = ibkr_service._to_app_symbol(symbol) if asset_type in {"forex", "fx", "cash"} else symbol.upper()
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

        if price <= 0 and (usd_val != "0" or venue != "ibkr"):
            quote = await get_quote.execute(symbol)
            price = float(quote.get("price", existing['entryPrice']))
        elif price <= 0:
            price = float(existing['entryPrice'] or 0)

        # Calculate shares from USD if provided
        if usd_val != "0":
            if price <= 0:
                return {"output": f"Error fetching price for {symbol}: unable to size order from USD amount.", "type": "error"}
            total_usd = float(usd_val[:-1]) * 1000 if usd_val.endswith('k') else float(usd_val)
            shares = total_usd / price

        if existing['shares'] < shares:
            return {"output": f"❌ Insufficient shares for {symbol}. Available: {existing['shares']:.4f}", "type": "error"}

        execution_msg = ""

        # --- REAL BROKER EXECUTION ---
        if venue == "ibkr":
            try:
                pass
            except Exception:
                pass
            try:
                res = await ibkr_service.place_market_order(
                    symbol,
                    shares,
                    "SELL",
                    asset_type=asset_type,
                    currency=str(kwargs.get("currency", "USD")),
                    exchange=kwargs.get("exchange"),
                    primary_exchange=kwargs.get("primary_exchange"),
                    last_trade_date=kwargs.get("last_trade_date"),
                )
                if "error" in res:
                    return {"output": f"❌ IBKR Order Failed: {res['error']}", "type": "error"}
                symbol = str(res.get("symbol", symbol)).upper()
                price = float(res.get("avgFillPrice", price))
                execution_msg = f"🚀 [IBKR] SELL ORDER EXECUTED LIVE ({res.get('asset_type', asset_type)})"
            except Exception as e:
                return {"output": f"❌ IBKR System Error: {str(e)}", "type": "error"}
        else:
            execution_msg = "✅ [SIMULATION] SELL ORDER EXECUTED"

        # Calculate PnL
        pnl = (price - existing['entryPrice']) * shares
        duckdb_repo.add_transaction("SELL", symbol, shares, price, realized_pnl=pnl, portfolio_id=portfolio_id)

        # Update Portfolio
        existing['shares'] -= shares
        if existing['shares'] <= 0.0001: # handle floating point
            holdings = [h for h in holdings if h['symbol'] != symbol]
        
        duckdb_repo.save_portfolio(holdings, portfolio_id)
        return {"output": f"{execution_msg}\nSymbol: {symbol}\nShares: {shares:.4f}\nPrice:  ${price:,.4f}\nTotal:  ${(shares*price):,.2f}\nRealized PnL: {'+' if pnl >= 0 else ''}${pnl:,.2f}"}

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

    if command == "models.options.fft":
        symbol = kwargs.get("symbol", "SPY")
        model = kwargs.get("model", "heston")
        rf = float(kwargs.get("rf", 0.045))
        html = await quant_models.get_fft_option_pricing(symbol, model=model, risk_free=rf)
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

    # ─── Factor / Sector Analytics ───────────────────────────────────
    if command in ("analytics.factor", "analytics.sector", "factor", "sector"):
        tickers_str = kwargs.get("tickers", kwargs.get("symbol", ""))
        if not tickers_str:
            # default to current portfolio
            holdings = duckdb_repo.get_portfolio("main")
            tickers_str = ",".join(h["symbol"] for h in holdings[:12]) if holdings else "AAPL,MSFT,NVDA"
        benchmark_sym = str(kwargs.get("benchmark", "SPY")).upper()
        days_param = int(kwargs.get("days", 252))
        html = await _generate_factor_html(tickers_str, benchmark_sym, days_param)
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


