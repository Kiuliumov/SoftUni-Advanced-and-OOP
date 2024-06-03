from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('TestHero', 5, 100, 15)
        self.enemy_hero = Hero('TestHero1', 6, 100, 20)

    def test_instantiation(self):
        self.assertEqual(self.hero.username, 'TestHero')
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 15)

    def test_battle_if_equal_usernames_raises(self):

        with self.assertRaises(Exception) as e:
            self.hero.battle(self.hero)
        self.assertEqual(str(e.exception), 'You cannot fight yourself')

    def test_battle_if_not_enough_health_raises(self):
        with self.assertRaises(ValueError) as e:
            self.hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(e.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_battle_if_enemy_not_enough_health_raises(self):
        with self.assertRaises(ValueError) as e:
            self.enemy_hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(e.exception), 'You cannot fight TestHero1. He needs to rest')

    def test_battle_if_draw(self):
        self.hero.health = 1
        self.enemy_hero.health = 1

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(result, 'Draw')

    def test_battle_if_loss(self):
        self.hero.health = 1
        self.enemy_hero.health = 150
        health = self.enemy_hero.health - (self.hero.damage * self.hero.level) + 5
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(health, self.enemy_hero.health)
        self.assertEqual(self.enemy_hero.level, 7)
        self.assertEqual(self.enemy_hero.damage, 25)
        self.assertEqual(result, 'You lose')

    def test_battle_if_win(self):
        self.hero.health = 150
        self.enemy_hero.health = 1

        health = self.hero.health - (self.enemy_hero.damage * self.enemy_hero.level) + 5

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(health, self.hero.health)
        self.assertEqual(self.hero.level, 6)
        self.assertEqual(self.hero.damage, 20)
        self.assertEqual(result, 'You win')



    def test_str_method(self):
        expected = f"Hero TestHero: 5 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 15\n"

        self.assertEqual(self.hero.__str__(), expected)


if __name__ == '__main__':
    main()
