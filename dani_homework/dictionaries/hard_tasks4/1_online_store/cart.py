# Cart
# Атрибути: private __items (dict: продукт → количество)
# Методи:
# add_product(product, qty) → проверява наличност преди добавяне
# total_price() → сумира общата стойност
from product import Product

class Cart:
    def __init__(self):
        # dict: продукт (обект) -> количество
        self.__items: dict[Product, int] = {}

    def add_product(self, product: Product, qty: int):
        # Добавя продукт в количката, като проверява наличността.
        if qty <= 0:
            raise ValueError("Quantity must be positive.")

        current = self.__items.get(product, 0)
        desired_total = current + qty

        # Проверяваме спрямо текущия наличен stock на продукта
        if not product.is_available(desired_total):
            raise ValueError(
                f"Not enough stock for {product.name}. "
                f"Requested: {desired_total}, available: {product.stock}"
            )

        self.__items[product] = desired_total

    def total_price(self) -> float:
        # Сумира общата стойност на продуктите в количката.
        return sum(p.price * q for p, q in self.__items.items())

    def items(self) -> dict:
        # Връща копие на артикулите (продукт -> количество).
        return dict(self.__items)

    def __str__(self):
        if not self.__items:
            return "Cart(empty)"
        parts = [f"{p.name} x{q}" for p, q in self.__items.items()]
        return "Cart(" + ", ".join(parts) + ")"
