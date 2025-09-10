# from item import Item
from book import Book
from dvd import DVD

b = Book("The Hobbit", 1937, "J.R.R. Tolkien")
d = DVD("Inception", 2010, 148)

#b.title = ""
b.print_info()
d.print_info()

print(Book.library_name)
b.title = "The Lord of the Rings"
print(b.title)
try:
    d.duration = -10
except ValueError as e:
    print("Error:", e)
