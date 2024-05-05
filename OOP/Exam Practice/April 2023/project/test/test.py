import unittest
from project.tennis_player import TennisPlayer

class TestTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer(name='Ivan', age=19, points=500)

    def test_instantiation(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        self.assertEqual(tennis_player.name, 'Ivan')
        self.assertEqual(tennis_player.age, 19)
        self.assertEqual(tennis_player.points, 500)
        self.assertEqual(tennis_player.wins, [])

    def test_name_setter_pass(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player.name = 'Ivan1'
        self.assertEqual(tennis_player.name, 'Ivan1')

    def test_name_setter_fail_if_less_than_2(self):
        with self.assertRaises(ValueError) as e:
            tennis_player = TennisPlayer(name='I', age=19, points=500)
        self.assertEqual(str(e.exception), 'Name should be more than 2 symbols!')

    def test_name_setter_fail_if_equals_2(self):
        with self.assertRaises(ValueError) as e:
            tennis_player = TennisPlayer(name='Iv', age=19, points=500)
        self.assertEqual(str(e.exception), 'Name should be more than 2 symbols!')

    def test_age_setter_pass(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player.age = 21
        self.assertEqual(tennis_player.age, 21)

    def test_age_setter_fail(self):
        with self.assertRaises(ValueError) as e:
            tennis_player = TennisPlayer(name='Ivan', age=15, points=500)
        self.assertEqual(str(e.exception), 'Players must be at least 18 years of age!')

    def test_points_setter_pass(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player.points = 600
        self.assertEqual(tennis_player.points, 600)

    def test_add_new_wins_method_when_adding_a_valid_win(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player.add_new_win('TestTournament')
        self.assertEqual(tennis_player.wins, ['TestTournament'])

    def test_add_new_wins_method_when_adding_an_already_added_tournament(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player.add_new_win('TestTournament')
        self.assertEqual(tennis_player.add_new_win('TestTournament'), 'TestTournament has been already added to the list of wins!')

    def test_less_than_when_player_has_more_points(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player_1 = TennisPlayer(name='Ivana', age=19, points=501)
        self.assertEqual(tennis_player < tennis_player_1, 'Ivana is a top seeded player and he/she is better than Ivan')

    def test_less_than_when_player_has_less_points(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player_1 = TennisPlayer(name='Ivana', age=19, points=499)
        self.assertEqual(tennis_player < tennis_player_1, 'Ivan is a better player than Ivana')

    def test_string_method(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player.add_new_win('TestTournament')
        tennis_player.add_new_win('TestTournament1')
        tennis_player.add_new_win('TestTournament2')
        tennis_player.add_new_win('TestTournament3')
        tennis_player.add_new_win('TestTournament4')
        str_player = tennis_player.__str__()
        compare_str = f"Tennis Player: Ivan\n" \
                      f"Age: 19\n" \
                      f"Points: 500.0\n" \
                      f"Tournaments won: TestTournament, TestTournament1, TestTournament2, TestTournament3, TestTournament4"
        self.assertEqual(str_player, compare_str)

    def test_wins_list_immutable(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        wins_list = tennis_player.wins
        wins_list.append('NewTournament')
        self.assertNotIn('NewTournament', tennis_player.wins)

    def test_instances_not_same(self):
        tennis_player_1 = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player_2 = TennisPlayer(name='Ivan', age=19, points=500)
        self.assertNotEqual(id(tennis_player_1), id(tennis_player_2))

    def test_age_edge_case_minimum(self):
        with self.assertRaises(ValueError) as e:
            tennis_player = TennisPlayer(name='Ivan', age=18, points=500)
        self.assertEqual(str(e.exception), 'Players must be at least 18 years of age!')

    def test_age_edge_case_maximum(self):
        tennis_player = TennisPlayer(name='Ivan', age=120, points=500)
        self.assertEqual(tennis_player.age, 120)

    def test_points_edge_case_zero(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=0)
        self.assertEqual(tennis_player.points, 0)

    def test_points_edge_case_negative(self):
        with self.assertRaises(ValueError) as e:
            tennis_player = TennisPlayer(name='Ivan', age=19, points=-100)
        self.assertEqual(str(e.exception), 'Points cannot be negative!')

    def test_tournament_name_edge_cases(self):
        tennis_player = TennisPlayer(name='Ivan', age=19, points=500)
        tennis_player.add_new_win('')
        tennis_player.add_new_win('VeryLongTournamentName' * 100)
        tennis_player.add_new_win('Tournament with special characters $%^&')
        self.assertEqual(tennis_player.wins, [''])

if __name__ == '__main__':
    unittest.main()
