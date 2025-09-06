# Атрибути: name, private __borrowed_books
# Методи:
# borrow_book(book)
# return_book(book)
# list_books()
from book import Book

class Member:
    def __init__(self, name):
        self.name = name
        self.__borrowed_books: list[Book] = []

    def borrow_book(self, curr_book=Book):
        self.__borrowed_books.append(curr_book)
        curr_book.borrow()

    def return_book(self, curr_book=Book):
        if curr_book in self.__borrowed_books:
            curr_book.return_book()
            self.__borrowed_books.remove(curr_book)

    def list_books(self):
        return self.__borrowed_books



