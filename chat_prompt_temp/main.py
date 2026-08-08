import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

llm = ChatGroq(
    model='llama-3.3-70b-versatile',
    temperature=0.2
)

template = ChatPromptTemplate.from_template(
    "explain this {topic} in 5 points."
)

prompt = template.invoke("Foundational Models")

result = llm.invoke(prompt)
print(result.content)

