from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def new_product(self):
        pass
