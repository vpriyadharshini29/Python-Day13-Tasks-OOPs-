# Movie class
class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.seats = [Seat(i) for i in range(1, 11)]  # 10 seats per movie

    @staticmethod
    def check_seat_availability(seats):
        return [seat for seat in seats if not seat.booked]

    def display_available_seats(self):
        available = Movie.check_seat_availability(self.seats)
        print(f"Available Seats for '{self.title}': {[seat.number for seat in available]}")

# Seat class
class Seat:
    def __init__(self, number):
        self.number = number
        self.booked = False

    def book(self):
        if not self.booked:
            self.booked = True
            return True
        return False

# Ticket class
class Ticket:
    def __init__(self, movie, seat, user):
        self.movie = movie
        self.seat = seat
        self.user = user

    def __str__(self):
        return f"Ticket: {self.user.name} - '{self.movie.title}' - Seat {self.seat.number}"

# User class
class User:
    def __init__(self, name):
        self.name = name

    def book_ticket(self, movie, seat_number):
        if 1 <= seat_number <= len(movie.seats):
            seat = movie.seats[seat_number - 1]
            if seat.book():
                ticket = Ticket(movie, seat, self)
                print("Booking Successful!")
                print(ticket)
            else:
                print("Seat already booked.")
        else:
            print("Invalid seat number.")

# Example usage
movie = Movie("Interstellar", "2h 49min")
user = User("Arjun")

movie.display_available_seats()
user.book_ticket(movie, 3)  # Booking seat 3
user.book_ticket(movie, 3)  # Trying to book same seat again

movie.display_available_seats()
