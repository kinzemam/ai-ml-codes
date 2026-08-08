import os 
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

parser = StrOutputParser()
load_dotenv()

model = ChatGroq(
    model='llama-3.3-70b-versatile',
    temperature=0.3
)

prompt = ChatPromptTemplate.from_template("Explain this {topic} in five points")

chain = prompt | model | parser


result = chain.invoke({
    "topic": "French Revolution"
})
print(result)
