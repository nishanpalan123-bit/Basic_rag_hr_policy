"""All settings for the app live here, in one place."""

import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env for local development
load_dotenv()


def get_secret(key: str):
    """Read API keys from environment variables or Streamlit Secrets."""

    # First, check local environment variables
    value = os.getenv(key)

    if value:
        return value

    # If not found, check Streamlit Cloud Secrets
    try:
        value = st.secrets.get(key)
        if value:
            return value
    except Exception:
        pass

    return None


# API keys
GROQ_API_KEY = get_secret("GROQ_API_KEY")
JINA_API_KEY = get_secret("JINA_API_KEY")


# Data paths
DATA_FILE_PATH = os.path.join("data", "Hr_policy.txt")
VECTOR_STORE_PATH = os.path.join("data", "faiss_index")


# Model settings
LLM_MODEL_NAME = "openai/gpt-oss-120b"
Embedding_model_name = "jina-embeddings-v2-base-en"


# Text splitting settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


# Retrieval settings
TOP_K_RESULTS = 3


# System prompt
system_prompt = """
You are a friendly HR assistant.
Always use the search_hr_policy tool to look up facts before answering.
If the answer isn't in the search result, say you don't know instead of guessing.
"""


def check_api_keys() -> None:
    """Stop early with a clear message if a required API key is missing."""

    if not GROQ_API_KEY:
        raise ValueError(
            "Missing GROQ_API_KEY. Add it to your .env file "
            "or configure it in Streamlit Cloud Secrets."
        )

    if not JINA_API_KEY:
        raise ValueError(
            "Missing JINA_API_KEY. Add it to your .env file "
            "or configure it in Streamlit Cloud Secrets."
        )