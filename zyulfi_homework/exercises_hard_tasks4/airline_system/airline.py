# Airline
# Атрибути: списък полети
# Методи: total_passengers(), busiest_flight()
from flight import Flight

class AirLine:
    def __init__(self):
        self.list_of_flight: list[Flight] = []

    def add_flight(self, curr_flight):
        self.list_of_flight.append(curr_flight)

    def total_passengers(self):
        return sum([curr_flight.amount_passenger() for curr_flight in self.list_of_flight])

    def busiest_flight(self):
        full_capacity = 0
        bus_flight = None
        for curr_flight in self.list_of_flight:
           if curr_flight.amount_passenger() >= full_capacity:
               full_capacity = curr_flight.capacity
               bus_flight = curr_flight
        return bus_flight

