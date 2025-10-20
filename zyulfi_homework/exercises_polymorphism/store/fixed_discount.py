# FixedDiscount: прилага фиксирано намаление
from exercises_polymorphism.store.discount import Discount


class FixedDiscount(Discount):
    def __init__(self, fix):
        self.fix = fix

    def apply(self, price):
        return price * (1 - self.fix/100)
