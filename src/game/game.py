from card.card import Card
from card.suit import Suit
from game.player import Player
from game.user import User
import random

class Game:
    def __init__(self) -> None:
        self.reset_game()
        self.__players = []
    
    def reset_game(self):        
        self.__deck = self.__create_deck()
        self.__card_iterator = iter(self.__deck)
        print("Shuffled deck")
        
    def add_player(self, player) -> Player :
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
        
    
    def play_round (self):
        # Distribui uma carta para cada jogador
        for player in self.__players:
            self.deal_card(player)
        # Continua distribuindo cartas para cada jogador até que ele tenha 17 pontos ou mais
        for player in self.__players:
            while player.get_hand_value() < 17:
                self.deal_card(player)
        # Exibe as cartas de cada jogador e seu valor total das cartas
        for player in self.__players:
            print(f"### {player.get_user().name} - Value {player.get_hand_value()} ###")
            for card in player.get_hand():
                print(f"Card {card.name} {card.suit.symbol}")
            print(f"######################################")
    
    def deal_card(self, player):
        # Distribui uma carta para o jogador
        player.add_card(self.get_next_card())
        
    def get_next_card(self):
        # Retorna a próxima carta do baralho
        return next(self.__card_iterator)
        
    def get_cards(self):
        # Retorna o baralho completo
        return self.__deck
    
    def __create_suits(self):
        # Cria as cartas de cada naipe
        suits = [("spade", "♠"), ("heart", "♥"), ("diamond", "♦"), ("clubs", "♣")]
        return (Suit(name, symbol) for name, symbol in suits)
    
    def __create_deck(self):        
        cards = []
        for suit in self.__create_suits():
            cards.append(Card("Ace", 1, suit))
            for i in range(2, 11):
                cards.append(Card(str(i), i, suit))
            cards.append(Card("Jack", 10, suit))
            cards.append(Card("Queen", 10, suit))
            cards.append(Card("King", 10, suit))
        
        random.shuffle(cards)

        #for card in cards:
        #    print(f"Card {card.name} {card.suit.get_symbol()}")

        return (cards)
