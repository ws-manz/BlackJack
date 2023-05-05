import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.game.humanPlayer import HumanPlayer
from src.game.user import User
from src.card.suit import Suit
from src.card.card import Card
from src.game.level import Level

class TestPlayer(unittest.TestCase):

    def setUp(self):
        user = User('Player', Level.BEGINNER, 1000.00)
        self.__player = HumanPlayer(user)
        
    def test_create_player(self):
        self.assertEqual(self.__player.get_user().name, "Player")
        self.assertEqual(self.__player.get_hand(), [])

    def test_add_card(self):
        self.__player.add_card(Card("Ace", 1, Suit("spade", "♠")))
        self.assertEqual(len(self.__player.get_hand()), 1)
        
    def test_add_bet_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.__player.get_user().add_funds(200)

if __name__ == '__main__':
    unittest.main()        