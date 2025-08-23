# Book има допълнителен private атрибут __author с @property
from item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title=str, author=str):
        super().__init__(title)
        self.__author = author

    @property
    def author(self) -> str:
        return self._Book__author
