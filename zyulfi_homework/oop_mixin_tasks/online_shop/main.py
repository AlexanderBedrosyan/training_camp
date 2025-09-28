from product import Product
from user import User
from cart import Cart

p1 = Product("Phone", 800)
p2 = Product("Laptop", 1500)

u = User("Maria")
cart = u.get_cart()
cart.add_product(p1)
cart.add_product(p2)

print(cart.total())  # 2300
print(cart.discounted_total(10))  # 2070.0