"""Encrypted, write-only storage for external integration credentials.

Provider credentials must be recoverable by the backend, so a password-style
one-way hash is not sufficient. This module uses AES-256-GCM for authenticated
encryption and keeps a keyed fingerprint only for change detection. The master
key is supplied out-of-band through CONFIG_ENCRYPTION_KEY and is never stored in
the vault file.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import re
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal
from urllib.parse import urlsplit

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


FieldKind = Literal["url", "host", "port", "text"]


@dataclass(frozen=True)
class PublicField:
    id: str
    label: str
    environment: str
    kind: FieldKind
    default: str
    hint: str = ""
    required: bool = True


@dataclass(frozen=True)
class SecretField:
    id: str
    label: str
    environment: str
    hint: str = ""
    required: bool = True
    aliases: tuple[str, ...] = ()

    @property
    def environments(self) -> tuple[str, ...]:
        """Environment names that must receive the same credential value."""
        return (self.environment, *self.aliases)


@dataclass(frozen=True)
class IntegrationDefinition:
    id: str
    label: str
    category: Literal["market_data", "ai", "brokers", "platform"]
    description: str
    fields: tuple[PublicField, ...] = ()
    secrets: tuple[SecretField, ...] = ()


INTEGRATIONS: tuple[IntegrationDefinition, ...] = (
    IntegrationDefinition(
        "api_server", "API Server", "platform",
        "Gateway de proveedores. Credenciales upstream gestionadas en Supabase Vault.",
        (PublicField("base_url", "URL del gateway", "API_SERVER_BASE_URL", "url", "http://127.0.0.1:3006"),),
        (SecretField("api_key", "Clave de aplicación", "API_SERVER_API_KEY"),),
    ),
    IntegrationDefinition(
        "deep_agent", "Deep Agent", "ai",
        "Agente mínimo con archivos efímeros y modelo compatible con OpenAI.",
        (
            PublicField("model", "Modelo", "DEEP_AGENT_MODEL", "text", "nvidia/nemotron-3-super-120b-a12b"),
            PublicField("base_url", "URL opcional", "DEEP_AGENT_BASE_URL", "url", "", "Vacía: usa NVIDIA NIM.", False),
        ),
        (SecretField("api_key", "Clave opcional", "DEEP_AGENT_API_KEY", "Vacía: usa NVIDIA_NIM_API_KEY.", False),),
    ),
    IntegrationDefinition(
        "yahoo",
        "Yahoo Finance",
        "market_data",
        "Fuente primaria de precios y búsqueda de instrumentos.",
        (PublicField("base_url", "URL de API", "YAHOO_FINANCE_BASE_URL", "url", "https://query2.finance.yahoo.com"),),
    ),
    IntegrationDefinition(
        "fmp",
        "Financial Modeling Prep",
        "market_data",
        "Fundamentales, cotizaciones y perfiles corporativos de respaldo.",
        (PublicField("base_url", "URL de API", "FMP_BASE_URL", "url", "https://financialmodelingprep.com/stable"),),
        (SecretField("api_key", "API key", "FMP_API_KEY"),),
    ),
    IntegrationDefinition(
        "polygon",
        "Polygon",
        "market_data",
        "Datos históricos y cierre de mercado.",
        (PublicField("base_url", "URL de API", "POLYGON_BASE_URL", "url", "https://api.polygon.io"),),
        (SecretField("api_key", "API key", "POLYGON_API_KEY"),),
    ),
    IntegrationDefinition(
        "alpha_vantage",
        "Alpha Vantage",
        "market_data",
        "Indicadores técnicos y series de mercado.",
        (PublicField("base_url", "URL de API", "ALPHA_VANTAGE_BASE_URL", "url", "https://www.alphavantage.co/query"),),
        (SecretField("api_key", "API key", "ALPHA_VANTAGE_API_KEY"),),
    ),
    IntegrationDefinition(
        "twelve_data",
        "Twelve Data",
        "market_data",
        "Cotizaciones y velas para instrumentos globales.",
        (PublicField("base_url", "URL de API", "TWELVE_DATA_BASE_URL", "url", "https://api.twelvedata.com"),),
        (SecretField("api_key", "API key", "TWELVE_DATA_API_KEY"),),
    ),
    IntegrationDefinition(
        "finazon",
        "Finazon",
        "market_data",
        "Datos de acciones estadounidenses.",
        (PublicField("base_url", "URL de API", "FINAZON_BASE_URL", "url", "https://api.finazon.io/latest/finazon/us_stocks_essential"),),
        (SecretField("api_key", "API key", "FINAZON_API_KEY"),),
    ),
    IntegrationDefinition(
        "bybit",
        "Bybit",
        "market_data",
        "Mercado cripto y, cuando se habilite, operaciones autenticadas.",
        (PublicField("base_url", "URL de API", "BYBIT_BASE_URL", "url", "https://api.bybit.com"),),
        (
            SecretField("api_key", "API key", "BYBIT_API_KEY", "Opcional para datos públicos.", False),
            SecretField("api_secret", "API secret", "BYBIT_API_SECRET", "Opcional para datos públicos.", False),
        ),
    ),
    IntegrationDefinition(
        "finviz",
        "Finviz",
        "market_data",
        "Screener, noticias y datos de mercado con sesión opcional.",
        (PublicField("base_url", "URL del servicio", "FINVIZ_BASE_URL", "url", "https://finviz.com"),),
        (
            SecretField("email", "Correo de acceso", "FINVIZ_EMAIL", "Opcional para contenido público.", False),
            SecretField("password", "Contraseña", "FINVIZ_PASSWORD", "Opcional para contenido público.", False),
        ),
    ),
    IntegrationDefinition(
        "fred",
        "Federal Reserve (FRED)",
        "market_data",
        "Series macroeconómicas usadas directamente y a través de OpenBB.",
        secrets=(
            SecretField(
                "api_key",
                "API key",
                "FRED_API_KEY",
                "También se aplica automáticamente al conector FRED de OpenBB.",
                aliases=("OPENBB_CREDENTIALS_FRED_API_KEY",),
            ),
        ),
    ),
    IntegrationDefinition(
        "nvidia_nim",
        "NVIDIA NIM",
        "ai",
        "Modelos Mistral, Mixtral, Kimi, DeepSeek y Nemotron.",
        (
            PublicField("base_url", "URL compatible con OpenAI", "NVIDIA_NIM_BASE_URL", "url", "https://integrate.api.nvidia.com/v1"),
            PublicField("default_model", "Modelo predeterminado", "NIM_MODEL_NAME", "text", "qwen/qwen3.5-397b-a17b"),
            PublicField("strategy_model", "Modelo del equipo de estrategia", "NVIDIA_STRATEGY_MODEL", "text", "nvidia/llama-3.3-nemotron-super-49b-v1.5"),
        ),
        (
            SecretField("default_key", "API key principal", "NVIDIA_NIM_API_KEY"),
            SecretField("mistral_key", "API key de Mistral", "NVIDIA_MISTRAL_LARGE_KEY", "Opcional; usa la principal si está vacía.", False),
            SecretField("mixtral_key", "API key de Mixtral", "NVIDIA_MIXTRAL_8X22B_KEY", "Opcional; usa la principal si está vacía.", False),
            SecretField("deepseek_key", "API key de DeepSeek", "NVIDIA_DEEPSEEK_KEY", "Opcional; usa la principal si está vacía.", False),
            SecretField("nemotron_key", "API key de Nemotron", "NVIDIA_NEMOTRON_KEY", "Opcional; usa la principal si está vacía.", False),
        ),
    ),
    IntegrationDefinition(
        "openbb",
        "OpenBB Platform",
        "platform",
        "Servidor local OpenBB y token opcional de la plataforma.",
        (PublicField("base_url", "URL del servidor", "OPENBB_API_BASE", "url", "http://127.0.0.1:6900"),),
        (SecretField("token", "Token", "OPENBB_TOKEN", "Opcional para una instancia local.", False),),
    ),
    IntegrationDefinition(
        "ibkr",
        "Interactive Brokers",
        "brokers",
        "Conexión a TWS o IB Gateway.",
        (
            PublicField("host", "Host", "IBKR_HOST", "host", "127.0.0.1"),
            PublicField("port", "Puerto", "IBKR_PORT", "port", "7497"),
            PublicField("client_id", "Client ID", "IBKR_CLIENT_ID", "port", "101"),
        ),
    ),
    IntegrationDefinition(
        "ctrader",
        "cTrader",
        "brokers",
        "Sesión Open API y cuenta de ejecución.",
        secrets=(
            SecretField("client_id", "Client ID", "CTRADER_CLIENT_ID"),
            SecretField("client_secret", "Client secret", "CTRADER_CLIENT_SECRET"),
            SecretField("access_token", "Access token", "CTRADER_ACCESS_TOKEN"),
            SecretField("account_id", "Account ID", "CTRADER_ACCOUNT_ID"),
        ),
    ),
    IntegrationDefinition(
        "mt5",
        "MetaTrader 5",
        "brokers",
        "Terminal y credenciales del gateway aislado de ejecución.",
        (
            PublicField(
                "terminal_path",
                "Ruta de terminal64.exe",
                "MT5_TERMINAL_PATH",
                "text",
                r"C:\Program Files\MetaTrader 5\terminal64.exe",
                "El gateway debe reiniciarse después de cambiar esta ruta.",
            ),
            PublicField(
                "server",
                "Servidor del broker",
                "MT5_SERVER",
                "text",
                "",
                "Opcional si el terminal ya conserva la sesión.",
                False,
            ),
        ),
        (
            SecretField(
                "gateway_token",
                "Token del gateway",
                "MT5_GATEWAY_TOKEN",
                "Protege las operaciones privilegiadas entre la API y el gateway.",
            ),
            SecretField(
                "login",
                "Login de cuenta",
                "MT5_LOGIN",
                "Opcional si el terminal ya conserva la sesión.",
                False,
            ),
            SecretField(
                "password",
                "Contraseña de cuenta",
                "MT5_PASSWORD",
                "Opcional si el terminal ya conserva la sesión.",
                False,
            ),
        ),
    ),
    IntegrationDefinition(
        "execution_gateway",
        "Execution Gateway",
        "platform",
        "Servicio interno que aísla la ejecución de órdenes.",
        (PublicField("base_url", "URL del servicio", "EXECUTION_GATEWAY_URL", "url", "http://127.0.0.1:8293"),),
    ),
    IntegrationDefinition(
        "openclaw",
        "OpenClaw",
        "platform",
        "Servicio local de automatización y herramientas.",
        (PublicField("base_url", "URL del servicio", "OPENCLAW_BASE_URL", "url", "http://127.0.0.1:3002"),),
    ),
    IntegrationDefinition(
        "logfire",
        "Pydantic Logfire",
        "platform",
        "Observabilidad opcional para trazas de FastAPI y llamadas de IA.",
        secrets=(
            SecretField(
                "token",
                "Write token",
                "LOGFIRE_TOKEN",
                "Opcional; requiere reiniciar la API para activar el envío de telemetría.",
                False,
            ),
        ),
    ),
)

INTEGRATION_BY_ID = {item.id: item for item in INTEGRATIONS}
_HOST_RE = re.compile(r"^(localhost|[A-Za-z0-9](?:[A-Za-z0-9.-]{0,251}[A-Za-z0-9])?|\[[0-9A-Fa-f:]+\])$")


class SecureConfigurationError(RuntimeError):
    """Raised when secure configuration is unavailable or invalid."""


def decode_master_key(encoded: str) -> bytes | None:
    if not encoded:
        return None
    try:
        padded = encoded + "=" * (-len(encoded) % 4)
        value = base64.urlsafe_b64decode(padded.encode("ascii"))
    except (ValueError, UnicodeError):
        return None
    return value if len(value) == 32 else None


def validate_public_value(field: PublicField, value: str, *, production: bool) -> str:
    value = value.strip()
    if not value:
        if field.required:
            raise ValueError(f"Valor inválido para {field.label}")
        return ""
    if len(value) > 2048 or any(ord(char) < 32 for char in value):
        raise ValueError(f"Valor inválido para {field.label}")
    if field.kind == "port":
        number = int(value)
        if not 0 <= number <= 65535:
            raise ValueError(f"Valor inválido para {field.label}")
        return str(number)
    if field.kind == "host":
        if not _HOST_RE.fullmatch(value):
            raise ValueError(f"Host inválido para {field.label}")
        return value
    if field.kind == "url":
        parsed = urlsplit(value)
        if parsed.username or parsed.password or parsed.fragment or not parsed.hostname:
            raise ValueError(f"URL inválida para {field.label}")
        is_loopback = parsed.hostname in {"localhost", "127.0.0.1", "::1"}
        if parsed.scheme != "https" and not (
            parsed.scheme == "http" and is_loopback and not production
        ):
            raise ValueError("Solo se permite HTTPS; HTTP se limita a loopback en desarrollo")
        return value.rstrip("/")
    return value


class SecureIntegrationStore:
    """Small encrypted repository with atomic writes and a strict allowlist."""

    def __init__(self, path: Path, encoded_master_key: str, *, production: bool = False):
        self.path = path
        self._key = decode_master_key(encoded_master_key)
        self.production = production
        self._lock = threading.RLock()

    @property
    def available(self) -> bool:
        return self._key is not None

    def _require_key(self) -> bytes:
        if self._key is None:
            raise SecureConfigurationError(
                "CONFIG_ENCRYPTION_KEY debe ser una clave URL-safe base64 de 32 bytes"
            )
        return self._key

    def _read(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"version": 1, "integrations": {}}
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SecureConfigurationError("El almacén seguro no se puede leer") from exc
        if payload.get("version") != 1 or not isinstance(payload.get("integrations"), dict):
            raise SecureConfigurationError("Formato de almacén seguro no compatible")
        return payload

    def _write(self, payload: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(f"{self.path.suffix}.tmp")
        serialized = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        temporary.write_text(serialized, encoding="utf-8")
        try:
            temporary.chmod(0o600)
        except OSError:
            pass
        temporary.replace(self.path)

    @staticmethod
    def _aad(integration_id: str, secret_id: str) -> bytes:
        return f"assetmanager:integration:v1:{integration_id}:{secret_id}".encode()

    def _encrypt(self, integration_id: str, secret_id: str, value: str) -> dict[str, str]:
        key = self._require_key()
        nonce = os.urandom(12)
        ciphertext = AESGCM(key).encrypt(
            nonce,
            value.encode("utf-8"),
            self._aad(integration_id, secret_id),
        )
        fingerprint = hmac.new(
            key,
            self._aad(integration_id, secret_id) + value.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return {
            "nonce": base64.urlsafe_b64encode(nonce).decode("ascii"),
            "ciphertext": base64.urlsafe_b64encode(ciphertext).decode("ascii"),
            "fingerprint": fingerprint,
        }

    def _decrypt(self, integration_id: str, secret_id: str, payload: dict[str, str]) -> str:
        try:
            nonce = base64.urlsafe_b64decode(payload["nonce"])
            ciphertext = base64.urlsafe_b64decode(payload["ciphertext"])
            plaintext = AESGCM(self._require_key()).decrypt(
                nonce,
                ciphertext,
                self._aad(integration_id, secret_id),
            )
            return plaintext.decode("utf-8")
        except Exception as exc:
            raise SecureConfigurationError(
                f"No se pudo descifrar la configuración de {integration_id}"
            ) from exc

    def hydrate(self, target: Any) -> None:
        """Apply persisted values before providers are instantiated."""
        if not self.path.exists():
            return
        self._require_key()
        with self._lock:
            payload = self._read()
            for integration in INTEGRATIONS:
                stored = payload["integrations"].get(integration.id, {})
                public_values = stored.get("fields", {})
                secret_values = stored.get("secrets", {})
                revoked_secrets = set(stored.get("revoked_secrets", []))
                for field in integration.fields:
                    if field.id in public_values:
                        self._apply(target, field.environment, str(public_values[field.id]))
                for field in integration.secrets:
                    if field.id in secret_values:
                        value = self._decrypt(integration.id, field.id, secret_values[field.id])
                        self._apply_secret(target, field, value)
                    elif field.id in revoked_secrets:
                        self._apply_secret(target, field, "")

    @staticmethod
    def _apply(target: Any, environment: str, value: str) -> None:
        os.environ[environment] = value
        if hasattr(target, environment):
            setattr(target, environment, value)

    @classmethod
    def _apply_secret(cls, target: Any, secret: SecretField, value: str) -> None:
        for environment in secret.environments:
            cls._apply(target, environment, value)

    def update(
        self,
        integration_id: str,
        *,
        fields: dict[str, str],
        secrets: dict[str, str],
        actor_id: int,
        target: Any,
    ) -> None:
        definition = INTEGRATION_BY_ID.get(integration_id)
        if definition is None:
            raise KeyError(integration_id)
        self._require_key()
        allowed_fields = {field.id: field for field in definition.fields}
        allowed_secrets = {field.id: field for field in definition.secrets}
        if set(fields) - allowed_fields.keys() or set(secrets) - allowed_secrets.keys():
            raise ValueError("La solicitud contiene campos no permitidos")
        clean_fields = {
            field_id: validate_public_value(
                allowed_fields[field_id], value, production=self.production
            )
            for field_id, value in fields.items()
        }
        clean_secrets: dict[str, str] = {}
        for secret_id, value in secrets.items():
            if not value or len(value) > 8192 or any(ord(char) < 32 for char in value):
                raise ValueError(f"Credencial inválida: {allowed_secrets[secret_id].label}")
            clean_secrets[secret_id] = value

        with self._lock:
            payload = self._read()
            stored = payload["integrations"].setdefault(integration_id, {})
            stored.setdefault("fields", {}).update(clean_fields)
            encrypted = stored.setdefault("secrets", {})
            revoked = set(stored.get("revoked_secrets", []))
            for secret_id, value in clean_secrets.items():
                encrypted[secret_id] = self._encrypt(integration_id, secret_id, value)
                revoked.discard(secret_id)
            stored["revoked_secrets"] = sorted(revoked)
            stored["updated_at"] = datetime.now(timezone.utc).isoformat()
            stored["updated_by"] = actor_id
            self._write(payload)

        for field_id, value in clean_fields.items():
            self._apply(target, allowed_fields[field_id].environment, value)
        for secret_id, value in clean_secrets.items():
            self._apply_secret(target, allowed_secrets[secret_id], value)

    def delete_secret(self, integration_id: str, secret_id: str, *, actor_id: int, target: Any) -> None:
        definition = INTEGRATION_BY_ID.get(integration_id)
        if definition is None:
            raise KeyError(integration_id)
        secret = next((item for item in definition.secrets if item.id == secret_id), None)
        if secret is None:
            raise KeyError(secret_id)
        self._require_key()
        with self._lock:
            payload = self._read()
            stored = payload["integrations"].setdefault(integration_id, {})
            stored.setdefault("secrets", {}).pop(secret_id, None)
            revoked = set(stored.get("revoked_secrets", []))
            revoked.add(secret_id)
            stored["revoked_secrets"] = sorted(revoked)
            stored["updated_at"] = datetime.now(timezone.utc).isoformat()
            stored["updated_by"] = actor_id
            self._write(payload)
        self._apply_secret(target, secret, "")

    def catalog(self, target: Any) -> list[dict[str, Any]]:
        with self._lock:
            payload = self._read() if self.path.exists() else {"integrations": {}}
        result: list[dict[str, Any]] = []
        for definition in INTEGRATIONS:
            stored = payload["integrations"].get(definition.id, {})
            stored_secrets = stored.get("secrets", {})
            revoked_secrets = set(stored.get("revoked_secrets", []))
            field_views = []
            for field in definition.fields:
                value = stored.get("fields", {}).get(
                    field.id, getattr(target, field.environment, field.default)
                )
                field_views.append(
                    {
                        "id": field.id,
                        "label": field.label,
                        "kind": field.kind,
                        "value": str(value),
                        "required": field.required,
                        "hint": field.hint,
                    }
                )
            secret_views = []
            for secret in definition.secrets:
                stored_in_vault = secret.id in stored_secrets
                configured_in_environment = any(
                    bool(getattr(target, environment, os.getenv(environment, "")))
                    for environment in secret.environments
                )
                configured = stored_in_vault or (
                    secret.id not in revoked_secrets and configured_in_environment
                )
                source = (
                    "vault"
                    if stored_in_vault
                    else "environment"
                    if configured
                    else None
                )
                secret_views.append(
                    {
                        "id": secret.id,
                        "label": secret.label,
                        "configured": configured,
                        "required": secret.required,
                        "source": source,
                        "hint": secret.hint,
                    }
                )
            required_ids = {item.id for item in definition.secrets if item.required}
            required_secrets_configured = all(
                item["configured"] for item in secret_views if item["id"] in required_ids
            )
            transport_setting = {"fmp": "FMP_TRANSPORT", "twelve_data": "TWELVE_DATA_TRANSPORT"}.get(definition.id)
            gateway_mode = transport_setting and getattr(target, transport_setting, "direct") == "gateway"
            if gateway_mode:
                required_secrets_configured = bool(getattr(target, "API_SERVER_API_KEY", ""))
                for item in secret_views:
                    item["required"] = False
                    item["hint"] = "Modo gateway: la credencial upstream se gestiona en API_Server."
            result.append(
                {
                    "id": definition.id,
                    "label": definition.label,
                    "category": definition.category,
                    "description": definition.description + (" Transporte: API_Server." if gateway_mode else ""),
                    "configured": required_secrets_configured,
                    "updated_at": stored.get("updated_at"),
                    "fields": field_views,
                    "secrets": secret_views,
                }
            )
        return result
