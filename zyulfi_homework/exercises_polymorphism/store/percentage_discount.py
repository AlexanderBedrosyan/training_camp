# PercentageDiscount: прилага % намаление
from exercises_polymorphism.store.discount import Discount


class PercentageDiscount(Discount):
    def __init__(self, rate):
        self.rate = rate

    def apply(self, price):
        return price - ((price * self.rate) / 100)


