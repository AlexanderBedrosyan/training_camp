# Order
# Атрибути: private __products
# Методи: add_product(product)
# order_total()
from product import Product

class Order:
    def __init__(self):
        self.__products = []  # private списък с продукти

    def add_product(self, product: Product):
        # Добавя продукт към поръчката.
        self.__products.append(product)

    def order_total(self) -> float:
        # Връща общата сума на поръчката.
        return sum(p.price for p in self.__products)

    def get_products(self):
        # Връща списък с продуктите (по желание).
        return list(self.__products)

    def __str__(self):
        products_str = ", ".join(p.name for p in self.__products)
        return f"Order([{products_str}])"
