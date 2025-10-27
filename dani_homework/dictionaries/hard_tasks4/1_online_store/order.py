# Order
# Атрибути: cart, status
# Методи: confirm_order() → ако има наличности, намалява стоката и сменя статуса
from cart import Cart
from product import Product

class Order:
    def __init__(self, cart: Cart):
        self.cart = cart
        self.status = "pending"  # pending | confirmed | failed

    def confirm_order(self) -> bool:
    # Ако има наличности за всички продукти, намалява стоката и сменя статуса на 'confirmed'.
    # Иначе оставя всичко непроменено и статус 'failed'.

        items = self.cart.items()  # Product -> qty

    # 1) Проверка за наличности
        for product, qty in items.items():
            if qty <= 0 or not product.is_available(qty):
                self.status = "failed"
                return False

    # 2) Всички са налични -> намаляваме стоката атомарно
        for product, qty in items.items():
    # reduce_stock тук трябва да успее, понеже току-що проверихме
            ok = product.reduce_stock(qty)
            if not ok:
    # В малко вероятен race case бихме върнали стоките назад, но тук
    # приемаме еднопоточен сценарий и отбелязваме неуспех.
                self.status = "failed"
                return False

        self.status = "confirmed"
        return True

    def __str__(self):
        return f"Order(status={self.status}, total={self.cart.total_price():.2f})"
