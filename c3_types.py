# ==========================================
# Challenge 3 : Inheritance for Vehicle Types
# ==========================================

# Goal:
# Create different vehicle types using inheritance.
#
# OOP Concept:
# - Inheritance
# - Parent class
# - Child class
# - super().__init__()
# - Method overriding
# - Code reuse
#
# Car, Truck and Motorcycle are all vehicles.
# They all have:
# - plate
# - make
# - model
# - year
# - kilometres
#
# They also all have:
# - fuel tank
# - fuel consumption
#
# Instead of writing the same code many times,
# we create one parent class called FuelledVehicle.
# Then Car, Truck and Motorcycle inherit from it.

from c1_vehicle import Vehicle
from c2_tank import FuelTank


class FuelledVehicle(Vehicle):

    # Constructor
    # This class inherits from Vehicle.
    # It also adds a fuel tank and fuel consumption.
    def __init__(self, plate: str, make: str, model: str, year: int, capacity: float, consumption: float) -> None:
        # Call the parent constructor.
        # This creates plate, make, model, year and kilometres.
        super().__init__(plate, make, model, year)

        # Create a FuelTank object for this vehicle.
        self.tank = FuelTank(capacity)

        # Store how many litres are used per 100 km.
        self.consumption = consumption

    # refuel()
    # Adds fuel to the vehicle's tank.
    def refuel(self, litres: float) -> None:
        self.tank.fill(litres)

    # drive()
    # This overrides Vehicle.drive().
    # First it calculates and consumes fuel.
    # Then it calls the parent drive() method
    # to add kilometres.
    def drive(self, km: int) -> float:
        if km <= 0:
            raise ValueError("Kilometres must be positive")
        fuel_used = self.consumption * km / 100

        # Validate fuel first.
        # If there is not enough fuel,
        # consume() raises a ValueError and kilometres will not change.
        self.tank.consume(fuel_used)

        # If fuel was consumed successfully,
        # then update the kilometres using the parent method.
        super().drive(km)

        return fuel_used

    
    # range_remaining()
    # Calculates how far the vehicle can still drive
    # with the fuel currently in the tank.
    def range_remaining(self) -> float:
        fuel_level = self.tank.get_level()
        distance = fuel_level / self.consumption * 100
        return round(distance, 2)


class Car(FuelledVehicle):

    # Constructor
    # A Car is a FuelledVehicle.
    # Cars have 50 L capacity and 6 L/100 km consumption.
    def __init__(self, plate: str, make: str, model: str, year: int, seats: int = 5) -> None:
        super().__init__(plate, make, model, year, 50.0, 6.0)
        self.seats = seats

    # describe()
    # This overrides the parent describe() method.
    def describe(self) -> str:
        return f"{super().describe()}, car, {self.seats} seats"


class Truck(FuelledVehicle):

    # Constructor
    # A Truck is a FuelledVehicle.
    # Trucks have 200 L capacity and 18 L/100 km consumption.
    def __init__(self, plate: str, make: str, model: str, year: int, payload_kg: int) -> None:
        super().__init__(plate, make, model, year, 200.0, 18.0)
        self.payload_kg = payload_kg

    # describe()
    # This overrides the parent describe() method.
    def describe(self) -> str:
        return f"{super().describe()}, truck, {self.payload_kg} kg payload"


class Motorcycle(FuelledVehicle):

    # Constructor
    # A Motorcycle is a FuelledVehicle.
    # Motorcycles have 15 L capacity and 3.5 L/100 km consumption.
    def __init__(self, plate: str, make: str, model: str, year: int) -> None:
        super().__init__(plate, make, model, year, 15.0, 3.5)

    # describe()
    # This overrides the parent describe() method.
    def describe(self) -> str:
        return f"{super().describe()}, motorcycle"


class Van(FuelledVehicle):

    # Constructor
    # A Van is a FuelledVehicle.
    # Vans have 75 L capacity and 9 L/100 km consumption.
    def __init__(self, plate: str, make: str, model: str, year: int, volume_m3: float) -> None:
        super().__init__(plate, make, model, year, 75.0, 9.0)
        self.volume_m3 = volume_m3

    # describe()
    # This overrides the parent describe() method.
    def describe(self) -> str:
        return f"{super().describe()}, van, {self.volume_m3} m3"


if __name__ == "__main__":
    # Create a Car object
    c = Car("B-CD-5678", "Toyota", "Yaris", 2023, seats=5)

    # Test car description
    print(c.describe())

    # Refuel the car
    c.refuel(20)
    print(f"Car fuel level: {c.tank.get_level()}")

    # Drive the car 100 km
    car_fuel_used = c.drive(100)
    print(f"Car fuel used: {car_fuel_used}")

    # Check car fuel level and kilometres
    print(f"Car fuel level after driving: {c.tank.get_level()}")
    print(f"Car kilometres: {c.kilometres}")

    # Create a Truck object
    tr = Truck("B-EF-9012", "MAN", "TGX", 2021, payload_kg=18000)

    # Test truck description
    print(tr.describe())

    # Test truck tank capacity
    print(f"Truck tank capacity: {tr.tank.get_capacity()}")

    # Refuel and drive the truck
    tr.refuel(150)
    truck_fuel_used = tr.drive(100)
    print(f"Truck fuel used: {truck_fuel_used}")
    print(f"Truck fuel level after driving: {tr.tank.get_level()}")

    # Create a Motorcycle object
    m = Motorcycle("B-GH-3456", "Yamaha", "MT-07", 2024)

    # Test motorcycle description
    print(m.describe())

    # Refuel and drive the motorcycle
    m.refuel(10)
    motorcycle_fuel_used = m.drive(100)
    print(f"Motorcycle fuel used: {motorcycle_fuel_used}")
    print(f"Motorcycle fuel level after driving: {m.tank.get_level()}")

    # Test failed drive.
    # This should raise a ValueError.
    # The truck fuel level and kilometres should not change.
    try:
        tr.drive(2000)
    except ValueError as e:
        print(f"Caught error: {e}")

    try:
        c.drive(0)
    except ValueError as e:
        print(f"Caught error: {e}")

    try:
        c.drive(-5)
    except ValueError as e:
        print(f"Caught error: {e}")
    
    print(f"Car fuel level after failed drives: {c.tank.get_level()}")
    print(f"Car kilometres after failed drives: {c.kilometres}")

    # Check that truck state did not change after failed drive
    print(f"Truck fuel level after failed drive: {tr.tank.get_level()}")
    print(f"Truck kilometres after failed drive: {tr.kilometres}")

    # Stretch test: Create a Van object
    van = Van("B-VN-1111", "Ford", "Transit", 2022, volume_m3=12.5)
    print(van.describe())

    # Test range_remaining()
    van.refuel(30)
    print(f"Van range remaining: {van.range_remaining()} km")
