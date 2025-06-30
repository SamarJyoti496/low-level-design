import datetime
from .ticket import Ticket

class ParkingFeeCalculator:
    """Calculates parking fees based on a simple hourly rate."""
    def __init__(self, hourly_rate: float):
        self.hourly_rate = hourly_rate

    def calculate_fee(self, ticket: Ticket) -> float:
        """Calculates the fee based on the duration the vehicle was parked."""
        duration = datetime.datetime.now() - ticket.entry_time
        duration_hours = duration.total_seconds() / 3600
        fee = duration_hours * self.hourly_rate
        return round(fee, 2)
