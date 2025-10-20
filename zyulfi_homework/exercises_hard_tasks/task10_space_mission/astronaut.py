# Astronaut: име, private __hours_in_space, метод add_hours(n)

class Astronaut:
    def __init__(self, name, hours_in_space):
        self.name = name
        self.__hours_in_space = hours_in_space

    def add_hours(self, curr_hours):
        if curr_hours > 0:
            self.__hours_in_space += curr_hours
        else:
            print("Hours cannot be less than 0")

    def get_hours(self):
        return self.__hours_in_space