"""
Mistral Large Provider — Implements ILLMProvider (Strategy Pattern).
"""

import requests
import json
from typing import AsyncGenerator, Optional, List, Dict
from ...domain.interfaces.llm_provider import ILLMProvider
from ...core.config import settings
from .prompts import build_messages


class MistralLargeProvider(ILLMProvider):
    INVOKE_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
    MODEL = "mistralai/mistral-large-3-675b-instruct-2512"

    @property
    def model_id(self) -> str:
        return self.MODEL

    @property
    def display_name(self) -> str:
        return "Mistral Large"

    def stream_chat(
        self, message: str, history: Optional[List[Dict[str, str]]] = None, system_context: str = ""
    ) -> AsyncGenerator[str, None]:
        headers = {
            "Authorization": f"Bearer {settings.NVIDIA_MISTRAL_LARGE_KEY}",
            "Accept": "text/event-stream",
        }
        payload = {
            "model": self.MODEL,
            "messages": build_messages(message, history, system_context),
            "max_tokens": 2048,
            "temperature": 0.15,
            "top_p": 1.00,
            "frequency_penalty": 0.00,
            "presence_penalty": 0.00,
            "stream": True,
        }
        resp = requests.post(self.INVOKE_URL, headers=headers, json=payload, stream=True)
        for line in resp.iter_lines():
            if not line:
                continue
            decoded = line.decode("utf-8")
            if decoded.startswith("data: "):
                data_str = decoded[6:]
                if data_str == "[DONE]":
                    break
                try:
                    data = json.loads(data_str)
                    content = data["choices"][0]["delta"].get("content", "")
                    if content:
                        yield content
                except Exception:
                    continue
