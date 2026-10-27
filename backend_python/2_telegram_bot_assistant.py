"""
Модуль 2: Telegram-бот помощник (Telegram API + GPT-4 + Python)
Отвечает на вопросы, напоминает о задачах и ведёт личный дневник.
"""
import os
import json
import urllib.request

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")

tasks = []
diary = []

def handle_message(text: str) -> str:
    if text.startswith("/remind"):
        task = text.replace("/remind", "").strip()
        tasks.append(task)
        return f"Задача добавлена: {task}"
    if text.startswith("/diary"):
        entry = text.replace("/diary", "").strip()
        diary.append(entry)
        return f"Запись сохранена в дневник: {entry}"
    return f"AI-ассистент: получено сообщение '{text}'. Задач: {len(tasks)}, записей: {len(diary)}."

if __name__ == "__main__":
    print(handle_message("/remind Сдать проект AIProjects"))
    print(handle_message("/diary Отличный продуктивный день!"))
