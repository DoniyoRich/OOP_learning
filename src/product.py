from src.base_product import BaseProduct
from src.mixin_log import MixinLog


class Product(BaseProduct, MixinLog):
    """ Класс Продуктов. """
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        """ Метод для пользовательского отображения информации по продукту. """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Получение информации об общей стоимости двух продуктов на складе. """
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, prod_dict):
        """ Создание нового продукта на основе словаря. """
        return cls(**prod_dict)

    @property
    def price(self):
        """ Геттер для получения данных о цене продукта. """
        return self.__price

    @price.setter
    def price(self, new_price):
        """ Сеттер для установления корректной (положительной) цены продукта. """
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        self.__price = new_price
