import os
import sys
from player.dealer import Dealer

from utils.base_class import BaseClass

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from object_value.result import Result
from player.participant import Participant


class PlayerManager(BaseClass):
    def __init__(self, bet: float):
        self.__bet = bet
    
    def update_balances(self, players: list[Participant], dealer: Dealer, winners: list[Participant]):
        self.logger.result_log(f"Dealer's cards: {[card.name + ' ' + card.suit.symbol for card in dealer.get_player().hand]} - Balance: {dealer.get_player().get_user().balance}")
        if len(winners) == 0:
            self.logger.log("\nDealer wins! All players lost.")
            self.logger.result_log("\nDealer wins! All players lost.")            
            for player in players:
                for hand in player.get_hands():
                    if hand.get_value() > 0:
                        player.get_user().update_balance(Result.LOSS, self.__bet) 
                        dealer.get_player().get_user().update_balance(Result.WIN, self.__bet)
                        self.logger.result_log(f"{player.get_user().name} loses. {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
        else:
            for player in players:
                for hand in player.get_hands():
                    if(hand.get_value() > 0):
                        if hand.win:
                            player.get_user().update_balance(Result.WIN, self.__bet) # bonifica os vencedores com o dobro da aposta
                            dealer.get_player().get_user().update_balance(Result.LOSS, self.__bet)
                            self.logger.result_log(f"{player.get_user().name} win! {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
                        else:
                            if hand.surrender:
                                #print(f" {player.get_user().name} surrender => {hand.win}")
                                player.get_user().update_balance(Result.LOSS, self.__bet/2) # penaliza os perdedores com o valor da aposta
                                dealer.get_player().get_user().update_balance(Result.WIN, self.__bet/2)
                                self.logger.result_log(f"{player.get_user().name} surrender. {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
                            else:
                                #print(f" {player.get_user().name} loss => {hand.win}")
                                player.get_user().update_balance(Result.LOSS, self.__bet) # penaliza os perdedores com o valor da aposta
                                dealer.get_player().get_user().update_balance(Result.WIN, self.__bet)
                                self.logger.result_log(f"{player.get_user().name} loses. {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
        self.logger.result_log(f"Dealer's cards: {[card.name + ' ' + card.suit.symbol for card in dealer.get_player().hand]} - Balance: {dealer.get_player().get_user().balance}")
