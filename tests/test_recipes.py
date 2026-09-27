from models import Member, Category, Recipe


def make_recipe():
    author = Member(1, "Мама", "admin")
    category = Category(1, "Суп", "Первые блюда")
    return Recipe(1, "Борщ", author, category, 90, "средне", False)


def test_recipe_creation():
    r = make_recipe()
    assert r.id == 1
    assert r.title == "Борщ"
    assert r.author.name == "Мама"
    assert r.category.name == "Суп"
    assert r.cooking_time == 90
    assert r.is_favorite is False


def test_recipe_is_quick():
    r = make_recipe()
    assert r.is_quick(100) is True
    assert r.is_quick(30) is False


def test_recipe_mark_favorite():
    r = make_recipe()
    r.mark_favorite()
    assert r.is_favorite is True


def test_recipe_str():
    r = make_recipe()
    text = str(r)
    assert "Борщ" in text
    assert "Мама" in text
    assert "Суп" in text


def test_recipe_to_data():
    r = make_recipe()
    data = r.to_data()
    assert data["author_id"] == 1
    assert data["category_id"] == 1
    assert data["title"] == "Борщ"
