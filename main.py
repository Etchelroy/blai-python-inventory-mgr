class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, quantity, price):
        if name in self.inventory:
            raise ValueError(f"Item '{name}' already exists.")
        self.inventory[name] = {"quantity": quantity, "price": price}

    def remove_item(self, name):
        if name not in self.inventory:
            raise KeyError(f"Item '{name}' not found.")
        del self.inventory[name]

    def update_quantity(self, name, quantity):
        if name not in self.inventory:
            raise KeyError(f"Item '{name}' not found.")
        self.inventory[name]["quantity"] = quantity
        if quantity < 5:
            print(f"WARNING: Low stock for '{name}' — only {quantity} left!")

    def get_total_value(self):
        return sum(v["quantity"] * v["price"] for v in self.inventory.values())


if __name__ == "__main__":
    mgr = InventoryManager()

    print("=== Adding items ===")
    mgr.add_item("Apple", 50, 0.30)
    mgr.add_item("Banana", 20, 0.15)
    mgr.add_item("Cherry", 6, 1.20)
    print("Added: Apple (50 @ $0.30), Banana (20 @ $0.15), Cherry (6 @ $1.20)")

    print("\n=== Duplicate add (expect error) ===")
    try:
        mgr.add_item("Apple", 10, 0.25)
    except ValueError as e:
        print(f"Error caught: {e}")

    print("\n=== Total inventory value ===")
    print(f"Total value: ${mgr.get_total_value():.2f}")

    print("\n=== Updating quantities ===")
    mgr.update_quantity("Apple", 3)
    mgr.update_quantity("Banana", 4)
    mgr.update_quantity("Cherry", 10)

    print("\n=== Total value after updates ===")
    print(f"Total value: ${mgr.get_total_value():.2f}")

    print("\n=== Removing an item ===")
    mgr.remove_item("Banana")
    print("Removed: Banana")
    print(f"Total value after removal: ${mgr.get_total_value():.2f}")

    print("\n=== Remove non-existent item (expect error) ===")
    try:
        mgr.remove_item("Mango")
    except KeyError as e:
        print(f"Error caught: {e}")