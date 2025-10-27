# Cart
#
# Атрибути: private __products
# Методи:
# add_product(product)
# total_price()
# apply_discount(discount)
from product import Product
from discount import Discount

class Cart:
    def __init__(self):
        self.__products = []  # private списък с продукти

    def add_product(self, product: Product):
        # Добавя продукт в количката.
        self.__products.append(product)

    def total_price(self) -> float:
        # Изчислява общата цена без намаление.
        return sum(p.price for p in self.__products)

    def apply_discount(self, discount: Discount) -> float:
        # Прилага отстъпката към общата сума и връща крайната цена.
        total = self.total_price()
        return discount.calculate(total)

    def __str__(self):
        items = ", ".join(p.name for p in self.__products)
        return f"Cart([{items}])"
