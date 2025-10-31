<h1 align="center">1. Fundamentals</h1>

# 1. What are vectors and embeddings?

Embeddings map inputs (text, images, audio) to numeric vectors in \(\mathbb{R}^d\) such that semantically similar inputs have nearby vectors.

## 1.1. Semantic vectors

Well-trained models learn geometry where proximity encodes meaning. This enables search and clustering without brittle keyword matching.

## 1.2. Distance metrics

- Cosine similarity: angle between vectors; robust to magnitude.
- Euclidean distance: straight-line distance; sensitive to scale.
- Dot product: scale-sensitive similarity often used with normalized vectors.

Choose cosine for most text embeddings; Euclidean can suit vision features; dot for normalized setups.

# 2. Similarity search

Given a query vector, find nearest neighbors in a collection. Brute force is O(Nd); approximate indexes (HNSW, IVF, PQ) trade tiny accuracy for big speed.

# 3. Embedding workflow

Input -> tokenize/transform -> model -> vector -> store -> index -> query -> results.


