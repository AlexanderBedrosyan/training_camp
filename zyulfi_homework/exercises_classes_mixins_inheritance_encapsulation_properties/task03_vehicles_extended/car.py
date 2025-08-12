# Car има private атрибут __brand и метод info()
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, max_speed, brand):
        super().__init__(max_speed)
        self.brand = brand

    def info(self):
        return super().describe()