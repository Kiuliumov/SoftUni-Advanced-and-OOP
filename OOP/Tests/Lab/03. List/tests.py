from unittest import TestCase, main
from extended_list import IntegerList

class TestIntegerList(TestCase):
    def setUp(self):
        self.intList = IntegerList(1,2,3,4,5,6,7,8,9,10,'a','b','c','d')

    def test_correct_init_data_receieving(self):
        self.assertTrue(1 in self.intList.get_data())
        self.assertFalse('a' in self.intList.get_data())

    def test_add_if_element_is_integer(self):
        expected_last_element = 5
        self.intList.add(expected_last_element)
        self.assertEqual(self.intList.get_data()[-1], expected_last_element)

    def test_add_if_element_is_not_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.intList.add('5')
        self.assertEqual('Element is not Integer', str(ve.exception))

    def test_remove_index_if_index_is_valid(self):
        expected_result = 5
        current_result = self.intList.remove_index(-1)
        self.assertEqual(current_result, expected_result)

    def test_remove_index_if_index_is_not_valid(self):
        with self.assertRaises(IndexError) as ie:
            self.intList.remove_index(99)
        self.assertEqual('Index is out of range', str(ie.exception))

    def test_get_if_index_is_valid(self):
        expected_result = self.intList.get_data()[0]
        current_result = self.intList.get(0)
        self.assertEqual(expected_result, current_result)

    def test_get_if_index_is_not_valid(self):
        with self.assertRaises(IndexError) as ie:
            self.intList.get(99)
        self.assertEqual('Index is out of range', str(ie.exception))

    def test_insert_if_element_and_index_are_both_valid(self):
        self.intList.insert(1, 1)
        self.assertEqual(self.intList.get(1), 1)

    def test_insert_if_element_is_not_valid(self):
        with self.assertRaises(ValueError) as ve:
            self.intList.insert(1, '1')
        self.assertEqual('Element is not an Integer', str(ve.exception))

    def test_insert_if_index_is_not_valid(self):
        with self.assertRaises(IndexError) as ie:
            self.intList.insert(99, 1)
        self.assertEqual('Index is out of range', str(ie.exception))

    def test_get_biggest(self):
        biggest = sorted(self.intList.get_data(), reverse=True)[0]
        self.assertEqual(self.intList.get_biggest(), biggest)

    def test_get_index(self):
        self.assertEqual(self.intList.get_data().index(1), self.intList.get_index(1))

if __name__ == '__main__':
    main()