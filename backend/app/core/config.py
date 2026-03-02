import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Asset Manager AI"
    API_V1_STR: str = "/api/v1"
    
    # Auth
    JWT_SECRET: str = os.getenv("JWT_SECRET", "supersecret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/asset_manager")
    
    # AI
    NVIDIA_NIM_API_KEY: str = os.getenv("NVIDIA_NIM_API_KEY", "")
    NVIDIA_MISTRAL_LARGE_KEY: str = os.getenv("NVIDIA_MISTRAL_LARGE_KEY", "")
    NVIDIA_MIXTRAL_8X22B_KEY: str = os.getenv("NVIDIA_MIXTRAL_8X22B_KEY", "")
    NVIDIA_DEEPSEEK_KEY: str = os.getenv("NVIDIA_DEEPSEEK_KEY", "")
    NVIDIA_NEMOTRON_KEY: str = os.getenv("NVIDIA_NEMOTRON_KEY", "")
    NIM_MODEL_NAME: str = os.getenv("NIM_MODEL_NAME", "qwen/qwen3.5-397b-a17b")
    
    # Financial Data
    FMP_API_KEY: str = os.getenv("FMP_API_KEY", "")
    POLYGON_API_KEY: str = os.getenv("POLYGON_API_KEY", "")
    ALPHA_VANTAGE_API_KEY: str = os.getenv("ALPHA_VANTAGE_API_KEY", "")
    TWELVE_DATA_API_KEY: str = os.getenv("TWELVE_DATA_API_KEY", "")
    FINAZON_API_KEY: str = os.getenv("FINAZON_API_KEY", "")
    
    # Bybit (Crypto Exchange)
    BYBIT_API_KEY: str = os.getenv("BYBIT_API_KEY", "")
    BYBIT_API_SECRET: str = os.getenv("BYBIT_API_SECRET", "")
    
    # Finviz (Scraping)
    FINVIZ_EMAIL: str = os.getenv("FINVIZ_EMAIL", "")
    FINVIZ_PASSWORD: str = os.getenv("FINVIZ_PASSWORD", "")
    
    # Real-time
    SOCKET_IO_PORT: int = 8000

settings = Settings()
