"""All setting for the app live here, in one place"""

import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

DATA_FILE_PATH = os.path.join("data","Hr_policy.txt")


VECTOR_STORE_PATH = os.path.join("data","faiss_index")


LLM_MODEL_NAME = "openai/gpt-oss-120b"
Embedding_model_name = "jina-embeddings-v2-base-en"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

TOP_K_RESULTS = 3


system_prompt=(
"""you are a friendly hr assistant.
    ALways use the search_hr_policy tool to look up
    facts before answering.
    If the answer isn't in the search result, say you don't know"
    instead of guessing
    """
)

def check_api_keys() -> None:
    """stop early with a clear message if a required API key is missing."""
    if not GROQ_API_KEY:
        raise ValueError("missing GROQ_API_KEY. please add it to your .env file")
    if not JINA_API_KEY:
        raise ValueError("Missing JINA_API_KEY. please add it to your .env file")