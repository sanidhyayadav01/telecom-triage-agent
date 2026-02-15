from langchain_core.prompts import PromptTemplate
from config import get_llm
from prompts.response_prompt import RESPONSE_PROMPT

llm = get_llm()

def generate_response(message, urgency, intent, entities):
    prompt = PromptTemplate.from_template(RESPONSE_PROMPT)
    chain = prompt | llm

    result = chain.invoke({
        "message": message,
        "urgency": urgency,
        "intent": intent,
        "entities": entities
    })

    return result.content
