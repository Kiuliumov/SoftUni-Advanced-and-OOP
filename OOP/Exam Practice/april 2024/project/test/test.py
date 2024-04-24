import unittest
from project.restaurant import Restaurant

class TestRestaurant(unittest.TestCase):

    def test_constructor(self):
        restaurant = Restaurant("Test Restaurant", 10)
        self.assertEqual(restaurant.name, "Test Restaurant")
        self.assertEqual(restaurant.capacity, 10)
        self.assertEqual(restaurant.waiters, [])

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            Restaurant("", 10)
        self.assertEqual(str(context.exception), "Invalid name!")

        with self.assertRaises(ValueError) as context:
            Restaurant("   ", 10)
        self.assertEqual(str(context.exception), "Invalid name!")

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError) as context:
            Restaurant("Test Restaurant", -10)
        self.assertEqual(str(context.exception), "Invalid capacity!")

    def test_add_waiter(self):
        restaurant = Restaurant("Test Restaurant", 2)
        self.assertEqual(restaurant.add_waiter("John"), "The waiter John has been added.")
        self.assertEqual(restaurant.add_waiter("Alice"), "The waiter Alice has been added.")
        self.assertEqual(restaurant.add_waiter("Bob"), "No more places!")

    def test_add_existing_waiter(self):
        restaurant = Restaurant("Test Restaurant", 2)
        restaurant.add_waiter("John")
        self.assertEqual(restaurant.add_waiter("John"), "The waiter John already exists!")

    def test_remove_waiter(self):
        restaurant = Restaurant("Test Restaurant", 2)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        self.assertEqual(restaurant.remove_waiter("John"), "The waiter John has been removed.")
        self.assertEqual(restaurant.remove_waiter("John"), "No waiter found with the name John.")

    def test_remove_nonexistent_waiter(self):
        restaurant = Restaurant("Test Restaurant", 2)
        self.assertEqual(restaurant.remove_waiter("John"), "No waiter found with the name John.")

    def test_get_total_earnings(self):
        restaurant = Restaurant("Test Restaurant", 2)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        restaurant.waiters[0]['total_earnings'] = 100
        restaurant.waiters[1]['total_earnings'] = 200
        self.assertEqual(restaurant.get_total_earnings(), 300)

    def test_get_waiters(self):
        restaurant = Restaurant("Test Restaurant", 2)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        restaurant.waiters[0]['total_earnings'] = 100
        restaurant.waiters[1]['total_earnings'] = 200
        self.assertEqual(len(restaurant.get_waiters(min_earnings=150)), 1)
        self.assertEqual(len(restaurant.get_waiters(max_earnings=150)), 1)
        self.assertEqual(len(restaurant.get_waiters(min_earnings=150, max_earnings=250)), 1)

    def test_get_waiters_no_earnings(self):
        restaurant = Restaurant("Test Restaurant", 2)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        self.assertEqual(len(restaurant.get_waiters(min_earnings=150)), 0)
        self.assertEqual(len(restaurant.get_waiters(min_earnings=150, max_earnings=250)), 0)

    def test_name_property(self):
        restaurant = Restaurant("Test Restaurant", 10)
        self.assertEqual(restaurant.name, "Test Restaurant")

        with self.assertRaises(ValueError) as context:
            restaurant.name = ""
        self.assertEqual(str(context.exception), "Invalid name!")

        with self.assertRaises(ValueError) as context:
            restaurant.name = "   "
        self.assertEqual(str(context.exception), "Invalid name!")

    def test_capacity_property(self):
        restaurant = Restaurant("Test Restaurant", 10)
        self.assertEqual(restaurant.capacity, 10)

        with self.assertRaises(ValueError) as context:
            restaurant.capacity = -5
        self.assertEqual(str(context.exception), "Invalid capacity!")

if __name__ == '__main__':
    unittest.main()
