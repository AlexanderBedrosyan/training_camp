# Задача 2: Банков мениджър
# Създай клас Bank, който пази клиенти и баланси.
# Условия:
# Речникът е {име: {"balance": сума, "transactions": []}}
# Метод deposit(name, amount) добавя сума и запис в транзакции.
# Метод withdraw(name, amount) намаля баланса, ако има достатъчно средства.
# Метод richest_client() връща името на най-богатия клиент.


class Bank:
    def __init__(self):
        self.bank_dict = {}

    def deposit(self, name, amount):
        if name not in self.bank_dict:
            self.bank_dict[name] = {
                "balance": amount,
                "transactions": ["deposit"]
            }
        else:
            self.bank_dict[name]["balance"] += amount
            self.bank_dict[name]["transactions"].append("deposit")

    def withdraw(self, name, amount):
        if name in self.bank_dict:
            if self.bank_dict[name]["balance"] >= amount:
                self.bank_dict[name]["balance"] -= amount
                self.bank_dict[name]["transactions"].append("withdraw")
            else:
                print("Insufficient availability")
        else:
            print(f"There is no customer named {name}.")

    def richest_client(self):
        return sorted(self.bank_dict.items(), key=lambda x: -x[1]["balance"])[0][0]


# Тест:
b = Bank()
b.deposit("Maria", 2000)
b.deposit("Ivan", 1000)
b.withdraw("Ivan", 300)
print(b.richest_client())  # Maria