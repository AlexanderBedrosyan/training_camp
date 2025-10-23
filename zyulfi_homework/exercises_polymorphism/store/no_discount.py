# NoDiscount: връща оригиналната цена
from exercises_polymorphism.store.discount import Discount


class NoDiscount(Discount):

    def apply(self, price):
        return price