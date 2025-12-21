import pytest

from app.shop import ShoppingCart


@pytest.fixture
def filled_cart():
    cart = ShoppingCart()
    cart.add_item('apple', 10)
    cart.add_item('banana', 20)
    return cart

def test_add_item(filled_cart):
    filled_cart.add_item('cherry', 100)
    assert 'cherry' in filled_cart.items

def test_get_total_price(filled_cart):
    assert filled_cart.get_total_price() == 30
