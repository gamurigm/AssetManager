"""
Agent Chat Routes — Clean Architecture
Uses LLM providers from the DI container (Strategy Pattern).
"""

import logging
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import json

from ...core.container import llm_providers
from ...agents.team.orchestrator import orchestrator
from ...services.risk_service import risk_service

logger = logging.getLogger("MMAM")

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    user_id: int
    portfolio: Optional[dict] = None
    history: Optional[List[dict]] = None
    market_regime: Optional[dict] = None


def _build_context(portfolio: Optional[dict], regime: Optional[dict] = None) -> str:
    """Build system context string from portfolio and regime data."""
    ctx_parts = []
    
    # Portfolio Context
    if portfolio:
        p = portfolio
        holdings = p.get('holdings', [])
        
        table_rows = []
        for h in holdings:
            sym = h.get("symbol", "N/A")
            shares = h.get("shares", 0)
            price = h.get("price", 0)
            val = shares * price
            chg = h.get("changePercent", 0)
            table_rows.append(f"| {sym} | {shares} | ${price:,.2f} | ${val:,.2f} | {chg:+.2f}% |")

        table_str = "\n".join(table_rows)

        ctx_parts.append(
            f"\n\n## 📊 REAL-TIME PORTFOLIO SNAPSHOT\n"
            f"**Total AUM:** ${p.get('total_value', 0):,.2f}\n"
            f"**Total PnL:** ${p.get('total_pnl', 0):,.2f} ({p.get('pnl_percent', 0):+.2f}%)\n\n"
            f"| Asset | Shares | Price | Value | Change |\n"
            f"| :--- | :--- | :--- | :--- | :--- |\n"
            f"{table_str}\n"
        )
        
        # Risk Analysis Context
        risk_report = risk_service.get_portfolio_risk_report(holdings)
        if "error" not in risk_report:
            ctx_parts.append(
                f"\n\n## 🛡️ PORTFOLIO RISK (PFAFF METHODOLOGY)\n"
                f"- **Modified VaR (95%):** {risk_report.get('mvar_95_percent')}% (${risk_report.get('mvar_95_cash', 0):,.2f})\n"
                f"- **Modified ES (mES):** {risk_report.get('mes_95_percent')}%\n"
                f"- **Gaussian VaR (Reference):** {risk_report['var_95_percent']}%\n"
                f"- **Portfolio Skewness:** {risk_report.get('skewness', 0)}\n"
                f"- **Excess Kurtosis:** {risk_report.get('excess_kurtosis', 0)}\n"
                f"- **Annualized Sharpe Ratio:** {risk_report['sharpe_ratio']}\n"
                f"- **Annualized Volatility:** {risk_report['annualized_volatility_percent']}%\n"
                f"- **Data Coverage:** {risk_report['coverage_percent']}% (Excluded: {', '.join(risk_report['missing_assets'])})\n"
            )
        else:
            ctx_parts.append(f"\n\n[Risk Analysis Unavailable: {risk_report.get('error')}]")
        
    # Market Regime Context
    if regime:
        r = regime
        symbol = r.get("symbol", "Unknown")
        analysis = r.get("regime_analysis", {})
        curr_regime = analysis.get("current_regime", "Unknown")
        
        ctx_parts.append(
            f"\n\n## 🧠 MARKET REGIME ANALYSIS ({symbol})\n"
            f"**Current State:** {curr_regime}\n"
            f"**Analysis:** {json.dumps(analysis, indent=2)}\n"
        )
        
    return "\n".join(ctx_parts)


@router.post("/chat")
async def chat(request: ChatRequest):
    """Orchestrator-based chat (multi-agent delegation)."""
    async def stream():
        async for chunk in orchestrator.run_stream(request.message, request.portfolio, request.market_regime):
            yield chunk
    return StreamingResponse(stream(), media_type="text/plain")


@router.post("/chat/mistral")
async def chat_mistral(request: ChatRequest):
    """Direct chat with Mistral Large via Strategy Pattern."""
    provider = llm_providers["mistral"]
    context = _build_context(request.portfolio, request.market_regime)

    def generate():
        try:
            for chunk in provider.stream_chat(request.message, request.history, context):
                yield chunk
        except Exception as e:
            logger.error(f"Mistral error: {e}")
            yield f"\n\n⚠️ Error from {provider.display_name}: {e}"

    return StreamingResponse(generate(), media_type="text/plain")


@router.post("/chat/mixtral")
async def chat_mixtral(request: ChatRequest):
    """Direct chat with Mixtral 8x22B via Strategy Pattern."""
    provider = llm_providers["mixtral"]
    context = _build_context(request.portfolio, request.market_regime)

    def generate():
        try:
            for chunk in provider.stream_chat(request.message, request.history, context):
                yield chunk
        except Exception as e:
            logger.error(f"Mixtral error: {e}")
            yield f"\n\n⚠️ Error from {provider.display_name}: {e}"

    return StreamingResponse(generate(), media_type="text/plain")


@router.post("/chat/kimi")
async def chat_kimi(request: ChatRequest):
    """Direct chat with Kimi K2.5 via Strategy Pattern."""
    provider = llm_providers["kimi"]
    context = _build_context(request.portfolio, request.market_regime)

    def generate():
        try:
            for chunk in provider.stream_chat(request.message, request.history, context):
                yield chunk
        except Exception as e:
            logger.error(f"Kimi error: {e}")
            yield f"\n\n⚠️ Error from {provider.display_name}: {e}"

    return StreamingResponse(generate(), media_type="text/plain")


@router.post("/chat/deepseek")
async def chat_deepseek(request: ChatRequest):
    """Direct chat with DeepSeek V3.2 (reasoning mode) via Strategy Pattern."""
    provider = llm_providers["deepseek"]
    context = _build_context(request.portfolio, request.market_regime)

    def generate():
        try:
            for chunk in provider.stream_chat(request.message, request.history, context):
                yield chunk
        except Exception as e:
            logger.error(f"DeepSeek error: {e}")
            yield json.dumps({"reasoning": "", "content": f"\n\n⚠️ Error from {provider.display_name}: {e}"}) + "\n"

    return StreamingResponse(generate(), media_type="application/x-ndjson")


@router.post("/chat/nemotron")
async def chat_nemotron(request: ChatRequest):
    """Direct chat with Nemotron Ultra 253B via Strategy Pattern."""
    provider = llm_providers["nemotron"]
    context = _build_context(request.portfolio, request.market_regime)

    def generate():
        try:
            for chunk in provider.stream_chat(request.message, request.history, context):
                yield chunk
        except Exception as e:
            logger.error(f"Nemotron error: {e}")
            yield f"\n\n⚠️ Error from {provider.display_name}: {e}"

    return StreamingResponse(generate(), media_type="text/plain")
