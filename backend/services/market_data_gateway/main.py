"""FastAPI process for market ingestion, storage, outbox and history access."""

from __future__ import annotations

import asyncio
import os
from contextlib import asynccontextmanager
from typing import Any, Literal

from confluent_kafka import Producer
from fastapi import FastAPI, HTTPException, Query

from services.market_data_gateway.service import (
    ApplicationMarketDataProvider,
    MarketDataSettings,
    MarketDataWorker,
)
from services.market_data_gateway.store import MarketDataStore
from services.platform.health import ServiceHealth
from services.platform.kafka import KafkaJsonPublisher, KafkaSettings


def build_worker() -> tuple[MarketDataWorker, Any]:
    settings = MarketDataSettings.from_env()
    health = ServiceHealth("market-data")
    provider = ApplicationMarketDataProvider()
    store = MarketDataStore(settings.database_path)
    producer = Producer(
        KafkaSettings(
            bootstrap_servers=settings.kafka_bootstrap_servers,
            client_id="market-data-v1",
        ).producer_config()
    )
    publisher = KafkaJsonPublisher(producer)
    return (
        MarketDataWorker(
            settings=settings,
            provider=provider,
            store=store,
            publisher=publisher,
            health=health,
        ),
        provider,
    )


def create_app(
    *,
    worker: MarketDataWorker | None = None,
    history_provider: Any = None,
) -> FastAPI:
    if worker is None:
        worker, default_provider = build_worker()
        history_provider = history_provider or default_provider
    health = worker.health
    task: asyncio.Task | None = None

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        nonlocal task
        task = asyncio.create_task(worker.run(), name="market-data-worker")
        yield
        worker.stop()
        if task:
            try:
                await asyncio.wait_for(task, timeout=5)
            except asyncio.TimeoutError:
                task.cancel()

    app = FastAPI(
        title="AssetManager Market Data",
        version="1.0.0",
        lifespan=lifespan,
    )

    @app.get("/health/live")
    async def live():
        return health.liveness()

    @app.get("/health/ready")
    async def ready():
        snapshot = health.readiness()
        if snapshot["status"] != "ready":
            raise HTTPException(status_code=503, detail=snapshot)
        return snapshot

    @app.get("/internal/v1/candles/{symbol}")
    async def candles(
        symbol: str,
        interval: Literal["1m", "5m"] = Query(default="1m"),
        period: str = Query(default="5d", min_length=2, max_length=8),
        start: str | None = None,
        end: str | None = None,
    ):
        if history_provider is None or not hasattr(history_provider, "get_intraday"):
            raise HTTPException(status_code=503, detail="History provider unavailable")
        result = await history_provider.get_intraday(
            symbol.upper(),
            interval=interval,
            period=period,
            start=start,
            end=end,
        )
        if result.get("error"):
            raise HTTPException(status_code=502, detail=result["error"])
        return result

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "services.market_data_gateway.main:app",
        host="0.0.0.0",
        port=int(os.getenv("MARKET_DATA_PORT", "8291")),
    )
