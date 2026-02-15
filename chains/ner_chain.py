from langchain_core.prompts import PromptTemplate
from config import get_llm
from prompts.ner_prompt import NER_PROMPT
from utils.json_parser import extract_json

llm = get_llm()

def extract_entities(message):
    prompt = PromptTemplate.from_template(NER_PROMPT)
    chain = prompt | llm
    result = chain.invoke({"message": message})

    return extract_json(result.content)
