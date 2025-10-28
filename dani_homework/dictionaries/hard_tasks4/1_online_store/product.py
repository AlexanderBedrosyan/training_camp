# Product
# Атрибути: name, price, stock
# Методи:
# reduce_stock(qty) → намалява стоката, ако има наличност
# is_available(qty) → проверява дали продуктът е наличен в нужното количество
class Product:
    def __init__(self, name: str, price: float, stock: int):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, qty: int) -> bool:
        # Проверява дали продуктът е наличен в нужното количество.
        if qty <= 0:
            return False
        return qty <= self.stock

    def reduce_stock(self, qty: int) -> bool:
        # Намалява стоката, ако има наличност. Връща True/False.
        if qty <= 0:
            return False
        if self.is_available(qty):
            self.stock -= qty
            return True
        return False

    def __str__(self):
        return f"Product({self.name}, price={self.price:.2f}, stock={self.stock})"
