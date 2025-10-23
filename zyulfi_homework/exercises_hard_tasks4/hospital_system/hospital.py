# Атрибути: списък от доктори
# Методи: total_patients(), most_busy_doctor()
from exercises_hard_tasks4.hospital_system.doctor import Doctor


class Hospital:
    def __init__(self):
        self.list_of_doctors: list[Doctor] = []

    def total_patients(self):
        return sum([curr_doct.num_patients() for curr_doct in self.list_of_doctors])

    def add_doctors(self, curr_doct):
        self.list_of_doctors.append(curr_doct)


    def most_busy_doctor(self):
        busy_doctor = None
        most_patient = 0

        for curr_doct in self.list_of_doctors:
            if curr_doct.num_patients() >= most_patient:
                most_patient = curr_doct.num_patients()
                busy_doctor = curr_doct
        return busy_doctor.name
