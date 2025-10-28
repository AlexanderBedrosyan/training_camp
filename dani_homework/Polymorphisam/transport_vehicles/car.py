# Car: връща distance / speed
from  vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, speed):
        self.speed = speed

    def travel_time(self, distance):
        return distance / self.speed