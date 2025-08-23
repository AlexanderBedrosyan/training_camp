# DiscountedItem: комбинира двете, добавя валидации
from item import Item
from discount_mixin import DiscountMixin

class DiscountedItem(DiscountMixin):
    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price