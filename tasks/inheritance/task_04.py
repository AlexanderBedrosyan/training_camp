# ✅ Задача 4 – Hierarchical Inheritance Създай клас Shape с метод draw(), който принтира "drawing shape...". Създай два
# класа Circle и Square, които наследяват Shape. Circle има метод draw_circle(), който принтира "drawing circle...", а
# Square има метод draw_square(), който принтира "drawing square...". Създай обект на Circle и на Square и извикай
# всички подходящи методи.

class Shape:
    def draw(self):
        print("drawing shape...")

class Circle(Shape):
    def draw_circle(self):
        print("drawing circle...")

class Square(Shape):
    def draw_square(self):
        print("drawing square...")

circle = Circle()
square = Square()

circle.draw()
circle.draw_circle()

square.draw()
square.draw_square()