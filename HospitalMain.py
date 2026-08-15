import Hospital


hospital = Hospital.Hospital("City Hospital", "Alexandria")

doctor1 = Hospital.Doctor("Haneen", "Cardiology")
doctor2 = Hospital.Doctor("Rahaf", "Neurology")

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

patient1 = Hospital.Patient("Ali", 25, "Heart Disease")
patient2 = Hospital.Patient("Salma", 30, "Alzheimer")

hospital.add_patient(patient1)
hospital.add_patient(patient2)

patient1.assign_doctor(doctor1)
doctor1.assign_patient(patient1)

patient2.assign_doctor(doctor2)
doctor2.assign_patient(patient2)

hospital.show_doctors()
hospital.show_patients()

doctor1.show_patients()
doctor2.show_patients()

patient1.show_info()
patient2.show_info()