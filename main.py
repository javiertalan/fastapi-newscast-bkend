from fastapi import FastAPI
import chromadb

app = FastAPI()

# Initialize ChromaDB (persistent storage)
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("news")

# Endpoint to add news articles to the database
@app.post("/add_news/")
def add_news(title: str, description: str, link: str):
    collection.add(
        documents=[f"{title} {description}"],
        metadatas=[{"title": title, "link": link}]
    )
    return {"message": "News added"}

# Endpoint to search for relevant news articles
@app.get("/search_news/")
def search_news(query: str):
    results = collection.query(query_texts=[query], n_results=5)
    return results["metadatas"]

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the AI-powered Newscast API"} 