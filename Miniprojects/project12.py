# Base class Device
class Device:
    def __init__(self, name):
        self.name = name
        self.status = False  # Off by default

    def operate(self):
        raise NotImplementedError("Subclasses should implement this method.")

# Light class inherits Device
class Light(Device):
    def operate(self):
        self.status = not self.status
        print(f"Light '{self.name}' turned {'ON' if self.status else 'OFF'}.")

# AC class inherits Device
class AC(Device):
    def operate(self):
        self.status = not self.status
        print(f"AC '{self.name}' turned {'ON' if self.status else 'OFF'}.")

# Fan class inherits Device
class Fan(Device):
    def operate(self):
        self.status = not self.status
        print(f"Fan '{self.name}' turned {'ON' if self.status else 'OFF'}.")

# SmartHub class (composition)
class SmartHub:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"Device '{device.name}' added to SmartHub.")

    def control_all(self):
        for device in self.devices:
            device.operate()

# Example usage
hub = SmartHub()

light1 = Light("Living Room Light")
ac1 = AC("Bedroom AC")
fan1 = Fan("Kitchen Fan")

hub.add_device(light1)
hub.add_device(ac1)
hub.add_device(fan1)

print("\nActivating all devices:")
hub.control_all()

print("\nToggling all devices again:")
hub.control_all()
