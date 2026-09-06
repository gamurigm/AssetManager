"""Publish reports and resolve their storage without changing download URLs."""

from __future__ import annotations

import asyncio
import re
from pathlib import Path
from uuid import uuid4

from app.core.config import settings
from app.infrastructure.artifacts.store import (
    ArtifactTooLarge, ArtifactUnavailable, FilesystemArtifactStore,
    S3ArtifactStore, s3_client, validate_key,
)


def artifact_store(backend: str):
    if backend == "filesystem":
        return FilesystemArtifactStore(Path(settings.REPORTS_DIR), settings.ARTIFACT_MAX_BYTES)
    try:
        return S3ArtifactStore(s3_client(settings), settings.S3_BUCKET, settings.ARTIFACT_MAX_BYTES)
    except Exception:
        raise ArtifactUnavailable() from None


def backend_for_key(key: str) -> str:
    # Storage is encoded in new names, so switching the write default does not
    # strand previous objects. Pre-existing filenames always resolve to disk.
    return "s3" if re.fullmatch(r"user-\d+-s3-[a-f0-9]{32}\.pdf", key) else "filesystem"


async def publish_report(path: Path, owner_id: int | None) -> str:
    backend = settings.ARTIFACT_STORAGE_BACKEND
    marker = "s3" if backend == "s3" else "fs"
    key = f"user-{owner_id if owner_id is not None else 0}-{marker}-{uuid4().hex}.pdf"

    def publish():
        with path.open("rb") as source:
            content = source.read(settings.ARTIFACT_MAX_BYTES + 1)
        if len(content) > settings.ARTIFACT_MAX_BYTES:
            raise ArtifactTooLarge("Report exceeds configured size limit")
        artifact_store(backend).put(key, content, "application/pdf")

    await asyncio.to_thread(publish)
    return key


async def read_report(key: str, principal):
    validate_key(key)
    # Preserve access to unowned legacy reports and isolate all owned reports,
    # including for managers (same rule as the original download endpoint).
    if key.startswith("user-") and not key.startswith(f"user-{principal.id}-"):
        raise PermissionError("Report belongs to another user")
    return await asyncio.to_thread(lambda: artifact_store(backend_for_key(key)).get(key))
