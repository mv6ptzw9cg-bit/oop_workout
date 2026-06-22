      
# ==========================================
# Challenge 1: Vehicle Class
# ==========================================

# Goal:
# Create our first class called Vehicle.
#
# OOP Concept:
# - Class
# - Object
# - Constructor (__init__)
# - Attributes
# - Methods
#
# Vehicle is the blueprint for every vehicle.
# Every object created from this class will have:
# - plate
# - make
# - model
# - year
# - kilometres
#
# We also create methods so every vehicle
# can drive, describe itself,
# and check whether it needs servicing.

class Vehicle:
    # Class attribute
    # Shared by every Vehicle object.
    # It counts how many vehicles have been created.
    fleet_size = 0

    # Constructor
    # Runs automatically whenever we create an object.
    # It initializes the object's attributes.
    def __init__(self, plate: str, make: str, model: str, year: int) -> None:
        self.plate = plate
        self.make = make
        self.model = model
        self.year = year
        self.kilometres = 0

        Vehicle.fleet_size += 1

    # drive()
    # Adds kilometres to the vehicle.
    # We check that km is positive.
    # If km is 0 or negative we raise a ValueError
    # because a vehicle cannot drive a negative distance.
    def drive(self, km: int) -> None:
        # Validate first.
        # We only update kilometres after every check passes.
        # This keeps the object's state correct if an error occurs.
        if km <= 0:
            raise ValueError("Kilometres must be positive")
        self.kilometres += km

    # describe()
    # Returns a formatted string describing the vehicle.
    # We return the string instead of printing it so it can be used anywhere in the program.
    def describe(self) -> str:
        return f"{self.year} {self.make} {self.model} ({self.plate})"

    # service_due()
    # Checks whether the vehicle needs servicing.
    # Returns True if the vehicle has travelled
    # more than 15000 km.
    def service_due(self) -> bool:
        return self.kilometres > 15000


if __name__ == "__main__":
    # Create a Vehicle object
    v = Vehicle("B-AB-1234", "Volkswagen", "Golf", 2022)

    # Test describe()
    print(v.describe())

    # Test the initial kilometres
    print(v.kilometres)

    # Drive 50 km and check the new kilometres
    v.drive(50)
    print(f"kilometres after driving 50 km: {v.kilometres}")

    # Drive another 120 km and check the total kilometres
    v.drive(120)
    print(f"Total kilometres: {v.kilometres}")

    # Check if the vehicle needs servicing
    print(v.service_due())

    # Drive enough kilometres so the vehicle needs servicing
    v.drive(15000)
    print(v.service_due())

    # Check the total number of Vehicle objects created
    print(Vehicle.fleet_size)

    # Test invalid input.
    # This should raise a ValueError.
    try:
        v.drive(-1)
    except ValueError as e:
        print(f"Caught error: {e}")
