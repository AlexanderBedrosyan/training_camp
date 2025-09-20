# Route
# Атрибути: start, end, distance

class Route:
    def __init__(self, start:str, end:str, distance:int or float):
        self.start = start
        self.end = end
        self.distance = distance

    def routе_distance(self) -> int or float:
        return self.distance

    def __str__(self):
        return f"Start point {self.start}, end point {self.end}, all distance {self.distance} km"

#test
r1=Route("Sofia", "Varna", 110)
print(r1.__str__())
