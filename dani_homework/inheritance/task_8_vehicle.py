# Mixins (за по-напреднали) Създай клас Vehicle с атрибут position.
# Създай миксин клас RadioMixin с метод play_radio(station),
# който принтира "Playing {station}".
# Създай клас Car, който наследява Vehicle и използва RadioMixin.
# Създай обект и извикай метода за радио.


class Vehicle:
    def __init__(self, position):
        self.position = position

class RadioMixin:
    def play_radio(self, station):
        print(f"Playing {station}")

class Car(Vehicle, RadioMixin):
    pass

# Тест
my_car = Car("Downtown")
my_car.play_radio("Jazz FM")
