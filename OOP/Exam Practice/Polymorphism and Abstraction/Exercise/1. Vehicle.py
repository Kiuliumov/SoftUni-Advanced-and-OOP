from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 0.9)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            print(f"Car traveled {distance} km.")
        else:
            print("Not enough fuel to drive this distance.")

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        print(f"Car refueled with {fuel} liters.")


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 1.6)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            print(f"Truck traveled {distance} km.")
        else:
            print("Not enough fuel to drive this distance.")

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
        print(f"Truck refueled with {fuel} liters.")
