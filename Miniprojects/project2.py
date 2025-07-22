# Base class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Derived class: Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.__grades = {}

    def add_grade(self, subject_name, grade):
        self.__grades[subject_name] = grade

    def get_grades(self):
        return self.__grades

# Derived class: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def update_marks(self, student, grade):
        student.add_grade(self.subject, grade)

# Subject class
class Subject:
    def __init__(self, name, max_marks):
        self.name = name
        self.max_marks = max_marks

# ReportCard class
class ReportCard:
    def __init__(self, student):
        self.student = student

    def generate_report(self):
        grades = self.student.get_grades()
        print(f"\nReport Card for {self.student.name} (ID: {self.student.student_id})")
        print("-" * 40)
        total = 0
        count = 0
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")
            total += grade
            count += 1
        average = total / count if count else 0
        print("-" * 40)
        print(f"Average Grade: {average:.2f}")
        self._determine_grade_type(average)

    # Polymorphism to handle different grading systems
    def _determine_grade_type(self, avg):
        if avg >= 90:
            print("Grade: A+ (Excellent)")
        elif avg >= 75:
            print("Grade: A (Very Good)")
        elif avg >= 60:
            print("Grade: B (Good)")
        elif avg >= 40:
            print("Grade: C (Needs Improvement)")
        else:
            print("Grade: F (Fail)")

# Example usage
student1 = Student("Alice", 14, "S101")
teacher1 = Teacher("Mr. Smith", 35, "Math")
teacher2 = Teacher("Mrs. Rose", 32, "Science")

teacher1.update_marks(student1, 88)
teacher2.update_marks(student1, 92)

report = ReportCard(student1)
report.generate_report()
