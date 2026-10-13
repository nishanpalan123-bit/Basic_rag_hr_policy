from langchain_community.embeddings import JinaEmbeddings
from . import config

def get_embedding_model():
    """Return a jina embedding model.
    Reads JINA_API_KEY from the environment"""
    return JinaEmbeddings(model_name=config.Embedding_model_name)