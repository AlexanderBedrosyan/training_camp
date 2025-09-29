# Vehicle (SpeedMixin)
# Атрибути: model, private __speed
# Методи: travel_time(route)
from oop_mixin_tasks.transport_network.route import Route
from oop_mixin_tasks.transport_network.speed_mixin import SpeedMixin

class Vehicle(SpeedMixin):
    def __init__(self, model=str, speed=float):
        self.model = model
        self.__speed = speed

    def travel_time(self, route=object):
        return SpeedMixin().time(route.distance, self.__speed)


