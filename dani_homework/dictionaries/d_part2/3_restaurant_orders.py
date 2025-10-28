# История:
# Ресторантът получава множество поръчки, а ти трябва да изчислиш сметките.
# Условие:
# Напиши функция calculate_order(menu, orders),
# която връща речник {маса: обща_сума} и общата сума.
#Очакван изход: ({'Маса1':30, 'Маса2':30}, 60)

def calculate_order(menu, orders):
    table_totals = {}
    grand_total = 0

    for table, items in orders.items():
        total = 0
        for item, qty in items.items():
            if item in menu:  # ако го има в менюто
                total += menu[item] * qty
        table_totals[table] = total
        grand_total += total

    return table_totals, grand_total

# --- Пример за използване ---
menu = {'салата': 10,'пица': 20,'вода': 2}

orders = {
    'Маса1': {'салата': 1, 'пица': 1},
    'Маса2': {'пица': 1, 'вода': 5}
}

result = calculate_order(menu, orders)
print(result)
