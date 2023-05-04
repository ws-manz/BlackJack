from card import Card
from suit import Suit
from player import Player
from user import User
import random

class Game:
    def __init__(self) -> None:
        self._clear()
        self.__players = []
    
    def _clear(self):        
        self.__deck = self.__create_deck()
        self.__card_iterator = iter(self.__deck)
        print("Shuffled deck")
        
    def add_player(self, player) -> Player :
        self.__players.append(player)
        
    def test(self):
        u1 = User("Marco", 1000)
        u2 = User("Pricila",1000)
        p1 = Player(u1)
        p2 = Player(u2)
        self.add_player(p1)
        self.add_player(p2)
        self.start_game()
        
    def start_game(self) :
        
        if len(self.__players) == 0 :
            print("*Insufficient number of players*")
            return

        print("*Game started, welcome!*")
        
        self.first_round()
        self.first_round()
        
        for player in self.__players:
            print(f"### {player.get_user().get_name()} - Value {player.get_hand_value()} ###")
            
            for card in player.get_cards():
                print(f"Card {card.get_name()} {card.get_suit().get_symbol()}")
                
            print(f"######################################")
        
        self._clear()
    
    def first_round(self):
        for player in self.__players:
            if(len(player.get_cards()) < 2):
                player.add_card(self.get_next_card())
    
    def get_next_card(self):
        return next(self.__card_iterator)
    
    def add_card(self, card) -> Card:
        self.__deck.append(card)
    
    def get_cards(self):
        return self.__deck
    
    def __create_suits(self):
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
        #    print(f"Card {card.get_name()} {card.get_suit().get_symbol()}")

        return (cards)
