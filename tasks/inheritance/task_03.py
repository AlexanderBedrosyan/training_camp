# ✅ Задача 3 – Multiple Inheritance Създай клас Mother с метод cook(), който принтира "cooking...". Създай клас Father
# с метод work(), който принтира "working...". Създай клас Child, който наследява и двата класа и има метод play(),
# който принтира "playing...". Създай обект на Child и извикай трите метода.

class Mother:
    def cook(self):
        print("cooking...")

class Father:
    def work(self):
        print("working...")

class Child(Mother, Father):
    def play(self):
        print("playing...")

current_child = Child()
current_child.cook()
current_child.work()
current_child.play()