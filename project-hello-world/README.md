# Chapter 1: Understanding LangChain Foundations

A LangChain chain (`PromptTemplate | ChatOpenAI`) that summarizes a person's bio and returns two interesting facts, with an Ollama switch and LangSmith tracing.

## Run it

```bash
cd project-hello-world
cp .env.example .env   # then fill in your keys
uv sync
uv run main.py
```

## Models

- Hosted (default): `ChatOpenAI(temperature=0, model="gpt-5.6-sol")`
- Local: `ChatOllama(temperature=0, model="gemma4")`. Run `ollama pull gemma4`, then swap the commented line in `main.py`.

## Environment variables

See `.env.example`: `OPENAI_API_KEY`, `LANGSMITH_TRACING`, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT=hello-world` (and optionally `LANGSMITH_ENDPOINT`).

Pinned to `langchain==1.3.8`. Exact versions are in `uv.lock`.
