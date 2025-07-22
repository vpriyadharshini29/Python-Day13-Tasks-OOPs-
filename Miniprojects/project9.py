# Class to represent a Gym Member
class Member:
    total_members = 0  # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Member.total_members += 1

    def __str__(self):
        return f"Member: {self.name}, Age: {self.age}"

# Class to represent a Trainer
class Trainer:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"Trainer: {self.name}, Specialty: {self.specialty}"

# Class for managing schedules
class Schedule:
    def __init__(self):
        self.sessions = []

    # Overloaded method to register 1 or many sessions using *args
    def register_sessions(self, *args):
        for session in args:
            self.sessions.append(session)
        print(f"Registered sessions: {', '.join(self.sessions)}")

    def display_schedule(self):
        print("Schedule:")
        for session in self.sessions:
            print(f"- {session}")

# Class to manage subscriptions
class Subscription:
    def __init__(self, member, trainer, schedule):
        self.member = member
        self.trainer = trainer
        self.schedule = schedule

    def details(self):
        print(f"Subscription Details:")
        print(self.member)
        print(self.trainer)
        self.schedule.display_schedule()

# Example usage
m1 = Member("Ravi", 25)
t1 = Trainer("Anita", "Weight Training")

s1 = Schedule()
s1.register_sessions("Monday 7AM", "Wednesday 7AM", "Friday 7AM")

sub1 = Subscription(m1, t1, s1)
sub1.details()

print(f"Total Members: {Member.total_members}")
