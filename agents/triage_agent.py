import json
from chains.classifier_chain import classify_message
from chains.ner_chain import extract_entities
from chains.response_chain import generate_response


class TelecomTriageAgent:

    # -----------------------------
    # Ticket Routing Logic
    # -----------------------------
    def route_ticket(self, intent: str) -> str:
        routing_map = {
            "network_issue": "🌐 Network Support Team",
            "billing_issue": "💳 Billing Support Team",
            "sim_issue": "📱 SIM Support Team",
            "technical_issue": "🛠 Technical Support Team",
            "general_query": "📞 Customer Care"
        }

        return routing_map.get(intent, "📞 Customer Care")

    # -----------------------------
    # Main Processing Pipeline
    # -----------------------------
    def process(self, message):

        print("\n🔎 Classifying message...")
        classification = classify_message(message)

        # Safety fallback (prevents UI crashes if LLM output changes)
        urgency = classification.get("urgency", "unknown")
        intent = classification.get("intent", "general_query")

        classification_json = {
            "urgency": urgency,
            "intent": intent
        }

        print("🧠 Extracting entities...")
        entities = extract_entities(message)

        print("✉️ Generating response...")
        response = generate_response(
            message,
            urgency,
            intent,
            entities
        )

        # Routing decision
        route = self.route_ticket(intent)

        # ---- Console Output (CLI still works) ----
        print("\n========== TRIAGE RESULT ==========\n")
        print(f"Urgency: {urgency}")
        print(f"Intent: {intent}")
        print(f"Routed To: {route}")
        print("\nEntities:")
        print(entities)
        print("\nDraft Response:")
        print(response)
        print("\n===================================")

        # ---- Structured Output (UI consumes this) ----
        return {
            "classification": classification_json,
            "entities": entities,
            "draft_response": response,
            "route": route
        }