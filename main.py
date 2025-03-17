from fastapi import FastAPI
import chromadb

app = FastAPI()

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("news")

# ✅ Ensure this endpoint allows POST requests
@app.post("/add_news/")
def add_news(title: str, description: str, link: str):
    collection.add(
        documents=[f"{title} {description}"],
        metadatas=[{"title": title, "link": link}]
    )
    return {"message": "News added"}
