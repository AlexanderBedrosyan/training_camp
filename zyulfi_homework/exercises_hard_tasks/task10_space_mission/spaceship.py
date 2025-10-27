# Spaceship: име, капацитет, метод can_carry(count)

class Spaceship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def can_carry(self, count) -> bool:
        if count > self.capacity:
            return True
        return False
