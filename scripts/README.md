<h1 align="center">Scripts</h1>

# 1. Purpose

Runnable examples for embeddings, similarity search, vector stores, and a minimal RAG loop.

# 2. Contents

- `embed_text.py`: encode a tiny corpus using Sentence Transformers
- `build_index_chroma.py`: index and query with Chroma (persistent at `data/chroma_store`)
- `query_similarity.py`: cosine similarity over in-memory vectors
- `rag_example.py`: retrieve from Chroma and feed a stubbed generator

# 3. Usage

Run inside the container:

```bash
python scripts/embed_text.py
python scripts/build_index_chroma.py
python scripts/query_similarity.py
python scripts/rag_example.py
```
