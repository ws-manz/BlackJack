import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.player import Player
from game.level import Level
from game.dealer import Dealer

from game.gameLogic import GameLogic
from game.cardDealer import CardDealer
from game.gameView import GameView


class Round:
    def __init__(self, players: list[Player], dealer: Dealer, bet: float = 1000.00) -> None:
        self.__players = players
        self.__dealer = dealer
        self.__bet = bet
        self.__game_logic = GameLogic(self.__players,  self.__dealer)
        self.__card_dealer = CardDealer(self.__players, self.__dealer, self.__bet)
        self.__game_view = GameView(self.__players, self.__dealer)

    def play(self):
        # Distribui uma carta para cada jogador e para o dealer
        for player in self.__players:
            if player.get_user().balance < self.__bet: # verifica se o saldo é suficiente para a aposta
                self.__players.remove(player) # remove o jogador da lista de jogadores
                continue
            self.__dealer.deal_card(player)

        self.__dealer.deal_card(self.__dealer.get_player())

        # Distribui mais cartas para cada jogador até que ele tenha atingido o valor mínimo para o nível dele ou tenha ultrapassado 21 pontos
        for player in self.__players:
            while True:
                if player.get_hand_value() >= 21:
                    break
                if player.play() == "hit":
                    self.__dealer.deal_card(player)
                else:
                    break

        # Dealer continua comprando cartas até atingir 17 pontos ou mais
        while self.__dealer.get_player().get_hand_value() < 17:
            self.__dealer.deal_card(self.__dealer.get_player())

        # Verifica o vencedor do jogo
        winners = []
        dealer_value = self.__dealer.get_player().get_hand_value()
        for player in self.__players:
            if player.get_hand_value() <= 21 and (dealer_value > 21 or player.get_hand_value() > dealer_value):
                winners.append(player)
                
         # Exibe as cartas de cada jogador e do dealer
        print("\nPlayers' cards and points:")
        for player in self.__players:
            #print(f"{player.get_user().name}: {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]} - Points: {player.get_hand_value()}")
            self.__game_view.display_player_cards(player)
        #print(f"Dealer: {[card.name + ' ' + card.suit.symbol for card in self.__dealer.get_player().get_hand()]} - Points: {self.__dealer.get_player().get_hand_value()}")
        
        self.__game_view.display_dealer_cards()

        if len(winners) == 0:
            print("\nDealer wins! All players lost.")
            for player in self.__players:
                player.get_user().update_balance(2, self.__bet) 
        else:
            for player in self.__players:
                if player in winners:
                    player.get_user().update_balance(1, self.__bet) # bonifica os vencedores com o dobro da aposta
                else:
                    player.get_user().update_balance(2, self.__bet) # penaliza os perdedores com o valor da aposta

        self.__game_view.display_round_result(self.__players)
        
                
