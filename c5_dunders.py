# ==========================================
# Challenge 5: Dunder Methods
# ==========================================

# Goal:
# Test the dunder methods added to Vehicle.
#
# OOP Concept:
# - __str__()
# - __repr__()
# - __eq__()
# - __hash__()
#
# These methods make Vehicle objects easier
# to print, compare, and use in sets
# and dictionaries.

from c3_types import Car, Truck
from c4_electric import ElectricCar


if __name__ == "__main__":

    # Create a Car object
    c = Car("B-CD-5678", "Toyota", "Yaris", 2023, seats=5)

    # Test __str__()
    print(str(c))

    # Test __repr__()
    print(repr(c))

    # Test equality with the same plate
    c2 = Car("B-CD-5678", "Toyota", "Corolla", 2020)
    print(c == c2)

    # Test equality with a different plate
    c3 = Car("B-XX-0000", "Toyota", "Yaris", 2023)
    print(c == c3)

    # Test equality between different subclasses
    tr = Truck("B-CD-5678", "MAN", "Other", 2000, payload_kg=1)
    print(c == tr)

    # Test __repr__() for Truck
    tr2 = Truck("B-EF-9012", "MAN", "TGX", 2021, payload_kg=18000)
    print(repr(tr2))

    # Test __repr__() for ElectricCar
    e = ElectricCar("B-EV-0001", "Tesla", "Model 3", 2024, battery_kwh=60.0, range_km=400)
    print(repr(e))

    # Test __hash__()
    vehicle_set = {c, c2}
    print(len(vehicle_set))

