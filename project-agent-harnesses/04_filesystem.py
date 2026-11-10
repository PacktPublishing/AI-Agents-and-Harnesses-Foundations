from deepagents import create_deep_agent
from models import model

agent = create_deep_agent(model=model)

TASK = (
    "Do this using your file tools, not your context:\n"
    "1. Write three files under /notes/ - planning.md, subagents.md, "
    "filesystem.md - each with a two-sentence description of that "
    "deep-agent capability.\n"
    "2. Then read the three files back and write a combined /summary.md "
    "that lists all three capabilities.\n"
    "3. Reply with only the contents of /summary.md."
)

result = agent.invoke({"messages": [{"role": "user", "content": TASK}]})

files = result.get("files", {})
for path in sorted(files):
    data = files[path]
    content = data.get("content", data) if isinstance(data, dict) else data
    print(f"\n----- {path} -----")
    print(content)
