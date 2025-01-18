from src.product import Product


class Category:
    """ Класс Категорий товаров. """
    name: str
    description: str
    __products: list[object]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """ Метод для добавления товара в список товаров. """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """ Геттер для получения списка товаров в заданном формате. """
        products_ = []
        for prod in self.__products:
            # print(prod.name)
            products_.append(f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n')

        return products_
