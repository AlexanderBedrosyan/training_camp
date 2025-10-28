# Astronaut: име, private __hours_in_space, метод add_hours(n)

class Astronaut:
    def __init__(self, name: str, hours_in_space: int):
        self.name = name
        self.__hours_in_space = hours_in_space  # private

    def add_hours(self, n: int):
        # Добавя летателни часове към астронавта.
        if n > 0:
            self.__hours_in_space += n

    def get_hours_in_space(self) -> int:
        # Връща общия брой часове в космоса.
        return self.__hours_in_space

    def __str__(self):
        return f"Astronaut({self.name}, {self.__hours_in_space}h)"
