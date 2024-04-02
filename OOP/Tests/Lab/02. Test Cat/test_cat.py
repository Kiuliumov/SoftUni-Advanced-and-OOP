from unittest import TestCase, main
from cat import Cat


class CatTest(TestCase):
    def setUp(self):
        self.cat = Cat('TestObject')

    def test_cat_size_increment_after_eating(self):
        expected_size = self.cat.size + 1
        self.cat.eat()
        self.assertEqual(self.cat.size, expected_size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)

    def test_cat_cannot_eat_if_it_is_already_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as e:
            self.cat.eat()
        self.assertEqual('Already fed.', str(e.exception))

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as e:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(e.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
