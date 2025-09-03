# Атрибути: private __products
# Методи:
# add_product(product)
# order_total()
from product import Product


class Order:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, curr_product=object) -> None:
        if curr_product.__class__.__name__ == "Product":
            self.__products.append(curr_product)
        else:
            raise ValueError("Error")

    def order_total(self) -> float or int:
        return sum([curr_product.price for curr_product in self.__products])
