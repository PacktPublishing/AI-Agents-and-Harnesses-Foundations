from deepagents import create_deep_agent
from models import model

agent = create_deep_agent(model=model)

TASK = (
    "Use your write_todos planning tool for this task. FIRST call "
    "write_todos to lay out a plan with one todo per section, "
    "then work through them one at a time, updating each todo's status "
    "(in_progress, then completed) as you go.\n\n"
    "Deliverable: a short internal briefing titled 'Should we adopt "
    "Deep Agents?' with exactly three sections: "
    "(1) what problem harnesses solve, (2) the four "
    "capabilities that make an agent deep, and (3) a recommendation."
)

result = agent.invoke({"messages": [{"role": "user", "content": TASK}]})

update = 0
for message in result["messages"]:
    for call in getattr(message, "tool_calls", None) or []:
        if call["name"] != "write_todos":
            continue
        update += 1
        print(f"--- Plan update #{update} ---")
        for todo in call["args"].get("todos", []):
            mark = {"completed": "[x]", "in_progress": "[~]"}.get(
                todo.get("status"), "[ ]"
            )
            print(f"  {mark} {todo.get('content')}")
