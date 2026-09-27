from datetime import datetime


def input_int(prompt: str) -> int:
    """Запросить целое число с обработкой ошибок."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите целое число.")


def input_date(prompt: str) -> str:
    """Запросить дату в формате YYYY-MM-DD."""
    while True:
        value = input(prompt)
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Неверный формат даты. Пример: 2026-09-15")
