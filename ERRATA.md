# Errata

These are places where the printed book and this repository differ because the printed code or command can't be used as-is. Page numbers are the printed page numbers.

## Repository layout

| Page | Book | Use instead |
|---|---|---|
| 2, 11, 43, 59, 78, 196 | `git checkout project/hello-world`, `project/search-agent`, `project/agents-under-the-hood`, `project/agent-harnesses` | Each chapter is a folder on `main`: `project-hello-world`, `project-search-agent`, `project-agents-under-the-hood`, `project-agent-harnesses`. `cd` into it. |
| 2 | `cd AI Agents and Harnesses Foundations` | `cd AI-Agents-and-Harnesses-Foundations` |
| 196 | The `git clone` URL is split across two lines | `git clone https://github.com/PacktPublishing/AI-Agents-and-Harnesses-Foundations` |
| 6 | `name = "AI Agents and Harnesses Foundations!"` in `pyproject.toml` | Not a valid package name. The projects are named `hello-world`, `search-agent`, `agents-under-the-hood`, `agent-harnesses`. |
| 79 | `git add` | `git add .` |

## Chapter 1

| Page | Book | Note |
|---|---|---|
| 26 | "we use the 270-million parameter variant" of Gemma 4 | The code uses `gemma4` (`ollama pull gemma4`). 270M is a Gemma 3 size. |
| 34 | `git commit -m "hello –world chain"` | The commit is referred to as `hello-world-chain`. |

## Chapter 3

| Page | Book | Repository |
|---|---|---|
| 81 | "Create a new file called `one_agent_loop_langchain_tool_calling.py`" | `1_agent_loop_langchain_tool_calling.py` (as on p.68 and in the Preface conventions). |
| 81, 85, 91 | `init_chat_model("ollama/qwen3.8:27b")`, `init_chat_model("openai/gpt-5.6-sol")` | `init_chat_model` expects `provider:model`. The `/` form raises "Unable to infer model provider" on `langchain==1.3.8`. Use `"ollama:qwen3.8:27b"` and `"openai:gpt-5.6-sol"`. |

## Chapter 4

| Page | Book | Repository |
|---|---|---|
| 102, 110 | `apply_Discount` | `apply_discount` |
| 109 | Trace names `langchain_agent_loop`, `ollama_agent_loop`, `ollama_chat` | The `@traceable` names in the code are `"LangChain Agent Loop"`, `"Ollama Agent Loop"` and `"Ollama Chat"`. |

## Chapter 5

| Page | Book | Repository |
|---|---|---|
| 125 | `f"{tool_name}{signature}- {docstring}"` | `f"{tool_name}{signature} - {docstring}"` (as on p.122) |
| 135 | `options={"stop": "\nObservation", ...}` | `options={"stop": ["\nObservation"], ...}` (as on p.133) |
| 142 | `re.search(r"Final Answer:\s*(.*)", output, re.DOTALL)` | `re.search(r"Final Answer:\s*(.+)", output)` (the version on p.144) |
| 147–148 | The parsed input is called `tool_input_run` on p.147 and `tool_input_raw` on p.148, so the code as printed raises `NameError` | `tool_input_raw` throughout. |
| 152 | `price = float(input_value)` | `input_value` is undefined. The cast is `price = float(price)` inside `apply_discount`, as in the p.121 listing. |
| 153 | Sample output `>> Executing apply_discount(1299.99, 'gold')` | The code prints `>> Executing apply_discount(price=1299.99, discount_tier='gold')`. |

## Chapter 7

| Page | Book | Repository |
|---|---|---|
| 200 | `02_planning_tool.py`: the line `Deep Agents?' with exactly three sections: "` is missing its opening `"` | `"Deep Agents?' with exactly three sections: "` |
| 209 | `04_filesystem.py`: `... if isinstance(data, dict)` and `else data` are printed on two lines | One line: `content = data.get("content", data) if isinstance(data, dict) else data` |
| 196–214 | `models.py` and the printing code around the listings (plan-update headers, `lookup_fact` body, summary and customer loops) are not printed | See `project-agent-harnesses/`. They produce the output shown in the book. |
