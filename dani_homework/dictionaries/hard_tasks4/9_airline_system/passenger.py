# Passenger
# Атрибути: name, private __tickets
# Методи: book_ticket(flight), num_tickets()
from flight import Flight

class Passenger:
    def __init__(self, name: str):
        self.name = name
        self.__tickets = []  # private списък от полети

    def book_ticket(self, flight: Flight):
        # Опитва да резервира билет за даден полет.
        if flight.book_passenger(self):
            self.__tickets.append(flight.code)
            print(f"🎫 {self.name} успешно резервира място за полет {flight.code}")
        else:
            print(f"❌ {self.name} не успя да резервира — полет {flight.code} е пълен.")

    def num_tickets(self) -> int:
        # Връща броя на закупените билети.
        return len(self.__tickets)

    def __str__(self):
        return f"Passenger({self.name}, tickets={self.__tickets})"
