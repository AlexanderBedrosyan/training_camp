class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented


# Примерно използване:
p1 = Product("Bread", 2.0)
p2 = Product("Milk", 3.5)

print(p1 > p2)   # True
print(p1 == p2)  # False
