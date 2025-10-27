# История:
# Собственик си на онлайн магазин. Всеки продукт има цена и наличност.
# Трябва да приемаш поръчки и да изчисляваш крайната сума,
# като актуализираш наличностите в склада.
from itertools import product

# Условие:
# Създай клас Store, който има методи:
# - add_product(name, price, stock)
# - process_order(order_dict) → връща обща сума и обновен склад
# Ако някой продукт не е наличен – пропусни го.

class Store:
    def __init__(self):
        self.list_of_product = {} # {"лаптоп": {price:1200, stock:5}}

    def add_product(self, curr_name, curr_price, curr_stock):
        self.list_of_product[curr_name] = {}
        self.list_of_product[curr_name]["price"] = curr_price
        self.list_of_product[curr_name]["stock"] = curr_stock

    def process_order(self, order_dict):
        all_price = 0
        for name, stock in order_dict.items():
            if name in self.list_of_product:
                if stock <= self.list_of_product[name]["stock"]:
                    self.list_of_product[name]["stock"] -= stock
                    all_price += stock * self.list_of_product[name]["price"]
        return (all_price, self.list_of_product)


store = Store()
store.add_product("лаптоп", 1200, 5)
store.add_product("мишка", 25, 10)
store.add_product("монитор", 300, 2)
print(store.process_order({"лаптоп": 2, "монитор": 3, "мишка": 5}))
# print(store.list_of_product)


# Очакван изход:
# (2625, {
# 'лаптоп': {'price': 1200, 'stock': 3},
# 'мишка': {'price': 25, 'stock': 5},
# 'монитор': {'price': 300, 'stock': 2}})