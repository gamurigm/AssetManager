"""Bounded artifact I/O. The caller runs these blocking operations in a thread."""

from __future__ import annotations

import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from app.core.errors import ExternalProviderError


class ArtifactUnavailable(ExternalProviderError):
    code = "artifact_storage_unavailable"
    user_message = "El almacenamiento de reportes no está disponible. Inténtalo nuevamente."


class ArtifactTooLarge(ValueError):
    pass


def validate_key(key: str) -> str:
    # Flat namespace preserves old report URLs and disallows Windows ADS too.
    if (not re.fullmatch(r"[A-Za-z0-9_^=.+-]+\.(?:pdf|html)", key)
            or ".." in key):
        raise FileNotFoundError("Report not found")
    return key


@dataclass(frozen=True)
class Artifact:
    content: bytes
    content_type: str


class ArtifactStore(Protocol):
    def put(self, key: str, content: bytes, content_type: str) -> None: ...
    def get(self, key: str) -> Artifact: ...
    def delete(self, key: str) -> None: ...


class FilesystemArtifactStore:
    def __init__(self, root: Path, max_bytes: int):
        self.root = root.resolve()
        self.max_bytes = max_bytes

    def _path(self, key: str) -> Path:
        path = self.root / validate_key(key)
        if path.is_symlink() or path.resolve().parent != self.root:
            raise FileNotFoundError("Report not found")
        return path

    def put(self, key: str, content: bytes, content_type: str) -> None:
        path = self._path(key)
        if len(content) > self.max_bytes:
            raise ArtifactTooLarge("Report exceeds configured size limit")
        self.root.mkdir(parents=True, exist_ok=True)
        fd, temporary = tempfile.mkstemp(dir=self.root, prefix=".artifact-")
        try:
            with os.fdopen(fd, "wb") as output:
                output.write(content)
            os.replace(temporary, path)
        finally:
            Path(temporary).unlink(missing_ok=True)

    def get(self, key: str) -> Artifact:
        with self._path(key).open("rb") as source:
            content = source.read(self.max_bytes + 1)
        if len(content) > self.max_bytes:
            raise ArtifactTooLarge("Report exceeds configured size limit")
        media_type = "application/pdf" if key.endswith(".pdf") else "text/html"
        return Artifact(content, media_type)

    def delete(self, key: str) -> None:
        self._path(key).unlink(missing_ok=True)


class S3ArtifactStore:
    def __init__(self, client, bucket: str, max_bytes: int):
        self.client = client
        self.bucket = bucket
        self.max_bytes = max_bytes

    def put(self, key: str, content: bytes, content_type: str) -> None:
        validate_key(key)
        if len(content) > self.max_bytes:
            raise ArtifactTooLarge("Report exceeds configured size limit")
        try:
            self.client.put_object(Bucket=self.bucket, Key=key, Body=content,
                                   ContentType=content_type)
        except Exception:
            raise ArtifactUnavailable() from None

    def get(self, key: str) -> Artifact:
        validate_key(key)
        from botocore.exceptions import ClientError

        try:
            response = self.client.get_object(Bucket=self.bucket, Key=key)
            body = response["Body"]
            try:
                content = body.read(self.max_bytes + 1)
                if len(content) > self.max_bytes:
                    raise ArtifactTooLarge("Report exceeds configured size limit")
                return Artifact(content, response.get("ContentType", "application/pdf"))
            finally:
                body.close()
        except ClientError as exc:
            if exc.response.get("Error", {}).get("Code") in {"NoSuchKey", "404"}:
                raise FileNotFoundError("Report not found") from None
            raise ArtifactUnavailable() from None
        except ArtifactTooLarge:
            raise
        except Exception:
            raise ArtifactUnavailable() from None

    def delete(self, key: str) -> None:
        validate_key(key)
        try:
            self.client.delete_object(Bucket=self.bucket, Key=key)
        except Exception:
            raise ArtifactUnavailable() from None


def s3_client(config):
    # Lazy import: filesystem deployments do not need the AWS dependency.
    import boto3
    from botocore.config import Config

    credentials = {}
    if config.S3_ACCESS_KEY_ID or config.S3_SECRET_ACCESS_KEY:
        if not (config.S3_ACCESS_KEY_ID and config.S3_SECRET_ACCESS_KEY):
            raise ArtifactUnavailable()
        credentials = {"aws_access_key_id": config.S3_ACCESS_KEY_ID,
                       "aws_secret_access_key": config.S3_SECRET_ACCESS_KEY}
    return boto3.client(
        "s3", endpoint_url=config.S3_ENDPOINT_URL or None,
        region_name=config.S3_REGION, **credentials,
        config=Config(s3={"addressing_style": "path"}, signature_version="s3v4",
                      connect_timeout=5, read_timeout=20,
                      retries={"mode": "standard", "total_max_attempts": 2}),
    )
