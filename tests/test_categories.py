from models import Category


def test_category_creation():
    c = Category(1, "Суп", "Первые блюда")
    assert c.id == 1
    assert c.name == "Суп"
    assert c.description == "Первые блюда"


def test_category_str():
    c = Category(1, "Суп")
    assert "Суп" in str(c)


def test_category_from_data():
    c = Category.from_data({"id": 2, "name": "Салат", "description": "Холодные"})
    assert c.id == 2
    assert c.name == "Салат"


def test_category_to_data():
    c = Category(1, "Суп", "Первые блюда")
    data = c.to_data()
    assert data == {"id": 1, "name": "Суп", "description": "Первые блюда"}
