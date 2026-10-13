from langchain.tools import tool

def create_search_tool(retriever):
    """Return a @tool function that searches the HR policy document."""

    @tool
    def search_hr_policy(question:str)->str:
        """search the hr policy document for information about leave, work from home,
        probation, notice period, reimbursement, code of conduct, holiday, or exitprocess"""

        matching_chunks = retriever.invoke(question)
        return"\n\n".join(chunk.page_content for chunk in matching_chunks)

    return search_hr_policy

