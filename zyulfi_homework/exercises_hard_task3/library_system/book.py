# Атрибути: title, author, private __available (True/False)
# Методи:
# borrow() → ако е налична, става False
# return_book() → връща я налична

class Book:
    def __init__(self, title=str, author=str):
        self.title = title
        self.author = author
        self.__available = True

    def borrow(self) -> None:
        if self.__available:
            self.__available = False
        else:
            self.__available = True

    def return_book(self) -> None:
        if not self.__available:
            self.__available = True
        else:
            self.__available = False

    def is_available(self):
        return self.__available

