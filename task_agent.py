!pip install huggingface_hub transformers

from huggingface_hub import InferenceClient
import os
import json

os.environ["HF_TOKEN"] = "hf_xxxxxxxxxxx"

client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")

TODO_LIST = []
SYSTEM_PROMPT = """YOU ARE A TODO-LIST MANAGEMENT ASSISTANT.
Available tools:
- add_task: Adds a task (example: {"action": "add_task", "action_input": {"task": "buy milk"}})
- remove_task: Removes a task by index (example: {"action": "remove_task", "action_input": {"index": 0}})
- list_tasks: Lists all tasks (example: {"action": "list_tasks", "action_input": {}})

**REQUIRED FORMAT:**
1. Logical reasoning
2. Action in JSON format ONLY between ```json and ```
3. Wait for Observation before responding

Correct example:
Thought: I need to add the task
Action:
```json
{"action": "add_task", "action_input": {"task": "buy bread"}}
```"""

def execute_action(action):
    if action["action"] == "add_task":
        TODO_LIST.append(action["action_input"]["task"])
        return f"Task added: {action['action_input']['task']}"
    elif action["action"] == "remove_task":
        if 0 <= action["action_input"]["index"] < len(TODO_LIST):
            return f"Removed: {TODO_LIST.pop(action['action_input']['index'])}"
        return "Error: Invalid index."
    elif action["action"] == "list_tasks":
        return f"Tasks: {TODO_LIST}" if TODO_LIST else "No tasks in the list."

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Add 'buy milk' to the list"}
]

max_retries = 3
retry_count = 0

while retry_count < max_retries:
    try:
        output = client.chat.completions.create(
            messages=messages,
            max_tokens=200,
            temperature=0.1,
            stop=["Observation:", "\n\n"]
        )
        thought = output.choices[0].message.content
        print("[DEBUG] Model:", thought)

        if "```json" not in thought:
            raise ValueError("Missing JSON block")
            
        json_str = thought.split("```json")[1].split("```")[0].strip()
        action_json = json.loads(json_str)
        
        observation = execute_action(action_json)
        print("[SUCCESS] Observation:", observation)
        
        messages.append({"role": "assistant", "content": f"Observation: {observation}"})
        
        final_output = client.chat.completions.create(
            messages=messages + [{"role": "user", "content": "Confirm the operation with Final Answer"}],
            max_tokens=50,
            temperature=0.1
        )
        final_response = final_output.choices[0].message.content
        print("\nFINAL ANSWER:", final_response.split("Final Answer:")[-1].strip())
        break

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        retry_count += 1
        messages.append({"role": "assistant", "content": f"ERROR: {str(e)}. Please retry with the correct format."})

else:
    print("Too many errors. Operation canceled.")
