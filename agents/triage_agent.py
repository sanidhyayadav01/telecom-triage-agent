import json
from chains.classifier_chain import classify_message
from chains.ner_chain import extract_entities
from chains.response_chain import generate_response


class TelecomTriageAgent:

    def process(self, message):

        print("\n🔎 Classifying message...")
        classification = classify_message(message)
        classification_json = classification

        print("🧠 Extracting entities...")
        entities = extract_entities(message)

        print("✉️ Generating response...")
        response = generate_response(
            message,
            classification_json["urgency"],
            classification_json["intent"],
            entities
        )

        return {
            "classification": classification_json,
            "entities": entities,
            "draft_response": response
        }
