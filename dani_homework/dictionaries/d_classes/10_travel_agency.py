# Създай клас TravelAgency, който следи клиенти и техните пътувания.
# Условия:
# Речник {име: {"trips": [дестинации], "spent": общо_сума}}
# Метод add_trip(name, destination, cost)
# Метод top_traveler() – връща клиента с най-големи разходи.
# Метод unique_destinations() – връща списък с всички различни дестинации.
class TravelAgency:
    def __init__(self):
        # Структура: {име: {"trips": [дестинации], "spent": общо_сума}}
        self.clients = {}

    def add_trip(self, name: str, destination: str, cost: float):
# Добавя пътуване за клиент, създава нов запис ако няма такъв.
        if cost < 0:
            raise ValueError("Цената не може да бъде отрицателна.")

        if name not in self.clients:
            self.clients[name] = {"trips": [], "spent": 0.0}

        self.clients[name]["trips"].append(destination)
        self.clients[name]["spent"] += cost

    def top_traveler(self) -> str:
 # Връща клиента, похарчил най-много пари.
        if not self.clients:
            return None
        return max(self.clients, key=lambda n: self.clients[n]["spent"])

    def unique_destinations(self) -> list:
# Връща списък с всички различни дестинации.
        destinations = set()
        for info in self.clients.values():
            destinations.update(info["trips"])
        return list(destinations)

    def __str__(self):
        return f"TravelAgency({len(self.clients)} clients)"

#Тест:
t = TravelAgency()
t.add_trip("Ivan", "Paris", 1200)
t.add_trip("Maria", "London", 800)
t.add_trip("Ivan", "Rome", 600)
print(t.top_traveler())  # Ivan
print(sorted(t.unique_destinations()))  # ['London', 'Paris', 'Rome']