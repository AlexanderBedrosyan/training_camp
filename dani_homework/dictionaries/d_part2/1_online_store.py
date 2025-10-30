# История:
# Собственик си на онлайн магазин. Всеки продукт има цена и наличност.
# Трябва да приемаш поръчки и да изчисляваш крайната сума,
# като актуализираш наличностите в склада.
# Условие:
# Създай клас Store, който има методи:
# - add_product(name, price, stock)
# - process_order(order_dict) → връща обща сума и обновен склад
# Ако някой продукт не е наличен – пропусни го.

# 2625, {
# 'лаптоп': {'price': 1200, 'stock': 3},
# 'мишка': {'price': 25, 'stock': 5},
# 'монитор': {'price': 300, 'stock': 2}})

class Store:
    def __init__(self):
        self.products = {}  # име: {price, stock}

    def add_product(self, name, price, stock):
        # Добавя нов продукт или обновява съществуващ.
        self.products[name] = {'price': price, 'stock': stock}

    def process_order(self, order_dict):
        # Връща обща сума и обновен склад.
        # Пропуска продукти, които ги няма или нямат наличност.
        total = 0

        for name, qty in order_dict.items():
            if name in self.products and self.products[name]['stock'] > 0:
                available = self.products[name]['stock']
                buy_qty = min(qty, available)  # колкото има налични
                total += buy_qty * self.products[name]['price']
                self.products[name]['stock'] -= buy_qty

        return total, self.products


# --- Пример за използване ---
store = Store()
store.add_product('лаптоп', 1200, 3)
store.add_product('мишка', 25, 5)
store.add_product('монитор', 300, 2)

order = {'лаптоп': 2, 'мишка': 3, 'монитор': 1, 'клавиатура': 1}

total, updated_stock = store.process_order(order)

print(total)          # 👉 2625
print(updated_stock)  # 👉 {'лаптоп': {'price': 1200, 'stock': 1}, 'мишка': {'price': 25, 'stock': 2}, 'монитор': {'price': 300, 'stock': 1}}