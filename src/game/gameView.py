from typing import List
from game.player import Player
from game.dealer import Dealer

class GameView:
    def __init__(self, players: List[Player], dealer: Dealer) -> None:
        self.__players = players
        self.__dealer = dealer
    
    def display_initial_cards(self):
        print("\nInitial cards:")
        for player in self.__players:
            print(f"{player.get_user().name}: {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]}")
        print(f"Dealer: [{self.__dealer.get_player().get_hand()[0].name} {self.__dealer.get_player().get_hand()[0].suit.symbol}, *]")

    def display_player_cards(self, player: Player):
        print(f"{player.get_user().name}'s cards: {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]} - Points: {player.get_hand_value()}")

    def display_dealer_cards(self):
        print(f"Dealer's cards: {[card.name + ' ' + card.suit.symbol for card in self.__dealer.get_player().get_hand()]} - Points: {self.__dealer.get_player().get_hand_value()}")

    def display_round_result(self, winners: List[Player]):
        print("\n")
        for player in self.__players:
            if player in winners:
                print(f"{player.get_user().name} wins! {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]} - Points: {player.get_hand_value()} - Bet: {player.get_user().balance}")
            else:
                print(f"{player.get_user().name} loses. {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]} - Points: {player.get_hand_value()} - Bet: {player.get_user().balance}")
        print("\n")
