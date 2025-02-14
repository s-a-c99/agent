# my_1st_agent.py
My First AI Agent – A minimalist agent framework LLM-powered to-do list manager using Zephyr-7B and Hugging Face Inference API. Supports add, remove, list tasks via tool calling.

# My First AI Agent 🧠✅  
A lightweight **LLM-powered agent** for managing a **to-do list**. Uses **Hugging Face's Inference API** with **Zephyr-7B**.  

## Features  
- 📝 **Add tasks**  
- ❌ **Remove tasks**  
- 📜 **List tasks**  
- 🎯 **Tool calling via structured JSON**  

## Setup  
1. Install dependencies:  
   ```bash
   pip install huggingface_hub transformers
   
2.Set up Hugging Face API Token:
os.environ["HF_TOKEN"] = "your_api_key"

3. Run the script:
python agent.py

Example Output
[DEBUG] Model: Thought: I need to add a task
Action:
{"action": "add_task", "action_input": {"task": "buy milk"}}

[SUCCESS] Observation: Task added: buy milk
FINAL ANSWER: Task added: buy milk

TODO
🔄 Improve multi-step reasoning
⚡ Add memory persistence
🌍 Deploy as an API
