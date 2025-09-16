# Атрибути: private __items (dict: продукт → количество)
# Методи:
# add_product(product, qty) → проверява наличност преди добавяне
# total_price() → сумира общата стойност
from product import Product

class Cart:
    def __init__(self):
        self.__items = {}

    def add_product(self, product:Product, qty=int) -> None:
        if product.is_available(qty):
            self.__items[product] = qty
        else:
            print("Qty not enough")

    def total_price(self) -> float:
        return sum([curr_product.total_price(curr_qty) for curr_product, curr_qty in self.__items.items()])

    def get_items(self) -> dict[]:
        return self.__items