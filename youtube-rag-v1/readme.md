# YouTube RAG

A simple Retrieval-Augmented Generation (RAG) project that takes a YouTube video ID, retrieves its transcript, stores transcript chunks as embeddings in Chroma, and uses an LLM to answer questions based on the video content.

## Features

* Extracts transcripts from YouTube videos
* Splits transcripts into smaller chunks
* Generates embeddings using Qwen3-Embedding
* Stores embeddings in a persistent Chroma vector database
* Performs similarity search to retrieve relevant transcript sections
* Uses Groq's LLM to generate answers from the retrieved context
* Preserves video timestamps as metadata

## RAG Pipeline

```text
YouTube Video ID
       ↓
Transcript Extraction
       ↓
LangChain Documents
       ↓
Text Chunking
       ↓
Qwen3 Embeddings
       ↓
Chroma Vector Database
       ↓
Similarity Search
       ↓
Relevant Transcript Chunks
       ↓
Groq LLM
       ↓
Answer
```

## Technologies Used

* Python
* LangChain
* YouTube Transcript API
* Ollama
* Qwen3-Embedding-0.6B
* Chroma
* Groq
* GPT-OSS-120B
* uv
* python-dotenv

## Prerequisites

Make sure you have:

* Python 3.10+
* [Ollama](https://ollama.com/)
* [uv](https://docs.astral.sh/uv/)
* A Groq API key
* A Chroma API Key

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd youtube-rag
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Install the embedding model

Make sure Ollama is running, then download Qwen3-Embedding:

```bash
ollama pull qwen3-embedding:0.6b
```

Verify the model:

```bash
ollama list
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
CHROMA_API_KEY=your_chroma_api_key
```

Do not commit `.env` to GitHub.

## Running the Project

Start the application with:

```bash
uv run main.py
```

Enter a YouTube video ID when prompted:

```text
Enter video ID: <youtube-video-id>
```

Then enter a question about the video:

```text
Enter query: What is this video about?
```

The application retrieves the most relevant transcript chunks and provides them to the LLM as context.

## How It Works

### 1. Transcript Extraction

The YouTube video ID is used to retrieve the video's transcript.

Each transcript snippet contains text and timing information.

### 2. Document Creation

Transcript snippets are converted into LangChain `Document` objects.

The transcript text is stored in `page_content`, while metadata contains information such as:

```python
{
    "start": snippet.start,
    "duration": snippet.duration,
    "video_id": video_id
}
```

### 3. Chunking

The transcript is split using `RecursiveCharacterTextSplitter`.

The current configuration is:

```python
chunk_size=1000
chunk_overlap=100
```

### 4. Embeddings

Each chunk is converted into a vector using:

```text
Qwen3-Embedding-0.6B
```

The embedding model runs locally through Ollama.

### 5. Chroma Vector Database

The generated embeddings and their corresponding chunks are stored in Chroma.

The database is persisted locally in:

```text
./chroma_db
```

### 6. Similarity Search

When the user asks a question, the question is converted into an embedding and compared with the stored transcript embeddings.

The top 5 most relevant chunks are retrieved.

```text
Question
   ↓
Embedding
   ↓
Similarity Search
   ↓
Top 5 Relevant Chunks
```

### 7. LLM Generation

The retrieved chunks are combined into a context and passed to the Groq LLM together with the user's question.

The model is instructed to answer using the provided context.

## Timestamp Metadata

Transcript timestamps are preserved in the document metadata.

This allows the project to eventually provide answers such as:

```text
The speaker discusses this topic around 05:42.
```

A future version can use this information to generate clickable YouTube timestamps.

## Project Structure

```text
youtube-rag/
│
├── main.py
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .env
└── chroma_db/
```

The following should **not** be committed:

```gitignore
.venv/
__pycache__/
.env
chroma_db/
*.pyc
```

## Example Queries

Try questions such as:

```text
What is this video about?
```

```text
What does the speaker say about Earth?
```

```text
Why does the speaker find Earth special?
```

```text
At what timestamp does the speaker discuss Earth?
```

You can also test the system with information that is not present in the video:

```text
What is the capital of France?
```

The model should ideally respond that it doesn't know when the information cannot be found in the retrieved transcript.

## Future Improvements

* Add automatic video title and metadata extraction
* Add video summarization
* Improve timestamp-aware answers
* Generate clickable YouTube timestamps
* Prevent duplicate video ingestion
* Detect already-processed videos
* Support multiple videos in Chroma
* Filter retrieval by `video_id`
* Separate ingestion and querying
* Add a React frontend
* Add an Express/FastAPI backend
* Add chat history
* Add transcript caching
* Experiment with different embedding models
* Add reranking for improved retrieval

## Learning Goal

The goal of this project is to understand how RAG can be applied to dynamic, real-world data such as YouTube transcripts.

The complete pipeline is:

```text
Transcript
    ↓
Documents
    ↓
Chunks
    ↓
Embeddings
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Retrieved Context
    ↓
LLM
    ↓
Answer
```
