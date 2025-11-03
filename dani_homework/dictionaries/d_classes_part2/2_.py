# Задача 2: Банката на бъдещето
# Създай клас FutureBank, който управлява клиенти и техните сметки.
# Всеки клиент има баланс и история на транзакции в речник {тип: сума}.
# Изисквания:
# add_client(name) — добавя клиент.
# transaction(name, type, amount) — записва транзакция и обновява баланса.
# client_balance(name) — връща текущия баланс.
# biggest_spender() — връща клиента с най-много отрицателни транзакции (разходи).

class FutureBank:                       # който управлява клиенти и техните сметки.
    def __init__(self):                 # Всеки клиент има баланс и история на транзакции в речник {тип: сума}.
        self.dict_clients = {}          #{"Mmimi": {"balance": 700, "history": {"deposit": 2000, "withdraw": 1300}}}}

    def add_client(self, name):                 # добавя клиент
        if name not in self.dict_clients:
            self.dict_clients[name] = {"balance": 0, "history": {}}

    def transaction(self, name, type, amount): # записва транзакция и обновява баланса
        if name not in self.dict_clients:
            print(f" The client {name} is not exist.")
            return

        client = self.dict_clients[name]

        if type not in client['history']:
            client["history"][type] = 0
        client["history"][type] += amount    # добавяме към историята транзакция

        if type == "deposite":
            client["balance"] += amount
        elif type == "withdraw":
            client["balance"] -= amount
        else:
            print(f"The transaction is not valid: {type}")


    def client_balance(self, name):            # връща текущия баланс
        if name not in self.dict_clients:
            print(f"The client {name} is not exist.")
            return
        return self.dict_clients[name]["balance"]

    def biggest_spender(self):                 # връща клиента с най-много отрицателни транзакции (разходи)
        if not self.dict_clients:
            return None
        return max(self.dict_clients, key=lambda  name: self.dict_clients[name]["history"].get("withdraw", 0))

    def __repr__(self):
        return f"FutureBank ({len(self.dict_clients)} клиенти)"
# Тест:
b = FutureBank()
b.add_client("Nikol")
b.transaction("Nikol", "deposit", 2000)
b.transaction("Nikol", "withdraw", 800)
b.transaction("Nikol", "withdraw", 500)
print(b.biggest_spender()) # Nikol

