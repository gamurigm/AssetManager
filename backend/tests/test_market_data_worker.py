from __future__ import annotations

import asyncio
from pathlib import Path

from services.market_data_gateway.service import (
    ApplicationMarketDataProvider,
    MarketDataSettings,
    MarketDataWorker,
)
from services.market_data_gateway.store import MarketDataStore
from services.platform.health import ServiceHealth


class FakeProvider:
    async def get_price(self, symbol: str) -> dict:
        return {
            "symbol": symbol,
            "price": 123.45,
            "volume": 10,
            "source": "fake-provider",
        }


class FakePublisher:
    def __init__(self, *, fail: bool = False) -> None:
        self.fail = fail
        self.events = []

    def publish_event(self, *, topic: str, event, key: str) -> None:
        if self.fail:
            raise RuntimeError("broker unavailable")
        self.events.append((topic, event, key))


class CacheAwareService:
    def __init__(self) -> None:
        self.kwargs = None

    async def get_price(self, symbol, **kwargs):
        self.kwargs = kwargs
        return {"symbol": symbol, "price": 1.0, "source": "fake"}


def settings(db_path: Path) -> MarketDataSettings:
    return MarketDataSettings(
        kafka_bootstrap_servers="kafka:9092",
        symbols=("AAPL", "SPY"),
        poll_interval_seconds=5,
        database_path=db_path,
        outbox_batch_size=100,
    )


def test_collection_persists_then_publishes_versioned_events(tmp_path: Path) -> None:
    store = MarketDataStore(tmp_path / "ticks.duckdb")
    publisher = FakePublisher()
    health = ServiceHealth("market-data")
    worker = MarketDataWorker(
        settings=settings(tmp_path / "ticks.duckdb"),
        provider=FakeProvider(),
        store=store,
        publisher=publisher,
        health=health,
    )

    collected = asyncio.run(worker.collect_once())

    assert collected == 2
    assert [item[2] for item in publisher.events] == ["AAPL", "SPY"]
    assert all(item[0] == "market.ticks.v1" for item in publisher.events)
    assert store.pending_events() == []


def test_publish_failure_keeps_outbox_event_for_replay(tmp_path: Path) -> None:
    db_path = tmp_path / "ticks.duckdb"
    store = MarketDataStore(db_path)
    worker = MarketDataWorker(
        settings=MarketDataSettings(
            kafka_bootstrap_servers="kafka:9092",
            symbols=("AAPL",),
            poll_interval_seconds=5,
            database_path=db_path,
            outbox_batch_size=100,
        ),
        provider=FakeProvider(),
        store=store,
        publisher=FakePublisher(fail=True),
        health=ServiceHealth("market-data"),
    )

    collected = asyncio.run(worker.collect_once())

    assert collected == 1
    assert len(store.pending_events()) == 1


def test_live_ingestion_bypasses_the_ui_quote_cache() -> None:
    service = CacheAwareService()
    provider = ApplicationMarketDataProvider(service=service)

    asyncio.run(provider.get_price("EURUSD"))

    assert service.kwargs == {"bypass_cache": True}
