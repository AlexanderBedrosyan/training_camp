# Атрибути: private __trips
# Методи: add_trip(), available_trips(), find_trip(destination)
from trip import Trip


class Agency:
    def __init__(self):
        self.__trips: list[Trip] = []

    def add_trip(self, curr_trip=Trip) -> None:
        self.__trips.append(curr_trip)

    def available_trips(self) -> list:
        list_of_available = []
        for curr_trip in self.__trips:
            if not curr_trip.is_booked():
                list_of_available.append(curr_trip)
        return list_of_available

    def find_trip(self, destination):
        for curr_trip in self.__trips:
            if destination == curr_trip.destination:
                print(curr_trip.destination)


