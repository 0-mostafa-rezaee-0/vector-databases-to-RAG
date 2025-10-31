from typing import List, Tuple

import numpy as np
from sentence_transformers import SentenceTransformer


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)


def main() -> None:
    docs: List[str] = [
        "Embeddings enable semantic search.",
        "Vector DBs store and retrieve embeddings efficiently.",
        "RAG improves LLMs with retrieved context.",
    ]
    query = "How to search semantically?"

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    doc_vecs = model.encode(docs, convert_to_numpy=True)
    q_vec = model.encode([query], convert_to_numpy=True)[0]

    sims: List[Tuple[float, str]] = [(cosine_similarity(q_vec, v), d) for v, d in zip(doc_vecs, docs)]
    sims.sort(reverse=True, key=lambda x: x[0])

    for score, text in sims:
        print(f"{score:.3f} :: {text}")


if __name__ == "__main__":
    main()


