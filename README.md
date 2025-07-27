readme_content = """# AI Chatbot (Slovak Language) 🤖

This is a simple Slovak-language chatbot written in Python. It learns new answers, stores them in a JSON file, and communicates interactively via the terminal.

## 🧠 Features
- Slovak conversation
- Learns from user input
- Stores Q&A in `pamat.json`
- Asks random AI questions on its own
- Commands: `!ukáž pamäť`, `!zabudni všetko`, `koniec`

## ▶️ How to run
- Run `spustit_chatbot.bat` (Windows)
- Or in terminal: `python chatbot_sk.py`
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
