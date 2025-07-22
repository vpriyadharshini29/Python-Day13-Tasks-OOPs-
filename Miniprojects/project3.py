# Product class
class Product:
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

# Cart class with dunder methods
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product_id):
        self.items = [p for p in self.items if p.product_id != product_id]

    def __add__(self, other):
        combined = Cart()
        combined.items = self.items + other.items
        return combined

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, product):
        return product in self.items

    def total_price(self):
        return sum(product.price for product in self.items)

    @staticmethod
    def calculate_tax(total, tax_rate=0.18):
        return total * tax_rate

# User class
class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product):
        self.cart.add_product(product)

    def checkout(self):
        total = self.cart.total_price()
        tax = Cart.calculate_tax(total)
        final = total + tax
        return final

# Order class
class Order:
    def __init__(self, user):
        self.user = user
        self.total_amount = user.checkout()

    def display_summary(self):
        print(f"Order Summary for {self.user.name}")
        for i, item in enumerate(self.user.cart.items, 1):
            print(f"{i}. {item}")
        print(f"Total: ₹{self.user.cart.total_price():.2f}")
        print(f"Tax: ₹{Cart.calculate_tax(self.user.cart.total_price()):.2f}")
        print(f"Amount to Pay: ₹{self.total_amount:.2f}")

# Example usage
p1 = Product("Laptop", 50000, 1)
p2 = Product("Mouse", 500, 2)
p3 = Product("Keyboard", 1500, 3)

user1 = User("Shreya")
user1.add_to_cart(p1)
user1.add_to_cart(p2)
user1.add_to_cart(p3)

order1 = Order(user1)
order1.display_summary()
