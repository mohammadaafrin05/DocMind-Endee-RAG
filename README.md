DocMind – Endee-powered RAG System

DocMind is a Retrieval-Augmented Generation (RAG) application that enables users to semantically search and query documents using vector embeddings stored in Endee.
It demonstrates how Endee can be used as a high-performance vector database for real-world AI applications.

Project Overview & Problem Statement
Problem

Traditional keyword search fails to capture semantic meaning. As document collections grow, users need a way to search based on intent and context, not exact words.

Solution

DocMind solves this by:

Converting documents into semantic embeddings

Storing them in Endee

Retrieving the most relevant content using vector similarity search

Serving results via a FastAPI backend

This architecture enables fast, accurate, and scalable document retrieval.

System Design & Technical Approach
High-Level Architecture
Documents
   ↓
SentenceTransformer (Embeddings)
   ↓
Endee Vector Database
   ↓
FastAPI Backend
   ↓
User Query → Semantic Search → Relevant Context

Components
Component	Description
SentenceTransformers	Generates vector embeddings from text
Endee	Stores and indexes embeddings for similarity search
FastAPI	Backend API for querying documents
Uvicorn	ASGI server for running the API
Docker	Runs Endee server
How Endee Is Used

Endee acts as the vector database in this system.

Responsibilities

Stores document embeddings

Performs similarity search

Returns top-K relevant results

Why Endee?

High-performance C++ backend

Efficient vector indexing

Simple HTTP API

Suitable for RAG workflows

Endee runs as a Docker service and is accessed by the Python application via HTTP.

Project Structure
DocMind-Endee-RAG/
├── data/
│   └── documents.txt        # Input documents
├── endee/                   # Endee Docker setup
├── ingest.py                # Document ingestion script
├── query.py                 # Semantic search logic
├── app.py                   # FastAPI application
├── requirements.txt
└── README.md

Setup Instructions
1️.Prerequisites

Python 3.10+

Docker & Docker Compose

Git

2️.Clone the Repository
git clone https://github.com/<your-username>/DocMind-Endee-RAG.git
cd DocMind-Endee-RAG

3️.Start Endee Server (Docker)
cd endee
docker-compose up --build


Endee will start at:
http://localhost:8080

Verify health:

curl http://localhost:8080/api/v1/health


Expected response:

{"status":"ok"}

4️.Set Up Python Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt

Ingest Documents into Endee

Ensure data/documents.txt contains sample text.

Run:

python ingest.py


Expected output:

 Documents successfully ingested into Endee


This step:

Reads documents

Creates embeddings

Stores them in Endee

 Run the API Server
uvicorn app:app --reload


API will be available at:

http://127.0.0.1:8000

 How to Check the Working Use Case
1️.Verify API Is Running

Open browser:

http://127.0.0.1:8000/


Response:

{"status":"DocMind Endee RAG running"}

2️.Ask a Semantic Question

Example:

http://127.0.0.1:8000/ask?question=What is Endee used for?


Expected response:

{
  "question": "What is Endee used for?",
  "answer": "Endee is used for storing and searching vector embeddings...",
  "sources": [
    "Endee is a high-performance vector database..."
  ]
}


This confirms:

Query embedding is generated

Endee similarity search is working

Relevant document context is returned

 Key Highlights

End-to-end RAG pipeline

Production-grade vector database

Clean FastAPI interface

Dockerized backend service

Easily extensible for LLM integration

 Future Enhancements

Add LLM (OpenAI / Ollama / HuggingFace) for answer generation

Support PDF ingestion

Add authentication

UI frontend
