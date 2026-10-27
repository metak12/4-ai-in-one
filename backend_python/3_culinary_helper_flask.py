"""
Модуль 3: Кулинарный помощник (GPT + Flask + PostgreSQL/SQLite)
Предлагает рецепты из продуктов, которые есть дома.
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

RECIPES = [
    {"title": "Фриттата с помидорами и сыром", "ingredients": ["яйца", "помидоры", "сыр", "молоко"], "time": 12},
    {"title": "Паста с курицей и грибами", "ingredients": ["макароны", "курица", "грибы", "сыр", "чеснок"], "time": 20},
]

@app.route("/api/recipes", methods=["POST"])
def match_recipes():
    data = request.get_json(force=True)
    pantry = [x.lower().strip() for x in data.get("ingredients", [])]
    results = []
    for r in RECIPES:
        have = [i for i in r["ingredients"] if i in pantry]
        pct = round(len(have) / len(r["ingredients"]) * 100)
        results.append({**r, "match_percent": pct, "have": have})
    results.sort(key=lambda x: x["match_percent"], reverse=True)
    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5000)
