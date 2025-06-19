from rag.loader import load_pdfs
from rag.splitter import split_texts
from rag.embedder import get_embedder
from rag.vectorstore import create_vectorstore
from config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP

def ingest():
    texts = load_pdfs(DATA_DIR)
    chunks = split_texts(texts, CHUNK_SIZE, CHUNK_OVERLAP)
    print(f"Total de chunks criados: {len(chunks)}")

    # Embeddings
    embedder = get_embedder()
    create_vectorstore(embedder, chunks)

if __name__ == "__main__":
    ingest()
