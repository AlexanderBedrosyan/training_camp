from book import Book
from member import Member
from library import Library

b1 = Book("1984", "Orwell")
b2 = Book("Dune", "Herbert")
m = Member("Ivan")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

m.borrow_book(b1)
print(lib.available_books())   # ['Dune']
m.return_book(b1)
print(lib.available_books())   # ['1984', 'Dune']
