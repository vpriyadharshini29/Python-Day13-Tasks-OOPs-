# Task: Register attendees, assign sessions, use @classmethod to view total attendees

# Attendee class
class Attendee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Session class
class Session:
    def __init__(self, title, speaker, time):
        self.title = title
        self.speaker = speaker
        self.time = time

# Event class
class Event:
    def __init__(self, name):
        self.name = name
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

# Registration class with class variable to track total registrations
class Registration:
    total_attendees = 0

    def __init__(self, attendee, event):
        self.attendee = attendee
        self.event = event
        self.assigned_sessions = []
        Registration.total_attendees += 1

    def assign_session(self, session):
        self.assigned_sessions.append(session)

    @classmethod
    def get_total_attendees(cls):
        return cls.total_attendees

    def display_registration(self):
        print(f"\nAttendee: {self.attendee.name} ({self.attendee.email})")
        print(f"Event: {self.event.name}")
        print("Sessions:")
        for s in self.assigned_sessions:
            print(f" - {s.title} by {s.speaker} at {s.time}")

# Example usage
event = Event("AI Conference 2025")
session1 = Session("AI & Ethics", "Dr. Smith", "10:00 AM")
session2 = Session("Machine Learning Basics", "Prof. Kumar", "12:00 PM")
event.add_session(session1)
event.add_session(session2)

attendee1 = Attendee("Alice", "alice@example.com")
attendee2 = Attendee("Bob", "bob@example.com")

reg1 = Registration(attendee1, event)
reg1.assign_session(session1)

reg2 = Registration(attendee2, event)
reg2.assign_session(session1)
reg2.assign_session(session2)

reg1.display_registration()
reg2.display_registration()

print(f"\nTotal Attendees Registered: {Registration.get_total_attendees()}")
