from models.categories import add_category, find_category_by_name


def test_add_category():
    categories = []
    add_category(categories, "Суп", "Первые блюда")
    assert len(categories) == 1
    assert categories[0]["name"] == "Суп"


def test_find_category_by_name():
    categories = []
    add_category(categories, "Суп", "Первые блюда")
    add_category(categories, "Салат", "Холодные блюда")
    assert find_category_by_name(categories, "суп")["id"] == 1
    assert find_category_by_name(categories, "САЛАТ")["id"] == 2
    assert find_category_by_name(categories, "Десерт") == {}
