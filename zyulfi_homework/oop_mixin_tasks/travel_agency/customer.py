# Customer (CancelMixin)
# Атрибути: name, private __trips
# Методи: book_trip(trip), list_trips()

from cancel_mixin import CancelMixin
from trip import Trip


class Customer(CancelMixin):
    def __init__(self, name=str):
        self.name = name
        self.__trips: list[Trip] = []

    def book_trip(self, curr_trip=Trip):
        if not curr_trip.is_booked():
            self.__trips.append(curr_trip)
            curr_trip.book()
        else:
            print("The trip is full")

    def list_trips(self):
        return self.__trips

