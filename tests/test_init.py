from src.main import Category


def test_init_prod_samsung(product_samsung):
    assert product_samsung.name == "Samsung"
    assert product_samsung.price == 120000.0


def test_init_category_notebooks(category_notebooks):
    assert category_notebooks.description == "Ультрабуки, планшеты"
    assert category_notebooks.products == ["ASUS", "SONY"]
    Category.category_count = 0
    Category.product_count = 0
