# Задача 2: Банката на бъдещето
# Създай клас FutureBank, който управлява клиенти и техните сметки.
# Всеки клиент има баланс и история на транзакции в речник {тип: сума}.
# Изисквания:
# add_client(name) — добавя клиент.
# transaction(name, types, amount) — записва транзакция и обновява баланса.
# client_balance(name) — връща текущия баланс.
# biggest_spender() — връща клиента с най-много отрицателни транзакции (разходи).


class FutureBank:
    def __init__(self):
        self.bank_dict = {}

    def add_client(self, name):
        if name not in self.bank_dict:
            self.bank_dict[name] = {}
            self.bank_dict[name]["types"] = []
            self.bank_dict[name]["amount"] = 0

    def transaction(self, name, curr_types, curr_amount):
        if name not in self.bank_dict:
            print(f"The {name} is not dict")
        else:
            if curr_types == "deposit":
                self.bank_dict[name]["types"].append(curr_types)
                self.bank_dict[name]["amount"] += curr_amount
            elif curr_types == "withdraw":
                if self.bank_dict[name]["amount"] >= curr_amount:
                    self.bank_dict[name]["types"].append(curr_types)
                    self.bank_dict[name]["amount"] -= curr_amount
                else:
                    print("Error")
            else:
                print("Error")

    def client_balance(self, name):
        return self.bank_dict[name]["amount"]

    def biggest_spender(self):
        return sorted(self.bank_dict.items(), key=lambda x: -x[1]["types"].count("withdraw"))[0][0]


# Тест:
b = FutureBank()
b.add_client("Nikol")
b.transaction("Nikol", "deposit", 2000)
b.transaction("Nikol", "withdraw", 800)
b.transaction("Nikol", "withdraw", 500)
b.add_client("Dragan")
b.transaction("Dragan", "deposit", 1000)
b.transaction("Dragan", "withdraw", 800)
b.transaction("Dragan", "withdraw", 100)
b.transaction("Dragan", "withdraw", 100)

print(b.client_balance("Nikol"))
print(b.bank_dict)
print(b.biggest_spender()) # Nikol