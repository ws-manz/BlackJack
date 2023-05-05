from typing import List
from player.participant import Participant
from player.dealer import Dealer
from utils.base_class import BaseClass

class GameView(BaseClass):
    def __init__(self, players: List[Participant], dealer: Dealer) -> None:
        self.__players = players
        self.__dealer = dealer
    
    def display_initial_cards(self):
        self.logger.log("\nInitial cards:")
        for player in self.__players:
            self.logger.log(f"{player.get_user().name}: {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]}")
        self.logger.log(f"Dealer: [{self.__dealer.get_player().get_hand()[0].name} {self.__dealer.get_player().get_hand()[0].suit.symbol}, *]")

    def display_player_cards(self, player: Participant):
        self.logger.log(f"{player.get_user().name}'s cards: {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]} - Points: {player.calculate_hand_value()}")

    def display_dealer_cards(self):
        self.logger.log(f"Dealer's cards: {[card.name + ' ' + card.suit.symbol for card in self.__dealer.get_player().get_hand()]} - Points: {self.__dealer.get_player().calculate_hand_value()}")

    def display_round_result(self, winners: List[Participant]):
        self.logger.log("\n")
        for player in self.__players:
            if player in winners:
                self.logger.log(f"{player.get_user().name} wins! {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]} - Points: {player.calculate_hand_value()} - Bet: {player.get_user().balance}")
            else:
                self.logger.log(f"{player.get_user().name} loses. {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]} - Points: {player.calculate_hand_value()} - Bet: {player.get_user().balance}")
        self.logger.log("\n")        