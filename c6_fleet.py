# ==========================================
# Challenge 6 : Fleet Manager
# ==========================================

# Goal:
# Create a Fleet class that stores
# different types of vehicles.
#
# OOP Concept:
# - Classes
# - Lists of objects
# - Polymorphism
# - Dunder methods
# - Error handling
#
# The Fleet can store Cars, Trucks,
# Motorcycles and ElectricCars together.
#
# This works because they all inherit
# from Vehicle and all have a drive() method.

from c1_vehicle import Vehicle
from c3_types import Car, Truck, Motorcycle
from c4_electric import ElectricCar

class Fleet:

    # Constructor
    # Creates a fleet with a name.
    # The fleet starts with an empty vehicle list.
    def __init__(self, name: str) -> None:
        self.name = name
        self._vehicles = []

    # add()
    # Adds a vehicle to the fleet.
    # If a vehicle with the same plate already exists,
    # raise a ValueError.
    def add(self, vehicle: Vehicle) -> None:
        if vehicle.plate in self:
            raise ValueError("Vehicle with this plate already exists")

        self._vehicles.append(vehicle)

    # remove()
    # Removes a vehicle from the fleet using its plate.
    # If the plate is not found, raise a KeyError.
    def remove(self, plate: str) -> None:
        vehicle = self.find(plate)

        if vehicle is None:
            raise KeyError("Vehicle not found")

        self._vehicles.remove(vehicle)

    # find()
    # Searches for a vehicle by plate.
    # Returns the vehicle if found.
    # Returns None if not found.
    def find(self, plate: str) -> Vehicle | None:
        for vehicle in self._vehicles:
            if vehicle.plate == plate:
                return vehicle

        return None

    # total_kilometres()
    # Adds together the kilometres
    # of every vehicle in the fleet.
    def total_kilometres(self) -> int:
        total = 0

        for vehicle in self._vehicles:
            total += vehicle.kilometres

        return total

    # drive_all()
    # Tries to drive every vehicle.
    #
    # If the drive works, the plate is added
    # to the successes list.
    #
    # If the drive fails, the plate and error message
    # are added to the failures list.
    def drive_all(self, km: int) -> tuple[list, list]:
        successes = []
        failures = []

        for vehicle in self._vehicles:
            try:
                vehicle.drive(km)
                successes.append(vehicle.plate)
            except ValueError as error:
                failures.append((vehicle.plate, str(error)))

        return successes, failures

    # __len__()
    # Allows us to use len(fleet).
    def __len__(self) -> int:
        return len(self._vehicles)

    # __iter__()
    # Allows us to write:
    # for vehicle in fleet:
    def __iter__(self):
        return iter(self._vehicles)

    # __contains__()
    # Allows us to check:
    # "B-1" in fleet
    def __contains__(self, plate: str) -> bool:
        for vehicle in self._vehicles:
            if vehicle.plate == plate:
                return True

        return False

    # __str__()
    # Returns a readable string for the fleet.
    def __str__(self) -> str:
        return f"Fleet '{self.name}': {len(self)} vehicle(s)"

    # Stretch
    # cars_only()
    # Returns only Car objects from the fleet.
    def cars_only(self) -> list[Car]:
        cars = []

        for vehicle in self._vehicles:

            # isinstance is okay here because
            # this method specifically asks for cars only.
            #
            # We do not use isinstance in print_summary()
            # because every vehicle already knows
            # how to print itself using __str__().
            if isinstance(vehicle, Car):
                cars.append(vehicle)

        return cars

    # Stretch
    # average_kilometres()
    # Returns the average kilometres in the fleet.
    def average_kilometres(self) -> float:
        if len(self._vehicles) == 0:
            return 0.0

        return self.total_kilometres() / len(self._vehicles)


# print_summary()
# Prints a report for the fleet.
#
# It uses a for loop directly on the fleet.
# This works because Fleet has __iter__().
#
# We do not need isinstance here because
# every vehicle knows how to describe itself
# using __str__().
def print_summary(fleet: Fleet) -> None:
    print("=== FLEET REPORT ===")
    print(fleet)
    print(f"Total kilometres: {fleet.total_kilometres()}")
    print("--------------------")

    for vehicle in fleet:
        print(vehicle)

    print("====================")


if __name__ == "__main__":
    # Create a Fleet object
    fleet = Fleet("Main")

    # Create different vehicle objects
    car = Car("B-1", "Toyota", "Yaris", 2023, seats=5)
    truck = Truck("B-2", "MAN", "TGX", 2021, payload_kg=18000)
    motorcycle = Motorcycle("B-3", "Yamaha", "MT-07", 2024)
    electric = ElectricCar("B-4", "Tesla", "Model 3", 2024, battery_kwh=60.0, range_km=400)

    # Add vehicles to the fleet
    fleet.add(car)
    fleet.add(truck)
    fleet.add(motorcycle)
    fleet.add(electric)

    # Test len()
    print(len(fleet))

    # Test __contains__()
    print("B-2" in fleet)
    print("B-99" in fleet)

    # Test find()
    print(fleet.find("B-3").make)
    print(fleet.find("B-99"))

    # Test duplicate plate
    try:
        fleet.add(Car("B-1", "Foo", "Bar", 2000))
    except ValueError as error:
        print(f"Caught error: {error}")

    # Test drive_all() with empty tanks and batteries.
    # This should fail for every vehicle.
    successes, failures = fleet.drive_all(10)
    print(successes)
    print(len(failures))

    # Refuel or charge every vehicle
    car.refuel(5)
    truck.refuel(5)
    motorcycle.refuel(5)
    electric.charge(20)

    # Test drive_all() again.
    # Now every vehicle should drive successfully.
    successes, failures = fleet.drive_all(10)
    print(len(successes))
    print(len(failures))

    # Test total kilometres
    print(fleet.total_kilometres())

    # Remove motorcycle from the fleet
    fleet.remove("B-3")

    # Test len() after removing
    print(len(fleet))

    # Test that motorcycle is no longer in fleet
    print("B-3" in fleet)

    # Test removing a vehicle that does not exist
    try:
        fleet.remove("B-99")
    except KeyError as error:
        print(f"Caught error: {error}")

    # Print the fleet report
    print_summary(fleet)

    # Stretch test: cars_only()
    for car in fleet.cars_only():
        print(car)

    # Stretch test: average_kilometres()
    print(fleet.average_kilometres())
