import os;

from dotenv import load_dotenv;
from langchain_groq import ChatGroq;

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

def chatbot_reply(message):
    result = llm.invoke(message)
    return result.content

while(True):
    user = input("You: ")
    if(user == 'exit'):
        break
    result = chatbot_reply(user)
    print("AI: ", result)
    print("enter exit to leave")
