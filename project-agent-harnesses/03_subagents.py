from deepagents import create_deep_agent
from langchain.tools import tool
from models import model

FACTS = {
    "subagents": (
        "Subagents are specialized, short-lived workers that handle isolated "
        "tasks with their own prompts and tools, then return concise results. "
        "They enable parallel work while keeping the main agent's context focused."
    ),
    "filesystem": (
        "The deep-agent filesystem gives agents tools to read, write, edit, list, "
        "and search files, so large artifacts live outside the context window."
    ),
    "planning": (
        "The planning tool (write_todos) lets an agent lay out a task list and "
        "update each item's status as it works through a long task."
    ),
}


@tool
def lookup_fact(topic: str) -> str:
    """Look up a factual summary about a deep-agent topic."""
    print(f">> [researcher] lookup_fact(topic={topic!r})")
    for key, fact in FACTS.items():
        if key in topic.lower():
            return fact
    return f"No fact found for {topic!r}. Known topics: {', '.join(FACTS)}."


fact_researcher = {
    "name": "fact-researcher",
    "description": (
        "Look up a factual summary for ONE deep-agent topic and return a "
        "single polished sentence. Delegate one topic per call."
    ),
    "system_prompt": (
        "You research one topic at a time. Call lookup_fact with the "
        "given topic, then return ONE clear sentence based only on what it returns. "
        "Do not add facts of your own."
    ),
    "tools": [lookup_fact],
}

COORDINATOR_PROMPT = (
    "You are a coordinator. You do NOT look up facts yourself, you have "
    "no lookup tool. For each topic the user asks about, delegate to the "
    "fact-researcher subagent using the task tool (one topic per "
    "delegation). "
    "Collect the returned sentences and combine them into a short "
    "bulleted summary. Keep your own context focused on coordination."
)

agent = create_deep_agent(
    model=model,
    system_prompt=COORDINATOR_PROMPT,
    subagents=[fact_researcher],
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Summarize two deep-agent capabilities: "
                "subagents and the filesystem.",
            }
        ]
    }
)

print("=== Coordinator's assembled summary ===")
print(result["messages"][-1].content)
