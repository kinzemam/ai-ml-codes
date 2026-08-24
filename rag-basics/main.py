from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
#TEXT FILE LOADER
loader = TextLoader('./data.txt')
documents = loader.load()

# TEXT SPLITTER - MAKES CHUNKS
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

#llm MODEL
llm = ChatGroq(
    model = 'openai/gpt-oss-120b',
    temperature=0
)

#PROMPT TEMPLATE
prompt = ChatPromptTemplate.from_template("Answer only from the provided context else just say you dont know-{question} context-{context}")

#PARSER
parser = StrOutputParser()

#EMBEDDING MODEL
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

#VECTOR STORE TO STORE EMBEDDINGS
vectordb = InMemoryVectorStore(embeddings)

#CREATING CHUNKS
chunks = text_splitter.split_documents(documents)

#STORING CHUNKS IN VECTOR STORE
vectordb.add_documents(documents=chunks)

#QUERY
query = input("ENTER YOUR QUERY: ")

#RETRIEVER
retriever = vectordb.as_retriever(kwargs={"k": 3})

#CHAIN - pipeline
chain = prompt | llm | parser

#retrieving relevant documents(top k chunks)
results = retriever.invoke(query)

#joining chunks together
context = "/n/n".join(doc.page_content for doc in results)

#invoking query
response = chain.invoke({'question': query, 'context':context})

print(response)