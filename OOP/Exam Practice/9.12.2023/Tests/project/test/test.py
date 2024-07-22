from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class RailwayStationTest(TestCase):

    def test__init__(self):
        railway_station = RailwayStation('Test')
        self.assertEqual(railway_station.name, 'Test')
        self.assertEqual(railway_station.arrival_trains, deque())
        self.assertEqual(railway_station.departure_trains, deque())

    def test_name_setter_if_name_empty(self):
        with self.assertRaises(ValueError) as ve:
            railway_station = RailwayStation('')
        self.assertEqual(str(ve.exception), 'Name should be more than 3 symbols!')

    def test_name_setter_if_name_less_than_three_characters(self):
        with self.assertRaises(ValueError) as ve:
            railway_station = RailwayStation('ab')
        self.assertEqual(str(ve.exception), 'Name should be more than 3 symbols!')

    def test_new_arrival_on_board(self):
        railway_station = RailwayStation('Test')
        railway_station.new_arrival_on_board('TestInfo')
        self.assertEqual(railway_station.arrival_trains, deque(['TestInfo']))

    def test_train_has_arrived_if_there_are_other_trains(self):
        railway_station = RailwayStation('Test')
        railway_station.new_arrival_on_board('TestInfo1')
        railway_station.new_arrival_on_board('TestInfo')
        result = railway_station.train_has_arrived('TestTrain')
        self.assertEqual(result, 'There are other trains to arrive before TestTrain.')

    def test_train_has_arrived_if_success(self):
        railway_station = RailwayStation('Test')
        railway_station.new_arrival_on_board('TestInfo')
        result = railway_station.train_has_arrived('TestInfo')
        self.assertEqual(result, 'TestInfo is on the platform and will leave in 5 minutes.')
        self.assertEqual(railway_station.departure_trains, deque(['TestInfo']))
        self.assertEqual(railway_station.arrival_trains, deque())


    def test_train_has_left_if_has_left(self):
        railway_station = RailwayStation('Test')
        railway_station.new_arrival_on_board('TestInfo')
        railway_station.train_has_arrived('TestInfo')
        result = railway_station.train_has_left('TestInfo')
        self.assertTrue(result)


    def test_train_has_left_if_has_not_left(self):
        railway_station = RailwayStation('Test')
        railway_station.new_arrival_on_board('TestInfo1')
        railway_station.train_has_arrived('TestInfo1')
        result = railway_station.train_has_left('TestInfo')
        self.assertFalse(result)


if __name__ == '__main__':
    main()