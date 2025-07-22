# Supplier class with encapsulated data
class Supplier:
    def __init__(self, name, contact):
        self.__name = name
        self.__contact = contact

    def get_info(self):
        return f"Supplier: {self.__name}, Contact: {self.__contact}"

# Item class
class Item:
    def __init__(self, name, price, quantity, supplier):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def __str__(self):
        return f"{self.name} - ₹{self.price} x {self.quantity}"

# Inventory class
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item
        print(f"Added {item.name} to inventory.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Removed {item_name} from inventory.")
        else:
            print(f"Item {item_name} not found.")

    def update_quantity(self, item_name, qty):
        if item_name in self.items:
            self.items[item_name].quantity = qty
            print(f"Updated {item_name} quantity to {qty}.")
        else:
            print(f"{item_name} not found.")

    def __contains__(self, item_name):
        return item_name in self.items

    def __getitem__(self, item_name):
        return self.items.get(item_name, "Item not found.")

    def display_inventory(self):
        print("Inventory List:")
        for item in self.items.values():
            print(item)

# Example usage
supplier1 = Supplier("ABC Distributors", "9876543210")
item1 = Item("Pen", 10, 100, supplier1)
item2 = Item("Notebook", 50, 200, supplier1)

inv = Inventory()
inv.add_item(item1)
inv.add_item(item2)
inv.display_inventory()

print("\nUpdate & Access:")
inv.update_quantity("Pen", 150)
print(inv["Pen"])

print("\nCheck Existence:")
print("Pencil" in inv)
print("Notebook" in inv)

print("\nSupplier Info:")
print(item1.supplier.get_info())
