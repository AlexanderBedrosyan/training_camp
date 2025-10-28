from product import Product
from cart import Cart
from discount import Discount

p1 = Product("Apple", 2.0)
p2 = Product("Milk", 3.5)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)

d = Discount(10)
print(cart.total_price())           # 5.5
print(cart.apply_discount(d))       # 4.95