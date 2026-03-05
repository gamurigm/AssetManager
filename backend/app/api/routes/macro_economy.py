from fastapi import APIRouter, Query
from ...services.openbb_native_service import openbb_native

router = APIRouter()

@router.get("/economy/gdp")
async def economy_gdp(country: str = Query("united_states", description="Country name")):
    """Get nominal GDP data via OpenBB FRED."""
    result = await openbb_native.execute("economy.gdp.nominal", {"provider": "oecd", "country": country})
    if "error" in result:
        return {"error": result["error"], "data": []}
    return {"output": result.get("output", ""), "source": "OpenBB (GDP)"}

@router.get("/economy/cpi")
async def economy_cpi(country: str = Query("united_states", description="Country name")):
    """Get Consumer Price Index data."""
    result = await openbb_native.execute("economy.cpi", {"provider": "fred", "country": country})
    if "error" in result:
        return {"error": result["error"], "data": []}
    return {"output": result.get("output", ""), "source": "OpenBB (CPI)"}

@router.get("/economy/interest-rates")
async def economy_interest_rates():
    """Get Federal Funds Rate via FRED."""
    result = await openbb_native.execute("economy.fred_series", {"provider": "fred", "symbol": "FEDFUNDS"})
    if "error" in result:
        return {"error": result["error"], "data": []}
    return {"output": result.get("output", ""), "source": "OpenBB (FRED: FEDFUNDS)"}

@router.get("/economy/unemployment")
async def economy_unemployment():
    """Get unemployment rate via FRED."""
    result = await openbb_native.execute("economy.fred_series", {"provider": "fred", "symbol": "UNRATE"})
    if "error" in result:
        return {"error": result["error"], "data": []}
    return {"output": result.get("output", ""), "source": "OpenBB (FRED: UNRATE)"}

@router.get("/economy/calendar")
async def economy_calendar():
    """Get upcoming economic events calendar."""
    result = await openbb_native.execute("economy.calendar", {"provider": "fmp"})
    if "error" in result:
        return {"error": result["error"], "data": []}
    return {"output": result.get("output", ""), "source": "OpenBB (Economic Calendar)"}
