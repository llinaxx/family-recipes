import json
import os
from db.database import get_connection

DATA_DIR = "data"

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def main():
    conn = get_connection()
    try:
        # 1. Семьи
        for f in load_json("families.json"):
            conn.execute(
                "INSERT INTO families (id, name, created_at) VALUES (?, ?, ?)",
                (f["id"], f["name"], f.get("created_at", "2026-01-01"))
            )
        
        # 2. Участники
        for m in load_json("members.json"):
            conn.execute(
                "INSERT INTO members (id, name, role, family_id) VALUES (?, ?, ?, ?)",
                (m["id"], m["name"], m["role"], m.get("family_id", 1))
            )
            
        # 3. Категории
        for c in load_json("categories.json"):
            conn.execute(
                "INSERT INTO categories (id, name, description) VALUES (?, ?, ?)",
                (c["id"], c["name"], c.get("description", ""))
            )
            
        # 4. Рецепты
        for r in load_json("recipes.json"):
            is_fav = 1 if r.get("is_favorite") else 0
            conn.execute(
                "INSERT INTO recipes (id, title, author_id, category_id, cooking_time, difficulty, is_favorite) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (r["id"], r["title"], r["author_id"], r["category_id"], r["cooking_time"], r.get("difficulty", "средне"), is_fav)
            )
            
        conn.commit()
        print("✅ Данные успешно импортированы!")
    except Exception as e:
        conn.rollback()
        print(f"❌ Ошибка импорта: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
