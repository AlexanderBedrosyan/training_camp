# базов клас Person
# Person: protected атрибут _name

# атрибут _name, метод get_info().
#•	Добави property name в Person, забраняващо празни низове:
# Ако за name е подадено празно място, то да връща грешка:
# „Name cannot be an empty string”
# o	Ако не е празно място, то да си закача атрибута.


class Person:
    school_name = "High School #1"

    def __init__(self, name):
        self._name = name

    def get_info(self):
        return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            print("Name cannot be an empty string")
        else:
            self._name = value
