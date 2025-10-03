# - **Member (BorrowMixin)**
#   - Атрибути: `name`, private `__borrowed_books`
#   - Методи: `list_books()`
from book import Book
from borrowmixin import BorrowMixin

class Member(BorrowMixin):
    def __init__(self, name=str):
        self.name = name
        self.__borrowed_books: list[Book] = []

    def list_books(self, ):
        return self.__borrowed_books
