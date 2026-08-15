class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def show_doctors(self):
        print("Doctors:")
        for doctor in self.doctors:
            print("Name:", doctor.name, ", Specialty:", doctor.specialty)

    def show_patients(self):
        print("Patients:")
        for patient in self.patients:
            print("Name:", patient.name, ", Illness:", patient.illness)


class Doctor(Hospital):
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.patients = []

    def assign_patient(self, patient):
        self.patients.append(patient)

    def show_patients(self):
        print("Patients under Dr.", self.name, ":")
        if len(self.patients) == 0:
            print("No patients assigned.")
        else:
            for patient in self.patients:
                print(patient.name)


class Patient(Hospital):
    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness
        self.doctor = None

    def assign_doctor(self, doctor):
        self.doctor = doctor

    def show_info(self):
        print("Patient Information")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Illness:", self.illness)

        if self.doctor:
            print("Assigned Doctor: Dr.", self.doctor.name)
        else:
            print("Assigned Doctor: None")