# ShapeManager: държи списък от фигури,
# метод total_area() и largest_shape()

class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

    # def largest_shape(self):
    #     if not self.shapes:
    #         return None
    #     return max(self.shapes, key=lambda s: s.area() )

    def largest_shape(self):
        if not self.shapes:
            return None

        largest = self.shapes[0]  # приемаме, че първата е най-голяма
        for shape in self.shapes[1:]:  # обхождаме останалите
            if shape.area() > largest.area():
                largest = shape
        return largest
