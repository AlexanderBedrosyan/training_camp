# Задача 3: Сравнение на книги
# Клас Book:
#   title
#   pages
# Имплементирайте:
# __le__ → сравнява по брой страници
# __ne__ → различни, ако страниците не съвпадат

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __ne__(self, other):
        return self.pages != other.pages

# Пример:

b1 = Book("1984", 300)
b2 = Book("Animal Farm", 120)
print(b1 <= b2)  # False
print(b1 != b2)  # True