# Store
# Атрибути: private __orders
# Методи: add_order(order)
# total_revenue()
from order import Order

class Store:
    def __init__(self):
        self.__orders = []  # private списък с поръчки

    def add_order(self, order: Order):
        # Добавя поръчка в магазина.
        self.__orders.append(order)

    def total_revenue(self) -> float:
        # Връща общия приход от всички поръчки.
        return sum(o.order_total() for o in self.__orders)

    def __str__(self):
        return f"Store({len(self.__orders)} orders)"
