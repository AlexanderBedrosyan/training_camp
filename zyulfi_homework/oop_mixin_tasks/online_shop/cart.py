# Атрибути: private __items
# Методи: add_product(product), total(), discounted_total(percent)

from product import Product
from discount_mixin import DiscountMixin


class Cart(DiscountMixin):
    def __init__(self):
        self.__items: list[Product] = []

    def add_product(self, curr_product=Product) -> None:
        self.__items.append(curr_product)

    def total(self) -> float:
        return sum([curr_product.price for curr_product in self.__items])

    def discounted_total(self, percent):
        return self.apply_discount(self.total(), percent)



