import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq;

load_dotenv()

messages = [
    SystemMessage(content="You are a software expert")
]

llm = ChatGroq(
    model='llama-3.3-70b-versatile',
    temperature=0.2
)

while(True):
    print("enter exit to quit")
    user = input("You: ").strip()
    if(user.lower() == 'exit'):
        print("AI: Goodbye")
        break
    messages.append(
        HumanMessage(content=user) 
    )
    result = llm.invoke(messages)
    messages.append(
        AIMessage(content=result.content)
    )
    print("AI: ", result.content)
