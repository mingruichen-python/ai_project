# Project Overview
This project is a lightweight command‑line chatbot client that connects to the Groq API and provides real‑time interaction with the llama‑3.1‑8b‑instant model.
It maintains a rolling conversation history, handles API requests, and offers a simple REPL‑style chat experience.
---
# Features
.Clean and minimal command‑line interface
.Persistent conversation history with automatic trimming
.Real‑time responses from Groq’s LLaMA models
.Error handling for network and API issues
.Easy to extend and integrate into larger applications
---
# Tech Stack
Python
requests for HTTP communication
Groq Chat Completions API
Standard I/O for interactive chat
---
# How to Run
1.Clone the repository
2.Install dependencies using:

pip install requests

3.Run the script

python main.py

4.Enter your Groq API key when prompted

Start chatting in the terminal (press E to exit)
---
# Results
The script successfully communicates with Groq’s LLaMA model, providing fast, low‑latency responses and maintaining a smooth interactive chat loop.
