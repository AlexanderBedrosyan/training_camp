# История:
# Потребители имат криптовалути. Трябва да изчислиш стойността на всеки портфейл.
# Очакван изход: ({'Иван':10000,'Мария':7000}, 'Иван')

def crypto_wallets(portfolios, prices):
    wallet_values = {}
    richest = None
    max_value = 0

    for name, wallet in portfolios.items():
        # wallet = {'BTC': колко, 'ETH': колко, ...}
        total = 0
        for coin, amount in wallet.items():
            if coin in prices:
                total += amount * prices[coin]
        wallet_values[name] = total

        if total > max_value:
            max_value = total
            richest = name

    return wallet_values, richest


# --- Пример за използване ---
portfolios = {
    'Иван': {'BTC': 0.2, 'ETH': 3},
    'Мария': {'BTC': 0.1, 'ETH': 2}
}

prices = {'BTC': 40000, 'ETH': 1000}
print(crypto_wallets(portfolios, prices))

