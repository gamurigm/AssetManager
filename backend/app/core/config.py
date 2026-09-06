"""Application configuration with environment-aware security defaults."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import Field, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from .secure_config import SecureIntegrationStore, decode_master_key


_BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )

    PROJECT_NAME: str = "Asset Manager AI"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"

    # Authentication is optional only for an explicitly non-production runtime.
    AUTH_REQUIRED: bool = False
    JWT_ISSUER: str = "assetmanager-api"
    JWT_AUDIENCE: str = "assetmanager-web"
    ALGORITHM: Literal["RS256"] = "RS256"
    JWT_PRIVATE_KEY_PATH: str = str(_BACKEND_DIR / "data" / "jwt-private.pem")
    JWT_PUBLIC_KEY_PATH: str = str(_BACKEND_DIR / "data" / "jwt-public.pem")
    # Inline PEM values are useful for managed secret stores. When present,
    # both values must be supplied and take precedence over the file paths.
    JWT_PRIVATE_KEY: SecretStr = SecretStr("")
    JWT_PUBLIC_KEY: SecretStr = SecretStr("")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    AUTH_COOKIE_NAME: str = "assetmanager_access_token"
    AUTH_COOKIE_SECURE: bool = False
    CONFIG_ENCRYPTION_KEY: SecretStr = SecretStr("")
    SECURE_CONFIG_PATH: str = str(_BACKEND_DIR / "data" / "secure-integrations.v1.json")

    # Comma-separated to keep .env configuration simple and deterministic.
    CORS_ORIGINS: str = (
        "http://localhost:3309,http://127.0.0.1:3309,"
        "http://localhost:3000,http://127.0.0.1:3000"
    )

    # Database
    DATABASE_URL: str = Field(
        default="postgresql://user:pass@localhost:5432/asset_manager",
        repr=False,
    )
    DATABASE_ECHO: bool = False

    # AI
    NVIDIA_NIM_BASE_URL: str = "https://integrate.api.nvidia.com/v1"
    NVIDIA_NIM_API_KEY: str = Field(default="", repr=False)
    NVIDIA_MISTRAL_LARGE_KEY: str = Field(default="", repr=False)
    NVIDIA_MIXTRAL_8X22B_KEY: str = Field(default="", repr=False)
    NVIDIA_DEEPSEEK_KEY: str = Field(default="", repr=False)
    NVIDIA_NEMOTRON_KEY: str = Field(default="", repr=False)
    NIM_MODEL_NAME: str = "qwen/qwen3.5-397b-a17b"
    DEEP_AGENT_MODEL: str = "nvidia/nemotron-3-super-120b-a12b"
    DEEP_AGENT_BASE_URL: str = ""
    DEEP_AGENT_API_KEY: str = Field(default="", repr=False)
    DEEP_AGENT_TIMEOUT_SECONDS: float = Field(default=60, gt=0, le=300)
    # Used by the multi-agent strategy team. This deployment is verified
    # against the configured NVIDIA credentials and can be overridden safely
    # from Settings > Integrations without changing source code.
    NVIDIA_STRATEGY_MODEL: str = "nvidia/llama-3.3-nemotron-super-49b-v1.5"
    NVIDIA_REQUEST_TIMEOUT_SECONDS: float = 45.0

    # Financial data
    YAHOO_FINANCE_BASE_URL: str = "https://query2.finance.yahoo.com"
    FMP_BASE_URL: str = "https://financialmodelingprep.com/stable"
    POLYGON_BASE_URL: str = "https://api.polygon.io"
    ALPHA_VANTAGE_BASE_URL: str = "https://www.alphavantage.co/query"
    TWELVE_DATA_BASE_URL: str = "https://api.twelvedata.com"
    FINAZON_BASE_URL: str = "https://api.finazon.io/latest/finazon/us_stocks_essential"
    BYBIT_BASE_URL: str = "https://api.bybit.com"
    FINVIZ_BASE_URL: str = "https://finviz.com"
    FMP_API_KEY: str = Field(default="", repr=False)
    POLYGON_API_KEY: str = Field(default="", repr=False)
    ALPHA_VANTAGE_API_KEY: str = Field(default="", repr=False)
    TWELVE_DATA_API_KEY: str = Field(default="", repr=False)
    API_SERVER_BASE_URL: str = "http://127.0.0.1:3006"
    API_SERVER_API_KEY: str = Field(default="", repr=False)
    API_SERVER_TIMEOUT_SECONDS: float = Field(default=25, gt=0, le=120)
    API_SERVER_MODE: Literal["gateway-only", "development-direct"] = "development-direct"
    FMP_TRANSPORT: Literal["direct", "gateway"] = "direct"
    FMP_GATEWAY_SLUG: str = "fmp"
    TWELVE_DATA_TRANSPORT: Literal["direct", "gateway"] = "direct"
    TWELVE_DATA_GATEWAY_SLUG: str = "twelvedata"
    FINAZON_API_KEY: str = Field(default="", repr=False)
    FRED_API_KEY: str = Field(default="", repr=False)
    OPENBB_CREDENTIALS_FRED_API_KEY: str = Field(default="", repr=False)

    # Brokers and data sources
    BYBIT_API_KEY: str = Field(default="", repr=False)
    BYBIT_API_SECRET: str = Field(default="", repr=False)
    FINVIZ_EMAIL: str = Field(default="", repr=False)
    FINVIZ_PASSWORD: str = Field(default="", repr=False)
    OPENBB_API_BASE: str = "http://127.0.0.1:6900"
    OPENBB_TOKEN: str = Field(default="", repr=False)
    IBKR_HOST: str = "127.0.0.1"
    IBKR_PORT: str = "7497"
    IBKR_CLIENT_ID: str = "101"
    CTRADER_CLIENT_ID: str = Field(default="", repr=False)
    CTRADER_CLIENT_SECRET: str = Field(default="", repr=False)
    CTRADER_ACCESS_TOKEN: str = Field(default="", repr=False)
    CTRADER_ACCOUNT_ID: str = Field(default="", repr=False)
    MT5_TERMINAL_PATH: str = r"C:\Program Files\MetaTrader 5\terminal64.exe"
    MT5_SERVER: str = ""
    MT5_GATEWAY_TOKEN: str = Field(default="", repr=False)
    MT5_LOGIN: str = Field(default="", repr=False)
    MT5_PASSWORD: str = Field(default="", repr=False)
    EXECUTION_GATEWAY_URL: str = "http://127.0.0.1:8293"
    OPENCLAW_BASE_URL: str = "http://127.0.0.1:3002"
    LOGFIRE_TOKEN: str = Field(default="", repr=False)

    SOCKET_IO_PORT: int = 8282
    REPORTS_DIR: str = "reports"
    ARTIFACT_STORAGE_BACKEND: Literal["filesystem", "s3"] = "filesystem"
    ARTIFACT_MAX_BYTES: int = Field(default=32 * 1024 * 1024, gt=0)
    S3_ENDPOINT_URL: str = ""
    S3_REGION: str = "us-east-1"
    S3_BUCKET: str = "assetmanager-reports"
    S3_ACCESS_KEY_ID: str = Field(default="", repr=False)
    S3_SECRET_ACCESS_KEY: str = Field(default="", repr=False)

    @property
    def cors_origins(self) -> list[str]:
        return [
            origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()
        ]

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT.strip().lower() in {"production", "prod"}

    @model_validator(mode="after")
    def validate_security_configuration(self) -> "Settings":
        if not self.JWT_ISSUER.strip():
            raise ValueError("JWT_ISSUER must not be empty")
        if not self.JWT_AUDIENCE.strip():
            raise ValueError("JWT_AUDIENCE must not be empty")

        has_inline_private = bool(self.JWT_PRIVATE_KEY.get_secret_value().strip())
        has_inline_public = bool(self.JWT_PUBLIC_KEY.get_secret_value().strip())
        if has_inline_private != has_inline_public:
            raise ValueError(
                "JWT_PRIVATE_KEY and JWT_PUBLIC_KEY must be configured together"
            )
        if not has_inline_private and (
            not self.JWT_PRIVATE_KEY_PATH.strip()
            or not self.JWT_PUBLIC_KEY_PATH.strip()
        ):
            raise ValueError(
                "JWT_PRIVATE_KEY_PATH and JWT_PUBLIC_KEY_PATH must be configured together"
            )

        if self.is_production:
            if not self.AUTH_REQUIRED:
                raise ValueError("AUTH_REQUIRED must be true in production")
            if not self.AUTH_COOKIE_SECURE:
                raise ValueError("AUTH_COOKIE_SECURE must be true in production")
            if any(origin == "*" for origin in self.cors_origins):
                raise ValueError("Wildcard CORS origins are forbidden in production")
            if decode_master_key(self.CONFIG_ENCRYPTION_KEY.get_secret_value()) is None:
                raise ValueError(
                    "CONFIG_ENCRYPTION_KEY must be URL-safe base64 encoding of 32 random bytes"
                )
            if self.API_SERVER_MODE != "gateway-only":
                raise ValueError("API_SERVER_MODE must be gateway-only in production")
        return self


settings = Settings()
secure_integration_store = SecureIntegrationStore(
    Path(settings.SECURE_CONFIG_PATH),
    settings.CONFIG_ENCRYPTION_KEY.get_secret_value(),
    production=settings.is_production,
)
secure_integration_store.hydrate(settings)
