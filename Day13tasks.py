
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

# Section 3: Encapsulation (21–25)

# 21. Create a Student class with private attributes _name and _marks. Use getter/setter methods.
class Student:
    def __init__(self, name, marks):
        self._name = name
        self._marks = marks

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Invalid marks")

s = Student("Rahul", 85)
print(s.get_name(), s.get_marks())
s.set_marks(95)
print(s.get_name(), s.get_marks())


# 22. Create a BankAccount class with balance as private variable. Ensure secure access via methods.
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__balance = initial_balance
        self.account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount("123456")
account.deposit(1000)
account.withdraw(300)
print("Balance:", account.get_balance())


# 23. Build a UserProfile class with encapsulated email, phone and provide validation in setters.
class UserProfile:
    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Invalid email")

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if len(phone) == 10 and phone.isdigit():
            self.__phone = phone
        else:
            print("Invalid phone number")

user = UserProfile("test@example.com", "9876543210")
print(user.get_email(), user.get_phone())
user.set_email("new@email.com")
user.set_phone("12345")  # Invalid


# 24. Restrict direct access to salary field in a class Employee, use getters/setters.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

emp = Employee("Priya", 50000)
print(emp.get_salary())
emp.set_salary(60000)
print(emp.get_salary())


# 25. Create a Locker system where the PIN is private and can only be changed via method.
class Locker:
    def __init__(self, pin):
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin and len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN changed successfully")
        else:
            print("PIN change failed")

locker = Locker("1234")
locker.change_pin("1234", "5678")  # success
locker.change_pin("0000", "9999")  # fail
# Section 4: Abstraction (26–30)

from abc import ABC, abstractmethod

# 26. Use abc module to define an abstract class Payment with abstract method pay().
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

payment = CreditCardPayment()
payment.pay(500)


# 27. Create an abstract class Shape with abstract method area() and concrete method describe().
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a shape.")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

sq = Square(4)
sq.describe()
print("Area:", sq.area())


# 28. Implement Animal abstract class with abstract speak() method. Create subclasses Dog, Cat.
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()


# 29. Create a template for Transport with abstract methods like start_engine() and stop_engine().
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Bus(Transport):
    def start_engine(self):
        print("Bus engine started")

    def stop_engine(self):
        print("Bus engine stopped")

bus = Bus()
bus.start_engine()
bus.stop_engine()


# 30. Create a base class Appliance with abstract method power_consumption(). Subclasses: Fridge, WashingMachine.
class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

class Fridge(Appliance):
    def power_consumption(self):
        return "Fridge consumes 150W"

class WashingMachine(Appliance):
    def power_consumption(self):
        return "Washing Machine consumes 500W"

fridge = Fridge()
wm = WashingMachine()
print(fridge.power_consumption())
print(wm.power_consumption())
# ================================
# Tasks 31–35: Polymorphism
# ================================

# Task 31 - Method Overriding
# Demonstrate method overriding with Animal base class and Dog subclass implementing speak().
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

d = Dog()
print("Task 31:", d.speak())


# Task 32 - Duck Typing
# Use polymorphism via duck typing – write a function that calls draw() on different shape objects.
class Circle:
    def draw(self):
        return "Drawing Circle"

class Square:
    def draw(self):
        return "Drawing Square"

def render_shape(shape):
    print("Task 32:", shape.draw())

render_shape(Circle())
render_shape(Square())


# Task 33 - Method Overloading using default arguments
# Simulate method overloading using default arguments in a class Calculator.
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print("Task 33:", calc.add(5), calc.add(5, 10), calc.add(5, 10, 15))


# Task 34 - Method Overloading using *args
# Simulate overloading using *args in a class Sum that can add 2, 3 or n numbers.
class Sum:
    def add(self, *args):
        return sum(args)

s = Sum()
print("Task 34:", s.add(2, 3), s.add(1, 2, 3), s.add(5, 10, 15, 20))


# Task 35 - Polymorphism with Notification subclasses
# Create a class Notification with method send(msg). Use subclasses SMS, Email, PushNotification.
class Notification:
    def send(self, msg):
        raise NotImplementedError

class SMS(Notification):
    def send(self, msg):
        return f"SMS: {msg}"

class Email(Notification):
    def send(self, msg):
        return f"Email: {msg}"

