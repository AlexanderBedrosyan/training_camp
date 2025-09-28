# - **Library**
#   - Атрибути: private `__books`
#   - Методи: `add_book()`, `available_books()`, `find_book(title)`
from book import Book

class Library:
    def __init__(self):
        self.__books: list[Book] = []

    def add_book(self, curr_book):
        self.__books.append(curr_book)

    def available_books(self):
        list_of_available_book = []
        for curr_book in self.__books:
            if curr_book.is_available():
                list_of_available_book.append(curr_book)
        return list_of_available_book

    def find_book(self, title):
        for curr_book in self.__books:
            if curr_book.title == title:
                return True
        return False

