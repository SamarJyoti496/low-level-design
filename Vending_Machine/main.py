from vending_machine import VendingMachine
from vending_machine_components import Inventory, Item

inventory = Inventory()
inventory.add_item(Item("Coke", 1.50), 5)
inventory.add_item(Item("Chips", 1.00), 10)
inventory.add_item(Item("Candy", 0.75), 0) # Sold out item

vm = VendingMachine(inventory)

print("\n--- TEST CASE 1: Successful Purchase ---")
vm.insert_coin(1.00)
vm.insert_coin(0.50)
vm.select_item("Coke")

print("\n--- TEST CASE 2: Select without paying ---")
vm.select_item("Chips")

print("\n--- TEST CASE 3: Insufficient Funds ---")
vm.insert_coin(0.50)
vm.select_item("Chips")

print("\n--- TEST CASE 4: Item Sold Out ---")
vm.insert_coin(1.00)
vm.select_item("Candy")

inventory.add_item(Item("Candy", 0.75), 1)
vm.insert_coin(1.00)
vm.select_item("Candy")