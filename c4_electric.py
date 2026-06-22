# ==========================================
# Challenge 4 : Polymorphism with ElectricCar
# ==========================================

# Goal:
# Create an ElectricCar class.
#
# OOP Concept:
# - Inheritance
# - Method overriding
# - Polymorphism
# - Private attributes (__)
# - Validation
#
# An ElectricCar is a kind of Vehicle,
# but it does not have a fuel tank.
#
# Instead of fuel, it has a battery.
# The battery is measured in kWh.
#
# ElectricCar inherits directly from Vehicle,
# not from FuelledVehicle.

from c1_vehicle import Vehicle
from c3_types import Car, Truck, Motorcycle


class ElectricCar(Vehicle):

    # Constructor
    # ElectricCar inherits from Vehicle.
    # It also adds battery size, range and charge.
    def __init__(
        self,
        plate: str,
        make: str,
        model: str,
        year: int,
        battery_kwh: float,
        range_km: int
    ) -> None:

        # Call the parent constructor.
        # This creates plate, make, model, year and kilometres.
        super().__init__(plate, make, model, year)

        # Validate battery size before storing it.
        if battery_kwh <= 0:
            raise ValueError("Battery size must be positive")

        # Validate range before storing it.
        if range_km <= 0:
            raise ValueError("Range must be positive")

        self.battery_kwh = battery_kwh
        self.range_km = range_km

        # Private attribute
        # The charge should not be changed directly from outside the class.
        self.__charge = 0.0

    # get_charge()
    # Returns the current battery charge.
    # The result is rounded to two decimal places.
    def get_charge(self) -> float:
        return round(self.__charge, 2)

    # charge()
    # Adds energy to the battery.
    # We validate first before changing the charge.
    def charge(self, kwh: float) -> None:

        # Check that the charge amount is positive.
        if kwh <= 0:
            raise ValueError("Charge amount must be positive")

        # Check that the battery will not overflow.
        if self.__charge + kwh > self.battery_kwh:
            raise ValueError("Battery capacity exceeded")

        # Update the charge after validation.
        self.__charge += kwh

    # drive()
    # This overrides Vehicle.drive().
    #
    # Vehicle.drive() only adds kilometres.
    # ElectricCar.drive() first uses battery charge,
    # then calls the parent drive() method.
    def drive(self, km: int) -> float:

        # Calculate how much energy is needed.
        # Formula:
        # energy used = battery_kwh * km / range_km
        energy_used = self.battery_kwh * km / self.range_km

        # Check if there is enough charge first.
        # This keeps the state unchanged if the drive fails.
        if energy_used > self.__charge:
            raise ValueError("Not enough charge")

        # Subtract the battery charge after validation.
        self.__charge -= energy_used

        # After charge was successfully used,
        # update kilometres using the parent method.
        super().drive(km)

        return energy_used

    # describe()
    # This overrides the parent describe() method.
    # It adds electric car information.
    def describe(self) -> str:
        return f"{super().describe()}, electric car"


# drive_all()
# This function shows polymorphism.
#
# Every vehicle has a drive() method,
# but each vehicle uses it differently.
#
# Car, Truck and Motorcycle use fuel.
# ElectricCar uses battery charge.
def drive_all(vehicles: list[Vehicle], km: int) -> list[float]:
    energy_used_list = []

    for vehicle in vehicles:
        energy_used = vehicle.drive(km)
        energy_used_list.append(energy_used)

    return energy_used_list


if __name__ == "__main__":
    # Create an ElectricCar object
    e = ElectricCar("B-EV-0001", "Tesla", "Model 3", 2024, battery_kwh=60.0, range_km=400)

    # Test electric car description
    print(e.describe())

    # Charge the electric car with 30 kWh
    e.charge(30)
    print(f"Electric car charge: {e.get_charge()}")

    # Drive electric car 100 km
    energy_used = e.drive(100)
    print(f"Energy used: {energy_used}")

    # Check charge and kilometres after driving
    print(f"Electric car charge after driving: {e.get_charge()}")
    print(f"Electric car kilometres: {e.kilometres}")

    # Test invalid charge amount
    try:
        e.charge(-5)
    except ValueError as error:
        print(f"Caught error: {error}")

    # Test battery overflow
    try:
        e.charge(100)
    except ValueError as error:
        print(f"Caught error: {error}")

    # Test not enough charge.
    # This should raise a ValueError and should not change kilometres.
    try:
        e.drive(1000)
    except ValueError as error:
        print(f"Caught error: {error}")

    # Check that state did not change after failed drive
    print(f"Electric car charge after failed drive: {e.get_charge()}")
    print(f"Electric car kilometres after failed drive: {e.kilometres}")

    # ==========================================
    # Polymorphism Test
    # ==========================================

    # Create different vehicles
    car = Car("B-1", "Toyota", "Yaris", 2023, seats=5)
    truck = Truck("B-2", "MAN", "TGX", 2021, payload_kg=18000)
    motorcycle = Motorcycle("B-3", "Yamaha", "MT-07", 2024)
    electric = ElectricCar("B-4", "Tesla", "Model 3", 2024, battery_kwh=60.0, range_km=400)

    # Refuel or charge each vehicle before driving
    car.refuel(10)
    truck.refuel(50)
    motorcycle.refuel(5)
    electric.charge(20)

    vehicles = [car, truck, motorcycle, electric]

    # Drive every vehicle using the same method name.
    # This works because every object has a drive() method.
    for vehicle in vehicles:
        vehicle.drive(50)

    # Check that all vehicles drove 50 km
    for vehicle in vehicles:
        print(f"{vehicle.describe()} - kilometres: {vehicle.kilometres}")

    # Stretch test: drive_all()
    used_list = drive_all(vehicles, 10)
    print(used_list)
