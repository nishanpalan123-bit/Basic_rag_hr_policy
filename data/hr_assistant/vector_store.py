from langchain_community.vectorstores import FAISS
import os
from .embeddings import get_embedding_model
from . import config

def build_vector_store(chunks):
    """Enbed every chunk and build a searchable FAISS index in memory."""
    embedding_model = get_embedding_model()
    return FAISS.from_documents(chunks,embedding_model)


def save_vector_store(vector_store , path : str = config.VECTOR_STORE_PATH)->None:
    """save the faiss index to disk
    so we don't have to rebuild it every time."""
    vector_store.save_local(path)

def load_vector_store(path: str = config.VECTOR_STORE_PATH):
    """load a previously saved faiss index from disk."""
    embedding_model = get_embedding_model()
    return FAISS.load_local(path, embedding_model,allow_dangerous_deserialization=True)

def vector_store_exists(path: str = config.VECTOR_STORE_PATH)-> bool:
    """check if a saved FAISS index already exists on disk."""
    return os.path.exists(os.path.join(path, "index.faiss"))

def get_retriever(vector_store, k:int = config.TOP_K_RESULTS):
    """turn a vector store into a retriever
    that returns the top-k matching chunks"""
    return vector_store.as_retriever(search_kwargs = {"k":k})