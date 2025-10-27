# История: Фирма анализира месечните си приходи и разходи.
# Условие: Напиши функция profit_report(finances), която връща
# {месец: печалба} и най-печелившия месец.

def profit_report(finances):
    profits = {}
    best_month = None
    best_profit = float('-inf')

    for month, report in finances.items():
        profit = report["приходи"] - report["разходи"]
        profits[month] = profit

        if profit > best_profit:
            best_profit = profit
            best_month = month

    return profits, best_month

data = {"Януари":{"приходи":2000,"разходи":2200},
        "Февруари":{"приходи":2500,"разходи":2600},
        "Март":{"приходи":3000,"разходи":3500}
        }
print(profit_report(data))

# Очакван изход: ({'Януари':500,'Февруари':-100,'Март':1000}, 'Март')