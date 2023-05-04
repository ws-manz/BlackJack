import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.card.deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_create_deck(self):
        self.assertEqual(len(self.deck.get_cards()), 52)
        # ... e assim por diante

    def test_shuffle_deck(self):
        original_order = [str(card) for card in self.deck.get_cards()]
        self.deck.shuffle_deck()
        new_order = [str(card) for card in self.deck.get_cards()]
        self.assertNotEqual(original_order, new_order)

if __name__ == '__main__':
    unittest.main()
