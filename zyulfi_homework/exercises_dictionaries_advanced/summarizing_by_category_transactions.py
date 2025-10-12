# Задача 11: Сумиране по категории (транзакции)
# Условие:
# sum_by_category(transactions) приема списък от речници {"категория":..., "сума":...}
# и връща агрегиране {категория: обща сума}.

def sum_by_category(curr_transactions):
    new_dict = {}
    for element in curr_transactions:
        product = list(element.values())[0]
        price = list(element.values())[1]
        if product not in new_dict:
            new_dict[product] = 0
        new_dict[product] += price
    return new_dict


transactions = [
  {"категория":"храна","сума":12},
  {"категория":"транспорт","сума":8},
  {"категория":"храна","сума":20}
]
print(sum_by_category(transactions))
# Очакван изход:
# {'храна': 32, 'транспорт': 8}
