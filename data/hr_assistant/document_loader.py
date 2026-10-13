from langchain_community.document_loaders import TextLoader
from . import config

def load_document(file_path: str = config.DATA_FILE_PATH):
    """Load a.txt file and return it as a list of Langchain Document"""
    loader = TextLoader(file_path, encoding="utf-8")
    return loader.load()