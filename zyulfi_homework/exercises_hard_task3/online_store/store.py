# Атрибути: private __orders
# Методи:
# add_order(order)
# total_revenue()
from order import Order


class Store:
    def __init__(self):
        self.__orders: list[Order] = []

    def add_order(self, curr_order=object) -> None:
        if curr_order.__class__.__name__ == "Order":
            self.__orders.append(curr_order)
        else:
            raise TypeError("Error")

    def total_revenue(self) -> float or int:
        return sum(curr_order.order_total() for curr_order in self.__orders)