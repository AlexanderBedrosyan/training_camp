# Passenger
# Атрибути: name, private __tickets
# Методи: book_ticket(flight), num_tickets()

class Passenger:
    def __init__(self, name=str):
        self.name = name
        self.__tickets = []

    def book_ticket(self, flight) -> None:
        self.__tickets.append(flight)

    def num_tickets(self) -> int:
        return len(self.__tickets)

    def get_tickets(self) -> list:
        return self.__tickets
