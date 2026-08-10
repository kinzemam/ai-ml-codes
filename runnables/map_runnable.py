from langchain_core.runnables import RunnableLambda, RunnableMap

#to run two runnables parallely
new_runnable = RunnableMap({
    "uppercase": lambda x:x.upper(),
    "reverse":lambda x:x[::-1],
})

print(new_runnable.invoke("Hello World"))