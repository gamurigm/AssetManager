"""
Agent Chat Routes — Clean Architecture
Uses LLM providers from the DI container (Strategy Pattern).
"""

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import json

from ...core.container import llm_providers
from ...agents.team.orchestrator import orchestrator

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
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="text/plain")


@router.post("/chat/mixtral")
async def chat_mixtral(request: ChatRequest):
    """Direct chat with Mixtral 8x22B via Strategy Pattern."""
    provider = llm_providers["mixtral"]
    context = _build_context(request.portfolio, request.market_regime)

    def generate():
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="text/plain")


@router.post("/chat/glm5")
async def chat_glm5(request: ChatRequest):
    """Direct chat with GLM-5 (reasoning mode) via Strategy Pattern."""
    provider = llm_providers["glm5"]
    context = _build_context(request.portfolio, request.market_regime)

    def generate():
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="application/x-ndjson")


@router.post("/chat/deepseek")
async def chat_deepseek(request: ChatRequest):
    """Direct chat with DeepSeek V3.2 (reasoning mode) via Strategy Pattern."""
    provider = llm_providers["deepseek"]
    context = _build_context(request.portfolio, request.market_regime)

    def generate():
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="application/x-ndjson")


@router.post("/chat/nemotron")
async def chat_nemotron(request: ChatRequest):
    """Direct chat with Nemotron Ultra 253B via Strategy Pattern."""
    provider = llm_providers["nemotron"]
    context = _build_context(request.portfolio, request.market_regime)

    def generate():
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="text/plain")
