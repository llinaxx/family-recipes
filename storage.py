import json
import os

DATA_DIR = "data"


def load_data(filename: str) -> list:
    """Загрузить данные из JSON-файла."""
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Ошибка чтения {filename}")
        return []


def save_data(filename: str, data: list) -> None:
    """Сохранить данные в JSON-файл."""
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
