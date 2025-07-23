# Multiple Inheritance

# Създай клас Mother с метод cook(), който принтира "cooking...".
# Създай клас Father с метод work(), който принтира "working...".
# Създай клас Child, който наследява и двата класа и има метод play(), който принтира "playing...".
# Създай обект на Child и извикай трите метода.

class Mother:
    def __init__(self, m_name):
        self.m_name = m_name

    def cook(self):
        print(f"{self.m_name} cooking...")

class Father:
    def __init__(self, f_name):
        self.f_name = f_name

    def work(self):
        print(f"{self.f_name} working...")

class Child(Mother, Father):
    def __init__(self, c_name):

        Mother.__init__(self, c_name)
        Father.__init__(self, c_name)
        self.c_name = c_name

    def play(self):
        print(f"{self.c_name} playing...")

# obcject child
child_i = Child("Yory")
child_i.cook()   # от Mother
child_i.work()   # от Father
child_i.play()   # от Child