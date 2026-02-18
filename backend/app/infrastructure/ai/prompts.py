"""
Shared system prompt for all financial AI models.
Extracted here to follow DRY and SRP — single source of truth.
"""

FINANCIAL_SYSTEM_PROMPT = (
    "You are a specialized Financial Intelligence Assistant for an Asset Management platform. "
    "Your expertise is STRICTLY LIMITED to financial markets, investments, trading, economics, and asset management. "
    "You are PROHIBITED from discussing or answering questions about any other topics, including but not limited to: "
    "general knowledge, entertainment, cooking, sports, personal advice, or creative writing. "
    "If a user asks about a non-financial topic, you must politely decline and state: "
    "'I am a specialized financial AI, I can only assist with investment and market-related queries.'"
)


def build_messages(message: str, history=None, system_context: str = ""):
    """Build the messages array for any OpenAI-compatible API."""
    system = FINANCIAL_SYSTEM_PROMPT
    if system_context:
        system += f"\n\n{system_context}"

    messages = [{"role": "system", "content": system}]
    if history:
        for msg in history:
            if msg.get("content"):
                messages.append({"role": msg.get("role", "user"), "content": msg["content"]})
    messages.append({"role": "user", "content": message})
    return messages
