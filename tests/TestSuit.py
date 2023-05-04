import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.card.suit import Suit


class TestSuit(unittest.TestCase):

    def test_create_suit(self):
        suit = Suit("Hearts","♥")
        self.assertEqual(suit.name, "Hearts")
        self.assertEqual(suit.symbol, "♥")

    #def test_invalid_suit(self):
    #    with self.assertRaises(ValueError):
    #        suit = Suit("Invalid Suit")

if __name__ == '__main__':
    unittest.main()               