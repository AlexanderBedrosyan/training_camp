# Airline Атрибути: списък полети
# Методи: total_passengers(), busiest_flight()
from flight import Flight

class Airline:
    def __init__(self, name: str):
        self.name = name
        self.flights = []

    def add_flight(self, flight: Flight):
        # Добавя полет към авиокомпанията.
        self.flights.append(flight)

    def total_passengers(self) -> int:
        # Връща общия брой на пътниците във всички полети.
        return sum(f.num_passengers() for f in self.flights)

    def busiest_flight(self) -> Flight:
        # Намира полета с най-много пътници.
        if not self.flights:
            return None
        return max(self.flights, key=lambda f: f.num_passengers())

    def __str__(self):
        return f"Airline({self.name}, {len(self.flights)} flights)"
