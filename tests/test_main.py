import src
from src.main import Category, Product
from unittest import mock


def test_init_prod_samsung(product_samsung):
    assert product_samsung.name == "Samsung"
    assert product_samsung.price == 120000.0


def test_init_category_notebooks(category_notebooks):
    assert category_notebooks.description == "Ультрабуки, планшеты"
    assert category_notebooks.products == ["ASUS", "SONY"]
    Category.category_count = 0
    Category.product_count = 0


def test_count_prods(product_samsung, product_poco, product_huawey):
    category_1 = Category("Телефоны", "Современные флагманы", [product_samsung, product_poco, product_huawey])
    assert category_1.product_count == 3
    Category.category_count = 0
    Category.product_count = 0


def test_count_categories(category_notebooks, category_washing_mashines):
    assert Category.category_count == 2
    Category.category_count = 0
    Category.product_count = 0

def test_if_main():
    with mock.patch('__main__.__name__', '__main__'):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        print(product1.name)
        print(product1.description)
        print(product1.price)
        print(product1.quantity)

        print(product2.name)
        print(product2.description)
        print(product2.price)
        print(product2.quantity)

        print(product3.name)
        print(product3.description)
        print(product3.price)
        print(product3.quantity)

        category1 = Category("Смартфоны",
                             "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                             [product1, product2, product3])

        print(category1.name == "Смартфоны")
        print(category1.description)
        print(len(category1.products))
        print(category1.category_count)
        print(category1.product_count)

        product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        category2 = Category("Телевизоры",
                             "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                             [product4])

        print(category2.name)
        print(category2.description)
        print(len(category2.products))
        print(category2.products)

        print(Category.category_count)
        print(Category.product_count)
