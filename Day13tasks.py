
# ========================================
# Section 1: Classes and Objects (1–10)
# ========================================

# 1. Car class with attributes and instantiation
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"{self.brand} {self.model} costs ${self.price}")

car1 = Car("Toyota", "Camry", 25000)
car2 = Car("Honda", "Civic", 22000)
car1.display()
car2.display()

# 2. BankAccount with deposit, withdraw, check balance
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance

# 3. Student class with name, age, grade via constructor
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# 4. Circle class with area and circumference
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# 5. Book class with display_info()
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Book: {self.title} by {self.author}")

# 6. Laptop class with class variable
class Laptop:
    warranty_period = "1 year"

    def __init__(self, brand):
        self.brand = brand

# 7. Movie class tracks total instances
class Movie:
    total_movies = 0

    def __init__(self, title):
        self.title = title
        Movie.total_movies += 1

# 8. Product class: instance vs class variable
class Product:
    category = "General"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

# 9. __str__ method in Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee {self.name}, Salary: {self.salary}"

# 10. Compare two Rectangle objects using __eq__
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

# ========================================
# Section 2: Inheritance (11–20)
# ========================================

# 11. Vehicle base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass

# 12. Use super() in constructor
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# 13. Shape → Square, Triangle with overridden area()
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# 14. Multi-level inheritance: Person → Employee → Manager
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

# 15. Multiple Inheritance: Father + Mother → Child
class Father:
    def skills(self):
        return ["Driving", "Fishing"]

class Mother:
    def skills(self):
        return ["Cooking", "Painting"]

class Child(Father, Mother):
    pass

# 16. Teacher Hierarchy
class Teacher:
    def teach(self):
        print("Teaching...")

class MathTeacher(Teacher):
    pass

class ScienceTeacher(Teacher):
    pass

# 17. isinstance() usage
s = Student("Alice", 14, "9th")
print(isinstance(s, Student))  # True

# 18. issubclass() usage
print(issubclass(Manager, Person))  # True

# 19. E-commerce product hierarchy
class Product:
    def __init__(self, name):
        self.name = name

class ElectronicProduct(Product):
    def __init__(self, name, warranty):
        super().__init__(name)
        self.warranty = warranty

class MobilePhone(ElectronicProduct):
    def __init__(self, name, warranty, os):
        super().__init__(name, warranty)
        self.os = os

# 20. MRO demonstration
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  # MRO resolves to B
