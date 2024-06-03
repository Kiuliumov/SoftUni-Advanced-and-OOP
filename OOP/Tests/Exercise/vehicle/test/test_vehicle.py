from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(500.0, 250.0)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 500.0)
        self.assertEqual(self.vehicle.capacity, 500.0)
        self.assertEqual(self.vehicle.horse_power, 250.0)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)


    def test_drive_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as contx:
            self.vehicle.fuel = 0
            self.vehicle.drive(550)
        self.assertEqual(str(contx.exception), 'Not enough fuel')

    def test_drive_enough_fuel(self):
        self.vehicle.fuel = 12
        self.vehicle.drive(5)
        self.assertEqual(self.vehicle.fuel, 5.75)

    def test_refuel_when_enough_capacity(self):
        self.vehicle.fuel = 350
        self.vehicle.refuel(150)
        self.assertEqual(self.vehicle.fuel, 500)

    def test_refuel_when_fulL_tank_raises(self):
        with self.assertRaises(Exception) as contx:
            self.vehicle.refuel(1500)
        self.assertEqual(str(contx.exception), 'Too much fuel')

    def test_str_method(self):
        self.assertEqual(self.vehicle.__str__(), f'The vehicle has {self.vehicle.horse_power} ' \
                                                 f'horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption')


if __name__ == '__main__':
    main()
