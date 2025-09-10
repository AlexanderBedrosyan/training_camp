# Student: име, private __grades (dict: курс → оценка); методи add_grade(), average()
from typing import Dict


class Student:
    def __init__(self, name:str):
        self.name = name
        self.__grades: Dict[str, float] = []
