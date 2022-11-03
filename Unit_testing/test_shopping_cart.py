import pytest
from unittest.mock import MagicMock
from shopping_cart import ShoppingCart
from item_database import ItemDatabase


@pytest.fixture
def cart():
    # All setup for the cart here...
    # Every added fixture to test is new, not reused
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    cart.add('apple')
    # assert True if statement is True, else Exception
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add('apple')
    assert 'apple' in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    # add max items to the cart
    for _ in range(5):
        cart.add('apple')
    # assert a failure on adding more than max_size items
    # test is passed if the OverflowError is raised
    with pytest.raises(OverflowError):
        cart.add('apple')


# test specific function pytest test_file.py::function_name
# -s to show all prints
def test_can_get_total_price(cart):
    cart.add('apple')
    cart.add('orange')

    item_database = ItemDatabase()

    # mock get method of DB class that hasn't been implemented yet
    # item_database.get = MagicMock(return_value=1.0)

    def mock_get_item(item: str):
        if item == 'apple':
            return 1.0
        elif item == 'orange':
            return 2.0

    item_database.get = MagicMock(side_effect=mock_get_item)
    # price_map = {'apple': 1.0, 'orange': 2.0}
    assert cart.get_total_price(item_database) == 3.0
