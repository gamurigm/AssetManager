"""Minimal Deep Agent configured for the project's OpenAI-compatible provider."""

from __future__ import annotations

from typing import Any

from deepagents import create_deep_agent
from deepagents.backends import StateBackend
from deepagents.profiles import (
    GeneralPurposeSubagentProfile, HarnessProfile, register_harness_profile,
)
from langchain_openai import ChatOpenAI
from langsmith import tracing_context

from ...core.config import settings


def _model() -> ChatOpenAI:
    api_key = settings.DEEP_AGENT_API_KEY or settings.NVIDIA_NIM_API_KEY
    if not api_key:
        raise ValueError("Configure NVIDIA_NIM_API_KEY or DEEP_AGENT_API_KEY in backend/.env")
    return ChatOpenAI(
        model=settings.DEEP_AGENT_MODEL or settings.NIM_MODEL_NAME,
        api_key=api_key,
        base_url=settings.DEEP_AGENT_BASE_URL or settings.NVIDIA_NIM_BASE_URL,
        use_responses_api=False,
        timeout=settings.DEEP_AGENT_TIMEOUT_SECONDS,
        max_retries=0,
    )


def _message_text(message: Any) -> str:
    content = getattr(message, "content", message)
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            item.get("text", "") if isinstance(item, dict) else str(item)
            for item in content
        )
    return str(content)


def build_deep_agent(model=None):
    """Build an ephemeral agent; no host filesystem, subagents or persistence."""
    selected_model = model if model is not None else _model()
    if isinstance(selected_model, ChatOpenAI):
        # Public profile API in the pinned SDK: subagents=[] alone still adds
        # the default general-purpose agent. Disable that default explicitly.
        register_harness_profile(
            f"openai:{selected_model.model_name}",
            HarnessProfile(general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False)),
        )
    return create_deep_agent(
        model=selected_model,
        backend=StateBackend(),
        subagents=[],
        system_prompt=(
            "You are a concise financial asset-management assistant. "
            "Answer the user's request directly and explain assumptions when needed. "
            "You may use the built-in virtual filesystem to draft and read notes. "
            "Files are ephemeral. No live market data or trading tools are connected."
        ),
    )


def invoke_deep_agent(user_request: str) -> str:
    """Invoke the minimal Deep Agent and return its final response text."""
    if not user_request.strip():
        raise ValueError("user_request must not be empty")
    agent = build_deep_agent()
    # LangSmith is an SDK transitive dependency; this example never sends traces.
    with tracing_context(enabled=False):
        result = agent.invoke(
            {"messages": [{"role": "user", "content": user_request}]},
            config={"recursion_limit": 30},
        )
    return _message_text(result["messages"][-1])
