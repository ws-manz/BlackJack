import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.game.player import Player
from src.game.user import User
from src.card.suit import Suit
from src.card.card import Card

class TestPlayer(unittest.TestCase):

    def test_create_player(self):
        u1 = User("Marco", 1000)
        player = Player(u1)
        self.assertEqual(player.get_user().name, "Marco")
        self.assertEqual(player.get_hand(), [])

    def test_add_card(self):
        u1 = User("Marco", 1000)
        player = Player(u1)
        player.add_card(Card("Ace", 1, Suit("spade", "♠")))
        self.assertEqual(len(player.get_hand()), 1)

if __name__ == '__main__':
    unittest.main()        