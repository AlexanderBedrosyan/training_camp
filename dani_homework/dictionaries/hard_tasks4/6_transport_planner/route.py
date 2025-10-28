# Route Атрибути: start, end, distance
# Метод: __str__()

class Route:
    def __init__(self, start:str, end:str, distance: float):
        self.start = start
        self.end = end
        self.distance = distance

    def __str__(self):
        return f"The start is {self.start}, the end is {self.end}, distance is {self.distance} km."