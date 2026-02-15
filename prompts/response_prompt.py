RESPONSE_PROMPT = """
You are a telecom support assistant.

Generate a professional draft response.

Context:
Urgency: {urgency}
Intent: {intent}
Entities: {entities}

Customer Message:
{message}

Write a helpful, empathetic telecom support reply.
"""
