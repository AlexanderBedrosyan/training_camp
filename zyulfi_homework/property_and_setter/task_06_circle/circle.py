# Клас Circle с:
# атрибут radius
# @property diameter
# @setter за diameter, който променя радиуса

class Circle:
    def __init__(self, radius=int):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
