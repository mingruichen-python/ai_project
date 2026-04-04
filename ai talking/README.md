## Project Overview
This project is a lightweight command‑line chatbot client that connects to the Groq API and provides real‑time interaction with the llama‑3.1‑8b‑instant model.
It maintains a rolling conversation history, handles API requests, and offers a simple REPL‑style chat experience.

## Features
- Clean and minimal command‑line interface
- Persistent conversation history with automatic trimming
- Real‑time responses from Groq’s LLaMA models
- Error handling for network and API issues
- Easy to extend and integrate into larger applications

## Tech Stack
- Python
- requests for HTTP communication
- Groq Chat Completions API (you can generate your own api at ‘https://console.groq.com’)
- Standard I/O for interactive chat

## How to Run
1. Clone the repository
2. Install dependencies using ‘pip install requests’
3. Run the script ‘python main.py’
4. Enter your Groq API key when prompted
5. Start chatting in the terminal (press E to exit)

## Example
<img width="2139" height="665" alt="屏幕截图 2026-04-04 204523" src="https://github.com/user-attachments/assets/b57eef42-497d-49d3-88d3-a58f7da9b38c" />
