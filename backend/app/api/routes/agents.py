from fastapi import APIRouter, Depends
from ...agents.orchestrator import route_query, AgentResponse
from ...services.nvidia_service import nvidia_service
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import json

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: int

@router.post("/chat", response_model=AgentResponse)
async def chat(request: ChatRequest):
    return await route_query(request.message, request.user_id)

@router.post("/chat/mistral")
async def chat_mistral(request: ChatRequest):
    def generate():
        for chunk in nvidia_service.chat_mistral_large(request.message):
            yield chunk
    return StreamingResponse(generate(), media_type="text/plain")

@router.post("/chat/mixtral")
async def chat_mixtral(request: ChatRequest):
    def generate():
        for chunk in nvidia_service.chat_mixtral_8x22b(request.message):
            yield chunk
    return StreamingResponse(generate(), media_type="text/plain")

@router.post("/chat/glm5")
async def chat_glm5(request: ChatRequest):
    def generate():
        for chunk in nvidia_service.chat_glm5(request.message):
            yield json.dumps(chunk) + "\n"
    return StreamingResponse(generate(), media_type="application/x-ndjson")
