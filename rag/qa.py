# rag/qa.py

from rag.embedder import get_embedder
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.docstore.document import Document
from config import OPENAI_API_KEY, OPENAI_LLM_MODEL


def load_vectorstore():
    embedder = get_embedder()
    return FAISS.load_local("faiss_index", embeddings=embedder, allow_dangerous_deserialization=True)

def ask_question(query: str):
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(
        model=OPENAI_LLM_MODEL,
        openai_api_key=OPENAI_API_KEY,
        temperature=0,
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",  # pode testar também "map_reduce" depois
        return_source_documents=True
    )

    result = chain.invoke(query)
    return result["result"]
