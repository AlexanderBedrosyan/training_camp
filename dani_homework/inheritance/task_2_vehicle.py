# Multilevel inheritance

# Създай клас Vehicle с метод move(), който принтира "moving...".
# Създай клас Car, който наследява Vehicle и има метод drive(), който принтира "driving...".
# Създай клас SportsCar, който наследява Car и има метод race(), който принтира "racing...".
# Създай обект на SportsCar и извикай трите метода.

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moving...")

class Car(Vehicle):
    def drive(self):
        print(f"{self.name} driving...")

class SportsCar(Car):
    def race(self):
        print(f"{self.name} racing...")

# Създаване на обект и тестване
sport_car_1 = SportsCar("Ferrari")
sport_car_1.move()   # от Vehicle
sport_car_1.drive()  # от Car
sport_car_1.race()   # от SportsCar