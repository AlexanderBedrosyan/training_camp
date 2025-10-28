# Hospital
# Атрибути: списък от доктори
# Методи: total_patients(), most_busy_doctor()
from doctor import Doctor

class Hospital:
    def __init__(self, name: str):
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor: Doctor):
        # Добавя доктор в болницата.
        self.doctors.append(doctor)

    def total_patients(self) -> int:
        # Връща общия брой пациенти в болницата.
        return sum(d.num_patients() for d in self.doctors)

    def most_busy_doctor(self) -> Doctor:
        # Връща доктора с най-много пациенти.
        if not self.doctors:
            return None
        return max(self.doctors, key=lambda d: d.num_patients())

    def __str__(self):
        return f"Hospital({self.name}, doctors={len(self.doctors)})"
