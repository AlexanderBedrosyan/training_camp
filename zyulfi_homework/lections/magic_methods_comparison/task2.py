# Задача 2: Сравнение на продукти
# Клас Product:
#   name
#   price
# Имплементирайте:
# __gt__ → сравнява цените
# __eq__ → равни ако цените са еднакви

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
       return self.price > other.price

    def __eq__(self, other):
        return self.price == other.price

# Пример:

p1 = Product("Bread", 2.0)
p2 = Product("Milk", 1.5)
print(p1 > p2)   # True
print(p1 == p2)  # False
