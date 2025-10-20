# Атрибути: name, specialty, private __patients
# Методи: add_patient(patient), num_patients()
from exercises_hard_tasks4.hospital_system.patient import Patient


class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.__patients: list[Patient] = []

    def add_patient(self, curr_patient) -> None:
        self.__patients.append(curr_patient)

    def num_patients(self) -> int:
        return len(self.__patients)