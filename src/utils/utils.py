import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Utils:
    @staticmethod
    def calculate_blackjack_probability(remaining_cards, hand):
        num_non_aces_and_tens = sum(1 for c in remaining_cards if c.value == 10)
        num_aces = sum(1 for c in remaining_cards if c.name == "Ace")

        # subtract the number of cards already in the player's hand from the count
        num_non_aces_and_tens -= len([c for c in hand if c.value == 10])
        num_aces -= len([c for c in hand if c.name == "Ace"])

        # calculate the probability of getting a blackjack
        if num_aces == 0:
            blackjack_prob = num_non_aces_and_tens / len(remaining_cards)
        else:
            non_aces_prob = num_non_aces_and_tens / len(remaining_cards)
            ace_prob = num_aces / len(remaining_cards)
            blackjack_prob = non_aces_prob * ace_prob * 2

        return round(blackjack_prob * 100, 2)