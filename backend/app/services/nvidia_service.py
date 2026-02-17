import requests
import json
from openai import OpenAI
from ..core.config import settings
from typing import AsyncGenerator, Optional

class NvidiaService:
    FINANCIAL_SYSTEM_PROMPT = (
        "You are a specialized Financial Intelligence Assistant for an Asset Management platform. "
        "Your expertise is STRICTLY LIMITED to financial markets, investments, trading, economics, and asset management. "
        "You are PROHIBITED from discussing or answering questions about any other topics, including but not limited to: "
        "general knowledge, entertainment, cooking, sports, personal advice, or creative writing. "
        "If a user asks about a non-financial topic, you must politely decline and state: "
        "'I am a specialized financial AI, I can only assist with investment and market-related queries.'"
    )

    @staticmethod
    def chat_mistral_large(message: str) -> AsyncGenerator[str, None]:
        invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {settings.NVIDIA_MISTRAL_LARGE_KEY}",
            "Accept": "text/event-stream"
        }
        payload = {
            "model": "mistralai/mistral-large-3-675b-instruct-2512",
            "messages": [
                {"role": "system", "content": NvidiaService.FINANCIAL_SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            "max_tokens": 2048,
            "temperature": 0.15,
            "top_p": 1.00,
            "stream": True
        }

        response = requests.post(invoke_url, headers=headers, json=payload, stream=True)
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                if decoded_line.startswith("data: "):
                    data_str = decoded_line[6:]
                    if data_str == "[DONE]":
                        break
                    try:
                        data = json.loads(data_str)
                        content = data["choices"][0]["delta"].get("content", "")
                        if content:
                            yield content
                    except:
                        continue

    @staticmethod
    def chat_mixtral_8x22b(message: str) -> AsyncGenerator[str, None]:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=settings.NVIDIA_MIXTRAL_8X22B_KEY
        )
        completion = client.chat.completions.create(
            model="mistralai/mixtral-8x22b-instruct-v0.1",
            messages=[
                {"role": "system", "content": NvidiaService.FINANCIAL_SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )
        for chunk in completion:
            if not getattr(chunk, "choices", None):
                continue
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content

    @staticmethod
    def chat_glm5(message: str) -> AsyncGenerator[dict, None]:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=settings.NVIDIA_GLM5_KEY
        )
        completion = client.chat.completions.create(
            model="z-ai/glm5",
            messages=[
                {"role": "system", "content": NvidiaService.FINANCIAL_SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            temperature=1,
            top_p=1,
            max_tokens=16384,
            extra_body={"chat_template_kwargs": {"enable_thinking": True, "clear_thinking": False}},
            stream=True
        )
        for chunk in completion:
            if not getattr(chunk, "choices", None):
                continue
            if len(chunk.choices) == 0 or getattr(chunk.choices[0], "delta", None) is None:
                continue
            delta = chunk.choices[0].delta
            reasoning = getattr(delta, "reasoning_content", None)
            content = getattr(delta, "content", None)
            
            yield {
                "reasoning": reasoning if reasoning else "",
                "content": content if content else ""
            }

nvidia_service = NvidiaService()
