from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# youtube transcript api 
yt_api = YouTubeTranscriptApi()

# prompt
prompt = ChatPromptTemplate.from_template("A transcript context of a youtube video is provided answer the query from the given context or say you dont know. question-{query} context-{context}")

# llm model
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.3)

# output parser
parser = StrOutputParser()

# chian
chain = prompt | llm | parser

# embedding model
embeddings = OllamaEmbeddings(
    model="qwen3-embedding:0.6b"
)

# text splitter - makes chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 300, chunk_overlap=50)

# vector store
vectordb = Chroma(
    collection_name="yt_transcipts",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)

# retriever
retriever = vectordb.as_retriever(search_kwargs={"k": 5})


video_id = input("id of the youtube video: ")
video_i = video_id.strip()
query = input('enter query: ')
query = query.strip()

result = yt_api.fetch(video_id)

text = '\n'.join(snippet.text for snippet in result)
documents = [
    Document(
        page_content=snippet.text, 
        metadata={"start": snippet.start, "duration":snippet.duration, "video_id":video_id}) 
        for snippet in result
    ]

chunks = text_splitter.split_documents(documents)

vectordb.add_documents(chunks)

results = retriever.invoke(query)

context = "\n".join(
    f"Timestamp: {(int(res.metadata['start']) //60):02d}:"
    f"{(int(res.metadata['start']) % 60):02d}\n"
    f"{res.page_content}"
    for res in results
    )

response = chain.invoke({"query": query, "context": context})

print(response)

