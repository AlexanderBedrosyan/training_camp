# Имаме речник с продукти и техните цени:
# products = {"bread": 1.2, "milk": 2.0, "cheese": 5.5, "apples": 3.3}
# Изисквания:
# Изведи продуктите, сортирани по цена (възходящо).
# Покажи само тези, чиято цена е над 2.0.
# Създай нов речник само с тези продукти, които имат цена над 2.0.
products = {"bread": 1.2, "milk": 2.0, "cheese": 5.5, "apples": 3.3}

sorted_products = dict(sorted(products.items(), key=lambda x: x[1]))

print("Продукти с цена над 2.0:")
for name, price in sorted_products.items():
    if price > 2.0:
        print(f"{name}: {price:.2f}")

# нов речник за продукти (цена > 2.0)
expensive_products = {name: price for name, price in products.items() if price > 2.0}

print("\nНов речник с по-скъпи продукти:")
print(expensive_products)