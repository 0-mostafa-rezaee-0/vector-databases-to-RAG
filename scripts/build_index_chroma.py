import os
from typing import List

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


def get_client(persist_dir: str) -> chromadb.Client:
    return chromadb.Client(Settings(is_persistent=True, persist_directory=persist_dir))


def main() -> None:
    persist_dir = os.environ.get("CHROMA_DIR", "./data/chroma_store")
    os.makedirs(persist_dir, exist_ok=True)

    client = get_client(persist_dir)
    collection = client.get_or_create_collection("demo")

    texts: List[str] = [
        "What is a vector database?",
        "How do embeddings work?",
        "Explain RAG in simple terms.",
    ]

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    vectors = model.encode(texts, convert_to_numpy=True).tolist()

    ids = [f"doc-{i}" for i in range(len(texts))]
    metadatas = [{"source": "demo", "i": i} for i in range(len(texts))]
    collection.upsert(ids=ids, documents=texts, embeddings=vectors, metadatas=metadatas)

    out = collection.query(query_texts=["What is RAG?"], n_results=2)
    print(out)


if __name__ == "__main__":
    main()


