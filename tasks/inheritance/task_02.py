# ✅ Задача 2 – Multilevel Inheritance Създай клас Vehicle с метод move(), който принтира "moving...". Създай клас Car,
# който наследява Vehicle и има метод drive(), който принтира "driving...". Създай клас SportsCar, който наследява Car и
# има метод race(), който принтира "racing...". Създай обект на SportsCar и извикай трите метода.

class Vehicle:

    def move(self):
        print("moving...")

class Car(Vehicle):
    def drive(self):
        print("driving...")

class SportsCar(Car):
    def race(self):
        print("racing...")

sport_car = SportsCar()
sport_car.move()
sport_car.drive()
sport_car.race()