# Задача 4: Управление на инвентар
# inventory = {"wood": 15, "iron": 8, "stone": 22}
# Изисквания:
# Добави нов материал, ако не съществува.
# Ако количеството падне под 10, изведи предупреждение.
# Сортирай материалите по количество (низходящо).

class Inventory:
    def __init__(self, curr_inventory):
        self.curr_inventory = curr_inventory

    def add_new_item(self, curr_item, item_num):
        if curr_item not in self.curr_inventory:
            self.curr_inventory[curr_item] = 0
        self.curr_inventory[curr_item] += item_num

    def remove_item(self, curr_item, num):
        # curr_invertory = {"wood": 15, "iron": 8, "stone": 22}
        # curr_item = wood
        # num = 5
        try:
            if self.curr_inventory[curr_item] < num:
                return "Not enough"
            self.curr_inventory[curr_item] -= num
            if self.curr_inventory[curr_item] < 10:
                print("Warning")
            return self.curr_inventory[curr_item]
        except KeyError:
             return "Error"

    def sorted_inventory(self):
        return dict(sorted(self.curr_inventory.items(), key=lambda item: -item[1]))


inventory = {"wood": 15, "iron": 8, "stone": 22}

inv = Inventory(inventory)
inv.add_new_item("iron", 2)
print(inv.curr_inventory)
inv.remove_item("iron", 5)
print(inv.curr_inventory)
print(inv.remove_item("iron", 12))