from person import Person


class Student(Person):
    def __init__(self, name:str, age:int):
        super().__init__(name, age)
        self.list_of_grades: list = []

    def average_grade_of_st(self):
        if len(self.list_of_grades) == 0:
            raise ValueError("Error")

        return sum([grade for grade in self.list_of_grades]) / len(self.list_of_grades)
