# Атрибути: start, end, distance
# Методи:
# __str__() → "Route {start} → {end}, {distance} km"

class Route:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance

    def __str__(self):
        return f"Route {self.start} → {self.end}, {self.distance} km"
