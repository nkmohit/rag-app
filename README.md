# Minimal RAG Backend (FastAPI, Chroma, Gemini)

This repository contains a minimal, production-oriented Retrieval-Augmented Generation (RAG) backend.

The intent of this project is not to be feature-complete, but to implement the core RAG pipeline correctly and clearly, with an emphasis on clean structure, correctness, and engineering fundamentals.

---

## Project Scope

This project deliberately implements only the essential components of a RAG system:

* Document upload
* Text extraction (TXT and PDF)
* Text chunking
* Embedding generation
* Vector storage using Chroma
* Semantic retrieval
* Answer generation using a large language model (Gemini)

The following are intentionally excluded:

* Frontend or user interface
* Authentication or authorization
* Streaming responses
* Agents or orchestration frameworks
* Evaluation pipelines
* Performance optimizations beyond correctness

The goal is clarity and correctness rather than breadth.

---

## Architecture Overview

```
Document Upload
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings (Sentence Transformers)
    ↓
Vector Database (Chroma)
    ↓
Semantic Retrieval
    ↓
LLM Generation (Gemini)
```

Each stage is implemented as a small, focused module with a single responsibility.

---

## Technology Stack

* Backend Framework: FastAPI
* Embedding Model: Sentence Transformers
* Vector Store: Chroma (local persistent storage)
* Language Model: Gemini (via google-genai SDK)
* Deployment: Docker

---

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/nkmohit/rag-app.git
cd rag-app
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Start the application

```bash
uvicorn main:app --reload
```

---

## API Endpoints

### Health Check

```
GET /health
```

### Upload Document

```
POST /upload
```

Accepts a TXT or PDF file and stores it locally.

---

### Index Document

```
POST /index
```

Runs the full ingestion pipeline: extraction, chunking, embedding, and indexing.

---

### Query (Retrieval-Augmented Generation)

```
POST /query
```

Example request:

```json
{
  "query": "What are the key differences between vector databases like Chroma and Pinecone?",
  "top_k": 3,
  "generate": true
}
```

* `top_k` controls how many chunks are retrieved
* `generate` toggles LLM-based answer generation

---

## Persistence Notes

* Chroma stores embeddings on local disk
* Data persists across application restarts
* In containerized deployments, storage is ephemeral unless a volume is mounted

This tradeoff is intentional for simplicity and portability.

---

## Rationale

Many RAG examples abstract away core mechanics behind frameworks or tooling.

This project exists to demonstrate:

* a correct end-to-end RAG flow
* clean backend architecture
* separation of ingestion, retrieval, and generation
* production-style structure without unnecessary complexity

A more feature-rich system (frontend, authentication, scaling, monitoring) can be built on top of this foundation in a separate project.

---

## License

MIT
