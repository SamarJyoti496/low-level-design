import time
from parking_system.parking_lot import ParkingLot
from parking_system.vehicles import MotorCycle, Car, Truck
from parking_system.fee_calculator import ParkingFeeCalculator

def main():
    """Main function to run the parking lot simulation."""
    print("--- Initializing Parking Lot System ---")
    # 1. Create the fee calculation
    fee_calculator = ParkingFeeCalculator(hourly_rate=10.0)

    # 2. Create the parking lot, injecting the fee calculator
    my_parking_lot = ParkingLot(fee_calculator=fee_calculator)

    print("\n--- Simulation Start ---")

    # 3. Create some vehicles
    motorcycle = MotorCycle("MC-001")
    car1 = Car("CAR-001")
    car2 = Car("CAR-002")
    truck = Truck("TRK-001")

    # 4. Park the vehicles
    mc_ticket = my_parking_lot.park_vehicle(motorcycle)
    car1_ticket = my_parking_lot.park_vehicle(car1)
    truck_ticket = my_parking_lot.park_vehicle(truck)

    # 5. Simulate some time passing
    print("\n... Vehicles are parked for a while ...")
    time.sleep(2) # Pauses execution for 2 seconds to simulate time passing

    # 6. Unpark a vehicle
    if car1_ticket:
        my_parking_lot.unpark_vehicle(car1_ticket)

    # 7. Try to park another car
    print("\n--- A new car arrives ---")
    my_parking_lot.park_vehicle(car2)

    print("\n--- Simulation End ---")


if __name__ == "__main__":
    main()