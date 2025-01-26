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

    def __str__(self):
        """ Метод для пользовательского отображения информации по категории. """
        return f"{self.name}, количество продуктов: {sum([prod.quantity for prod in self.__products])} шт."

    def add_product(self, product_: Product):
        """ Метод для добавления товара в список товаров. """
        if isinstance(product_, Product):
            self.__products.append(product_)
            Category.product_count += 1
            return
        else:
            raise TypeError

    @property
    def products(self):
        """ Геттер для получения списка товаров в заданном формате. """
        products_ = []
        for prod in self.__products:
            products_.append(f'{str(prod)}\n')

        return products_
