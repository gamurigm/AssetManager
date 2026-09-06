"""Exercise the actual SDK graph and its built-in file tools without a paid model."""
import json

import httpx
from langchain_openai import ChatOpenAI
from langsmith import tracing_context
import pytest

from app.agents.deep_agent import main_agent
from app.core.config import settings


def test_minimal_agent_invokes_builtin_file_tool_and_returns_result(monkeypatch):
    calls = []

    def respond(request):
        body = json.loads(request.content)
        calls.append(body)
        names = {tool["function"]["name"] for tool in body["tools"]}
        assert "write_file" in names
        assert "task" not in names
        if len(calls) == 1:
            message = {"role": "assistant", "content": None, "tool_calls": [{
                "id": "call_file", "type": "function", "function": {
                    "name": "write_file", "arguments": json.dumps({"file_path": "/notes.txt", "content": "Risk notes"}),
                },
            }]}
            reason = "tool_calls"
        else:
            assert any(msg["role"] == "tool" for msg in body["messages"])
            message = {"role": "assistant", "content": "Saved ephemeral notes."}
            reason = "stop"
        return httpx.Response(200, json={"id": "chatcmpl-fixture", "object": "chat.completion",
            "created": 1, "model": "test-model", "choices": [{"index": 0, "message": message, "finish_reason": reason}]})

    with httpx.Client(transport=httpx.MockTransport(respond)) as client:
        model = ChatOpenAI(model="test-model", api_key="test", base_url="http://model.test/v1",
                           http_client=client, use_responses_api=False, max_retries=0)
        monkeypatch.setattr(main_agent, "_model", lambda: model)
        with tracing_context(enabled=False):
            assert main_agent.invoke_deep_agent("Draft risk notes") == "Saved ephemeral notes."
    assert len(calls) == 2


def test_agent_rejects_empty_request_and_missing_key(monkeypatch):
    with pytest.raises(ValueError, match="empty"):
        main_agent.invoke_deep_agent(" ")
    monkeypatch.setattr(settings, "DEEP_AGENT_API_KEY", "")
    monkeypatch.setattr(settings, "NVIDIA_NIM_API_KEY", "")
    with pytest.raises(ValueError, match="Configure"):
        main_agent._model()
