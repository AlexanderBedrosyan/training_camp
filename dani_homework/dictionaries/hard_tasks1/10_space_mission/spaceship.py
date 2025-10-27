# Spaceship: име, капацитет, метод can_carry(count)
class Spaceship:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

    def can_carry(self, count: int) -> bool:
        # Проверява дали корабът може да побере даден брой астронавти.
        return count <= self.capacity

    def __str__(self):
        return f"Spaceship({self.name}, capacity={self.capacity})"
