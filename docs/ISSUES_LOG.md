# Project Issues & Resolutions Log

This file documents critical errors encountered during development and their resolutions. Always consult this before debugging similar symptoms.

## 1. Frontend `Failed to fetch` (Console TypeError)

**Symptoms:**
- Frontend logs: `TypeError: Failed to fetch` at `ClientDashboard.useEffect.fetchPrices`.
- Context: Happens immediately on page load when fetching market data.

**Root Cause:**
- Frontend and Backend port mismatch.
- Frontend tries to fetch from `http://127.0.0.1:8282`.
- Backend might be running on `port 8000` or not running at all.

**Resolution:**
1. **Verify Backend Port:** Open `backend/app/main.py` and ensure `uvicorn.run(..., port=8282)`.
2. **Verify Frontend Fetch URL:** Open `frontend/src/app/client/dashboard/page.tsx` and ensure `fetch('http://localhost:8282/...')`.
3. **Avoid Bottlenecks:** Do not use `asyncio.sleep` or long delays in paths called in parallel by `Promise.all` in the frontend; it causes `Failed to fetch` due to browser connection limits.
4. **Restart Backend:** Use `.\run_app.ps1` to clear zombies.

---

## 2. Rate Limiting (404 Not Found on Quotes)

**Symptoms:**
- Backend logs show consecutive `404 Not Found` for valid tickers (AAPL, MSFT).
- Logs show `[GetQuote] ⛔ provider rate limited`.

**Resolution:**
- **Wait Logic:** The system now waits 1.5s for Yahoo to refill instead of failing.
- **Limits:** Dev limits increased in `rate_limiter.py`.
- **Action:** If persistent, restart backend to clear in-memory rate limit caches (if using memory backend) or check `.rate_limit_cache` folder.

---

## 3. Pydantic Log Noise

**Symptoms:**
- Console flooded with `Pydantic APIEx validate_python`.

**Resolution:**
- Default Pydantic instrumentation in Logfire is DISABLED in `backend/app/main.py` line 25.
- Uncomment only for deep debugging.
