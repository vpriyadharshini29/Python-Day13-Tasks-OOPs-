# Menu item class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Order class contains list of MenuItems
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def calculate_total(self):
        return sum(item.price for item in self.items)

# Bill class with class variable for tax rate
class Bill:
    tax_rate = 0.05  # 5% GST

    def __init__(self, order):
        self.order = order

    def generate(self):
        subtotal = self.order.calculate_total()
        tax = self.calculate_tax(subtotal)
        total = subtotal + tax
        return subtotal, tax, total

    @staticmethod
    def calculate_tax(amount):
        return amount * Bill.tax_rate

# Customer class composes an Order
class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def place_order(self, menu_items):
        for item in menu_items:
            self.order.add_item(item)

    def print_bill(self):
        bill = Bill(self.order)
        subtotal, tax, total = bill.generate()
        print(f"Customer: {self.name}")
        print("Items Ordered:")
        for item in self.order.items:
            print(f"- {item.name}: ₹{item.price}")
        print(f"Subtotal: ₹{subtotal}")
        print(f"Tax: ₹{tax}")
        print(f"Total: ₹{total}")

# Example usage
menu1 = MenuItem("Paneer Butter Masala", 200)
menu2 = MenuItem("Naan", 40)
menu3 = MenuItem("Lassi", 60)

customer = Customer("Priya")
customer.place_order([menu1, menu2, menu3])
customer.print_bill()
