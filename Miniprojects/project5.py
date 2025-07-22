from abc import ABC, abstractmethod

# Abstract base class
class Person(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass

# Doctor class inherits Person
class Doctor(Person):
    def __init__(self, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self.specialization = specialization

    def get_role(self):
        return "Doctor"

# Patient class inherits Person
class Patient(Person):
    def __init__(self, name, age, gender, symptoms):
        super().__init__(name, age, gender)
        self.symptoms = symptoms

    def get_role(self):
        return "Patient"

# Appointment class aggregates Doctor and Patient
class Appointment:
    def __init__(self, doctor, patient, date, time):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def display_details(self):
        print(f"Appointment on {self.date} at {self.time}")
        print(f"Doctor: Dr. {self.doctor.name} ({self.doctor.specialization})")
        print(f"Patient: {self.patient.name} (Symptoms: {self.patient.symptoms})")

# Prescription class
class Prescription:
    def __init__(self, patient, doctor, medicines):
        self.patient = patient
        self.doctor = doctor
        self.medicines = medicines

    def show_prescription(self):
        print(f"Prescription for {self.patient.name}:")
        for med in self.medicines:
            print(f" - {med}")
        print(f"Prescribed by Dr. {self.doctor.name}")

# Example Usage
doc = Doctor("Meera", 40, "Female", "Cardiology")
pat = Patient("Raj", 55, "Male", "Chest Pain")

appt = Appointment(doc, pat, "2025-07-25", "10:30 AM")
appt.display_details()

pres = Prescription(pat, doc, ["Aspirin", "Blood Pressure Tablet"])
pres.show_prescription()
