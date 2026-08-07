"""FastAPI process hosting the real-time analysis consumer."""

from __future__ import annotations

import asyncio
import os
from contextlib import asynccontextmanager
from pathlib import Path

from confluent_kafka import Consumer, Producer
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

from app.agents.strategies.engine import StrategyConfig, StrategyFactory
from services.platform.health import ServiceHealth
from services.platform.kafka import (
    KafkaDeadLetterPublisher,
    KafkaJsonPublisher,
    KafkaSettings,
)
from services.strategy_engine.service import (
    AnalysisSettings,
    AnalysisWorker,
    StrategyRuntime,
)


def build_worker() -> AnalysisWorker:
    settings = AnalysisSettings.from_env()
    kafka = KafkaSettings(
        bootstrap_servers=settings.kafka_bootstrap_servers,
        client_id="analysis-worker-v1",
    )
    consumer = Consumer(kafka.consumer_config(group_id=settings.consumer_group))
    producer = Producer(kafka.producer_config())
    publisher = KafkaJsonPublisher(producer)
    health = ServiceHealth("analysis-worker")
    runtimes = {
        symbol: StrategyRuntime(
            symbol=symbol,
            strategy_name=settings.strategy_name,
            engine=StrategyFactory.create(settings.strategy_name),
            config=StrategyConfig.default(),
            publisher=publisher,
            account_size=settings.account_size,
        )
        for symbol in settings.symbols
    }
    return AnalysisWorker(
        consumer=consumer,
        runtimes=runtimes,
        health=health,
        dead_letter_publisher=KafkaDeadLetterPublisher(publisher),
    )


def create_app(*, worker: AnalysisWorker | None = None) -> FastAPI:
    worker = worker or build_worker()
    task: asyncio.Task | None = None

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        nonlocal task
        task = asyncio.create_task(worker.run(), name="analysis-worker")
        yield
        worker.stop()
        if task:
            try:
                await asyncio.wait_for(task, timeout=5)
            except asyncio.TimeoutError:
                task.cancel()

    app = FastAPI(
        title="AssetManager Analysis Worker",
        version="1.0.0",
        lifespan=lifespan,
    )

    @app.get("/health/live")
    async def live():
        return worker.health.liveness()

    @app.get("/health/ready")
    async def ready():
        snapshot = worker.health.readiness()
        if snapshot["status"] != "ready":
            raise HTTPException(status_code=503, detail=snapshot)
        return snapshot

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "services.strategy_engine.main:app",
        host="0.0.0.0",
        port=int(os.getenv("ANALYSIS_PORT", "8292")),
    )
