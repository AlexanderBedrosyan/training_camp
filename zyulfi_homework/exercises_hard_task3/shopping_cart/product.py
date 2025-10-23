# Атрибути: name, price
# Метод: __str__() → "Product {name}, price {price}"

class Product:
    def __init__(self, name=str, price=float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product {self.name}, price {self.price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Error")
        self._price = value


# p = Product("banana", 3.50)
# print(str(p))
# p.price = -20
