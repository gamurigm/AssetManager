"""
Kimi K2.5 Provider — Implements ILLMProvider (Strategy Pattern).
Multimodal MoE model with reasoning capabilities.
"""

import json
from openai import OpenAI
from typing import AsyncGenerator, Optional, List, Dict
from ...domain.interfaces.llm_provider import ILLMProvider
from ...core.config import settings
from .prompts import build_messages


class KimiProvider(ILLMProvider):
    MODEL = "moonshotai/kimi-k2.5"

    @property
    def model_id(self) -> str:
        return self.MODEL

    @property
    def display_name(self) -> str:
        return "Kimi K2.5"

    def stream_chat(
        self, message: str, history: Optional[List[Dict[str, str]]] = None, system_context: str = ""
    ) -> AsyncGenerator[str, None]:
        api_key = settings.NVIDIA_NIM_API_KEY
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key,
        )
        completion = client.chat.completions.create(
            model=self.MODEL,
            messages=build_messages(message, history, system_context),
            temperature=0.7,
            max_tokens=4096,
            stream=True,
        )
        for chunk in completion:
            if not getattr(chunk, "choices", None) or not chunk.choices:
                continue
            delta = chunk.choices[0].delta
            content = getattr(delta, "content", None) or ""
            if content:
                yield content
