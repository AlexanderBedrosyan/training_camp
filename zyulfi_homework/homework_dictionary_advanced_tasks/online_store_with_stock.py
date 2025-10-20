# Задача 6: Онлайн магазин с наличности
# stock = {"T-shirt": 10, "Shoes": 3, "Hat": 7, "Socks": 15}
# prices = {"T-shirt": 25, "Shoes": 60, "Hat": 15, "Socks": 5}
# Изисквания:
#
# Намери стойността на наличностите (цена × количество).
# Изведи общата стойност на склада.
# Сортирай артикулите по стойност.

def total_value(curr_stock, curr_prices):
    total_dict = {}
    for key_stock, value_stock in curr_stock.items():
        total_dict[key_stock] = value_stock * curr_prices[key_stock]
    return total_dict

def total_sum(curr_stock, curr_prices):
    return sum(total_value(curr_stock, curr_prices).values())

def sorted_item(curr_stock, curr_prices):
    return dict(sorted(total_value(curr_stock, curr_prices).items(), key=lambda item: item[1]))

stock = {"T-shirt": 10, "Shoes": 3, "Hat": 7, "Socks": 15}
prices = {"T-shirt": 25, "Shoes": 60, "Hat": 15, "Socks": 5}

print(total_value(stock, prices))
print(total_sum(stock, prices))
print(sorted_item(stock, prices))