# Library
# Атрибути: private __books
# Методи:
# add_book(book)
# available_books()
from book import Book


class Library:
    def __init__(self):
        self.__books: list[Book] = []

    def add_book(self, book):
        self.__books.append(book)

    def available_books(self):
        available_books = []
        for current_book in self.__books:
            if current_book.is_available():
                available_books.append(current_book.title)

        return available_books



