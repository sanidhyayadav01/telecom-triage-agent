CLASSIFIER_PROMPT = """
You are a telecom support triage classifier.

Classify the message into:

Urgency:
- low
- medium
- high
- critical

Intent:
- billing
- network_issue
- sim_issue
- complaint
- outage
- other

Return ONLY JSON:

{{
 "urgency": "",
 "intent": ""
}}

Message:
{message}
"""
