class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

# The Inventory class manages the stock.
# This follows SRP, separating inventory logic from the main machine.
class Inventory:
    def __init__(self):
        self._stock = {}

    def add_item(self, item: Item, quantity: int):
        print(f"Stocking {quantity} units of {item.name}.")
        self._stock[item.name] = {"item": item, "quantity": quantity}

    def get_item(self, item_name: str) -> Item | None:
        return self._stock.get(item_name, {}).get("item")

    def get_quantity(self, item_name: str) -> int:
        return self._stock.get(item_name, {}).get("quantity", 0)

    def dispense_item(self, item_name: str):
        if self.get_quantity(item_name) > 0:
            self._stock[item_name]["quantity"] -= 1
            print(f"Dispensed one {item_name}.")
            return True
        print(f"ERROR: {item_name} is sold out.")
        return False
          
     
