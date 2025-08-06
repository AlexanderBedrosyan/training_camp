# Клас BioMixin с метод bio() → "{name}, age {age}"
# Създай Student(Person, BioMixin)


class BioMixin
    def bio(self):
        return f"{self.name}, age {self.age}"
