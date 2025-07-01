from abc import ABC, abstractmethod

# Forward declaration to resolve circular dependency
class VendingMachine:
    pass

class State(ABC):
    @abstractmethod
    def insert_coin(self, machine: VendingMachine, amount: float):
        pass

    @abstractmethod
    def select_item(self, machine: VendingMachine, item_name: str):
        pass

    @abstractmethod
    def dispense_item(self, machine: VendingMachine, item_name: str):
        pass
    
    @abstractmethod
    def press_cancel_button(self, machine: VendingMachine):
        pass

class NoCoinState(State):
     def insert_coin(self, machine: VendingMachine, amount: float):
        machine.current_credit += amount
        print(f"Inserted ${amount:.2f}. Total credit: ${machine.current_credit:.2f}")
        # Transition to the HasCoinState
        machine.set_state(HasCoinState())

     def select_item(self, machine: VendingMachine, item_name: str):
        print("ERROR: Please insert a coin first.")

     def dispense_item(self, machine: VendingMachine, item_name: str):
        print("ERROR: Cannot dispense without payment.")
     
     def press_cancel_button(self, machine: VendingMachine):
        print("ERROR: Cannot cancel, item is already being dispensed.")

class HasCoinState(State):
     def insert_coin(self, machine: VendingMachine, amount: float):
        machine.current_credit += amount
        print(f"Inserted ${amount:.2f}. Total credit: ${machine.current_credit:.2f}")

     def select_item(self, machine: VendingMachine, item_name: str):
        item = machine.inventory.get_item(item_name)
        if not item:
            print("ERROR: Invalid item selected.")
            # We should also refund here if the user can't proceed
            machine.refund()
            machine.set_state(NoCoinState())
            return

        if machine.inventory.get_quantity(item_name) == 0:
            print(f"ERROR: {item_name} is sold out.")
            machine.refund()
            machine.set_state(NoCoinState()) # Transition back to start
            return

        if machine.current_credit < item.price:
            print(f"ERROR: Insufficient credit. {item.name} costs ${item.price:.2f}")
            # The user might want to add more money, so we don't refund yet.
            return

        # Transition to the DispensingState
        machine.set_state(DispensingState())
        machine.state.dispense_item(machine, item_name)

     def dispense_item(self, machine: VendingMachine, item_name: str):
        print("ERROR: Please select an item first.")

     def press_cancel_button(self, machine: VendingMachine):
        print("Purchase cancelled.")
        machine.refund()
        machine.set_state(NoCoinState())

class DispensingState(State):
     def insert_coin(self, machine: VendingMachine, amount: float):
        print("ERROR: Cannot insert coin during dispensing.")

     def select_item(self, machine: VendingMachine, item_name: str):
        print("ERROR: Already dispensing an item.")

     def dispense_item(self, machine: VendingMachine, item_name: str):
        print(f"--- Dispensing {item_name} ---")
        item = machine.inventory.get_item(item_name)
        machine.inventory.dispense_item(item_name)
        
        change = machine.current_credit - item.price
        if change > 0:
            print(f"Dispensing change: ${change:.2f}")
        
        machine.current_credit = 0
        # Transition back to the NoCoinState
        machine.set_state(NoCoinState())
     
     def press_cancel_button(self, machine: VendingMachine):
        print("ERROR: Cannot cancel, item is already being dispensed.")
