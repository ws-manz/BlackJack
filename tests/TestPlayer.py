import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.player.player import Player
from src.game.user import User
from src.card.suit import Suit
from src.card.card import Card
from src.object_value.level import Level

class TestPlayer(unittest.TestCase):

    def setUp(self):
        user = User('Player', Level.BEGINNER, 1000.00)
        self.__player = Player(user)
        
    def test_create_player(self):
        self.assertEqual(self.__player.get_user().name, "Player")
        self.assertEqual(self.__player.hand.get_cards(), [])

    def test_add_card(self):
        self.__player.hand.add_card(Card("Ace", 1, Suit("spade", "♠")))
        self.assertEqual(len(self.__player.hand), 1)
        
    def test_can_afford_bet(self):
        self.assertFalse(self.__player.get_user().can_afford_bet(10000.00))

if __name__ == '__main__':
    unittest.main()        