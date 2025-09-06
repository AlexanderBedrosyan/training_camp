# Атрибути: private __books
# Методи:
# add_book(book)
# available_books()

from book import Book

class Library:
    def __init__(self):
        self.__books: list[Book] = []

    def add_book(self, curr_book=Book):
        if curr_book.__class__.__name__ == "Book":
            self.__books.append(curr_book)
        else:
            raise TypeError("Not object")

    def available_books(self) -> list:
        available_books = []
        for curr_book in self.__books:
            if curr_book.is_available():
                available_books.append(curr_book.title)
        return available_books

