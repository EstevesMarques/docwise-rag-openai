from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from typing import List
import os

def create_vectorstore(embeddings, chunks: List[str], persist_path: str = "faiss_index"):
    documents = [Document(page_content=chunk) for chunk in chunks]
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(persist_path)
    print(f"Índice FAISS salvo em: {persist_path}")
