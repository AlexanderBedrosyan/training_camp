# Задача 10: Туристическа агенция
# Създай клас TravelAgency, който следи клиенти и техните пътувания.
# Условия:
# Речник {име: {"trips": [дестинации], "spent": общо_сума}}
# Метод add_trip(name, destination, cost)
# Метод top_traveler() – връща клиента с най-големи разходи.
# Метод unique_destinations() – връща списък с всички различни дестинации.


class TravelAgency:
    def __init__(self):
        self.travel_dict = {}

    def add_trip(self, name, destination, cost):
        if name not in self.travel_dict:
            self.travel_dict[name] = {
                "trips": [],
                "spent": 0
            }
        self.travel_dict[name]["trips"].append(destination)
        self.travel_dict[name]["spent"] += cost

    def top_traveler(self):
        return sorted(self.travel_dict.items(), key=lambda x: -x[1]["spent"])[0][0]

    def unique_destinations(self):
        list_of_destinations = []
        for curr_name, curr_trips in self.travel_dict.items():
            list_of_destinations += curr_trips["trips"]
            # for element in curr_trips["trips"]:
            #     if element not in list_of_destinations:
            #         list_of_destinations.append(element)
        return sorted(list(set(list_of_destinations)))


# {име: {"trips": [дестинации], "spent": общо_сума}}
# Тест:
t = TravelAgency()
t.add_trip("Ivan", "Paris", 1200)
t.add_trip("Maria", "London", 800)
t.add_trip("Maria", "Rome", 800)
t.add_trip("Ivan", "Rome", 600)
print(t.top_traveler())  # Ivan
print((t.unique_destinations()))  # ['London', 'Paris', 'Rome']
t.unique_destinations()
print(t.travel_dict)