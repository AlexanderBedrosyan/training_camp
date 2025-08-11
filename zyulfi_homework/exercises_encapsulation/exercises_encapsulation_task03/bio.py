# Задача 3
# bio.py:
# Клас BioMixin с метод bio() → "{name}, age {age}"

class BioMixin:
    def bio(self):
        return f"{self.name}, age {self.age}"