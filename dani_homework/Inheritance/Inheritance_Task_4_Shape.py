# Hierarchical Inheritance
#
# Създай клас Shape с метод draw(), който принтира "drawing shape...".
# Създай два класа Circle и Square, които наследяват Shape.
# Circle има метод draw_circle(), който принтира "drawing circle...",
# а Square има метод draw_square(), който принтира "drawing square...".
# Създай обект на Circle и на Square и извикай всички подходящи методи.

class Shape:
    def __init__(self, sh_name):
        self.sh_name = sh_name

    def draw(self):
        print(f"{self.sh_name} drawing shape...")


class Circle(Shape):
    def __init__(self, c_name):
        super().__init__(c_name)  # get from Shape
        self.c_name = c_name

    def draw_circle(self):
        print(f"{self.c_name} drawing circle...")


class Square(Shape):
    def __init__(self, sq_name):
        super().__init__(sq_name)  # get from Shape
        self.sq_name = sq_name

    def draw_square(self):
        print(f"{self.sq_name} drawing square...")


# objects
circle_i = Circle("The Circle")
square_n = Square("The Square")

# test
circle_i.draw()         # от Shape
circle_i.draw_circle()  # от Circle
print()
square_n.draw()         # от Shape
square_n.draw_square()  # от Square
