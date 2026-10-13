from langchain_text_splitters import RecursiveCharacterTextSplitter
from . import config

def split_into_chunks(documents):
    """split documents into small overlaping chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = config.CHUNK_SIZE,
        chunk_overlap = config.CHUNK_OVERLAP
    )
    return text_splitter.split_documents(documents)