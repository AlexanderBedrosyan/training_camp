from product import Product
from cart import Cart
from оrder import Order

p1 = Product("banana", 2.55, 20)
p2 = Product("apple", 2, 30)
p1.reduce_stock(10)
p1.reduce_stock(30)
print(p1.total_price(10))

c1 = Cart()
c1.add_product(p1, 5)
c1.add_product(p2, 10)

print(c1.total_price())

o1 = Order(c1)
p1.stock = 0
print(o1.confirm_order())







