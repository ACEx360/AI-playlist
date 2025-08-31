# DuckDuckGoSearchRun changed to ddgs 
# There is Waring message when using DuckDuckGoSearchRun
# Making Custom Tool using ddgs to Work around that

from typing import Optional, Type
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from langchain.callbacks.manager import CallbackManagerForToolRun
from ddgs import DDGS 

class DDGInput(BaseModel):
    query: str = Field(..., description="The search query to look up.")

class DDGSearchTool(BaseTool):
    """DuckDuckGo tool using ddgs backend."""

    name: str = "ddgs_search"
    description: str = (
        "A wrapper around DuckDuckGo Search using ddgs. "
        "Useful for answering questions about current events. "
        "Input should be a search query."
    )
    args_schema: Type[BaseModel] = DDGInput

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        formatted = []
        for r in results:
            formatted.append(
                f"[snippet: {r.get('body','')}, "
                f"title: {r.get('title','')}, "
                f"link: {r.get('href','')}]"
            )
        return ", ".join(formatted)

print("----------------Example----------------------")
if __name__ == "__main__":
    tool = DDGSearchTool()
    query = "Pune weather today"
    output = tool.invoke({"query": query})
    print("Search Results:\n", output)
