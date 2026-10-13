from langchain.agents import create_agent
from . import config

def create_hr_agent(llm, tools):
    """return a langchain agent that can call our tools to answer questions."""
    return create_agent(model=llm,tools=tools, system_prompt=config.system_prompt)