NER_PROMPT = """
Extract telecom-related entities.

Find:
- customer_id
- phone_number
- ticket_id
- date

Return JSON only:

{{
 "customer_id": "",
 "phone_number": "",
 "ticket_id": "",
 "date": ""
}}

Message:
{message}
"""
