class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __le__(self, other):
        if isinstance(other, Book):
            return self.pages <= other.pages
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Book):
            return self.pages != other.pages
        return NotImplemented


# Примерно използване:
b1 = Book("1984", 300)
b2 = Book("Animal Farm", 120)

print(b1 <= b2)  # False
print(b1 != b2)  # True
