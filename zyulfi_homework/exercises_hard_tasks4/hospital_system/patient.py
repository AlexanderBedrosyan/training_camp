# Атрибути: name, private __diagnoses
# Методи: add_diagnosis(diagnosis), list_diagnoses()

class Patient:
    def __init__(self, name=str):
        self.name = name
        self.__diagnoses = []

    def add_diagnosis(self, curr_diagnosis):
        self.__diagnoses.append(curr_diagnosis)

    def list_diagnoses(self):
        return self.__diagnoses