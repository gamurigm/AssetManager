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


def _build_portfolio_context(portfolio: Optional[dict]) -> str:
    """Build system context string from portfolio data."""
    if not portfolio:
        return ""
    p = portfolio
    return (
        f"\n\n[REAL-TIME PORTFOLIO DATA]\n"
        f"Total Value: ${p.get('total_value', 0):,.2f}\n"
        f"Total P&L: ${p.get('total_pnl', 0):,.2f} ({p.get('pnl_percent', 0):.2f}%)\n"
        f"Assets: {p.get('holdings', [])}"
    )


@router.post("/chat")
async def chat(request: ChatRequest):
    """Orchestrator-based chat (multi-agent delegation)."""
    async def stream():
        async for chunk in orchestrator.run_stream(request.message, request.portfolio):
            yield chunk
    return StreamingResponse(stream(), media_type="text/plain")


@router.post("/chat/mistral")
async def chat_mistral(request: ChatRequest):
    """Direct chat with Mistral Large via Strategy Pattern."""
    provider = llm_providers["mistral"]
    context = _build_portfolio_context(request.portfolio)

    def generate():
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="text/plain")


@router.post("/chat/mixtral")
async def chat_mixtral(request: ChatRequest):
    """Direct chat with Mixtral 8x22B via Strategy Pattern."""
    provider = llm_providers["mixtral"]
    context = _build_portfolio_context(request.portfolio)

    def generate():
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="text/plain")


@router.post("/chat/glm5")
async def chat_glm5(request: ChatRequest):
    """Direct chat with GLM-5 (reasoning mode) via Strategy Pattern."""
    provider = llm_providers["glm5"]
    context = _build_portfolio_context(request.portfolio)

    def generate():
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="application/x-ndjson")


@router.post("/chat/deepseek")
async def chat_deepseek(request: ChatRequest):
    """Direct chat with DeepSeek V3.2 (reasoning mode) via Strategy Pattern."""
    provider = llm_providers["deepseek"]
    context = _build_portfolio_context(request.portfolio)

    def generate():
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="application/x-ndjson")


@router.post("/chat/nemotron")
async def chat_nemotron(request: ChatRequest):
    """Direct chat with Nemotron Ultra 253B via Strategy Pattern."""
    provider = llm_providers["nemotron"]
    context = _build_portfolio_context(request.portfolio)

    def generate():
        for chunk in provider.stream_chat(request.message, request.history, context):
            yield chunk

    return StreamingResponse(generate(), media_type="text/plain")
