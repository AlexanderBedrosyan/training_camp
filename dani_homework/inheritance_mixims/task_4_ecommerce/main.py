from item import Item
from cart import Cart

cart = Cart()
cart.add_item(Item("Laptop", 1000))
cart.add_item(Item("Mouse", 50))
print(cart.total)  # 1050