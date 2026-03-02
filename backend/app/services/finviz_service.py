"""
Finviz Service — Web Scraper for Finviz.com
Handles authentication, session management, and HTML table parsing.
Designed to be generic enough to scrape any Finviz page.
"""

import asyncio
import re
from datetime import datetime
from typing import Dict, Any, List, Optional

import httpx
from bs4 import BeautifulSoup

from ..core.config import settings
from ..core.container import duckdb_repo


class FinvizService:
    """
    Scraper for Finviz.com using authenticated sessions.
    Uses httpx with browser-like headers to bypass basic bot detection.
    """

    BASE_URL = "https://finviz.com"
    LOGIN_URL = "https://finviz.com/login_submit.ashx"

    # Realistic browser headers to avoid 403
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://finviz.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    def __init__(self):
        self._client: Optional[httpx.AsyncClient] = None
        self._logged_in = False
        self._lock = asyncio.Lock()

    async def _ensure_client(self) -> httpx.AsyncClient:
        """Lazily create and return the httpx client with cookie jar."""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                headers=self.HEADERS,
                follow_redirects=True,
                timeout=20,
            )
            self._logged_in = False
        return self._client

    async def _login(self) -> bool:
        """
        Authenticate with Finviz using email/password.
        Stores session cookies for subsequent requests.
        """
        if self._logged_in:
            return True

        async with self._lock:
            # Double check after acquiring lock
            if self._logged_in:
                return True

            email = settings.FINVIZ_EMAIL
            password = settings.FINVIZ_PASSWORD

            if not email or not password:
                print("[FinvizService] WARNING: No credentials configured. Scraping without login.")
                return False

            client = await self._ensure_client()

            try:
                # First, visit the login page to get any CSRF tokens / cookies
                login_page = await client.get(f"{self.BASE_URL}/login.ashx")

                # Extract any hidden form fields (CSRF token, viewstate, etc.)
                soup = BeautifulSoup(login_page.text, "lxml")
                form_data = {}
                hidden_inputs = soup.find_all("input", {"type": "hidden"})
                for inp in hidden_inputs:
                    name = inp.get("name")
                    value = inp.get("value", "")
                    if name:
                        form_data[name] = value

                # Add credentials
                form_data["email"] = email
                form_data["password"] = password
                # Finviz uses these field names for their login form
                form_data["remember"] = "true"

                # Submit login
                resp = await client.post(
                    self.LOGIN_URL,
                    data=form_data,
                    headers={
                        **self.HEADERS,
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Referer": f"{self.BASE_URL}/login.ashx",
                        "Origin": self.BASE_URL,
                    },
                )

                # Check if login succeeded by looking for redirect or session cookie
                if resp.status_code in (200, 302):
                    # Verify we're actually logged in by checking for auth cookies
                    cookies = dict(client.cookies)
                    if any(k for k in cookies if k.lower() in ("finviz", "screenerurl", ".aspxauth")):
                        self._logged_in = True
                        print("[FinvizService] SUCCESS: Logged in to Finviz successfully.")
                        return True

                    # Some logins redirect back — check if we can access a protected page
                    test_resp = await client.get(f"{self.BASE_URL}/screener.ashx")
                    if test_resp.status_code == 200 and "logout" in test_resp.text.lower():
                        self._logged_in = True
                        print("[FinvizService] SUCCESS: Logged in to Finviz (verified via page).")
                        return True

                print(f"[FinvizService] ERROR: Login may have failed (status: {resp.status_code}).")
                # Continue anyway — some pages work without full auth
                return False

            except Exception as e:
                print(f"[FinvizService] ERROR: Login error: {e}")
                return False

    async def _get_page(self, url: str) -> Optional[str]:
        """Fetch a page with the authenticated session."""
        client = await self._ensure_client()
        await self._login()

        try:
            # Small delay to be respectful
            await asyncio.sleep(0.5)

            resp = await client.get(url, headers={
                **self.HEADERS,
                "Referer": f"{self.BASE_URL}/",
            })

            if resp.status_code == 403:
                print(f"[FinvizService] 403 Forbidden for {url}. Retrying after re-login...")
                self._logged_in = False
                await self._login()
                resp = await client.get(url)

            if resp.status_code != 200:
                print(f"[FinvizService] HTTP {resp.status_code} for {url}")
                return None

            return resp.text

        except Exception as e:
            print(f"[FinvizService] Error fetching {url}: {e}")
            return None

    def _parse_table(self, html: str, table_class: str = None, table_id: str = None) -> List[Dict[str, Any]]:
        """
        Generic table parser — extracts rows from any HTML table.
        Returns a list of dicts with column headers as keys.
        """
        soup = BeautifulSoup(html, "lxml")

        # Find the target table
        table = None
        if table_id:
            table = soup.find("table", {"id": table_id})
        if not table and table_class:
            table = soup.find("table", {"class": table_class})
        if not table:
            # Try to find the main data table (largest one)
            tables = soup.find_all("table")
            if tables:
                # Pick the table with the most rows
                table = max(tables, key=lambda t: len(t.find_all("tr")))

        if not table:
            return []

        rows = table.find_all("tr")
        if len(rows) < 2:
            return []

        # Extract headers from first row
        header_row = rows[0]
        headers = []
        for th in header_row.find_all(["th", "td"]):
            text = th.get_text(strip=True)
            headers.append(text)

        if not headers:
            return []

        # Parse data rows
        results = []
        for row in rows[1:]:
            cells = row.find_all("td")
            if len(cells) != len(headers):
                continue

            record = {}
            for i, cell in enumerate(cells):
                key = headers[i]
                # Check for links
                link = cell.find("a")
                if link:
                    text = link.get_text(strip=True)
                    href = link.get("href", "")
                    if href and not href.startswith("http"):
                        href = f"{self.BASE_URL}/{href.lstrip('/')}"
                    record[key] = text
                    if href and key == "Ticker":
                        record["ticker_url"] = href
                    elif href and key == "SEC Form 4":
                        record["sec_url"] = href
                else:
                    record[key] = cell.get_text(strip=True)

            # Add row color class for transaction type highlighting
            row_class = row.get("class", [])
            if isinstance(row_class, list):
                record["_row_class"] = " ".join(row_class)

            if record:
                results.append(record)

        return results

    def _clean_insider_data(self, raw_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Clean and normalize insider trading data."""
        cleaned = []
        for row in raw_rows:
            try:
                record = {
                    "ticker": row.get("Ticker", ""),
                    "owner": row.get("Owner", ""),
                    "relationship": row.get("Relationship", ""),
                    "date": self._parse_date(row.get("Date", "")),
                    "transaction": row.get("Transaction", ""),
                    "cost": self._parse_number(row.get("Cost", "")),
                    "shares": self._parse_int(row.get("#Shares", "")),
                    "value": self._parse_number(row.get("Value ($)", "")),
                    "shares_total": self._parse_int(row.get("#Shares Total", "")),
                    "sec_form_4": row.get("SEC Form 4", ""),
                }

                # Add URLs if present
                if "ticker_url" in row:
                    record["ticker_url"] = row["ticker_url"]
                if "sec_url" in row:
                    record["sec_url"] = row["sec_url"]

                # Derive transaction type for frontend coloring
                txn = record["transaction"].lower()
                if "buy" in txn or "purchase" in txn:
                    record["type"] = "buy"
                elif "sale" in txn or "sell" in txn:
                    record["type"] = "sell"
                elif "option" in txn or "exercise" in txn:
                    record["type"] = "option"
                else:
                    record["type"] = "other"

                cleaned.append(record)
            except Exception:
                continue

        return cleaned

    @staticmethod
    def _parse_date(val: str) -> Optional[str]:
        """Parse Finviz date format (e.g. Feb 26 '26) to YYYY-MM-DD."""
        if not val or val == "-":
            return None
        try:
            # Format: 'MMM DD ''YY' or 'MMM DD'
            # If current year, sometimes year is omitted or uses 'YY
            val = val.replace("'", "").strip()
            # Try parsing with year
            parts = val.split()
            if len(parts) == 3:
                # Feb 26 26
                dt = datetime.strptime(val, "%b %d %y")
                return dt.strftime("%Y-%m-%d")
            elif len(parts) == 2:
                # Feb 26 (Assume current year)
                dt = datetime.strptime(val, "%b %d")
                dt = dt.replace(year=datetime.now().year)
                return dt.strftime("%Y-%m-%d")
            return None
        except (ValueError, TypeError):
            return None

    @staticmethod
    def _parse_number(val: str) -> Optional[float]:
        """Parse a number string, handling commas and empty values."""
        if not val or val == "-":
            return None
        try:
            return float(val.replace(",", "").replace("$", ""))
        except (ValueError, TypeError):
            return None

    @staticmethod
    def _parse_int(val: str) -> Optional[int]:
        """Parse an integer string, handling commas."""
        if not val or val == "-":
            return None
        try:
            return int(val.replace(",", ""))
        except (ValueError, TypeError):
            return None

    # -------------------------------------------------------
    #  Public API — Specific Scrapers
    # -------------------------------------------------------

    async def get_insider_trading(
        self,
        filter_type: str = "latest",
        tc: int = 7,
    ) -> Dict[str, Any]:
        """
        Scrape insider trading data from Finviz.

        Args:
            filter_type: "latest", "top_week", "top_owner_week"
            tc: Transaction type filter (7 = All Transactions)
        """
        # Build URL with filter
        url = f"{self.BASE_URL}/insidertrading.ashx?tc={tc}"

        # Add filter based on type
        if filter_type == "top_week":
            url += "&o=-transactionValue&t=7"
        elif filter_type == "top_owner_week":
            url += "&o=-ownedPercentage&t=7"

        html = await self._get_page(url)
        if not html:
            return {"error": "Failed to fetch insider trading page", "rows": []}

        # Parse the table
        raw_rows = self._parse_table(html)
        if not raw_rows:
            return {"error": "No data table found on page", "html_length": len(html), "rows": []}

        # Clean the data
        cleaned = self._clean_insider_data(raw_rows)

        # Save to DuckDB for persistence and change tracking
        saved_count = 0
        if cleaned:
            saved_count = duckdb_repo.save_insider_trades(cleaned)

        return {
            "source": "Finviz (Insider Trading)",
            "filter": filter_type,
            "count": len(cleaned),
            "new_records": saved_count,
            "rows": cleaned,
            "fetched_at": datetime.utcnow().isoformat() + "Z",
        }

    async def get_stored_insider_trades(
        self,
        ticker: Optional[str] = None,
        limit: int = 100
    ) -> Dict[str, Any]:
        """Fetch previously scraped insider trades from the database."""
        trades = duckdb_repo.get_insider_trades(ticker, limit)
        return {
            "source": "DuckDB (Historical Insider Trading)",
            "ticker": ticker,
            "count": len(trades),
            "rows": trades,
        }

    async def scrape_generic(self, path: str) -> Dict[str, Any]:
        """
        Scrape any Finviz page and return raw table data.

        Args:
            path: Relative path on Finviz, e.g. "insidertrading.ashx?tc=7"
        """
        if path.startswith("http"):
            url = path
        else:
            url = f"{self.BASE_URL}/{path.lstrip('/')}"

        html = await self._get_page(url)
        if not html:
            return {"error": f"Failed to fetch {url}", "rows": []}

        raw_rows = self._parse_table(html)
        return {
            "source": f"Finviz ({path})",
            "count": len(raw_rows),
            "rows": raw_rows,
            "fetched_at": datetime.utcnow().isoformat() + "Z",
        }

    async def close(self):
        """Close the httpx client session."""
        if self._client and not self._client.is_closed:
            await self._client.aclose()
            self._client = None
            self._logged_in = False


finviz_service = FinvizService()
