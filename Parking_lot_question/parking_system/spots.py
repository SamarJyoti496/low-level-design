from .enums import ParkingSpotType
from .vehicles import Vehicle

class ParkingSpot:
    """Represents a single parking spot in the lot."""
    def __init__(self, spot_id: int, spot_type: ParkingSpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.parked_vehicle: Vehicle | None = None
        self.is_occupied = False

    def park_vehicle(self, vehicle: Vehicle):
        """Marks the spot as occupied by a vehicle."""
        if not self.is_occupied:
            self.parked_vehicle = vehicle
            self.is_occupied = True
        else:
            raise Exception(f"Spot {self.spot_id} is already occupied.")

    def unpark_vehicle(self):
        """Frees up the spot."""
        if self.is_occupied:
            self.parked_vehicle = None
            self.is_occupied = False
        else:
            raise Exception(f"Spot {self.spot_id} is already empty.")