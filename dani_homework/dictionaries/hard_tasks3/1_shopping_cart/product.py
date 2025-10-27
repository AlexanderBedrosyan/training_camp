# Product
# Атрибути: name, price
# Метод: __str__() → "Product {name}, price {price}"

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product {self.name}, price {self.price}"
