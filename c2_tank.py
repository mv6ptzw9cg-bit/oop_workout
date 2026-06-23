# ==========================================
# Challenge 2 : FuelTank Class
# ==========================================

# Goal:
# Create a FuelTank class.
#
# OOP Concept:
# - Class
# - Constructor (__init__)
# - Encapsulation
# - Private attributes (__)
# - Getter methods
# - Validation
#
# The FuelTank class stores information
# about the fuel inside a vehicle.
#
# The fuel level should not be changed
# directly from outside the class.
# Instead, we use methods to safely
# fill and consume fuel.

class FuelTank:

    # Constructor
    # Runs automatically whenever we create a FuelTank object.
    # It initializes the tank's capacity and fuel level.
    def __init__(self, capacity: float) -> None:

        # Validate the capacity before creating the tank.
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        # Private attributes
        # Double underscores make these variables private.
        # Other classes should use methods instead
        # of accessing them directly.
        self.__capacity = capacity
        self.__level = 0.0

    # get_level()
    # Returns the current fuel level.
    # The result is rounded to two decimal places.
    def get_level(self) -> float:
        return round(self.__level, 2)

    # get_capacity()
    # Returns the maximum capacity of the tank.
    # The result is rounded to two decimal places.
    def get_capacity(self) -> float:
        return self.__capacity

    # fill()
    # Adds fuel to the tank.
    # We validate first before changing the fuel level.
    # This keeps the object's state correct if an error occurs.
    def fill(self, litres: float) -> None:

        # Check that the amount of fuel is positive.
        if litres <= 0:
            raise ValueError("Fuel amount must be positive")

        # Check that the tank will not overflow.
        if self.__level + litres > self.__capacity:
            raise ValueError("Tank capacity exceeded")

        # Update the fuel level after validation.
        self.__level += litres

    # consume()
    # Removes fuel from the tank.
    # We validate first before changing the fuel level.
    def consume(self, litres: float) -> None:

        # Check that the amount is positive.
        if litres <= 0:
            raise ValueError("Fuel amount must be positive")

        # Check that there is enough fuel.
        if litres > self.__level:
            raise ValueError("Not enough fuel")

        # Update the fuel level after validation.
        self.__level -= litres

    # fill_to_full()
    # Fills the tank completely.
    # Returns how many litres were added.
    def fill_to_full(self) -> float:
        litres_added = self.__capacity - self.__level
        self.__level = self.__capacity
        return litres_added

    # percent_full()
    # Returns how full the tank is as a percentage.
    # The result is rounded to one decimal place.
    def percent_full(self) -> float:
        return round((self.__level / self.__capacity) * 100, 1)


if __name__ == "__main__":
    # Create a FuelTank object
    t = FuelTank(50.0)

    # Test the initial fuel level
    print(t.get_level())

    # Test the tank capacity
    print(t.get_capacity())

    # Fill the tank with 20 litres
    t.fill(20)
    print(f"Fuel level after adding 20 L: {t.get_level()}")

    # Add another 10.5 litres
    t.fill(10.5)
    print(f"Fuel level after adding another 10.5 L: {t.get_level()}")

    # Test tank overflow.
    # This should raise a ValueError and should not change the fuel level.
    try:
        t.fill(25)
    except ValueError as e:
        print(f"Caught error: {e}")

    # Check that the fuel level stayed the same after the failed overflow
    print(f"Fuel level after failed overflow: {t.get_level()}")

    # Test invalid fuel amount.
    # This should raise a ValueError.
    try:
        t.fill(-5)
    except ValueError as e:
        print(f"Caught error: {e}")

    # Remove 10 litres
    t.consume(10)
    print(f"Fuel level after consuming 10 L: {t.get_level()}")

    # Test consuming too much fuel.
    # This should raise a ValueError and should not change the fuel level.
    try:
        t.consume(100)
    except ValueError as e:
        print(f"Caught error: {e}")

    # Check that the fuel level stayed the same after the failed consume
    print(f"Fuel level after failed consume: {t.get_level()}")

    try:
        t.consume(-5)
    except ValueError as e:
        print(f"Caught error: {e}")

    # Test invalid capacity.
    # This should raise a ValueError.
    try:
        FuelTank(-1)
    except ValueError as e:
        print(f"Caught error: {e}")

    # Test that private attributes cannot be accessed directly.
    # This should raise an AttributeError.
    try:
        print(t.__level)
    except AttributeError as e:
        print(f"Caught error: {e}")

    # Stretch test: fill the tank to full
    litres_added = t.fill_to_full()
    print(f"Litres added to fill the tank: {litres_added}")
    print(f"Fuel level after filling to full: {t.get_level()}")

    # Stretch test: check how full the tank is as a percentage
    print(f"Tank percentage: {t.percent_full()}%")
