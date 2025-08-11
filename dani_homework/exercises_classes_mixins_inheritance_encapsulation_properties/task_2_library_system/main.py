from book import Book
from dvd import DVD

b = Book("1984", "Orwell")
b.checkout()
print(b.is_available())  # False

d = DVD("Inception", 148)
print(d.is_long())  # True