# Атрибути: name, price, stock
# Методи:
# reduce_stock(qty) → намалява стоката, ако има наличност
# is_available(qty) → проверява дали продуктът е наличен в нужното количество

class Product:
    def __init__(self,name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, qty=int) -> bool:
        if qty <= self.stock:
            return True
        return False

    def reduce_stock(self, qty=int) -> bool:
        if self.is_available(qty):
            self.stock -= qty
            return True
        else:
            return False

    def total_price(self, qty) -> float:
        if self.is_available(qty):
            return qty * self.price
        else:
            raise ValueError("Not enough")