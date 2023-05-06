from typing import List
from player.participant import Participant
from player.dealer import Dealer
from utils.base_class import BaseClass

class GameView(BaseClass):
    def __init__(self, players: List[Participant], dealer: Dealer) -> None:
        self.__players = players
        self.__dealer = dealer
        
    def display_players_balance(self):
        self.logger.log("\nPlayers' balance:")
        for player in self.__players:
            self.logger.log(f"{player.get_user().name}: {player.get_user().balance}")
        self.logger.log("\n")
    
    def display_player_cards(self, player: Participant):
        self.logger.log(f"{player.get_user().name}'s cards: {[card.name + ' ' + card.suit.symbol for card in player.hand.get_cards()]} - Points: {player.hand.get_value()}")

    def display_dealer_cards(self):
        self.logger.log(f"Dealer's cards: {[card.name + ' ' + card.suit.symbol for card in self.__dealer.get_player().hand.get_cards()]} - Points: {self.__dealer.get_player().hand.get_value()}")

    def display_round_result(self, winners: List[Participant]):
        self.logger.log("\n")
        for player in self.__players:
            if player in winners:
                self.__display_player_wins_info(player)
            else:
                self.__display_player_loss_info(player)
        self.logger.log("\n")        
        
    def __display_player_wins_info(self, player: Participant):
        for hand in player.get_hands():
            if hand.get_value() > 0:
                self.logger.log(f"{player.get_user().name} win! {[str(card) for card in hand.get_cards()]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
        #else:
        #    self.logger.log(f"{player.get_user().name} is not playing due to insufficient balance: {player.get_user().balance}")
            
    def __display_player_loss_info(self, player: Participant):
        if(player.surrender):
            self.logger.log(f"{player.get_user().name} surrender. {[str(card) for card in player.hand.get_cards()]} - Points: {player.hand.get_value()} - Balance: {player.get_user().balance}")
        else:
            for hand in player.get_hands():
                if hand.get_value() > 0:
                    self.logger.log(f"{player.get_user().name} loses. {[str(card) for card in hand.get_cards()]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")