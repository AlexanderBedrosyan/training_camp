from patient import Patient
from doctor import Doctor
from hospital import Hospital

# Пациенти
p1 = Patient("Ivan Petrov")
p1.add_diagnosis("Flu")
p1.add_diagnosis("Cough")

p2 = Patient("Maria Dimitrova")
p2.add_diagnosis("Allergy")

p3 = Patient("Georgi Ivanov")
p3.add_diagnosis("Fracture")

# Доктори
d1 = Doctor("Dr. Stoyanov", "Therapist")
d2 = Doctor("Dr. Petrova", "Orthopedic")

d1.add_patient(p1)
d1.add_patient(p2)
d2.add_patient(p3)

# Болница
hospital = Hospital("City Hospital")
hospital.add_doctor(d1)
hospital.add_doctor(d2)

# Извеждане
print("Общо пациенти в болницата:", hospital.total_patients())
print("Най-натоварен доктор:", hospital.most_busy_doctor().name)
print("Пациенти на Dr. Stoyanov:", [p.name for p in d1.get_patients()])
