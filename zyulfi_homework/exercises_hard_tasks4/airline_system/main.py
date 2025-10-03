from airline import AirLine
from flight import Flight
from passenger import Passenger

p1 = Passenger("Zyulfi")
p2 = Passenger("Gugov")
p3 = Passenger("Ivanov")
a1 = AirLine()
f1 = Flight("Sofia", 10)
f2 = Flight("Plovdiv", 10)
f1.book_passenger(p1)
f1.book_passenger(p2)
f2.book_passenger(p1)
f2.book_passenger(p2)
f1.book_passenger(p3)

print(f1.is_full())
print(f2.is_full())

a1.add_flight(f1)
a1.add_flight(f2)
print(a1.busiest_flight().code)