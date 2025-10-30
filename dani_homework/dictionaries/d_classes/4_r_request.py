# Задача 4: Ресторантски поръчки
# Създай клас Restaurant, който следи клиентски поръчки.
#
# Условия:
# Речник {клиент: {"orders": [{"item": име, "price": сума}], "total": сума}}
# Метод add_order(client, item, price)
# Метод top_client() – връща клиента с най-голяма сметка.
from pprint import pprint

class Restaurant:
    def __init__(self):
        self.rest_dict = {}

    def add_order(self, client, item, price):
        item_dict = {"item": item, "price": price}
        if client not in self.rest_dict:
            self.rest_dict[client] = {}
            self.rest_dict[client]["orders"] = []
            self.rest_dict[client]["total"] = 0

        self.rest_dict[client]["orders"].append(item_dict)
        self.rest_dict[client]['total'] += price

    def top_client(self):
        return sorted(self.rest_dict.items(), key=lambda x: x[1]["total"], reverse=True)[0][0]

# Тест:
r = Restaurant()
r.add_order("Nikol", "Pizza", 15)
r.add_order("Ivan", "Pasta", 10)
r.add_order("Nikol", "Juice", 5)
pprint(r.rest_dict)
print(r.top_client())  # Nikol