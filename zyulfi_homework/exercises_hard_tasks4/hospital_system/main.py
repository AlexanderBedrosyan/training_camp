from exercises_hard_tasks4.hospital_system.doctor import Doctor
from exercises_hard_tasks4.hospital_system.hospital import Hospital
from patient import Patient

p1 = Patient("Ivancho")
p2 = Patient("Dragancho")
p3 = Patient("Petkanco")

p1.add_diagnosis("zaples")
p1.add_diagnosis("halcukane")
p2.add_diagnosis("NTR")
p2.add_diagnosis("PERT")
p2.add_diagnosis("STRG")
p3.add_diagnosis("DRTS")
p3.add_diagnosis("TSER")

#print(p1.list_diagnoses())

doc1 = Doctor("Ivanov", "UNG")
doc2 = Doctor("Petkov", "Hirurg")
doc1.add_patient(p1)
doc2.add_patient(p2)
doc2.add_patient(p3)

hos1 = Hospital()
hos1.add_doctors(doc1)
hos1.add_doctors(doc2)

for curr_doct in hos1.list_of_doctors:
    print(curr_doct.name, curr_doct.num_patients())

print(hos1.most_busy_doctor())


