# История:
# Фирма анализира месечните си приходи и разходи.
# Условие:
# Напиши функция profit_report(finances), която връща
# {месец: печалба} и най-печелившия месец.
# Очакван изход: ({'Януари':500,'Февруари':-100,'Март':1000}, 'Март')

def profit_report(finances):
    profits = {}
    best_month = None
    max_profit = float('-inf')

    for month, data in finances.items():
        # data = {'приходи': ..., 'разходи': ...}
        profit = data['приходи'] - data['разходи']
        profits[month] = profit

        if profit > max_profit:
            max_profit = profit
            best_month = month

    return profits, best_month

# Пример
finances = {
    'Януари': {'приходи': 1500, 'разходи': 1000},
    'Февруари': {'приходи': 900, 'разходи': 1000},
    'Март': {'приходи': 2000, 'разходи': 1000}
}

result = profit_report(finances)
print(result)
