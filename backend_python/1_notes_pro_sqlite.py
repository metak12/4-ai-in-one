"""
Модуль 1: Заметки Pro (ChatGPT + Python + SQLite)
Умный блокнот с автотегами, поиском по смыслу и генерацией summary заметок.
"""
import sqlite3
import os
from typing import List, Dict

DB_PATH = "notes_pro.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT,
            summary TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def auto_tag_and_summarize(title: str, content: str) -> Dict[str, str]:
    text = f"{title} {content}".lower()
    clusters = {
        "#ии": ["gpt", "llm", "нейросеть", "модель", "ai"],
        "#разработка": ["python", "sqlite", "код", "api", "flask", "fastapi"],
        "#финансы": ["бюджет", "деньги", "расходы", "доход"],
        "#учёба": ["лекция", "конспект", "книга", "статья"]
    }
    tags = [tag for tag, words in clusters.items() if any(w in text for w in words)]
    if not tags:
        tags = ["#заметка"]
    sentences = [s.strip() for s in content.split(".") if s.strip()]
    summary = sentences[0] + "." if sentences else content[:120]
    return {"tags": ", ".join(tags), "summary": summary}

def add_note(title: str, content: str):
    meta = auto_tag_and_summarize(title, content)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO notes (title, content, tags, summary) VALUES (?, ?, ?, ?)",
        (title, content, meta["tags"], meta["summary"])
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    add_note("Тест Заметки Pro", "Интеграция SQLite и ChatGPT для автотегов и summary.")
    print("База notes_pro.db успешно инициализирована!")
