# Professor – добавя списък от предмети,
# метод teach(course), и
# list_courses()

from person import Person

class Professor(Person):
    def __init__(self, name: str, id: str) -> None:

        super().__init__(name, id)
        self._courses: list[str] = []

    def teach(self, course: str) -> None:
        self._courses.append(course)

    def list_courses(self) -> list[str]:
        return self._courses


