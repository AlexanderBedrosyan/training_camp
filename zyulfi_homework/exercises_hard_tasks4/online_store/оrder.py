# Атрибути: cart, status
# Методи:
# confirm_order() → ако има наличности, намалява стоката и сменя статуса

from cart import Cart

class Order:
    def __init__(self, cart:Cart):
        self.cart = cart
        self.status = False

    def confirm_order(self):
        for curr_product, curr_qty in self.cart.get_items().items():
            if not curr_product.is_available(curr_qty):
                return f"This {curr_product.name} is not enough"
        self.status = True

        for curr_product, curr_qty in self.cart.get_items().items():
            curr_product.reduce_stock(curr_qty)
        return "Order completed"
