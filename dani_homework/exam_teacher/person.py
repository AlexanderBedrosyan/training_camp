class Person:
    school_name = "High School #1"

    def __init__(self, name: str)-> None:
        self._name: str = name

    def get_info(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError("Name cannot be an empty string")
        self._name = value