from fastapi import APIRouter, Depends
from ...agents.team.orchestrator import orchestrator
from ...services.nvidia_service import nvidia_service
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from typing import List, Optional
import json

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: int
    portfolio: Optional[dict] = None
    history: Optional[List[dict]] = None

@router.post("/chat")
async def chat(request: ChatRequest):
    # Use streaming for the orchestrator to improve perceived speed
    def generate():
        # Note: we ignore user_id for now as orchestrator is a singleton for demo
        # but in production we would retrieve context by user_id
        async def stream():
            async for chunk in orchestrator.run_stream(request.message, request.portfolio):
                yield chunk
        return stream()
    
    return StreamingResponse(generate(), media_type="text/plain")

@router.post("/chat/mistral")
async def chat_mistral(request: ChatRequest):
    def generate():
        for chunk in nvidia_service.chat_mistral_large(request.message, request.history, request.portfolio):
            yield chunk
    return StreamingResponse(generate(), media_type="text/plain")

@router.post("/chat/mixtral")
async def chat_mixtral(request: ChatRequest):
    def generate():
        for chunk in nvidia_service.chat_mixtral_8x22b(request.message, request.history, request.portfolio):
            yield chunk
    return StreamingResponse(generate(), media_type="text/plain")

@router.post("/chat/glm5")
async def chat_glm5(request: ChatRequest):
    def generate():
        for chunk in nvidia_service.chat_glm5(request.message, request.history, request.portfolio):
            yield json.dumps(chunk) + "\n"
    return StreamingResponse(generate(), media_type="application/x-ndjson")
