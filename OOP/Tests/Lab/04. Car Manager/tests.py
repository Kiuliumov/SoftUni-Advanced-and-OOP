import unittest
from car_manager import Car
class TestCar(unittest.TestCase):
    def test_initialization(self):
        car = Car("Toyota", "Camry", 7.5, 60)
        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.fuel_consumption, 7.5)
        self.assertEqual(car.fuel_capacity, 60)
        self.assertEqual(car.fuel_amount, 0)

    def test_make_validation(self):
        with self.assertRaises(Exception):
            car = Car("", "Camry", 7.5, 60)

    def test_model_validation(self):
        with self.assertRaises(Exception):
            car = Car("Toyota", "", 7.5, 60)

    def test_fuel_consumption_validation(self):
        with self.assertRaises(Exception):
            car = Car("Toyota", "Camry", 0, 60)

    def test_fuel_capacity_validation(self):
        with self.assertRaises(Exception):
            car = Car("Toyota", "Camry", 7.5, 0)

    def test_refuel(self):
        car = Car("Toyota", "Camry", 7.5, 60)
        car.refuel(20)
        self.assertEqual(car.fuel_amount, 20)

    def test_refuel_negative_amount(self):
        car = Car("Toyota", "Camry", 7.5, 60)
        with self.assertRaises(Exception):
            car.refuel(-20)

    def test_drive(self):
        car = Car("Toyota", "Camry", 7.5, 60)
        car.refuel(30)
        car.drive(200)
        self.assertEqual(car.fuel_amount, 15)

    def test_drive_not_enough_fuel(self):
        car = Car("Toyota", "Camry", 7.5, 60)
        with self.assertRaises(Exception):
            car.drive(200)

if __name__ == '__main__':
    unittest.main()
