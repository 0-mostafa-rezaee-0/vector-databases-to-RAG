from typing import List

from sentence_transformers import SentenceTransformer
from chromadb import Client
from chromadb.config import Settings


def retrieve(client: Client, query: str, top_k: int = 3) -> List[str]:
    coll = client.get_or_create_collection("rag")
    res = coll.query(query_texts=[query], n_results=top_k)
    return res.get("documents", [[]])[0]


def generate(prompt: str) -> str:
    # Placeholder generator: in real usage, call an LLM (e.g., OpenAI)
    return f"[LLM Answer] {prompt[:200]}"


def main() -> None:
    client = Client(Settings(is_persistent=True, persist_directory="./data/chroma_store"))
    coll = client.get_or_create_collection("rag")

    # Seed a tiny knowledge base if empty
    if coll.count() == 0:
        docs = [
            "RAG retrieves relevant documents and augments LLM prompts.",
            "Embeddings map text to vectors enabling semantic similarity.",
            "Chroma is a lightweight local vector database.",
        ]
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        vecs = model.encode(docs, convert_to_numpy=True).tolist()
        coll.upsert(ids=[f"kb-{i}" for i in range(len(docs))], documents=docs, embeddings=vecs)

    question = "What is RAG and why use it?"
    contexts = retrieve(client, question, top_k=2)
    context_block = "\n".join(f"- {c}" for c in contexts)
    prompt = f"Answer the question using the context.\nContext:\n{context_block}\n\nQuestion: {question}\nAnswer:"
    print(generate(prompt))


if __name__ == "__main__":
    main()


