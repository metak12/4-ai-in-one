"""
Модуль 4: AI-подкаст студия (TTS + Whisper + FastAPI)
Превращает статьи в аудио-подкасты с озвучкой нейросетью.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Podcast Studio API")

class ArticleRequest(BaseModel):
    title: str
    content: str

@app.post("/api/generate-podcast")
def generate_podcast(req: ArticleRequest):
    sentences = [s.strip() for s in req.content.split(".") if s.strip()]
    first_point = sentences[0] if sentences else req.content
    script = [
        {"speaker": "Алексей", "text": f"Всем привет! Сегодня обсуждаем статью: {req.title}."},
        {"speaker": "Мария", "text": f"Привет! Главная мысль материала: {first_point}."},
        {"speaker": "Алексей", "text": "Отличный разбор! Слушайте нас в приложении AIProjects."}
    ]
    return {"title": req.title, "script": script}
