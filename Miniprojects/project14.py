# Base User class
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# Customer class inheriting from User
class Customer(User):
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address

# Restaurant class
class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu  # dict of item:price

    def show_menu(self):
        print(f"Menu of {self.name}:")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")

# Order class aggregating Restaurant
class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items  # list of item names
        self.total = self.calculate_total()

    def calculate_total(self):
        return sum(self.restaurant.menu[item] for item in self.items)

    def show_order(self):
        print(f"Order by {self.customer.name} from {self.restaurant.name}")
        for item in self.items:
            print(f"- {item}: ₹{self.restaurant.menu[item]}")
        print(f"Total: ₹{self.total}")

# Base Delivery class (polymorphism example)
class Delivery:
    def deliver(self):
        pass

class BikeDelivery(Delivery):
    def deliver(self):
        print("Delivered by bike.")

class DroneDelivery(Delivery):
    def deliver(self):
        print("Delivered by drone.")

# Example usage
menu = {"Burger": 100, "Fries": 50, "Coke": 30}
restaurant = Restaurant("Foodie Hub", menu)
customer = Customer("Alice", "9876543210", "123 Main Street")

restaurant.show_menu()

order = Order(customer, restaurant, ["Burger", "Coke"])
order.show_order()

# Polymorphic delivery
delivery = BikeDelivery()
delivery.deliver()
