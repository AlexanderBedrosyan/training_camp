from item import Item
from book import Book
from dvd import DVD
from mixins import PrintableMixin

b = Book("The Hobbit", 1937, "J.R.R. Tolkien")
d = DVD("Inception", 2010, 148)

b.print_info()
d.print_info()

print(Book.library_name)
b.title = "The Lord of the Rings"
print(b.title)

#d.duration = -10
b1 = Book("The Hobbit", 1937, "Ivanov")
b1.author = None
