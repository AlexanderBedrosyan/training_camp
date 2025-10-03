# Cage
# Атрибути: номер, списък животни, капацитет
# Методи: add_animal(a) (проверка за капацитет), count_animals()
from exercises_hard_tasks4.zoo_management.animal import Animal


class Cage:
    def __init__(self, number:int, capacity:int):
        self.number = number
        self.capacity = capacity
        self.list_of_animals: list[Animal] = []

    def add_animal(self,curr_animal) -> None:
        if not self.is_full():
            self.list_of_animals.append(curr_animal)
        else:
            print("The cage is full")

    def is_full(self) -> bool:
        if len(self.list_of_animals) == self.capacity:
            return True
        return False

    def count_animals(self) -> int:
        return len(self.list_of_animals)
