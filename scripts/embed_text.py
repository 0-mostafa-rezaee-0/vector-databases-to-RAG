import argparse
from typing import List

from sentence_transformers import SentenceTransformer
from tqdm import tqdm


def load_corpus() -> List[str]:
    return [
        "Vector databases enable fast similarity search.",
        "Embeddings map text into numerical vectors.",
        "RAG combines retrieval with generation for grounded answers.",
    ]


def main(model_name: str) -> None:
    corpus = load_corpus()
    model = SentenceTransformer(model_name)
    embeddings = model.encode(corpus, convert_to_numpy=True, show_progress_bar=True)

    for text, vec in zip(corpus, embeddings):
        print(f"{text}\nDim: {len(vec)}  First3: {vec[:3]}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    args = parser.parse_args()
    main(args.model)


