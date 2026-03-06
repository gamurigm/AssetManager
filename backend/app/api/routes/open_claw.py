from fastapi import APIRouter, Body, HTTPException
from ...services.open_claw_service import open_claw_service
from typing import Optional, Dict, Any

router = APIRouter()

@router.post("/task")
async def execute_open_claw_task(
    instruction: str = Body(..., embed=True),
    context: Optional[Dict[str, Any]] = Body(None)
):
    """
    Delegate a web-automation or scraping task to OpenClaw.
    """
    result = await open_claw_service.run_task(instruction, context)
    return result

@router.post("/notify")
async def send_external_notification(
    platform: str = Body(...),
    target: str = Body(...),
    message: str = Body(...)
):
    """
    Send a message via OpenClaw's connected messaging accounts (WhatsApp, Telegram, etc).
    """
    result = await open_claw_service.send_notification(platform, target, message)
    return result

@router.get("/status")
async def get_open_claw_status():
    """
    Check if the local OpenClaw service is reachable.
    """
    # Simple check - try to run a no-op or just check connectivity
    # For now, just return a diagnostic ping result
    import httpx
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            res = await client.get(f"{open_claw_service.base_url}/health")
            return {"online": res.status_code == 200, "url": open_claw_service.base_url}
    except:
        return {"online": False, "url": open_claw_service.base_url, "note": "Ensure OpenClaw is running on port 3000"}
