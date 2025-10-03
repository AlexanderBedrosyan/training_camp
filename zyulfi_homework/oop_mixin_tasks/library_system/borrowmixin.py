# - **BorrowMixin**
# Методи: `borrow(book)`, `return_book(book)`

from book import Book

class BorrowMixin:
    def borrow(self, book=Book):
        if book.is_available():
            book.set_unavailable()
            self._Member__borrowed_books.append(book)
            return True
        return False

    def return_book(self, book=Book):
        if not book.is_available():
            book.set_available()
            return True
        return False
