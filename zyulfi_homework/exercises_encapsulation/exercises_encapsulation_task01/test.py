# Свържи двата чрез нов клас Car(Vehicle, Engine), който стартира двигателя.
from vehicle import Vehicle
from engine import Engine

class Car(Vehicle, Engine):
    def __init__(self, current_type, power):
        Vehicle.__init__(self, current_type)
        Engine.__init__(self, power)



# Примерен вход:
car = Car("sedan", 180)
car.start()          # Starting sedan
print(car.power)     # 180