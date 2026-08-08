import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

parser = StrOutputParser()

model = ChatGroq(
    model='llama-3.3-70b-versatile',
    temperature=0.3
)

prompt1 = ChatPromptTemplate.from_template("Explain {topic} in depth and detail")
prompt2 = ChatPromptTemplate.from_template("Summarise the {text} in 5-6 points")
prompt3 = ChatPromptTemplate.from_template("Based on the {text} generate 10 quiz questions")

prompt4 = ChatPromptTemplate.from_template("Based on this summary {summary} and here are the 10 quiz questions based on it {quiz}. Just align and rearrange them in a proper fashion")
chain1 = prompt1 | model | parser | prompt2 | model | parser #this chain consists of 2 prompts first generates a long text on the given topic second prompts takes it as input and summarises it in five points
chain2 = prompt1 | model | parser | prompt3 | model | parser #this chain consists of 2 prompts first generates a long text on the given topic second prompts takes it as input and generates 10 questions based on it
chain3 = prompt4 | model | parser #this chain has a single prompt which takes result of chain1 and chain2 and input and merges them to give a single output

topic = "Jeffrey Epstein"
result = chain3.invoke({
    "summary": chain1.invoke(topic),
    "quiz":chain2.invoke(topic)
})
print(result)