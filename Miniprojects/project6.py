from abc import ABC, abstractmethod

# Base Vehicle class
class Vehicle(ABC):
    def __init__(self, brand, model, rate_per_day):
        self.brand = brand
        self.model = model
        self.rate_per_day = rate_per_day

    @abstractmethod
    def calculate_rent(self, days):
        pass

# Subclass Bike
class Bike(Vehicle):
    def calculate_rent(self, days):
        return self.rate_per_day * days

# Subclass Car
class Car(Vehicle):
    def calculate_rent(self, days):
        # Extra insurance fee added
        return (self.rate_per_day * days) + 500

# Customer class
class Customer:
    def __init__(self, name, license_no):
        self.name = name
        self.license_no = license_no

# Rental system to handle vehicle bookings
class Rental:
    tax_rate = 0.18  # Class variable

    def __init__(self, customer, vehicle, days):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days

    def generate_bill(self):
        base_rent = self.vehicle.calculate_rent(self.days)
        tax = Rental.calculate_tax(base_rent)
        total = base_rent + tax
        print(f"Customer: {self.customer.name}")
        print(f"Vehicle: {self.vehicle.brand} {self.vehicle.model}")
        print(f"Days: {self.days}")
        print(f"Base Rent: ₹{base_rent}")
        print(f"Tax: ₹{tax}")
        print(f"Total Amount: ₹{total}")

    @staticmethod
    def calculate_tax(amount):
        return amount * Rental.tax_rate

# Example Usage
cust = Customer("Arjun", "DL-98765")
vehicle = Car("Toyota", "Innova", 2000)

rental = Rental(cust, vehicle, 3)
rental.generate_bill()
