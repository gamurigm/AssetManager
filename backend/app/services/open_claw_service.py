import httpx
from app.core.logging import logger
from typing import Optional, Dict, Any

class OpenClawService:
    """
    Interface for OpenClaw AI Agent.
    Enables web automation, scraping, and external messaging (WhatsApp/Telegram).
    """
    def __init__(self, base_url: str = "http://127.0.0.1:3002"):
        self.base_url = base_url
        self.timeout = httpx.Timeout(60.0, connect=10.0)

    async def run_task(self, instruction: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Send a high-level instruction to OpenClaw (e.g., 'Scrape recent news about NVDA from Reddit').
        """
        logger.info(f"🚀 [OpenClaw] Sending task: {instruction}")
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                # Assuming OpenClaw has a standard task endpoint
                response = await client.post(
                    f"{self.base_url}/api/task",
                    json={
                        "instruction": instruction,
                        "context": context or {},
                        "is_proactive": True
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    logger.info(f"✅ [OpenClaw] Task succeeded: {result.get('summary', 'No summary')}")
                    return {"status": "success", "data": result}
                else:
                    logger.error(f"❌ [OpenClaw] Error {response.status_code}: {response.text}")
                    return {"status": "error", "message": response.text}
        
        except Exception as e:
            logger.error(f"⚠️ [OpenClaw] Connection failed: {str(e)}")
            return {
                "status": "offline", 
                "message": f"OpenClaw service not detected at {self.base_url}. Please ensure OpenClaw runtime is running."
            }

    async def send_notification(self, platform: str, target: str, message: str) -> Dict[str, Any]:
        """
        Commands OpenClaw to send a message via external platforms (WhatsApp, Telegram, etc).
        """
        instruction = f"Send a {platform} message to {target}. Message: {message}"
        return await self.run_task(instruction)

open_claw_service = OpenClawService()
