from abc import ABCMeta, abstractmethod


class Clothes(metaclass=ABCMeta):
    @abstractmethod
    def get_cloth_amount(self):
        """Amount of cloth required"""


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def get_cloth_amount(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def get_cloth_amount(self):
        return self.height * 2 + 0.3


coat = Coat(40)
costume = Costume(1.8)
print(f'Total cloth amount for coat: {coat.get_cloth_amount:.2f} m\u00b2')
print(f'Total cloth amount for costume: {costume.get_cloth_amount:.2f} m\u00b2')
