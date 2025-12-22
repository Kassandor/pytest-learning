import pytest


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def is_admin(self):
        return self.role == 'admin'


@pytest.fixture
def admin_user():
    print("\n[conftest] Создание admin_user")
    return User(name="Admin", role="admin")
