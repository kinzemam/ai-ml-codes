from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda, RunnableSequence

double = RunnableLambda(
    lambda x:x*2
)

add100 = RunnableLambda(
    lambda x: x+100
)

#to run two runnables serially one after another
chain = RunnableSequence(
    double, add100
)

print(chain.invoke(10))


#we can also write chains like this to get the same result

chain2 = RunnableSequence(
    lambda x:x*2,
    lambda x:x+100,
)
print(chain2.invoke(10))