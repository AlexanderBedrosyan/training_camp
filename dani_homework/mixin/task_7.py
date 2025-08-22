# Създай клас person с атрибут name и
# клас SpeakerMixin, с метод speak() връщащ "Speaking...".
# Направи клас Teacher, който наследява и от двата, и тествай speak().
# ------------------------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

class SpeakerMixin:
    def speak(self):
        return "Speaking..."

class Teacher(Person, SpeakerMixin):
    def __init__(self, name):
        super().__init__(name)  # Викаме person

teacher = Teacher("Mr. Gochev")
print(f"{teacher.name} {teacher.speak()}")
