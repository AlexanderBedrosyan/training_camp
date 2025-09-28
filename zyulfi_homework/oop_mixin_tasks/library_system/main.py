# **main.py**
# ```python

from book import Book
from member import Member
from library import Library

b1 = Book("1984", "George Orwell")
b2 = Book("Dune", "Frank Herbert")

lib = Library()
lib.add_book(b1); lib.add_book(b2)

m = Member("Ivan")
m.borrow(b1)
print([book.title for book in m.list_books()])  # ['1984']
print([book.title for book in lib.available_books()])  # ['Dune']
m.return_book(b1)
print(b1.is_available())  # True
