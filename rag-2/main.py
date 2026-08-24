from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_chroma import Chroma
load_dotenv()

#DOCUMENT LOADER
loader = PyPDFLoader("./data.pdf")
documents = loader.load()

# TEXT SPLITTER 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

# prompt
prompt = ChatPromptTemplate.from_template("Answer the question from the provided context only or say you dont know - question {query}  context- {context}")

# LLM MODEL
llm = ChatGroq(
    model = 'openai/gpt-oss-120b',
    temperature=0
)

# OUTPUT PARSER
parser = StrOutputParser()

# CHAIN
chain = prompt | llm | parser

# EMBEDDING MODEL
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# VECTOR STORE
vector_db = Chroma(
    collection_name="pdf_documents",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

# RETRIEVER
retriever = vector_db.as_retriever(search_kwargs = {"k": 5})

# CHUNKING PROCESS
chunks = text_splitter.split_documents(documents)

# ADDING CHUNKS TO VECTOR DB
vector_db.add_documents(chunks)

# QUERY
query = input('enter your query: ')

# RETRIEVAL PROCESS
results = retriever.invoke(query)


context = "\n".join(result.page_content for result in results)

response = chain.invoke({"query" : query, "context": context})

print(response)




