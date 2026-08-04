"""
Search tools for the research agents.
We support two options:
1. Tavily (better quality - recommended if you have a free API key)
2. DuckDuckGo (completely free, no API key needed)
"""

from crewai.tools import tool
from duckduckgo_search import DDGS
import os


@tool("DuckDuckGo Search")
def duckduckgo_search(query: str) -> str:
    """
    Search the web using DuckDuckGo (free, no API key needed).
    Use this to find recent information about a topic.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=6))
        
        if not results:
            return "No results found for this query."
        
        formatted = []
        for i, r in enumerate(results, 1):
            formatted.append(
                f"{i}. {r.get('title', 'No title')}\n"
                f"   URL: {r.get('href', 'No URL')}\n"
                f"   {r.get('body', 'No description')}\n"
            )
        return "\n".join(formatted)
    except Exception as e:
        return f"Search failed: {str(e)}"


def get_search_tools():
    """
    Return the best available search tools.
    Prefers Tavily if API key exists, otherwise falls back to DuckDuckGo.
    """
    tools = [duckduckgo_search]

    # Try to add Tavily if the user has set the key
    tavily_key = os.getenv("TAVILY_API_KEY")
    if tavily_key and tavily_key != "tvly-your-tavily-key-here":
        try:
            from crewai_tools import TavilySearchTool
            tavily_tool = TavilySearchTool()
            tools.insert(0, tavily_tool)  # Prefer Tavily
            print("✅ Using Tavily + DuckDuckGo for search")
        except Exception:
            print("⚠️ Tavily key found but tool failed to load. Using DuckDuckGo only.")
    else:
        print("ℹ️ Using free DuckDuckGo search (add TAVILY_API_KEY for better results)")

    return tools
