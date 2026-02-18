"""
DeepSeek V3.2 Provider — Implements ILLMProvider (Strategy Pattern).
Supports reasoning/thinking tokens.
"""

import json
from openai import OpenAI
from typing import AsyncGenerator, Optional, List, Dict
from ...domain.interfaces.llm_provider import ILLMProvider
from ...core.config import settings
from .prompts import build_messages


class DeepSeekProvider(ILLMProvider):
    MODEL = "deepseek-ai/deepseek-v3.2"

    @property
    def model_id(self) -> str:
        return self.MODEL

    @property
    def display_name(self) -> str:
        return "DeepSeek V3.2 (Reasoning)"

    def stream_chat(
        self, message: str, history: Optional[List[Dict[str, str]]] = None, system_context: str = ""
    ) -> AsyncGenerator[str, None]:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=settings.NVIDIA_DEEPSEEK_KEY,
        )
        completion = client.chat.completions.create(
            model=self.MODEL,
            messages=build_messages(message, history, system_context),
            temperature=1,
            top_p=0.95,
            max_tokens=8192,
            extra_body={"chat_template_kwargs": {"thinking": True}},
            stream=True,
        )
        for chunk in completion:
            if not getattr(chunk, "choices", None) or not chunk.choices:
                continue
            delta = chunk.choices[0].delta
            reasoning = getattr(delta, "reasoning_content", None) or ""
            content = getattr(delta, "content", None) or ""
            # Emit structured output with reasoning
            yield json.dumps({"reasoning": reasoning, "content": content}) + "\n"
