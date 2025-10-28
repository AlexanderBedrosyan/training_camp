# История:Потребители имат криптовалути.
# Трябва да изчислиш стойността на всеки портфейл.
# def portfolio_value(users):
# totals = {u: sum(q*p for q,p in vals.values()) for u, vals in users.items()}
# best = max(totals, key=totals.get) return totals, best
# users = { "Иван": {"BTC":(0.1,60000),"ETH":(2,2000)}, "Мария": {"BTC":(0.05,60000),"DOGE":(1000,0.08)} } print(portfolio_value(users))
# # Очакван изход: ({'Иван':10000,'Мария':7000}, 'Иван')

# class CryptoWallet:
#     def __init__(self, portfolio, prices):

def portfolio_value(users_details):
    wallet_values = {}

    for name, curr_portfolio in users_details.items():
        cur_value = 0
        for value in curr_portfolio.values():
            qw = value[0]
            price = value[1]
            cur_value += qw * price

        wallet_values[name] = cur_value

    return wallet_values, list(sorted(wallet_values.items(), key=lambda x: x[1], reverse=True))[0][0]



users = {
    "Иван": {"BTC":(0.1,60000),"ETH":(2,2000)},
    "Мария": {"BTC":(0.05,60000),"DOGE":(1000,0.08)}
}
print(portfolio_value(users))