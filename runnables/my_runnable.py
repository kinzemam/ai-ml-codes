from langchain_core.runnables import Runnable, RunnableLambda

# HOW TO CREATE CUSTOM RUNNABLES
class My_Runnable(Runnable):
    def invoke(self, input):
        return input.upper()

new_runnable = My_Runnable()
result = new_runnable.invoke("LangChain")
print(result)


#WE CAN ALSO USE LAMBDA FUNCTIONS
double = RunnableLambda(
    lambda x: x*2
)
print(double.invoke(5))