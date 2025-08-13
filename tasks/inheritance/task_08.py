# ✅ Задача 8 – Mixins (за по-напреднали) Създай клас Vehicle с атрибут vehicle_type. Създай миксин клас RadioMixin с метод
# play_radio(station), който принтира "Playing {station}". Създай клас Car, който наследява Vehicle и използва
# RadioMixin. Създай обект и извикай метода за радио.

class Vehicle:

    def __init__(self, vehicle_type, diesel):
        self.vehicle_type = vehicle_type
        self.diesel = diesel

class RadioMixin:
    def play_radio(self, station):
        print(f"Playing {station}")

class ChargerMixin:
    def is_need_charge(self):
        if self.diesel < 10:
            print("Need to add more diesel!")
        else:
            print("Diesel is enough!")

    def add_diesel(self, diesel):
        self.diesel += diesel

    def divide_diesel(self, diesel):
        if self.diesel - diesel > 0:
            self.diesel -= diesel
        else:
            print("Diesel is not enough!")


class Car(Vehicle, RadioMixin, ChargerMixin):
    pass

class Truck(Vehicle, RadioMixin, ChargerMixin):
    pass

car = Car("Trabant", 20)
car.play_radio("Veselina")
car.is_need_charge()
car.divide_diesel(50)
car.add_diesel(50)
print(car.diesel)
