# Base Person class
class Person:
    def __init__(self, name, age):
        self._name = name  # Encapsulated
        self._age = age

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

# Department class (aggregated in Student)
class Department:
    def __init__(self, dept_name, hod):
        self.dept_name = dept_name
        self.hod = hod

    def __str__(self):
        return f"Department: {self.dept_name}, HOD: {self.hod}"

# Student class inherits Person and aggregates Department
class Student(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)  # Call parent constructor
        self.department = department

    def display(self):
        print(self.get_info())
        print(self.department)

# AdmissionForm class for collecting and verifying details
class AdmissionForm:
    def __init__(self):
        self._verified = False

    def verify_documents(self):
        self._verified = True
        print("Documents Verified")

    def is_verified(self):
        return self._verified

# Example usage
form = AdmissionForm()
form.verify_documents()

if form.is_verified():
    dept = Department("Computer Science", "Dr. Sharma")
    student = Student("Sneha", 19, dept)
    print("\nAdmission Successful!")
    student.display()
else:
    print("Admission Denied: Documents not verified.")
