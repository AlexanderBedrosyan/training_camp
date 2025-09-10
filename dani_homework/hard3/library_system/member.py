# Member
# Атрибути: name, private __borrowed_books
# Методи:
# borrow_book(book)
# return_book(book)
# list_books()
from book import Book


class Member:
    def __init__(self, name:str):
        self.name = name
        self.__borrowed_books: list[Book] = []

    def borrow_book(self, current_book:Book):
        self.__borrowed_books.append(current_book)
        current_book.borrow()

    def return_book(self, current_book:Book):
        if current_book in self.__borrowed_books:
            current_book.return_book()
            self.__borrowed_books.remove(current_book)

    def list_books(self):
        return self.__borrowed_books