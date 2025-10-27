# Patient
# Атрибути: name, private __diagnoses
# Методи: add_diagnosis(diagnosis), list_diagnoses()

class Patient:
    def __init__(self, name: str):
        self.name = name
        self.__diagnoses = []  # private списък с диагнози

    def add_diagnosis(self, diagnosis: str):
        # Добавя диагноза към пациента.
        self.__diagnoses.append(diagnosis)

    def list_diagnoses(self):
        # Връща списък с всички диагнози.
        return list(self.__diagnoses)

    def __str__(self):
        return f"Patient({self.name}, diagnoses={self.__diagnoses})"