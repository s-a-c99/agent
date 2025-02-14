# 🤖 AI Agent 🧠 
A minimalist **agent framework LLM-powered** to-do list manager using **Zephyr-7B** and **Hugging Face Inference API**. Implements JSON tool calling for atomic task management (add/remove/list).

## Features  
- 📝 **Add tasks**  
- ❌ **Remove tasks**  
- 📋 **List tasks**  
- 🎯 **Tool calling via structured JSON**  

## 🚀 Quick Setup 
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   
2. Set up Hugging Face API Token:
   ```bash
   export HF_TOKEN="hf_xxxxxxxx"

3. Run the script:
   ```bash
   python task_agent.py

## 💻 Example Output
```bash
[DEBUG] Model: Thought: I need to add a task
Action:
{"action": "add_task", "action_input": {"task": "buy milk"}}

[SUCCESS] Observation: Task added: buy milk
FINAL ANSWER: Task added: buy milk
```

## TODO
🔄 Improve multi-step reasoning
⚡ Add memory persistence
🌎 Deploy as an API

## 📜 License  
MIT 
