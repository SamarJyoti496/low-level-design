from abc import ABC, abstractmethod
from .enums import VehicleType

class Vehicle(ABC):
     """Abstract base class for all the vehicles"""
     def __init__(self, license_plate: str):
          self.license_plate = license_plate
     
     @abstractmethod
     def get_type(self) -> VehicleType:
          pass

class MotorCycle(Vehicle):
     def get_type(self):
          return VehicleType.MOTORCYCLE

class Car(Vehicle):
     def get_type(self):
          return VehicleType.CAR

class Truck(Vehicle):
     def get_type(self):
          return VehicleType.TRUCK 