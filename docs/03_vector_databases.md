<h1 align="center">3. Vector Databases</h1>

# 1. Core idea

Store vectors with metadata and provide fast similarity search via specialized indexes (e.g., HNSW).

# 2. Local vs. Cloud

- Local (Chroma, PGVector, Qdrant local): quick start, full control.
- Cloud (Pinecone, Qdrant Cloud): managed scale, high availability.

# 3. Options at a glance

- Chroma: embedded DB, simple Python API, good for prototyping.
- PGVector: PostgreSQL extension; combine structured + vector.
- Pinecone: fully managed vector DB, high-perf indexes.
- Qdrant: open-source vector DB with HNSW, filters, payloads.

# 4. Selection tips

- Prototype with Chroma; need SQL joins -> PGVector; need managed scale -> Pinecone; want OSS with filters -> Qdrant.


