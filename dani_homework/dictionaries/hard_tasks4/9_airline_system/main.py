from passenger import Passenger
from flight import Flight
from airline import Airline

# Пътници
p1 = Passenger("Ivan")
p2 = Passenger("Maria")
p3 = Passenger("John")

# Полети
f1 = Flight("BG101", 2)
f2 = Flight("BG202", 3)

# Авиокомпания
air = Airline("Bulgaria Air")
air.add_flight(f1)
air.add_flight(f2)

# Резервации
p1.book_ticket(f1)
p2.book_ticket(f1)
p3.book_ticket(f1)  # няма място
p3.book_ticket(f2)

print("\n--- Обобщение ---")
print("Общо пътници:", air.total_passengers())
print("Най-натоварен полет:", air.busiest_flight().code)
