# Клас person с:
# private атрибут __height
# @property и @setter за height, който не приема отрицателни стойности

class Person:
    def __init__(self, height=int):
        self.__height = height

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Cannot be less than 0")
        self.__height = value
