from product import Product
from order import Order
from store import Store

p1 = Product("Laptop", 1200)
p2 = Product("Mouse", 25)

o1 = Order()
o1.add_product(p1)
o1.add_product(p2)

s = Store()
s.add_order(o1)

print(o1.order_total())    # 1225
print(s.total_revenue())   # 1225