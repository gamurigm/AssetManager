"""Opt-in real Kumo contract; creates and removes only its own unique bucket."""
import asyncio
import os
from types import SimpleNamespace
from uuid import uuid4

import httpx
import pytest

from app.core.config import settings
from app.infrastructure.artifacts.store import S3ArtifactStore, s3_client
from app.infrastructure.http.api_server_client import ApiServerClient
from app.services import artifact_service


@pytest.mark.integration
def test_gateway_fixture_to_pdf_to_real_kumo(tmp_path, monkeypatch):
    endpoint = os.getenv("KUMO_TEST_ENDPOINT")
    if not endpoint:
        pytest.skip("Set KUMO_TEST_ENDPOINT to an isolated Kumo instance")
    monkeypatch.setattr(settings, "S3_ENDPOINT_URL", endpoint)
    monkeypatch.setattr(settings, "S3_ACCESS_KEY_ID", "test")
    monkeypatch.setattr(settings, "S3_SECRET_ACCESS_KEY", "test")
    monkeypatch.setattr(settings, "S3_REGION", "us-east-1")
    bucket = "assetmanager-test-" + uuid4().hex
    monkeypatch.setattr(settings, "S3_BUCKET", bucket)
    monkeypatch.setattr(settings, "ARTIFACT_STORAGE_BACKEND", "s3")
    monkeypatch.setattr(settings, "API_SERVER_BASE_URL", "http://gateway.test")
    monkeypatch.setattr(settings, "API_SERVER_API_KEY", "test-gateway-key")
    client = s3_client(settings)
    client.create_bucket(Bucket=bucket)
    created = []

    async def run():
        def fixture(request):
            assert request.url.path == "/api/v1/gateway/fmp/quote"
            assert "apikey" not in request.url.params
            return httpx.Response(200, json=[{"symbol": "AAPL", "price": 123}])
        async with httpx.AsyncClient(transport=httpx.MockTransport(fixture)) as transport:
            quote = (await ApiServerClient(transport).get("fmp", "quote", {"symbol": "AAPL"})).json()[0]
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)
        pdf.cell(text=f"{quote['symbol']}: {quote['price']}")
        source = tmp_path / "generated.pdf"
        pdf.output(str(source))
        key = await artifact_service.publish_report(source, 7)
        created.append(key)
        artifact = await artifact_service.read_report(key, SimpleNamespace(id=7))
        assert artifact.content == source.read_bytes()
        assert artifact.content_type == "application/pdf"
        with pytest.raises(PermissionError):
            await artifact_service.read_report(key, SimpleNamespace(id=8))
        monkeypatch.setattr(settings, "ARTIFACT_STORAGE_BACKEND", "filesystem")
        assert (await artifact_service.read_report(key, SimpleNamespace(id=7))).content == artifact.content
        assert client.list_objects_v2(Bucket=bucket)["Contents"][0]["Key"] == key
        store = S3ArtifactStore(client, bucket, settings.ARTIFACT_MAX_BYTES)
        store.delete(key)
        with pytest.raises(FileNotFoundError):
            store.get(key)
    try:
        asyncio.run(run())
    finally:
        for key in created:
            client.delete_object(Bucket=bucket, Key=key)
        client.delete_bucket(Bucket=bucket)
