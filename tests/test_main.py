from itertools import product
from unittest import mock

from src.main import main
from src.product import Product
from src.category import Category


def test_init_prod_samsung(product_samsung):
    assert product_samsung.name == "Samsung"
    assert product_samsung.price == 120000.0


def test_init_category_notebooks(category_notebooks, notebook_asus, notebook_sony):
    assert category_notebooks.description == "Ультрабуки, планшеты"
    assert category_notebooks.products == ['ASUS, 86000.0 руб. Остаток: 54 шт.\n',
                                           'SONY, 95000.0 руб. Остаток: 68 шт.\n']
    Category.category_count = 0
    Category.product_count = 0


def test_count_prods(product_samsung, product_poco, product_huawey):
    category_1 = Category("Телефоны", "Современные флагманы", [product_samsung, product_poco, product_huawey])
    assert category_1.product_count == 3
    Category.category_count = 0
    Category.product_count = 0


def test_count_categories(category_notebooks, category_phones):
    assert Category.category_count == 2


def test_new_product_and_price_getter(new_product_dict):
    new_prod = Product.new_product(new_product_dict)
    assert new_prod.name == 'NOVA S100 Ultra'
    assert new_prod.description == '1024GB, Белый цвет, 1000MP камера'
    assert new_prod.quantity == 3
    assert new_prod.price == 200000.0


def test_product_price_setter(new_product_dict):
    prod = Product.new_product(new_product_dict)
    prod.price = 125000.0
    assert prod.price == 125000.0
    Category.category_count = 0
    Category.product_count = 0


def test_product_wrong_price(new_product_dict, capsys):
    prod = Product.new_product(new_product_dict)

    prod.price = -20000.0
    captured = capsys.readouterr()
    assert prod.price == 200000.0
    assert 'Цена не должна быть нулевая или отрицательная' in captured.out

    prod.price = 0
    captured = capsys.readouterr()
    assert prod.price == 200000.0
    assert 'Цена не должна быть нулевая или отрицательная' in captured.out


def test_add_product_to_category(category_notebooks, product_huawey):
    assert Category.category_count == 1
    assert Category.product_count == 2
    category_notebooks.add_product(product_huawey)
    assert Category.product_count == 3


# @patch(src.main.Category)
# @patch(src.main.Product)
def test_main(capsys, out_main):
    main()
    captured = capsys.readouterr()
    assert out_main in captured.out


"""
def test_if_main():
    with mock.patch('__main__.__name__', '__main__'):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3]
        )

        print(category1.products)
        product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        category1.add_product(product4)
        print(category1.products)
        print(category1.product_count)

        new_product = Product.new_product(
            {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
             "quantity": 5})
        print(new_product.name)
        print(new_product.description)
        print(new_product.price)
        print(new_product.quantity)

        new_product.price = 800
        print(new_product.price)

        new_product.price = -100
        print(new_product.price)
        new_product.price = 0
        print(new_product.price)
"""
