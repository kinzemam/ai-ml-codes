# PDF RAG with LangChain, Chroma & Groq

A simple **Retrieval-Augmented Generation (RAG)** project that loads information from a PDF, splits it into chunks, generates embeddings, stores them in a persistent Chroma vector database, retrieves relevant information using similarity search, and uses an LLM to generate an answer from the retrieved context.

## 🚀 RAG Pipeline

```text
PDF Document
     ↓
PyPDFLoader
     ↓
Text Splitting
     ↓
Ollama Embeddings
     ↓
Chroma Vector Database
     ↓
Similarity Search
     ↓
Relevant Context
     ↓
Groq LLM
     ↓
Final Answer
```

## 🧠 How It Works

### 1. PDF Loading

The PDF is loaded using LangChain's `PyPDFLoader`.

```text
data.pdf
   ↓
PyPDFLoader
   ↓
LangChain Documents
```

### 2. Document Chunking

The extracted document is split into smaller chunks using `RecursiveCharacterTextSplitter`.

Current configuration:

```text
chunk_size = 200
chunk_overlap = 20
```

Chunking allows the retrieval system to search smaller, more relevant sections of the document rather than the entire PDF.

### 3. Embeddings

Each chunk is converted into a numerical vector using:

**`nomic-embed-text`**

The embedding model is run locally through **Ollama**.

```text
Text Chunk
    ↓
nomic-embed-text
    ↓
Embedding Vector
```

### 4. Persistent Vector Database

The embeddings and document chunks are stored using **Chroma**.

The database is configured with:

```text
./chroma_db
```

This means the vector database persists on disk instead of existing only in memory.

### 5. Similarity Search

When a user enters a question, the query is converted into an embedding and compared with the stored vectors.

The retriever currently returns the top **5** relevant chunks.

```text
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Top 5 Relevant Chunks
```

### 6. LLM Generation

The retrieved chunks are combined into a context and passed to the LLM along with the user's question.

The model is instructed to answer using only the retrieved context and respond that it doesn't know when the information isn't available.

## 🛠️ Technologies Used

* **Python**
* **LangChain**
* **PyPDF**
* **RecursiveCharacterTextSplitter**
* **Ollama**
* **nomic-embed-text**
* **Chroma**
* **Groq**
* **GPT-OSS-120B**
* **uv**
* **python-dotenv**
* **Git & GitHub**

## 📋 Prerequisites

Make sure you have the following installed:

* Python 3.10+
* `uv`
* Ollama
* Git

You also need:

* A Groq API key
* The `nomic-embed-text` Ollama model

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd rag-2
```

### 2. Install dependencies

This project uses `uv` for dependency management.

```bash
uv sync
```

### 3. Install the Ollama embedding model

Make sure Ollama is installed and running.

Then:

```bash
ollama pull nomic-embed-text
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

**Never commit your `.env` file to GitHub.**

## ▶️ Running the Project

Run the application using:

```bash
uv run main.py
```

The program will ask:

```text
enter your query:
```

You can then ask questions related to the information contained in `data.pdf`.

### Example

```text
enter your query: What is artificial intelligence?
```

The application will:

```text
Question
   ↓
Query Embedding
   ↓
Chroma Similarity Search
   ↓
Relevant PDF Chunks
   ↓
Context + Question
   ↓
GPT-OSS-120B
   ↓
Answer
```

## 💾 Persistent Storage

Unlike an in-memory vector store, Chroma stores the vector database in:

```text
./chroma_db
```

This allows the embeddings to persist after the Python program terminates.

The `chroma_db` directory is intentionally excluded from Git using `.gitignore`.

The PDF and source code are committed to the repository, while the local vector database can be generated again when setting up the project.

## 📁 Project Structure

```text
rag-2/
│
├── data.pdf              # Source document
├── main.py               # RAG application
├── .env                  # API keys (not committed)
├── .gitignore
├── pyproject.toml        # Project dependencies
├── uv.lock               # Locked dependencies
└── chroma_db/            # Local persistent vector database
```

## 🧪 Testing the RAG System

Try questions that are answered in `data.pdf`, for example:

```text
What is artificial intelligence?
```

```text
What are the three types of machine learning?
```

```text
What is supervised learning?
```

```text
What is an embedding?
```

```text
Why are vector databases useful in RAG?
```

You can also test questions that are **not present in the PDF**:

```text
What is the capital of France?
```
## Demo Run

<img width="2034" height="316" alt="image" src="https://github.com/user-attachments/assets/ff8a5a31-4303-4e09-97ef-1d335711f315" />

<img width="2142" height="353" alt="image" src="https://github.com/user-attachments/assets/49e95116-d1cf-4b7a-b246-8dcc02ce0051" />

The model should respond that it doesn't know because the answer is not present in the retrieved context.

## 🔑 Key Concepts Learned

This project demonstrates the fundamental components of a RAG system:

* PDF document loading
* Document chunking
* Chunk overlap
* Text embeddings
* Local embedding models
* Vector databases
* Persistent vector storage
* Similarity search
* Retrievers
* Prompt templates
* Context injection
* LLM generation
* Basic RAG architecture

## 🔮 Future Improvements

Possible improvements to this project include:

* Separate document ingestion from querying
* Prevent duplicate document insertion
* Detect modified documents
* Add document metadata and filtering
* Use a larger collection of documents
* Experiment with different chunk sizes
* Experiment with different embedding models
* Add a persistent database such as PostgreSQL + pgvector
* Add a web interface
* Add conversation history
* Evaluate retrieval quality
* Implement hybrid search and reranking

## 🎯 Purpose

This project was built as a hands-on introduction to **Retrieval-Augmented Generation**.

The main goal was to understand how:

**documents → chunks → embeddings → vector database → retrieval → LLM**

work together to create a basic RAG application.