class PushNotification(Notification):
    def send(self, msg):
        return f"Push: {msg}"

notifiers = [SMS(), Email(), PushNotification()]
for n in notifiers:
    print("Task 35:", n.send("Hello"))

# ================================
# Tasks 36–40: Magic (Dunder) Methods
# ================================

# Task 36 - __add__ for Vector
# Override __add__() in a Vector class to allow vector addition using +.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print("Task 36:", v1 + v2)


# Task 37 - __len__ in Playlist
# Override __len__() in a Playlist class to return number of songs.
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["Song1", "Song2", "Song3"])
print("Task 37:", len(p))


# Task 38 - __getitem__ and __setitem__
# Override __getitem__() and __setitem__() in a class that mimics a shopping cart.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, key):
        return self.items.get(key, 0)

    def __setitem__(self, key, value):
        self.items[key] = value

cart = ShoppingCart()
cart["apple"] = 3
cart["banana"] = 2
print("Task 38:", cart["apple"], cart["banana"])


# Task 39 - __contains__ in Inventory
# Override __contains__() in a custom Inventory class to check if item exists.
class Inventory:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

inv = Inventory(["pen", "pencil", "eraser"])
print("Task 39:", "pen" in inv, "marker" in inv)


# Task 40 - Comparison in Money class
# Create a class Money and implement __eq__, __gt__, __lt__ for comparing amounts.
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

m1 = Money(100)
m2 = Money(150)
print("Task 40: Equal?", m1 == m2, "| Greater?", m1 > m2, "| Lesser?", m1 < m2)
# ================================
# Tasks 46–50: Real-World Mini Projects (OOP)
# ================================

# Task 46 - Bank Account System
# Create a BankAccount class with deposit, withdraw, and balance display features.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"{self.owner}'s Balance: ₹{self.balance}")

acc = BankAccount("Priya", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()


# Task 47 - Library Management System
# Create Library and Book classes. Allow borrow/return features and display books.

class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"Borrowed '{title}'")
                return
        print("Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"Returned '{title}'")
                return
        print("Book not found or already returned")

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f" - {book.title} [{status}]")

lib = Library()
lib.add_book("Python 101")
lib.add_book("Data Structures")
lib.display_books()
lib.borrow_book("Python 101")
lib.display_books()
lib.return_book("Python 101")
lib.display_books()


# Task 48 - Student Report Card
# Class Student stores marks for subjects and calculates total/average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # dictionary: subject -> mark

    def total(self):
        return sum(self.marks.values())

    def average(self):
        return self.total() / len(self.marks)

    def show_report(self):
        print(f"Report Card for {self.name}")
        for subject, mark in self.marks.items():
            print(f" - {subject}: {mark}")
        print(f"Total: {self.total()} | Average: {self.average():.2f}")

stud = Student("Arun", {"Math": 90, "Science": 85, "English": 80})
stud.show_report()


# Task 49 - Online Shopping Cart
# Class Product, Cart with add/remove/view/checkout functionality.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
        print(f"Added {product.name}")

    def remove(self, product_name):
        for p in self.items:
            if p.name == product_name:
                self.items.remove(p)
                print(f"Removed {p.name}")
                return
        print("Item not found")

    def view_cart(self):
        print("Cart Contents:")
        for item in self.items:
            print(f" - {item.name}: ₹{item.price}")
        print(f"Total: ₹{self.total_price()}")

    def total_price(self):
        return sum(p.price for p in self.items)

cart = Cart()
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)
cart.add(p1)
cart.add(p2)
cart.view_cart()
cart.remove("Mouse")
cart.view_cart()


# Task 50 - Attendance Tracker
# Create Student and AttendanceTracker classes to record attendance.

class AttendanceTracker:
    def __init__(self):
        self.attendance = {}  # student -> list of present/absent

    def mark_attendance(self, student, status):
        if student not in self.attendance:
            self.attendance[student] = []
        self.attendance[student].append(status)

    def show_attendance(self, student):
        records = self.attendance.get(student, [])
        present_count = records.count("Present")
        total = len(records)
        print(f"{student}'s Attendance: {present_count}/{total} Present")

tracker = AttendanceTracker()
tracker.mark_attendance("Meena", "Present")
tracker.mark_attendance("Meena", "Absent")
tracker.mark_attendance("Meena", "Present")
tracker.show_attendance("Meena")
