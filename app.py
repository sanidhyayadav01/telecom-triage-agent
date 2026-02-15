from agents.triage_agent import TelecomTriageAgent
from utils.formatter import display_result

agent = TelecomTriageAgent()

print("📡 Telecom Support Triage Agent Started")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Customer Message > ")

    if user_input.lower() == "exit":
        break

    result = agent.process(user_input)
    display_result(result)
