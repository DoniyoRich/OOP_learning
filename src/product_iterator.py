class ProductIterator:
    """ Класс итератор для прохода по списку товаров. """

    def __init__(self, categ_obj):
        """ Инициализация итератора. """
        self.category = categ_obj
        self.index = 0

    def __iter__(self):
        """ Возвращает объект для итерирования (итератор). """
        self.index = 0
        return self

    def __next__(self):
        """
        Возвращает очередной элемент последовательности, если не достигнут предел.
        Иначе вызывается исключение StopIteration.
        """
        if self.index < len(self.category.products):
            prod_ = self.category.products[self.index]
            self.index += 1
            return prod_
        else:
            raise StopIteration
