from fastapi import APIRouter

router = APIRouter()

@router.get("/history")
async def get_trading_history():
    return []
