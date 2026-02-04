import requests
from sentence_transformers import SentenceTransformer

ENDEE_URL = "http://localhost:8080"
INDEX_NAME = "documents"

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(query, top_k=3):
    vector = model.encode([query])[0].tolist()

    payload = {
        "vector": vector,
        "level": top_k
    }

    response = requests.post(
        f"{ENDEE_URL}/api/v1/index/{INDEX_NAME}/search",
        json=payload
    )

    if response.status_code != 200:
        return []

    data = response.json()
    results = data.get("results", [])
    return [item["metadata"]["text"] for item in results]