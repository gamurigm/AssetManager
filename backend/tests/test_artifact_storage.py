from __future__ import annotations

import asyncio
from io import BytesIO
from types import SimpleNamespace

import boto3
import pytest
from botocore.response import StreamingBody
from botocore.stub import Stubber

from app.core.config import settings
from app.infrastructure.artifacts.store import (
    ArtifactTooLarge, ArtifactUnavailable, FilesystemArtifactStore, S3ArtifactStore,
)
from app.services import artifact_service


def test_filesystem_contract_and_size_limit(tmp_path):
    store = FilesystemArtifactStore(tmp_path, 16)
    store.put("user-1-test.pdf", b"%PDF-original", "application/pdf")
    assert store.get("user-1-test.pdf").content == b"%PDF-original"
    store.put("user-1-test.pdf", b"%PDF-new", "application/pdf")
    assert store.get("user-1-test.pdf").content_type == "application/pdf"
    with pytest.raises(ArtifactTooLarge):
        store.put("user-1-test.pdf", b"x" * 17, "application/pdf")
    assert store.get("user-1-test.pdf").content == b"%PDF-new"
    store.delete("user-1-test.pdf")
    with pytest.raises(FileNotFoundError):
        store.get("user-1-test.pdf")


@pytest.mark.parametrize("key", ["../secret.pdf", "a/b.pdf", "a\\b.pdf", "a:secret.pdf", 'a".pdf'])
def test_rejects_unsafe_keys(tmp_path, key):
    with pytest.raises(FileNotFoundError):
        FilesystemArtifactStore(tmp_path, 100).put(key, b"x", "application/pdf")


def test_s3_errors_are_distinct_from_missing_and_close_body():
    client = boto3.client("s3", region_name="us-east-1", aws_access_key_id="test", aws_secret_access_key="test")
    store = S3ArtifactStore(client, "reports", 4)
    source = BytesIO(b"12345")
    with Stubber(client) as stub:
        stub.add_response("get_object", {"Body": StreamingBody(source, 5)},
                          {"Bucket": "reports", "Key": "a.pdf"})
        with pytest.raises(ArtifactTooLarge):
            store.get("a.pdf")
        assert source.closed
        stub.add_client_error("get_object", service_error_code="NoSuchKey", http_status_code=404)
        with pytest.raises(FileNotFoundError):
            store.get("a.pdf")
        stub.add_client_error("get_object", service_error_code="AccessDenied", http_status_code=403)
        with pytest.raises(ArtifactUnavailable):
            store.get("a.pdf")


def test_publish_and_download_preserve_owner_and_legacy_files(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "REPORTS_DIR", str(tmp_path / "reports"))
    monkeypatch.setattr(settings, "ARTIFACT_STORAGE_BACKEND", "filesystem")
    source = tmp_path / "generated.pdf"
    source.write_bytes(b"%PDF-test")

    async def run():
        key = await artifact_service.publish_report(source, 7)
        assert (await artifact_service.read_report(key, SimpleNamespace(id=7))).content == b"%PDF-test"
        with pytest.raises(PermissionError):
            await artifact_service.read_report(key, SimpleNamespace(id=8))
        # New write configuration must not reroute a previously local report.
        monkeypatch.setattr(settings, "ARTIFACT_STORAGE_BACKEND", "s3")
        assert (await artifact_service.read_report(key, SimpleNamespace(id=7))).content == b"%PDF-test"
        assert artifact_service.backend_for_key("user-7-backtest_AAPL.pdf") == "filesystem"
        assert artifact_service.backend_for_key("user-7-s3-" + "a" * 32 + ".pdf") == "s3"
    asyncio.run(run())
