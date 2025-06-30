import datetime
from .vehicles import Vehicle
from .spots import ParkingSpot

class Ticket:
    """Represents a ticket issued to a vehicle upon parking."""
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = f"{vehicle.license_plate}-{spot.spot_id}-{datetime.datetime.now().timestamp()}"
        self.entry_time = datetime.datetime.now()
        self.spot_assigned = spot
        self.vehicle_details = vehicle