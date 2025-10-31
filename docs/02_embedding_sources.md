<h1 align="center">2. Embedding Sources</h1>

# 1. Modalities

- Text: sentences, passages, docs
- Image: patches, full images
- Audio: speech, clips

# 2. Popular models

- OpenAI embeddings (`text-embedding-3-*`): simple API, strong quality, paid.
- Sentence Transformers (Hugging Face): local, many sizes, free; e.g., `all-MiniLM-L6-v2`.

# 3. Practical guidance

- Start with `sentence-transformers/all-MiniLM-L6-v2` locally.
- Switch to OpenAI for better multilingual coverage or quality at scale.
- Batch inputs; cache results; store model name and dim with vectors.


