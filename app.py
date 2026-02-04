from fastapi import FastAPI
from query import semantic_search

app = FastAPI()

@app.get("/")
def root():
    return {"status": "DocMind Endee RAG running"}

@app.get("/ask")
def ask(question: str):
    results = semantic_search(question)

    if not results:
        return {
            "question": question,
            "answer": "No relevant information found"
        }

    return {
        "question": question,
        "answer": " ".join(results),
        "sources": results
    }