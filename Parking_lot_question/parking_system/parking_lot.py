# parking_system/parking_lot.py

from .enums import VehicleType, ParkingSpotType
from .vehicles import Vehicle
from .spots import ParkingSpot
from .ticket import Ticket
from .fee_calculator import ParkingFeeCalculator

class ParkingLot:
    """The main class that manages the entire parking lot."""
    def __init__(self, fee_calculator: ParkingFeeCalculator):
        # Using Composition to create and own the spots
        self._small_spots = [ParkingSpot(i, ParkingSpotType.SMALL) for i in range(1, 11)]
        self._medium_spots = [ParkingSpot(i, ParkingSpotType.MEDIUM) for i in range(11, 31)]
        self._large_spots = [ParkingSpot(i, ParkingSpotType.LARGE) for i in range(31, 36)]
        
        # Using Dependency Injection for the fee calculator (adheres to DIP)
        self._fee_calculator = fee_calculator
        self._issued_tickets = {}

    def _find_available_spot(self, vehicle_type: VehicleType) -> ParkingSpot | None:
        """Finds an appropriate spot based on vehicle type."""
        if vehicle_type == VehicleType.MOTORCYCLE:
            spots_to_check = self._small_spots + self._medium_spots + self._large_spots
        elif vehicle_type == VehicleType.CAR:
            spots_to_check = self._medium_spots + self._large_spots
        elif vehicle_type == VehicleType.TRUCK:
            spots_to_check = self._large_spots
        else:
            return None

        for spot in spots_to_check:
            if not spot.is_occupied:
                return spot
        return None

    def park_vehicle(self, vehicle: Vehicle) -> Ticket | None:
        """Parks a vehicle and returns a ticket if successful."""
        # Polymorphism: vehicle.get_type() works for any Vehicle subclass
        spot = self._find_available_spot(vehicle.get_type())
        
        if not spot:
            print(f"Sorry, no available spots for vehicle type: {vehicle.get_type().name}")
            return None
            
        spot.park_vehicle(vehicle)
        ticket = Ticket(vehicle, spot)
        self._issued_tickets[ticket.ticket_id] = ticket
        print(f"Vehicle {vehicle.license_plate} parked at Spot ID {spot.spot_id} ({spot.spot_type.name}).")
        return ticket

    def unpark_vehicle(self, ticket: Ticket) -> float:
        """Unparks a vehicle and returns the calculated fee."""
        fee = self._fee_calculator.calculate_fee(ticket)
        
        spot = ticket.spot_assigned
        spot.unpark_vehicle()
        
        del self._issued_tickets[ticket.ticket_id]
        
        print(f"Vehicle {ticket.vehicle_details.license_plate} unparked from Spot ID {spot.spot_id}. Fee: ${fee}")
        return fee