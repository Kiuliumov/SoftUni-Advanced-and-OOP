from project.mammal import Mammal
from unittest import TestCase, main



class MammalTest(TestCase):

    def setUp(self):
        self.mammal = Mammal('Ken', 'Dog', 'Bark')


    def test_init(self):
        self.assertEqual(self.mammal.name, 'Ken')
        self.assertEqual(self.mammal.type, 'Dog')
        self.assertEqual(self.mammal.sound, 'Bark')

    def test_make_sound(self):
        expected = f'{self.mammal.name} makes {self.mammal.sound}'
        sound = self.mammal.make_sound()
        self.assertEqual(sound, expected)

    def test_get_kingdom(self):
        kingdom = self.mammal.get_kingdom()
        self.assertEqual(kingdom, 'animals')

    def test_info(self):
        expected = f'{self.mammal.name} is of type {self.mammal.type}'
        info = self.mammal.info()
        self.assertEqual(info, expected)


if __name__ == '__main__':
    main()