"""
Interface: LLM Provider (DIP + Strategy Pattern)
All AI model integrations must implement this contract.
"""

from abc import ABC, abstractmethod
from typing import AsyncGenerator, Optional, List, Dict, Any


class ILLMProvider(ABC):
    """Contract for all LLM providers (NVIDIA NIM, OpenAI, local models)."""

    @property
    @abstractmethod
    def model_id(self) -> str:
        """Unique model identifier."""
        ...

    @property
    @abstractmethod
    def display_name(self) -> str:
        """Human-readable name for the UI."""
        ...

    @abstractmethod
    def stream_chat(
        self,
        message: str,
        history: Optional[List[Dict[str, str]]] = None,
        system_context: str = "",
    ) -> AsyncGenerator[str, None]:
        """Stream chat response token by token."""
        ...
