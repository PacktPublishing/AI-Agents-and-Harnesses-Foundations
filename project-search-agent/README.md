# Chapter 2: Building Your First Agent

A search agent built with LangChain's `create_agent`. It has a custom `@tool search` backed by the Tavily SDK and returns structured output (`AgentResponse` with `Source` objects).

This is the state the book commits at the end of the chapter. The book also shows two intermediate steps:

1. A placeholder `search` tool that always returns `"Tokyo weather is sunny"`.
2. The built-in `TavilySearch` tool from `langchain_tavily`, which the book has you revert before committing:
   ```python
   from langchain_tavily import TavilySearch

   search_tool = TavilySearch()
   tools = [search_tool]
   ```

## Run it

```bash
cd project-search-agent
cp .env.example .env   # then fill in your keys
uv sync
uv run main.py
```

## Environment variables

See `.env.example`: `OPENAI_API_KEY`, `LANGSMITH_TRACING`, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT=search-agent`, `TAVILY_API_KEY`.

Model: `gpt-5.6-sol`. Pinned to `langchain==1.3.8`. Exact versions are in `uv.lock`.
