import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.card.card import Card
from src.card.suit import Suit


class TestCard(unittest.TestCase):

    def test_get_name(self):
        card = Card("Ace", 1, Suit("Spades", "♠"))
        self.assertEqual(card.name, "Ace")

    def test_value(self):
        card = Card("Ace", 1, Suit("Spades", "♠"))
        self.assertEqual(card.value, 1)

    def test_get_suit(self):
        card = Card("Ace", 1, Suit("Spades", "♠"))
        self.assertEqual(card.suit.name, "Spades")
        self.assertEqual(card.suit.symbol, "♠")

if __name__ == '__main__':
    unittest.main()
