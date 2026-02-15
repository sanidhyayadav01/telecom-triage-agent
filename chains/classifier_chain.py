from langchain_core.prompts import PromptTemplate
from config import get_llm
from prompts.classifier_prompt import CLASSIFIER_PROMPT
from utils.json_parser import extract_json

llm = get_llm()

def classify_message(message):
    prompt = PromptTemplate.from_template(CLASSIFIER_PROMPT)
    chain = prompt | llm
    result = chain.invoke({"message": message})
    return extract_json(result.content)

