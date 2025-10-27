# Задача 1: Сортиране на продукти по цена
# Имаме речник с продукти и техните цени:
# products = {"bread": 1.2, "milk": 2.0, "cheese": 5.5, "apples": 3.3}
#
# Изисквания:
# Изведи продуктите, сортирани по цена (възходящо).
# Покажи само тези, чиято цена е над 2.0.
# Създай нов речник само с тези продукти, които имат цена над 2.0.

products = {"bread": 1.2, "milk": 2.0, "cheese": 5.5, "apples": 3.3}

def sorted_dict(curr_dict):
    return dict(sorted(curr_dict.items(), key=lambda item: item[1]))

def output_by_value(curr_dict, curr_value):
    new_dict = {}
    for key, value in curr_dict.items():
        if value > curr_value:
            new_dict[key] = value
    return new_dict


print(sorted_dict(products))
print(output_by_value(products, 2))





