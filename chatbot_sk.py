import json
import os
import random

MEMORY_FILE = "pamat.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

ai_questions = [
    "Vieš, čo je algoritmus?",
    "Aký je tvoj obľúbený programovací jazyk?",
    "Zaujíma ťa umelá inteligencia?",
    "Vieš, čo robí premenná v kóde?",
    "Máš nejaký obľúbený IT projekt?",
    "Chceš ma niečo naučiť?",
    "Čo si sa dnes naučil?"
]

def normalize(text):
    return text.lower().strip()

def save_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

print("AI Chatbot (slovenský) 🤖")
print("Napíš otázku alebo príkaz. (napr. !ukáž pamäť, !zabudni všetko)")
ask_next = False

while True:
    user_input = input("Ty: ").strip()
    user_input_norm = normalize(user_input)

    if user_input_norm in ["koniec", "exit", "quit"]:
        print("Bot: Maj sa pekne! 👋")
        break

    if user_input_norm == "!ukáž pamäť":
        if memory:
            print("Bot: Zatiaľ poznám tieto otázky:")
            for q in memory:
                print(f"- {q}")
        else:
            print("Bot: Zatiaľ si nič nepamätám.")
        ask_next = False

    elif user_input_norm == "!zabudni všetko":
        print("Bot: Si si istý? napíš 'áno' pre potvrdenie")
        ask_next = "confirm_reset"

    elif ask_next == "confirm_reset" and user_input_norm == "áno":
        memory.clear()
        save_memory()
        print("Bot: V poriadku, vymazal som všetku pamäť.")
        ask_next = False

    elif user_input_norm in memory:
        print(f"Bot: {memory[user_input_norm]}")
        if random.random() < 0.5:
            print(f"Bot: {random.choice(ai_questions)}")
        ask_next = False

    elif ask_next == "learning":
        memory[last_question] = user_input
        save_memory()
        print("Bot: Zapamätám si to. Ďakujem! 👌")
        if random.random() < 0.5:
            print(f"Bot: {random.choice(ai_questions)}")
        ask_next = False

    else:
        print("Bot: Túto otázku ešte nepoznám. Ako mám odpovedať?")
        last_question = user_input_norm
        ask_next = "learning"
