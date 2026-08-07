from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from services.contracts.events import MarketTickV1
from services.market_data_gateway.store import MarketDataStore


def test_tick_and_outbox_event_are_persisted_atomically(tmp_path: Path) -> None:
    store = MarketDataStore(tmp_path / "market.duckdb")
    event = MarketTickV1.create(
        source="unit-test",
        symbol="SPY",
        price=550.25,
        volume=100,
        observed_at=datetime.now(timezone.utc),
        correlation_id="corr-outbox-1",
    )

    assert store.record_tick(event) is True
    assert store.record_tick(event) is False

    pending = store.pending_events(limit=10)
    assert len(pending) == 1
    assert pending[0].event_id == event.event_id

    store.mark_published(event.event_id)
    assert store.pending_events(limit=10) == []


def test_unpublished_event_survives_store_recreation(tmp_path: Path) -> None:
    db_path = tmp_path / "market.duckdb"
    event = MarketTickV1.create(
        source="unit-test",
        symbol="AAPL",
        price=250.0,
        volume=1,
        observed_at=datetime.now(timezone.utc),
        correlation_id="corr-outbox-2",
    )
    MarketDataStore(db_path).record_tick(event)

    reopened = MarketDataStore(db_path)

    assert [item.event_id for item in reopened.pending_events()] == [event.event_id]
