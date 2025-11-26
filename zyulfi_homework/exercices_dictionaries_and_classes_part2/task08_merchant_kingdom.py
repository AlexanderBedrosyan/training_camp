# Задача 8: Кралство на търговците
# Създай клас MerchantKingdom, който следи градове и тяхната търговия.
# Изисквания:
# Речник {град: {"goods": {стока: количество}, "revenue": печалба}}
# add_city(name)
# sell_goods(city, item, quantity, price)
# richest_city() — връща града с най-много приходи.
# total_goods() — връща общо количество продадени стоки.

class MerchantKingdom:
    def __init__(self):
        self.kingdom_dict = {}

    def add_city(self, name):
        if name not in self.kingdom_dict:
            self.kingdom_dict[name] = {}
            self.kingdom_dict[name]["goods"] = {}
            self.kingdom_dict[name]["revenue"] = 0

    def sell_goods(self, city, item, quantity, price):
        if city not in self.kingdom_dict:
            self.add_city(city)
        self.kingdom_dict[city]["goods"][item] = {
            "quantity": quantity,
            "price": price
            }

        self.kingdom_dict[city]["revenue"] += quantity * price

    def richest_city(self):
        return sorted(self.kingdom_dict.items(), key=lambda x: -x[1]["revenue"])[0][0]

    def total_goods(self):
        total = 0
        for curr_name, curr_values in self.kingdom_dict.items():
            for item, details in curr_values["goods"].items():
                total += details["quantity"]
        return total

# Тест:
k = MerchantKingdom()
k.add_city("Varna")
k.sell_goods("Varna", "Wine", 50, 10)
k.sell_goods("Varna", "Oil", 20, 30)
k.add_city("Burgas")
k.sell_goods("Burgas", "Banana", 100, 3)
k.sell_goods("Burgas", "Apple", 200, 5)

print(k.kingdom_dict)
print(k.richest_city()) # Varna
print(k.total_goods()) # 70

k.total_goods()