# ЗАДАЧА 3: Ресторант и поръчки

# История:
# Ресторантът получава множество поръчки, а ти трябва да изчислиш сметките.

# Условие:
# Напиши функция calculate_order(menu, orders),
# която връща речник {маса: обща_сума} и общата сума.
# menu = {"паста":10,"пица":12,"салата":6}
# orders = {"Маса1":{"пица":2,"салата":1},"Маса2":{"паста":3}}
# print(calculate_order(menu, orders))

class Restorant:
    def __init__(self, menu, orders):
        self.menu = menu
        self.orders = orders

    def calculate_order(self):
        orders_dict = {}
        for curr_table, curr_orders in self.orders.items(): # маса, {поръчка}
            sum_orders = 0
            try:
                for curr_product, curr_quantity in curr_orders.items(): # {списък от поръчки}
                    sum_orders += curr_quantity * self.menu[curr_product]
                    orders_dict[curr_table] = sum_orders
            except KeyError:
                print("Error")

        return orders_dict, sum(list(orders_dict.values()))


menu = {"паста":10,"пица":12,"салата":6}
orders = {"Маса1":{"пица":2,"салата":1},"Маса2":{"паста":3}}

r = Restorant(menu, orders)

print(r.calculate_order())

# Очакван изход: ({'Маса1':30, 'Маса2':30}, 60)