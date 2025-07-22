from abc import ABC, abstractmethod

# Abstract User class
class User(ABC):
    def __init__(self, username):
        self._username = username  # Encapsulated attribute

    @abstractmethod
    def show_dashboard(self):
        pass

# Admin subclass
class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.exams = []

    def create_exam(self, title):
        exam = Exam(title)
        self.exams.append(exam)
        print(f"Exam '{title}' created.")
        return exam

    def show_dashboard(self):
        print(f"Admin: {self._username}")
        print("Exams Created:")
        for exam in self.exams:
            print(f"- {exam.title}")

# Student subclass
class Student(User):
    def __init__(self, username):
        super().__init__(username)
        self.scores = {}

    def take_exam(self, exam):
        print(f"{self._username} is taking exam: {exam.title}")
        score = 0
        for q in exam.questions:
            print(f"Q: {q.text}")
            for i, opt in enumerate(q.options):
                print(f"  {i + 1}. {opt}")
            ans = int(input("Enter choice (1-4): "))
            if q.check_answer(ans - 1):
                score += 1
        self.scores[exam.title] = score
        print(f"Score: {score}/{len(exam.questions)}")

    def show_dashboard(self):
        print(f"Student: {self._username}")
        print("Exam Results:")
        for exam, score in self.scores.items():
            print(f"- {exam}: {score}")

# Question class with private correct answer
class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.__correct_index = correct_index  # Private

    def check_answer(self, index):
        return index == self.__correct_index

# Exam class containing questions
class Exam:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

# Example usage
admin = Admin("admin1")
exam1 = admin.create_exam("Python Basics")

q1 = Question("What is the output of print(2**3)?", ["5", "6", "8", "9"], 2)
q2 = Question("Which keyword is used for function?", ["fun", "def", "define", "function"], 1)

exam1.add_question(q1)
exam1.add_question(q2)

student = Student("Shan")
# To simulate actual exam, uncomment below:
# student.take_exam(exam1)
student.show_dashboard()
