import pytest

from src.product_iterator import ProductIterator


def test_product_iterator(category_phones):
    prod_iter = ProductIterator(category_phones)
    assert prod_iter.index == 0


def test_product_iteration(category_phones):
    prod_iter = ProductIterator(category_phones)
    assert next(prod_iter) == "Samsung, 120000.0 руб. Остаток: 5 шт.\n"
    assert next(prod_iter) == "POCO, 90000.0 руб. Остаток: 12 шт.\n"
    assert next(prod_iter) == "Huawey, 144000.0 руб. Остаток: 3 шт.\n"

    with pytest.raises(StopIteration):
        assert next(prod_iter)
