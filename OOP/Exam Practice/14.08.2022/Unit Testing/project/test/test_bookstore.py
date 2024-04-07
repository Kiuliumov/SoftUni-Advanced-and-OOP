import unittest
from exam_practice.bookstore import Bookstore

class TestBookstore(unittest.TestCase):

    def setUp(self):
        self.bookstore = Bookstore(100)  # Setting a books limit of 100 for testing

    def test_books_limit_setter(self):
        with self.assertRaises(ValueError):
            self.bookstore.books_limit = 0  # Setting books limit to zero
        with self.assertRaises(ValueError):
            self.bookstore.books_limit = -1  # Setting books limit to a negative value

    def test_receive_book(self):
        # Test receiving books within the limit
        self.assertEqual(self.bookstore.receive_book("Book1", 10), "10 copies of Book1 are available in the bookstore.")
        self.assertEqual(len(self.bookstore), 10)  # Check the total number of books

        # Test receiving books exceeding the limit
        with self.assertRaises(Exception):
            self.bookstore.receive_book("Book2", 91)  # Attempting to receive more than the limit

    def test_sell_book(self):
        # Adding books to the store
        self.bookstore.receive_book("Book1", 20)
        self.bookstore.receive_book("Book2", 15)

        # Test selling books
        self.assertEqual(self.bookstore.sell_book("Book1", 10), "Sold 10 copies of Book1")
        self.assertEqual(len(self.bookstore), 25)  # Check the total number of books after selling

        # Test selling more copies than available
        with self.assertRaises(Exception):
            self.bookstore.sell_book("Book2", 20)

        # Test selling non-existing book
        with self.assertRaises(Exception):
            self.bookstore.sell_book("NonExistingBook", 5)

    def test_str_method(self):
        # Adding books to the store
        self.bookstore.receive_book("Book1", 20)
        self.bookstore.receive_book("Book2", 15)

        expected_output = "Total sold books: 0\nCurrent availability: 35\n - Book1: 20 copies\n - Book2: 15 copies"
        self.assertEqual(str(self.bookstore), expected_output)


if __name__ == '__main__':
    unittest.main()
