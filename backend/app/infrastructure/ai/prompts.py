"""
Shared system prompt for all financial AI models.
Extracted here to follow DRY and SRP — single source of truth.
"""

FINANCIAL_SYSTEM_PROMPT = (
    "You are a specialized Financial Intelligence Assistant for an Asset Management platform. "
    "Your expertise is centered on financial markets, investments, trading, economics, and asset management. "
    "While you should be polite and engage in basic greetings (e.g., 'hello', 'hey'), "
    "you are PROHIBITED from answering complex non-financial questions about general knowledge, cooking, sports, etc. "
    "If a user asks a complex non-financial question, politely state that your specialization is market analysis."
)


def build_messages(message: str, history=None, system_context: str = ""):
    """Build the messages array for any OpenAI-compatible API.

    Enforces strict user/assistant alternation required by NVIDIA NIM models
    (e.g. Mixtral).  Consecutive same-role messages are merged into one.
    """
    system = FINANCIAL_SYSTEM_PROMPT
    if system_context:
        system += f"\n\n{system_context}"

    messages = [{"role": "system", "content": system}]

    if history:
        for msg in history:
            content = msg.get("content")
            if not content:
                continue
            role = msg.get("role", "user")
            # Merge consecutive messages with the same role
            if messages and messages[-1]["role"] == role:
                messages[-1]["content"] += "\n" + content
            else:
                messages.append({"role": role, "content": content})

    # Append the new user message (merge if last message is also "user")
    if messages and messages[-1]["role"] == "user":
        messages[-1]["content"] += "\n" + message
    else:
        messages.append({"role": "user", "content": message})

    return messages
