class MixinLog:

    def __repr__(self):
        print(f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})")
