from models import Member


def test_member_creation():
    m = Member(1, "Мама", "admin")
    assert m.id == 1
    assert m.name == "Мама"
    assert m.role == "admin"


def test_member_is_admin():
    admin = Member(1, "Мама", "admin")
    user = Member(2, "Папа", "member")
    assert admin.is_admin() is True
    assert user.is_admin() is False


def test_member_str():
    m = Member(1, "Мама", "admin")
    assert "Мама" in str(m)


def test_member_from_data():
    m = Member.from_data({"id": 1, "name": "Мама", "role": "admin"})
    assert m.id == 1
    assert m.is_admin() is True
