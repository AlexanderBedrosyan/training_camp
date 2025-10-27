# Doctor
# Атрибути: name, specialty, private __patients
# Методи: add_patient(patient), num_patients()
from patient import Patient

class Doctor:
    def __init__(self, name: str, specialty: str):
        self.name = name
        self.specialty = specialty
        self.__patients = []  # private списък от пациенти

    def add_patient(self, patient: Patient):
        # Добавя пациент към списъка на доктора.
        self.__patients.append(patient)

    def num_patients(self) -> int:
        # Връща броя на пациентите на доктора.
        return len(self.__patients)

    def get_patients(self):
        # Връща копие на списъка с пациенти.
        return list(self.__patients)

    def __str__(self):
        return f"Doctor({self.name}, {self.specialty}, {len(self.__patients)} patients)"
