import unittest
from rps_logic import determine_winner

class TestRPSLogic(unittest.TestCase):
    def test_draw(self):
        self.assertEqual(determine_winner("Rock", "Rock"), "Draw")

    def test_player_wins(self):
        self.assertEqual(determine_winner("Rock", "Scissors"), "Player Wins!")

    def test_computer_wins(self):
        self.assertEqual(determine_winner("Rock", "Paper"), "Computer Wins!")

if __name__ == '__main__':
    unittest.main()
