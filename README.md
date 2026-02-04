📘 DocMind – Semantic Search & RAG using Endee
1. Project Overview & Problem Statement
Project Overview

DocMind is an AI-based semantic search and Retrieval-Augmented Generation (RAG) system built using Endee as the vector database.
The system allows users to ask natural language questions and retrieves the most relevant information from a set of documents based on semantic similarity, not just keyword matching.

Problem Statement

Traditional keyword-based search systems fail to understand the meaning and intent behind user queries. This leads to irrelevant results, especially when queries are phrased differently from the stored text.

The goal of this project is to:

Convert documents into vector embeddings

Store and search them efficiently using a vector database

Retrieve the most relevant context for a given query

2. System Design / Technical Approach
High-Level Architecture
User Query
   ↓
FastAPI Backend (Python)
   ↓
Sentence Transformer (Embeddings)
   ↓
Endee Vector Database (C++ / Docker)
   ↓
Top-K Semantic Results
   ↓
Final Answer (RAG-style)

Technical Flow

Documents are converted into embeddings using a transformer model.

Embeddings are stored in Endee (vector database).

User queries are also embedded using the same model.

Endee performs vector similarity search.

Retrieved results are returned as contextual answers.

3. How Endee is Used

Endee is deployed as a standalone C++ vector database server using Docker.

It is not used as a Python library.

Python communicates with Endee via REST APIs.

Endee handles:

Vector storage

Indexing

Semantic similarity search

Indexes are auto-created during ingestion.

This setup reflects a real-world production architecture where the database and application layers are decoupled.

4. Project Structure
DocMind-Endee-RAG/
│
├── app.py              # FastAPI application
├── ingest.py           # Document ingestion script
├── query.py            # Semantic search logic
├── requirements.txt    # Python dependencies
│
├── data/
│   └── documents.txt   # Sample documents
│
├── endee/
│   ├── docker-compose.yml
│   ├── infra/Dockerfile
│   ├── src/
│   └── install.sh
│
└── venv/

5. Setup & Execution Instructions
Prerequisites

Python 3.10+

Docker & Docker Compose

WSL (for Windows users)

Step 1: Clone the Repository
git clone <your-github-repo-url>
cd DocMind-Endee-RAG

Step 2: Start Endee Vector Database
cd endee
docker-compose up --build


Endee will run at:

http://localhost:8080

Step 3: Set Up Python Environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Step 4: Ingest Documents
python ingest.py


Expected output:

✅ All documents successfully ingested into Endee

Step 5: Run FastAPI Application
uvicorn app:app --reload


API runs at:

http://127.0.0.1:8000

Step 6: Test the Application

Open in browser:

http://127.0.0.1:8000/ask?question=What is Endee?


You will receive a semantic answer based on stored documents.

6. Features Demonstrated

Semantic Search

Retrieval-Augmented Generation (RAG-style)

Vector database integration using Endee

REST-based AI system architecture

Dockerized backend with Python ML pipeline
