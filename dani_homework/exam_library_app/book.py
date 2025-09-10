# `Book` и `DVD` наследяват `Item`.
from item import Item
from mixins import PrintableMixin

class Book(Item, PrintableMixin):
    def __init__(self, title=str, year=int, author=str):
        super().__init__(title, year)
        self.__author = author

    def get_info(self):
        return f"Book: {self._title}({self.year}), author: {self.__author}"

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if value is None:
            raise ValueError("Author name cannot be None")
        self.__author = value
