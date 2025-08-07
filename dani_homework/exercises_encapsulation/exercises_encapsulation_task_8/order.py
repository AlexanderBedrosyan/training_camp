# Клас Order с:
# protected атрибут _total
# метод add_item(price)

class Order:
    def __init__(self):
        self._total = 0  # protected атрибут

    def add_item(self, price):
        self._total += price