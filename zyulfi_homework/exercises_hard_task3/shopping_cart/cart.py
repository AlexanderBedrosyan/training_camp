# Атрибути: private __products
# Методи:
# add_product(product)
# total_price()
# apply_discount(discount)
from discount import Discount
from product import Product


class Cart:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, curr_product=object) -> None:
        if curr_product.__class__.__name__ == "Product":
           self.__products.append(curr_product)
        else:
            raise TypeError("Not object")

    def total_price(self) -> float or int:
        return sum([curr_product.price for curr_product in self.__products])

    def apply_discount(self, curr_discount: Discount):
        for curr_product in self.__products:
            curr_product.price = curr_discount.calculate(curr_product.price)
        return self.total_price()


# p = Product("banana", 100)
# d = Discount(10)
# c = Cart()
# c.add_product(p)
# print(c.total_price())
# print(c.apply_discount(d))

