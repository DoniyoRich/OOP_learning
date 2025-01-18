import pytest

from src.product import Product
from src.category import Category


@pytest.fixture(scope="function")
def product_samsung():
    yield Product("Samsung", "Супертелефон", 120000.0, 5)


@pytest.fixture(scope="function")
def product_poco():
    yield Product("POCO", "Телефон с хорошей камерой", 90000.0, 12)


@pytest.fixture(scope="function")
def product_huawey():
    yield Product("Huawey", "Флагман с удобной доставкой", 144000.0, 3)


@pytest.fixture(scope="function")
def notebook_asus():
    return Product("ASUS", "Ноутбуки ASUS", 86000.0, 54)


@pytest.fixture(scope="function")
def notebook_sony():
    return Product("SONY", "Ноутбуки SONY", 95000.0, 68)


@pytest.fixture(scope="function")
def category_notebooks(notebook_asus, notebook_sony):
    yield Category("Ноутбуки", "Ультрабуки, планшеты", [notebook_asus, notebook_sony])


@pytest.fixture(scope="function")
def category_phones(product_samsung, product_poco, product_huawey):
    yield Category("Телефоны", "Современные телефоны", [product_samsung, product_poco, product_huawey])


@pytest.fixture(scope="function")
def new_product_dict():
    return {"name": "NOVA S100 Ultra", "description": "1024GB, Белый цвет, 1000MP камера",
            "price": 200000.0,
            "quantity": 3}


@pytest.fixture(scope="function")
def out_main():
    return "['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\\n', 'Iphone 15, 210000.0 руб. Остаток: 8 шт.\\n', 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\\n']"


# @pytest.fixture
# def product():
#     return Product
#
#
# @pytest.fixture
# def category():
#     return Category
