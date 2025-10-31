<h1 align="center">Data</h1>

# 1. Purpose

Store small datasets, derived embeddings, and local vector DB artifacts.

# 2. Layout

- `chroma_store/`: default persistent directory for Chroma examples
- Other CSV/JSON/text files you add for experimentation

# 3. Notes

- Large datasets should not be baked into Docker images; mount as volumes.