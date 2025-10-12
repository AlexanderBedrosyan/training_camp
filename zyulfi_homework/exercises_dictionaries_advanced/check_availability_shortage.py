# Задача 14: Проверка на наличности (недостиг)
# Условие:
# check_stock(stock, items) проверява дали stock покрива items (и количествата).
# Връща списък на недостигащи артикули.

def check_stock(stock, items):
    new_dict = []
    for product, quantity in stock.items(): # мляко, 10; хляб, 5
        try:
            if quantity < items[product]:
                new_dict.append(product)
        except KeyError:
            print("Mising product")
        # if product in items:
        #     quantity_in_items = items[product]
        #     if quantity_in_items > quantity:
        #         new_dict.append(product)
    return new_dict

print(check_stock({"мляко":10,"хляб":5}, {"мляко":8,"хляб":6}))
# Очакван изход:
# ['хляб']