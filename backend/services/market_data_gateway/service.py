"""Market-data application service with single-writer persistence."""

from __future__ import annotations

import asyncio
import logging
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol

from services.contracts.events import MarketTickV1
from services.platform.health import ServiceHealth

from .store import MarketDataStore


logger = logging.getLogger("assetmanager.market_data")


class QuoteProvider(Protocol):
    async def get_price(self, symbol: str) -> dict[str, Any]: ...


class EventPublisher(Protocol):
    def publish_event(self, *, topic: str, event: MarketTickV1, key: str) -> None: ...


@dataclass(frozen=True)
class MarketDataSettings:
    kafka_bootstrap_servers: str
    symbols: tuple[str, ...]
    poll_interval_seconds: float
    database_path: Path
    outbox_batch_size: int = 500

    @classmethod
    def from_env(cls) -> "MarketDataSettings":
        backend_root = Path(__file__).resolve().parents[2]
        symbols = tuple(
            item.strip().upper()
            for item in os.getenv(
                "MARKET_DATA_SYMBOLS",
                "AAPL,MSFT,TSLA,SPY,BTC/USD",
            ).split(",")
            if item.strip()
        )
        return cls(
            kafka_bootstrap_servers=os.getenv(
                "KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"
            ),
            symbols=symbols,
            poll_interval_seconds=max(
                0.25, float(os.getenv("MARKET_DATA_POLL_SECONDS", "5"))
            ),
            database_path=Path(
                os.getenv(
                    "MARKET_DATA_DB_PATH",
                    str(backend_root / "data" / "market_data.duckdb"),
                )
            ),
            outbox_batch_size=max(
                1, int(os.getenv("MARKET_DATA_OUTBOX_BATCH_SIZE", "500"))
            ),
        )


class ApplicationMarketDataProvider:
    """Transitional adapter around the existing provider cascade."""

    def __init__(self, service: Any = None) -> None:
        if service is None:
            from app.services.market_data import market_data_service

            service = market_data_service
        self._service = service

    async def get_price(self, symbol: str) -> dict[str, Any]:
        # The UI cache is intentionally bypassed for the live event stream.
        return await self._service.get_price(symbol, bypass_cache=True)

    async def get_intraday(
        self,
        symbol: str,
        *,
        interval: str,
        period: str,
        start: str | None = None,
        end: str | None = None,
    ) -> dict[str, Any]:
        return await self._service.get_intraday(
            symbol,
            interval=interval,
            period=period,
            start=start,
            end=end,
        )


class MarketDataWorker:
    TOPIC = "market.ticks.v1"

    def __init__(
        self,
        *,
        settings: MarketDataSettings,
        provider: QuoteProvider,
        store: MarketDataStore,
        publisher: EventPublisher,
        health: ServiceHealth,
    ) -> None:
        self.settings = settings
        self.provider = provider
        self.store = store
        self.publisher = publisher
        self.health = health
        self._stop_event = asyncio.Event()
        for dependency in ("provider", "store", "kafka"):
            self.health.register_dependency(dependency)
        self.health.set_dependency("store", ready=True)

    async def collect_once(self) -> int:
        results = await asyncio.gather(
            *(self._collect_symbol(symbol) for symbol in self.settings.symbols),
            return_exceptions=True,
        )
        collected = sum(result is True for result in results)
        provider_errors = [result for result in results if isinstance(result, Exception)]
        self.health.set_dependency(
            "provider",
            ready=collected > 0 or not provider_errors,
            detail=(
                f"{collected}/{len(self.settings.symbols)} symbols collected"
                if not provider_errors
                else f"{len(provider_errors)} provider error(s)"
            ),
        )
        await self.dispatch_outbox()
        return collected

    async def _collect_symbol(self, symbol: str) -> bool:
        data = await self.provider.get_price(symbol)
        if not data or data.get("error") or float(data.get("price", 0) or 0) <= 0:
            return False
        timestamp = data.get("timestamp")
        if isinstance(timestamp, (int, float)):
            observed_at = datetime.fromtimestamp(float(timestamp), tz=timezone.utc)
        elif isinstance(timestamp, str):
            observed_at = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            if observed_at.tzinfo is None:
                observed_at = observed_at.replace(tzinfo=timezone.utc)
        else:
            observed_at = datetime.now(timezone.utc)
        event = MarketTickV1.create(
            source=str(data.get("source") or "market-data"),
            symbol=symbol,
            price=float(data["price"]),
            volume=float(data.get("volume", 0) or 0),
            observed_at=observed_at,
        )
        return self.store.record_tick(event)

    async def dispatch_outbox(self) -> int:
        published = 0
        for event in self.store.pending_events(self.settings.outbox_batch_size):
            try:
                await asyncio.to_thread(
                    self.publisher.publish_event,
                    topic=self.TOPIC,
                    event=event,
                    key=event.symbol,
                )
            except Exception as exc:
                self.health.set_dependency("kafka", ready=False, detail=str(exc))
                logger.warning("Kafka publish failed; outbox retained: %s", exc)
                break
            self.store.mark_published(event.event_id)
            published += 1
        if published or not self.store.pending_events(limit=1):
            self.health.set_dependency("kafka", ready=True)
        return published

    async def run(self) -> None:
        self.health.mark_started()
        while not self._stop_event.is_set():
            try:
                await self.collect_once()
            except Exception as exc:
                logger.exception("Market data cycle failed: %s", exc)
            try:
                await asyncio.wait_for(
                    self._stop_event.wait(),
                    timeout=self.settings.poll_interval_seconds,
                )
            except asyncio.TimeoutError:
                pass

    def stop(self) -> None:
        self._stop_event.set()
        self.health.mark_stopped()
