"""
Creational Pattern: Factory Method
-------------------------------------
Defines an interface for creating an object, but lets a factory
function/method decide which concrete class to instantiate. Decouples
client code from concrete classes.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self) -> str:
        ...


class Car(Vehicle):
    def drive(self) -> str:
        return "Driving a car."


class Truck(Vehicle):
    def drive(self) -> str:
        return "Driving a truck."


class Motorcycle(Vehicle):
    def drive(self) -> str:
        return "Riding a motorcycle."


class VehicleFactory:
    """Client code asks the factory for a vehicle type by name and
    never needs to know which concrete class gets instantiated."""

    _vehicle_types = {
        "car": Car,
        "truck": Truck,
        "motorcycle": Motorcycle,
    }

    @classmethod
    def create_vehicle(cls, vehicle_type: str) -> Vehicle:
        vehicle_cls = cls._vehicle_types.get(vehicle_type.lower())
        if vehicle_cls is None:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
        return vehicle_cls()


if __name__ == "__main__":
    for kind in ["car", "truck", "motorcycle"]:
        vehicle = VehicleFactory.create_vehicle(kind)
        print(vehicle.drive())

    assert isinstance(VehicleFactory.create_vehicle("car"), Car)
    try:
        VehicleFactory.create_vehicle("plane")
        assert False, "Expected ValueError"
    except ValueError:
        pass
    print("Factory Method checks passed.")
