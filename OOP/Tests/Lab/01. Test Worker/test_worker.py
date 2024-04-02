from unittest import TestCase, main
from worker import Worker
class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Test', 25000, 100)

    def test_correct_instantiation(self):
        self.assertEqual('Test', self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_work_method_energy_decrease_and_money_increase_by_salary(self):
        expected_energy = self.worker.energy - 1
        expected_money = self.worker.salary
        self.worker.work()
        self.assertEqual(self.worker.energy, expected_energy)
        self.assertEqual(self.worker.money, expected_money)

    def test_if_energy_is_less_or_equal_than_zero_trows_an_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as e:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(e.exception))

    def test_rest_method(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(self.worker.energy, expected_energy)

    def test_get_info(self):
        self.assertEqual(self.worker.get_info(), f'{self.worker.name} has saved {self.worker.money} money.')

if __name__ == '__main__':
    main()
