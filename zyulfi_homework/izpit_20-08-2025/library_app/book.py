# клас Book, наследява Item
# `Book`: добави private атрибут `__author`
#•	Добави property author за Book, което не позволява None:
# o	Ако за името е подадено празно място, то да връща грешка:
# „Author name cannot be None”
# o	Ако не е None място, то да си закача атрибута.

from item import Item

class Book(Item):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.__author = author

    def print_info(self):
        print(f"Book: {self.get_info()}, author: {self.__author}")

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if value is None:
            raise ValueError("Author name cannot be None")
        else:
            self.__author = value