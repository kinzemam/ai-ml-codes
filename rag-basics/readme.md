# RAG Basics with LangChain

A simple **Retrieval-Augmented Generation (RAG)** project built with **Python and LangChain**.

This project demonstrates how to take information from a text document, split it into smaller chunks, convert those chunks into embeddings, store them in a vector store, retrieve the most relevant chunks using similarity search, and provide that context to an LLM to generate an answer.

## 🚀 What I Built

The project implements a basic RAG pipeline:

```text
Text Document
     ↓
Document Loader
     ↓
Text Chunking
     ↓
Embeddings
     ↓
Vector Store
     ↓
Similarity Search / Retriever
     ↓
Relevant Context
     ↓
LLM
     ↓
Generated Answer
```

### How it works

1. **Load the document**
   A `.txt` file is loaded using LangChain's `TextLoader`.

2. **Split the document into chunks**
   `RecursiveCharacterTextSplitter` divides the document into smaller pieces so that relevant sections can be retrieved efficiently.

3. **Generate embeddings**
   The chunks are converted into vector representations using the `nomic-embed-text` embedding model through Ollama.

4. **Store the embeddings**
   The generated embeddings and their corresponding document chunks are stored using LangChain's `InMemoryVectorStore`.

5. **Retrieve relevant information**
   When a user asks a question, the question is embedded and similarity search is performed against the stored vectors.

6. **Generate the answer**
   The retrieved chunks are provided as context to the LLM, which generates an answer based on the retrieved information.

## 🛠️ Technologies & Tools

* **Python** — Programming language
* **LangChain** — RAG framework and application orchestration
* **LangChain Community** — Document loading utilities
* **LangChain Text Splitters** — Document chunking
* **Ollama** — Local model runtime
* **nomic-embed-text** — Embedding model
* **InMemoryVectorStore** — Vector storage and similarity search
* **Groq / OpenAI-compatible LLM** — Text generation
* **uv** — Python package and environment management
* **python-dotenv** — Environment variable management
* **Git & GitHub** — Version control

## 📋 Prerequisites

Before running the project, make sure you have:

* Python 3.10+
* [uv](https://docs.astral.sh/uv/)
* [Ollama](https://ollama.com/)
* A Groq API key (or another compatible LLM API key)

You can verify Python and uv with:

```bash
python --version
uv --version
```

Verify Ollama with:

```bash
ollama --version
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd rag-basics
```

### 2. Create the virtual environment

If you're using `uv`:

```bash
uv sync
```

### 3. Install the embedding model

Make sure Ollama is running and pull the embedding model:

```bash
ollama pull nomic-embed-text
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

Do **not** commit your `.env` file to GitHub.

## ▶️ Running the Project

Run the application with:

```bash
uv run main.py
```

The program will:

1. Load the text document.
2. Split it into chunks.
3. Generate embeddings.
4. Store the embeddings in the vector store.
5. Perform similarity search based on the user's query.
6. Send the retrieved context to the LLM.
7. Generate the final answer.

## 🧠 Key Concepts Learned

This project helped me understand the fundamental components of a RAG system:

* Document loading
* Text chunking
* Chunk overlap
* Embeddings
* Vector stores
* Similarity search
* Retrievers
* Context injection
* Prompt templates
* LLM invocation
* Basic RAG architecture

## 📌 Current Limitations

This is a learning project, so it intentionally uses a simple setup.

* `InMemoryVectorStore` is temporary and does not persist data between program executions.
* The project currently works with a simple `.txt` document.
* Retrieval and generation are implemented as a basic RAG pipeline.
* Ollama is required for the local embedding model.

## 🔮 Possible Improvements

Future improvements could include:

* Persistent vector databases such as Chroma or Qdrant
* PDF and web document loaders
* Better chunking strategies
* Retrieval evaluation
* Metadata filtering
* Conversational memory
* Streaming responses
* A web interface
* More advanced RAG techniques such as hybrid search and reranking

## 📚 Project Purpose

This project was created as a hands-on introduction to **Retrieval-Augmented Generation** and to understand how embeddings, vector databases, retrieval, and LLMs work together to build a RAG application.
