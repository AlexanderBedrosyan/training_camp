# ЗАДАЧА 7: Пътуваща агенция
# ---------------------------------------------------------------
# История:
# Туристическа агенция има оферти за различни дестинации.
# Трябва да изчислиш стойността на всяко пътуване и най-скъпото.
#
# trips = {"Рим":500,"Париж":700,"Атина":400} bookings = {"Иван":{"дестинация":"Париж","хора":2},"Мария":{"дестинация":"Рим","хора":1}} print(calculate_trips(trips, bookings))
#
# Очакван изход: ({'Иван':1400,'Мария':500}, 'Иван')

class TravelAgency:
    def __init__(self, trips, bookings):
        self.trips = trips
        self.bookings = bookings

    def calculate_trips(self):
        trips_dict = {}
        for name, curr_trip in self.bookings.items():
            try:
                destination = curr_trip["дестинация"]
                people = curr_trip["хора"]
                total_ex = people * self.trips[destination]
                trips_dict[name] = total_ex
            except KeyError:
                continue
        return trips_dict

    def expensive(self):
        return list(sorted(self.calculate_trips().items(), key=lambda item: -item[1]))[0][0]

    def finale_result(self):
        return self.calculate_trips(), self.expensive()


trips = {"Рим":500,"Париж":700,"Атина":400}
bookings = {"Иван":{"дестинация":"Париж","хора":2},"Мария":{"дестинация":"Рим","хора":1}}

# Очакван изход: ({'Иван':1400,'Мария':500}, 'Иван')

travel = TravelAgency(trips, bookings)
print(travel.finale_result())
# print(calculate_trips(trips, bookings))