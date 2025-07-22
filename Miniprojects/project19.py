# Task: Enroll students, assign instructors, use submit() method differently for types of assignments

# Instructor class
class Instructor:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

# Student class
class Student:
    def __init__(self, name):
        self.name = name
        self.assignments = []

    def submit_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"{self.name} submitted: {assignment.submit()}")

# Base Assignment class (demonstrating polymorphism)
class Assignment:
    def __init__(self, title):
        self.title = title

    def submit(self):
        return f"Assignment '{self.title}' submitted."

# WrittenAssignment subclass
class WrittenAssignment(Assignment):
    def submit(self):
        return f"Written assignment '{self.title}' uploaded as PDF."

# QuizAssignment subclass
class QuizAssignment(Assignment):
    def submit(self):
        return f"Quiz '{self.title}' completed online."

# Course class
class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def show_course_info(self):
        print(f"\nCourse: {self.course_name}")
        print(f"Instructor: {self.instructor.name} ({self.instructor.expertise})")
        print("Enrolled Students:", ", ".join([s.name for s in self.students]))

# Example usage
instructor = Instructor("Dr. Meera", "Data Science")
course = Course("Intro to Python", instructor)

student1 = Student("John")
student2 = Student("Priya")

course.enroll_student(student1)
course.enroll_student(student2)

assignment1 = WrittenAssignment("Python Basics Essay")
assignment2 = QuizAssignment("Week 1 Quiz")

student1.submit_assignment(assignment1)
student2.submit_assignment(assignment2)

course.show_course_info()
