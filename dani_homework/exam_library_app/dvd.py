# `Book` и `DVD` наследяват `Item`.
from item import Item
from mixins import PrintableMixin

class DVD(Item, PrintableMixin):
    def __init__(self, title=str, year=int, duration=int):
        super().__init__(title, year)
        self.__duration = duration

    def get_info(self):
        return f"DVD: {self._title}({self.year}), duration: {self.__duration}"

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if value <= 0:
            raise ValueError("Duration cannot be less than or equal to zero")
        self.__duration = value