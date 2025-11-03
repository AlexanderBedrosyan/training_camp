# Задача 8: Кралство на търговците
# Създай клас MerchantKingdom, който следи градове и тяхната търговия.
# Изисквания: Речник {град: {"goods": {стока: количество}, "revenue": печалба}}
# add_city(name)
# sell_goods(city, item, quantity, price)
# richest_city() — връща града с най-много приходи.
# total_goods() — връща общо количество продадени стоки.

class MerchantKingdom:
    def __init__(self):
        self.dict_cities = {}
    #{град: {"goods": {стока: количество}, "revenue": печалба}}

    def add_city(self, name):
        if name not in self.dict_cities:
            self.dict_cities[name] = {"goods": {}, "revenue": 0}

    def sell_goods(self, city, item, quantity, price):
        if city not in self.dict_cities:
            print(f"The city '{city}' does not exist!")
            return
        city_data = self.dict_cities[city]

        # Добавяме количество от стоката
        if item not in city_data["goods"]:
            city_data["goods"][item] = 0
        city_data["goods"][item] += quantity

        # Добавяме приходите
        city_data["revenue"] += quantity * price

    def richest_city(self):
        if not self.dict_cities:
            return None
        return max(self.dict_cities, key=lambda c: self.dict_cities[c]["revenue"])

    def total_goods(self):
        total = 0
        for city_data in self.dict_cities.values():
            total += sum(city_data["goods"].values())
        return total

# Тест:
k = MerchantKingdom()
k.add_city("Varna")
k.sell_goods("Varna", "Wine", 50, 10)
k.sell_goods("Varna", "Oil", 20, 30)
print(k.richest_city()) # Varna
print(k.total_goods()) # 70