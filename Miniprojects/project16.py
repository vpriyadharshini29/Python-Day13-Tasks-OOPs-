# Passenger class
class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Seat class
class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.booked = False
        self.passenger = None

# Bus class (contains Seats → Composition)
class Bus:
    def __init__(self, bus_number, total_seats):
        self.bus_number = bus_number
        self.seats = [Seat(i + 1) for i in range(total_seats)]

    def check_availability(self):
        return [seat for seat in self.seats if not seat.booked]

    def book_seat(self, passenger):
        available = self.check_availability()
        if available:
            seat = available[0]
            seat.booked = True
            seat.passenger = passenger
            return Booking(self.bus_number, seat, passenger)
        else:
            return None

# Booking class
class Booking:
    def __init__(self, bus_number, seat, passenger):
        self.bus_number = bus_number
        self.seat = seat
        self.passenger = passenger

    def __eq__(self, other):
        return (self.bus_number == other.bus_number and
                self.seat.seat_number == other.seat.seat_number and
                self.passenger.name == other.passenger.name)

    def __str__(self):
        return (f"Booking Confirmed:\nPassenger: {self.passenger.name}, Age: {self.passenger.age}\n"
                f"Bus No: {self.bus_number}, Seat No: {self.seat.seat_number}")

# Example usage
bus = Bus("KA-09-1234", 3)

p1 = Passenger("Alice", 28)
p2 = Passenger("Bob", 30)

booking1 = bus.book_seat(p1)
booking2 = bus.book_seat(p2)

if booking1:
    print(booking1)
if booking2:
    print("\n", booking2)

# Comparing bookings
print("\nBooking1 == Booking2?", booking1 == booking2)
