# AI-Agents-and-Harnesses-Foundations

AI Agents and Harnesses Foundations, published by Packt.

Each chapter's code lives in its own folder on `main`:

| Chapter | Folder | Book reference |
|---|---|---|
| 1. Understanding LangChain Foundations | [`project-hello-world`](project-hello-world) | branch `project/hello-world` |
| 2. Building Your First Agent | [`project-search-agent`](project-search-agent) | branch `project/search-agent` |
| 3. Understanding Agents Under the Hood | [`project-agents-under-the-hood`](project-agents-under-the-hood) (`1_agent_loop_langchain_tool_calling.py`) | branch `project/agents-under-the-hood` |
| 4. Building Agent Loop Without a Framework | [`project-agents-under-the-hood`](project-agents-under-the-hood) (`2_agent_loop_raw_function_calling.py`) | |
| 5. ReAct From Scratch | [`project-agents-under-the-hood`](project-agents-under-the-hood) (`3_raw_react_prompt.py`) | |
| 6. Prompt and Context Engineering | (no code) | |
| 7. Agent Harnesses and Deep Agents | [`project-agent-harnesses`](project-agent-harnesses) | branch `project/agent-harnesses` |

> **Where the book says `git checkout project/<name>`**, `cd` into the matching `project-<name>` folder instead. Every folder is a standalone uv project: `cp .env.example .env`, fill in your keys, then `uv sync`.

## Versions

Every project is locked to `langchain==1.3.8`, the version the book is written against. Chapter 7 also pins `deepagents==0.6.8`. Exact versions of everything are in each folder's `uv.lock`. All projects need Python 3.11 or newer.

## Models

| Where | Model |
|---|---|
| Ch1, Ch2, Ch7 (hosted) | `gpt-5.6-sol` |
| Ch1 (local, Ollama) | `gemma4` |
| Ch3–5 (local, Ollama) | `qwen3.8:27b` |

## Errata

The small places where the printed code can't run as-is, and what the repository does instead, are listed in [ERRATA.md](ERRATA.md).
