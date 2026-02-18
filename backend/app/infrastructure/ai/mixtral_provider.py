"""
Mixtral 8x22B Provider — Implements ILLMProvider (Strategy Pattern).
"""

from openai import OpenAI
from typing import AsyncGenerator, Optional, List, Dict
from ...domain.interfaces.llm_provider import ILLMProvider
from ...core.config import settings
from .prompts import build_messages


class MixtralProvider(ILLMProvider):
    MODEL = "mistralai/mixtral-8x22b-instruct-v0.1"

    @property
    def model_id(self) -> str:
        return self.MODEL

    @property
    def display_name(self) -> str:
        return "Mixtral 8x22B"

    def stream_chat(
        self, message: str, history: Optional[List[Dict[str, str]]] = None, system_context: str = ""
    ) -> AsyncGenerator[str, None]:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=settings.NVIDIA_MIXTRAL_8X22B_KEY,
        )
        completion = client.chat.completions.create(
            model=self.MODEL,
            messages=build_messages(message, history, system_context),
            temperature=0.5,
            max_tokens=1024,
            stream=True,
        )
        for chunk in completion:
            if not getattr(chunk, "choices", None):
                continue
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content
