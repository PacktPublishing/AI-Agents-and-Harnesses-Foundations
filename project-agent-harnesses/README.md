# Chapter 7: Agent Harnesses and Deep Agents

Five short, self-contained scripts that build up a LangChain Deep Agent one capability at a time.

| Script | What it demonstrates | What changes |
|---|---|---|
| `01_bare_agent.py` | The assembled harness and the invoke contract | Nothing, just a model |
| `02_planning_tool.py` | Explicit planning with `write_todos` | Built-in, no new argument |
| `03_subagents.py` | Hierarchical delegation and context isolation | `subagents=` |
| `04_filesystem.py` | Offloading intermediate state to files | Built-in, no new argument |
| `05_system_prompt.py` | Shaping behavior and boundaries | `system_prompt=` |

## Run it

You need Python 3.11 or newer, an OpenAI API key, and [uv](https://docs.astral.sh/uv/).

```bash
cd project-agent-harnesses
cp .env.example .env   # set OPENAI_API_KEY=sk-...
uv sync
uv run python 01_bare_agent.py
```

## Which model the examples use

All five scripts import one shared model object, `from models import model`. `models.py` is the only place a model is named (`openai:gpt-5.6-sol`). Change that line to use a different model or provider.

## Optional: watching the agent work

Add these to `.env` to send traces to LangSmith:

```
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_...
```

Pinned to `deepagents==0.6.8` and `langchain==1.3.8`. Exact versions are in `uv.lock`.
