from vending_machine_states import State, NoCoinState
from vending_machine_components import Inventory

class VendingMachine:
     def __init__(self, inventory: Inventory):
        self.inventory = inventory # Composition
        self.state: State = NoCoinState() # Start in the NoCoinState
        self.current_credit = 0.0

     def set_state(self, state: State):
        print(f"** Machine transitioning to {state.__class__.__name__} **")
        self.state = state

     # The machine delegates all actions to its current state object.
     def insert_coin(self, amount: float):
        self.state.insert_coin(self, amount)

     def select_item(self, item_name: str):
        self.state.select_item(self, item_name)

     def refund(self):
          """A new method to handle refunding money."""
          if self.current_credit > 0:
               print(f"Refunding ${self.current_credit:.2f}.")
               self.current_credit = 0.0