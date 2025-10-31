<h1 align="center">Notebooks</h1>

# 1. Purpose

Interactive exploration of embeddings, vector databases, and RAG.

# 2. Contents

- `01_embeddings_basics.ipynb`
- `02_vector_db_comparison.ipynb`
- `03_rag_pipeline.ipynb`

## Usage

Notebooks in this folder can be run through:

1. VS Code with the Jupyter extension (when connected to the Docker container)
2. Jupyter Lab/Notebook interface by accessing http://localhost:8888 in your browser
3. Direct execution through the Python kernel in the container

## Benefits of Containerized Notebooks

- Consistent execution environment
- Reproducible analysis across different systems
- Pre-configured dependencies
- Isolation from system-level conflicts

## Best Practices

- Keep notebooks organized and focused on specific tasks
- Include markdown cells to document your analysis
- Remember to save outputs before shutting down containers
- Consider converting finished notebooks to Python scripts for production use
- Use relative paths for accessing data (e.g., `../data/sample.csv`) 