# OOP Inventory Merger using Operator Overloading

class Inventory:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        merged = self.items.copy()

        for item, quantity in other.items.items():
            if item in merged:
                merged[item] += quantity
            else:
                merged[item] = quantity

        return Inventory(merged)

    def display(self):
        for item, quantity in self.items.items():
            print(item, ":", quantity)

n1 = int(input("Enter number of items in Inventory 1: "))
inventory1 = {}

for i in range(n1):
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory1[item] = quantity

n2 = int(input("\nEnter number of items in Inventory 2: "))
inventory2 = {}

for i in range(n2):
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory2[item] = quantity

inv1 = Inventory(inventory1)
inv2 = Inventory(inventory2)

merged_inventory = inv1 + inv2

print("\nMerged Inventory:")
merged_inventory.display()