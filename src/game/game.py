from card.card import Card
from card.suit import Suit
from game.player import Player
from game.level import Level
from game.dealer import Dealer  # importa a classe Dealer
from card.deck import Deck 
import random

class Game:
    def __init__(self) -> None:
        self.__players = []
        self.__dealer = Dealer()  # cria o objeto Dealer
        self.__deck = Deck()
        
    def reset_game(self):        
        self.__deck = Deck()
        print("Shuffled deck")
        
    def add_player(self, player : Player) -> Player :
        self.__players.append(player)
        
    def start_game(self) :
        # Verifica se há pelo menos um jogador no jogo
        if len(self.__players) == 0 :
            print("*Insufficient number of players*")
            return
        
        # Informa que o jogo começou
        print("*Game started, welcome!*")
        # Inicia a rodada
        self.play_round()
        # Reinicia o jogo
        self.reset_game()
        
    
    def play_round(self):
        # Distribui uma carta para cada jogador e para o dealer
        for player in self.__players:
            self.deal_card(player)
        self.deal_card(self.__dealer.get_player())

        # Define o valor mínimo de pontos para parar de receber cartas, de acordo com o nível do jogador
        level_min_values = {Level.BEGINNER: 17, Level.INTERMEDIATE: 18, Level.ADVANCED: 19}

        # Distribui mais cartas para cada jogador até que ele tenha atingido o valor mínimo para o nível dele ou tenha ultrapassado 21 pontos
        for player in self.__players:
            while True:
                if player.get_hand_value() >= 21:
                    break
                if player.get_hand_value() < level_min_values[player.get_user().level]:
                    self.deal_card(player)
                else:
                    break

        # Dealer continua comprando cartas até atingir 17 pontos ou mais
        while self.__dealer.get_player().get_hand_value() < 17:
            self.deal_card(self.__dealer.get_player())

        # Exibe as cartas de cada jogador e do dealer
        print("\nPlayers' cards and points:")
        for player in self.__players:
            print(f"{player.get_user().name}: {[card.name + ' ' + card.suit.symbol for card in player.get_hand()]} - Points: {player.get_hand_value()}")
        print(f"Dealer: {[card.name + ' ' + card.suit.symbol for card in self.__dealer.get_player().get_hand()]} - Points: {self.__dealer.get_player().get_hand_value()}")


        # Verifica o vencedor do jogo
        winners = []
        dealer_value = self.__dealer.get_player().get_hand_value()
        for player in self.__players:
            if player.get_hand_value() <= 21 and (dealer_value > 21 or player.get_hand_value() > dealer_value):
                winners.append(player)
        if len(winners) == 0:
            print("\nDealer wins! All players lost.")
        else:
            print("\nWinners:")
            for winner in winners:
                print(f"{winner.get_user().name} - {winner.get_hand_value()} points")


    def deal_card(self, player : Player):
        # Distribui uma carta para o jogador
        player.add_card(self.__deck.get_next_card())
                
    def get_cards(self):
        # Retorna o baralho completo
        return self.__deck    
