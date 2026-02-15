import json
import re


def extract_json(text: str):
    """
    Extract first valid JSON object from LLM output.
    Works even if model adds explanations or markdown.
    """

    try:
        # Remove markdown ```json ```
        text = re.sub(r"```json|```", "", text)

        # Find JSON object
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            json_str = match.group(0)
            return json.loads(json_str)

    except Exception:
        pass

    # fallback safe structure
    return {
        "customer_id": "Not Provided",
        "phone_number": "Not Provided",
        "ticket_id": "Not Provided",
        "date": "Not Provided"
    }
