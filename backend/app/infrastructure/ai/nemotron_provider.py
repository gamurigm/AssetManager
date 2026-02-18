"""
NVIDIA Llama 3.1 Nemotron Ultra 253B Provider — Implements ILLMProvider (Strategy Pattern).
Supports detailed thinking mode via system prompt.
"""

from openai import OpenAI
from typing import AsyncGenerator, Optional, List, Dict
from ...domain.interfaces.llm_provider import ILLMProvider
from ...core.config import settings
from .prompts import build_messages


class NemotronProvider(ILLMProvider):
    MODEL = "nvidia/llama-3.1-nemotron-ultra-253b-v1"

    @property
    def model_id(self) -> str:
        return self.MODEL

    @property
    def display_name(self) -> str:
        return "Nemotron Ultra 253B"

    def stream_chat(
        self, message: str, history: Optional[List[Dict[str, str]]] = None, system_context: str = ""
    ) -> AsyncGenerator[str, None]:
        # Nemotron uses "detailed thinking on" in system prompt to enable reasoning
        thinking_prefix = "detailed thinking on\n\n"
        full_context = thinking_prefix + system_context if system_context else thinking_prefix

        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=settings.NVIDIA_NEMOTRON_KEY,
        )
        completion = client.chat.completions.create(
            model=self.MODEL,
            messages=build_messages(message, history, full_context),
            temperature=0.6,
            top_p=0.95,
            max_tokens=4096,
            frequency_penalty=0,
            presence_penalty=0,
            stream=True,
        )
        for chunk in completion:
            if not getattr(chunk, "choices", None) or not chunk.choices:
                continue
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content
