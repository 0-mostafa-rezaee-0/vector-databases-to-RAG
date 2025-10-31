<h1 align="center">5. Implementation Guide</h1>

# 1. Install dependencies

Dependencies are listed in `requirements.txt`. Do not modify Docker files. Rebuild to install:

```bash
docker compose up --build -d
```

# 2. Run the container

Use your existing `docker-compose.yml`/`start.sh` to start Jupyter and development environment.

# 3. Example scripts

- `scripts/embed_text.py`: create embeddings for a small corpus
- `scripts/embed_images.py`: image embeddings (requires Pillow and a vision model when needed)
- `scripts/build_index_chroma.py`: store/query in Chroma
- `scripts/query_similarity.py`: generic similarity query example
- `scripts/rag_example.py`: minimal RAG loop

# 4. Notebooks

- `notebooks/01_embeddings_basics.ipynb`: vectors and similarity
- `notebooks/02_vector_db_comparison.ipynb`: compare stores
- `notebooks/03_rag_pipeline.ipynb`: end-to-end RAG


