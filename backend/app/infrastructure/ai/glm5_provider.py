"""
GLM-5 Provider — Implements ILLMProvider (Strategy Pattern).
Supports reasoning/thinking tokens.
"""

import json
from openai import OpenAI
from typing import AsyncGenerator, Optional, List, Dict
from ...domain.interfaces.llm_provider import ILLMProvider
from ...core.config import settings
from .prompts import build_messages


class GLM5Provider(ILLMProvider):
    MODEL = "z-ai/glm5"

    @property
    def model_id(self) -> str:
        return self.MODEL

    @property
    def display_name(self) -> str:
        return "GLM-5 (Reasoning)"

    def stream_chat(
        self, message: str, history: Optional[List[Dict[str, str]]] = None, system_context: str = ""
    ) -> AsyncGenerator[str, None]:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=settings.NVIDIA_GLM5_KEY,
        )
        completion = client.chat.completions.create(
            model=self.MODEL,
            messages=build_messages(message, history, system_context),
            temperature=1,
            max_tokens=16384,
            extra_body={"chat_template_kwargs": {"enable_thinking": True, "clear_thinking": False}},
            stream=True,
        )
        for chunk in completion:
            if not getattr(chunk, "choices", None) or not chunk.choices:
                continue
            delta = chunk.choices[0].delta
            reasoning = getattr(delta, "reasoning_content", None) or ""
            content = getattr(delta, "content", None) or ""
            # Emit as JSON for structured output
            yield json.dumps({"reasoning": reasoning, "content": content}) + "\n"
