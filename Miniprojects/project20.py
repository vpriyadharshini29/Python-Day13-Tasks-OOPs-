# Task: Generate tracking ID, link sender/receiver, validate ID

import random

# Sender class
class Sender:
    def __init__(self, name, address):
        self.name = name
        self.address = address

# Receiver class
class Receiver:
    def __init__(self, name, address):
        self.name = name
        self.address = address

# Tracking utility class
class Tracking:
    @staticmethod
    def generate_tracking_id():
        return "TRK" + str(random.randint(10000, 99999))

    @staticmethod
    def validate_tracking_id(tracking_id):
        return tracking_id.startswith("TRK") and tracking_id[3:].isdigit()

# Parcel class using composition
class Parcel:
    def __init__(self, sender, receiver, weight):
        self.sender = sender
        self.receiver = receiver
        self.weight = weight
        self.tracking_id = Tracking.generate_tracking_id()

    def display_info(self):
        print(f"\nTracking ID: {self.tracking_id}")
        print(f"From: {self.sender.name}, Address: {self.sender.address}")
        print(f"To: {self.receiver.name}, Address: {self.receiver.address}")
        print(f"Weight: {self.weight}kg")

# Example usage
sender = Sender("Alice", "123 Sender Street")
receiver = Receiver("Bob", "789 Receiver Avenue")

parcel = Parcel(sender, receiver, 2.5)
parcel.display_info()

# Validate tracking ID
is_valid = Tracking.validate_tracking_id(parcel.tracking_id)
print("Valid Tracking ID?" , "Yes" if is_valid else "No")
