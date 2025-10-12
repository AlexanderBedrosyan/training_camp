# Задача 7: Изчисляване на сметка за покупки
# Условие:
# Функция calculate_bill(store, purchases) приема store = {артикул: цена} и purchases = [(артикул, количество), ...].
# Връща крайна сума (round 2).

# [("ябълки",2),("портокали",1)]))

def calculate_bill(store, purchases):
    purchases_dict = {}
    for i in range(len(purchases)):
        purchases_dict[purchases[i][0]] = purchases[i][1]

    total_dict = {}

    for key, value in purchases_dict.items():
        if key in store:
            total_dict[key] = value
        else:
            print(f"The product {key} you are looking for does not exist.")

    for key, value in store.items():
        if key in total_dict:
            total_dict[key] *= value

    return sum(total_dict.values())


store = {"ябълки":3.5, "банани":2.8, "портокали":4.0}

print(calculate_bill(store, [("ябълки",2),("портокали",1), ("череши", 2), ("банани",2)]))

# Очакван изход:
# 11.0

store = {"ябълки": 3.5, "банани": 2.8, "портокали": 4.0}
print(calculate_bill(store, [("ябълки", 2), ("портокали", 1), ("череши", 2), ("банани", 2)]))
# Очакван изход:
# 11.0




# Втори вариант
# Задача 7: Изчисляване на сметка за покупки
# Условие:
# Функция calculate_bill(store, purchases) приема store = {артикул: цена} и purchases = [(артикул, количество), ...].
# Връща крайна сума (round 2).
# [("ябълки",2),("портокали",1)]))
def calculate_bill(store, purchases):
    total_value = 0
    for purchase in purchases:
        product = purchase[0]
        quantity = purchase[1]
        try:
            total_value += (quantity * store[product])
        except KeyError:
            print(f"{product} product is missing in market list")
    return total_value
    # total_dict = {}
    #
    # for key, value in purchases_dict.items():
    #     if key in store:
    #         total_dict[key] = value
    #     else:
    #         print(f"The product {key} you are looking for does not exist.")
    #
    # for key, value in store.items():
    #     if key in total_dict:
    #         total_dict[key] *= value
    # return sum(total_dict.values())

store = {"ябълки": 3.5, "банани": 2.8, "портокали": 4.0}
print(calculate_bill(store, [("ябълки", 2), ("портокали", 1), ("череши", 2), ("банани", 2)]))
# Очакван изход:
# 11.0

