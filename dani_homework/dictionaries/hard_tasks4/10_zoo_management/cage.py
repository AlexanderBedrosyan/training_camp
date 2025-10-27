# Cage
# Атрибути: номер, списък животни, капацитет
# Методи: add_animal(a) (проверка за капацитет), count_animals()
from animal import Animal


class Cage:
    def __init__(self, number:int, animals, capacity:int):
        self.number = number
        self.animals: list[Animal] = []
        self.capacity = capacity

    def add_animal(self, current_animal:Animal):
        if len(self.animals) < self.capacity:
            self.animals.append(current_animal)
        else:
            raise ValueError(f" The cage {self.number} is full")

    def count_animals(self) -> int:
        return len(self.animals)

    def __str__(self):
        animals_str = ", ".join(str(a) for a in self.animals) if self.animals else "Not animals"
        return f"The cage {self.number} (capacity {self.capacity}): {animals_str}"

c=Cage(325, [], 15 )
a1=Animal("Tiger", 'BigCat')
a2=Animal("Tiger1", 'BigCat')
print(a1)

c.add_animal(a1)
c.add_animal(a2)

print(c.count_animals())

