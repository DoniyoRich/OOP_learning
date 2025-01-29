import pytest

from src.lawngrass import LawnGrass
from src.main import main
from src.product import Product
from src.category import Category
from src.smartphone import Smartphone


def test_init_prod_samsung(product_samsung):
    assert product_samsung.name == "Samsung"
    assert product_samsung.price == 120000.0


def test_init_category_notebooks(category_notebooks, notebook_asus):
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


def test_add_wrong_product_to_category(smartphone1, smartphone2):
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])

    with pytest.raises(TypeError):
        category_smartphones.add_product("Не смартфон")


def test_add_different_products():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    with pytest.raises(TypeError):
        smartphone1 + grass2

    with pytest.raises(TypeError):
        grass2 + smartphone1


def test_product_str(product_poco):
    assert str(product_poco) == "POCO, 90000.0 руб. Остаток: 12 шт."


def test_category_str(category_notebooks):
    assert str(category_notebooks) == "Ноутбуки, количество продуктов: 122 шт."


def test_product_add(product_samsung, product_huawey):
    assert product_samsung + product_huawey == 1_032_000.0


def test_mixin_repr(capsys):
    Product("SONY", "Ноутбуки SONY", 95000.0, 68)
    captured = capsys.readouterr()
    assert "Product('SONY', 'Ноутбуки SONY', 95000.0, 68)" in captured.out


def test_main(capsys, out_main):
    main()
    captured = capsys.readouterr()
    assert out_main in captured.out
