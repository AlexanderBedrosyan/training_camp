from product import Product
from cart import Cart
from order import Order

# Продукти
laptop = Product("Laptop", 1200.0, stock=5)
mouse = Product("Mouse", 25.0, stock=10)
print(laptop)
print(mouse)

# Количка
cart = Cart()
cart.add_product(laptop, 1)
cart.add_product(mouse, 1)
print(cart)
print("Cart total:", cart.total_price())  # 1225.0

# Поръчка
order = Order(cart)
ok = order.confirm_order()
print("Order confirmed?", ok)
print("Order status:", order.status)
print(laptop)  # stock намален с 1
print(mouse)   # stock намален с 1

# Демонстрация: опит за надвишаване на наличност
try:
    cart2 = Cart()
    cart2.add_product(laptop, 10)  # ще вдигне грешка (недостатъчна наличност)
except ValueError as e:
    print("Expected error:", e)


# Product знае собствената си цена и наличност.
# is_available(qty) проверява количества,
# reduce_stock(qty) намалява при успех.
# Cart пази продукти и количества в private речник.
# add_product проверява, че общото желано количество в количката не превишава текущия stock.
# Order първо проверява наличност за всички артикули;
# ако всичко е ОК, намалява стоките и става confirmed, иначе failed.
