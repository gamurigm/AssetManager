from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from ...core.database import get_db
from ...models.models import WatchlistItem
from typing import List

router = APIRouter()

@router.get("/")
async def get_watchlist(user_id: int, db: AsyncSession = Depends(get_db)):
    """Get watchlist for a specific user."""
    result = await db.execute(select(WatchlistItem).where(WatchlistItem.user_id == user_id))
    return result.scalars().all()

@router.post("/{symbol}")
async def add_to_watchlist(symbol: str, user_id: int, db: AsyncSession = Depends(get_db)):
    """Add a symbol to the user's watchlist."""
    # Check if already exists
    result = await db.execute(select(WatchlistItem).where(
        (WatchlistItem.user_id == user_id) & (WatchlistItem.symbol == symbol)
    ))
    if result.scalar_one_or_none():
        return {"message": "Symbol already in watchlist"}
    
    item = WatchlistItem(user_id=user_id, symbol=symbol)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item

@router.delete("/{symbol}")
async def remove_from_watchlist(symbol: str, user_id: int, db: AsyncSession = Depends(get_db)):
    """Remove a symbol from the user's watchlist."""
    await db.execute(delete(WatchlistItem).where(
        (WatchlistItem.user_id == user_id) & (WatchlistItem.symbol == symbol)
    ))
    await db.commit()
    return {"message": "Removed from watchlist"}
