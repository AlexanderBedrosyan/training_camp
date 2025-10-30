# Задача 2: Банков мениджър
# Създай клас Bank, който пази клиенти и баланси.
# Условия:
# Речникът е {име: {"balance": сума, "transactions": []}}
# Метод deposit(name, amount) добавя сума и запис в транзакции.
# Метод withdraw(name, amount) намаля баланса, ако има достатъчно средства.
# Метод richest_client() връща името на най-богатия клиент.

class Bank:
    def __init__(self):
        self.dict_client_balance = {}

    def deposit(self, name, amount):
        if name not in self.dict_client_balance:
            self.dict_client_balance[name] = {
                "balance": amount,
                "transactions": ["deposit"]
            }
        else:
            self.dict_client_balance[name]["balance"] += amount
            self.dict_client_balance[name]["transactions"].append("deposit")

    def withdraw(self, curr_name, amount):
        if curr_name not in self.dict_client_balance:
            return

        if self.dict_client_balance[curr_name]["balance"] < amount:
            return

        self.dict_client_balance[curr_name]["balance"] -= amount
        self.dict_client_balance[curr_name]["transactions"].append("withdraw")

    def richest_client(self):
        return sorted(self.dict_client_balance.items(), key=lambda x: -x[1]["balance"])[0][0]


# Тест:
b = Bank()
b.deposit("Maria", 2000)
b.deposit("Ivan", 1000)
b.withdraw("Ivan", 300)
print(b.richest_client())  # Maria
