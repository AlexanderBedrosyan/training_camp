# Клас Rectangle с:
# атрибути width и height
# @property area (само за четене)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return  self.width * self.height

