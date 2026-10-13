from langchain_groq import ChatGroq
from . import config

def get_llm():
    """return a groq caht model. reads GROQ_API_KEY  from the environment"""
    return ChatGroq(model=config.LLM_MODEL_NAME, temperature=0)