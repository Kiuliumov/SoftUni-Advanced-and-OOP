from project.trip import Trip
from unittest import TestCase, main

class TestTrip(TestCase):

    def test_init(self):
        trip = Trip(1500000, 7, True)
        self.assertEqual(trip.budget, 1500000)
        self.assertEqual(trip.travelers, 7)
        self.assertEqual(trip.is_family, True)
        self.assertEqual(trip.booked_destinations_paid_amounts, {})

    def test_travelers_setter_raises(self):
        with self.assertRaises(ValueError) as ve:
            Trip(1500000, -1, True)
        self.assertEqual(str(ve.exception), 'At least one traveler is required!')

    def test_travelers_setter(self):
        trip = Trip(1500000, 7, True)
        self.assertEqual(trip.travelers, 7)

    def test_is_family_setter(self):
        trip = Trip(1500000, 1, True)
        self.assertEqual(trip.is_family, False)
        trip = Trip(1500000, 5, True)
        self.assertEqual(trip.is_family, True)

    def test_book_a_trip_when_destination_is_not_valid(self):
        trip = Trip(1500000, 7, True)
        self.assertEqual(trip.book_a_trip('Test'), 'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip_enough_budget_when_not_family_booking(self):
        trip = Trip(8000, 1, False)
        return_statement = trip.book_a_trip('New Zealand')
        self.assertEqual(trip.budget, 500)
        self.assertEqual(return_statement, 'Successfully booked destination New Zealand! Your budget left is 500.00')
        self.assertEqual(trip.booked_destinations_paid_amounts, {'New Zealand':7500})

    def test_book_a_trip_enough_budget_when_family_booking(self):
        trip = Trip(34000, 5, True)
        return_statement = trip.book_a_trip('New Zealand')
        self.assertEqual(trip.budget, 250)
        self.assertEqual(return_statement, 'Successfully booked destination New Zealand! Your budget left is 250.00')
        self.assertEqual(trip.booked_destinations_paid_amounts, {'New Zealand':33750})

    def test_book_a_trip_when_not_enough_budget(self):
        trip = Trip(33000, 5, True)
        return_statement = trip.book_a_trip('New Zealand')
        self.assertEqual(return_statement, 'Your budget is not enough!')

    def test_booking_status_if_no_bookings(self):
        trip = Trip(34000, 5, True)
        self.assertEqual(trip.booking_status(), 'No bookings yet. Budget: 34000.00')

    def test_booking_status_if_bookings(self):
        trip = Trip(34000, 5, True)
        trip.book_a_trip('New Zealand')
        return_statement = trip.booking_status()
        expected = 'Booked Destination: New Zealand\nPaid Amount: 33750.00\nNumber of Travelers: 5\nBudget Left: 250.00'
        self.assertEqual(return_statement,expected)


if __name__ == '__main__':
    main()