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
        self.logger.result_log("\nPlayers' balance:")
        for player in self.__players:
            self.logger.log(f"Player: {player.get_user().name} Gender: {player.get_user().gender} Level: {player.get_user().level} Balance: {player.get_user().balance}")
            self.logger.result_log(f"Player: {player.get_user().name} Gender: {player.get_user().gender} Level: {player.get_user().level} Balance: {player.get_user().balance}")
        self.logger.log("\n")
        self.logger.result_log("\n")
    
    def display_player_cards(self, player: Participant):
        self.logger.log(f"{player.get_user().name}'s cards: {[card.name + ' ' + card.suit.symbol for card in player.hand]} - Points: {player.hand.get_value()}")

    def display_dealer_cards(self):
        self.logger.log(f"Dealer's cards: {[card.name + ' ' + card.suit.symbol for card in self.__dealer.get_player().hand]} - Points: {self.__dealer.get_player().hand.get_value()}")

    def display_round_result(self, winners: List[Participant]):
        self.logger.log("\n")
        for player in self.__players:
            if player in winners:
                self.__display_player_wins_info(player)
            self.__display_player_loss_info(player)
        
        self.logger.log("\n")        
        
    def __display_player_wins_info(self, player: Participant):
        for hand in player.get_hands():
            if hand.win:
                self.logger.log(f"{player.get_user().name} win! {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
            
    def __display_player_loss_info(self, player: Participant):
        for hand in player.get_hands():
            if(hand.surrender):
                self.logger.log(f"{player.get_user().name} surrender. {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
            else:
                if not hand.win and hand.get_value() > 0:
                    self.logger.log(f"{player.get_user().name} loses. {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
                    
    def __display_player_detail_info(self, player: Participant):
        for hand in player.get_hands():
            self.logger.log(f"{player.get_user().name} info. {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")