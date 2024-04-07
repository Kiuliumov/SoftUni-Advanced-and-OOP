from exam_practice.toy_store import ToyStore
import unittest

class TestToyStore(unittest.TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_add_toy_success(self):
        result = self.store.add_toy("A", "Teddy Bear")
        self.assertEqual(result, "Toy:Teddy Bear placed successfully!")
        self.assertEqual(self.store.toy_shelf["A"], "Teddy Bear")

    def test_add_toy_shelf_already_taken(self):
        self.store.toy_shelf["A"] = "Robot"
        with self.assertRaises(Exception) as context:
            self.store.add_toy("A", "Teddy Bear")
        self.assertEqual(str(context.exception), "Shelf is already taken!")

    def test_add_toy_toy_already_in_shelf(self):
        self.store.toy_shelf["A"] = "Teddy Bear"
        with self.assertRaises(Exception) as context:
            self.store.add_toy("A", "Teddy Bear")
        self.assertEqual(str(context.exception), "Toy is already in shelf!")

    def test_add_toy_invalid_shelf(self):
        with self.assertRaises(Exception) as context:
            self.store.add_toy("Z", "Action Figure")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_remove_toy_success(self):
        self.store.toy_shelf["B"] = "Doll"
        result = self.store.remove_toy("B", "Doll")
        self.assertEqual(result, "Remove toy:Doll successfully!")
        self.assertIsNone(self.store.toy_shelf["B"])

    def test_remove_toy_invalid_shelf(self):
        with self.assertRaises(Exception) as context:
            self.store.remove_toy("Z", "Action Figure")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_remove_toy_toy_not_in_shelf(self):
        self.store.toy_shelf["C"] = "Car"
        with self.assertRaises(Exception) as context:
            self.store.remove_toy("C", "Robot")
        self.assertEqual(str(context.exception), "Toy in that shelf doesn't exists!")

if __name__ == "__main__":
    unittest.main()
