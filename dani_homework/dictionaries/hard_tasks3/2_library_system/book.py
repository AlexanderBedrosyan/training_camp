# Book
# Атрибути: title, author, private __available (True/False)
# Методи:
# borrow() → ако е налична, става False
# return_book() → връща я нали

class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
        self.__available = True

    def borrow(self) -> bool:
        if self.__available:
            self.__available = False

    def return_book(self):
        if self.__available is False:
            self.__available = True

    def is_available(self):
        return self.__available

