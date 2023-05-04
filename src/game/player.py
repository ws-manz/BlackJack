import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod

from card.card import Card
from game.user import User
from typing import Any

class Player(ABC):
    """
    Classe abstrata que representa um jogador.
    """

    def __init__(self, user: User) -> None:
        """
        Inicializa a instância de Player com um objeto User e reseta as cartas do jogador.

        Args:
            user (User): Objeto User que representa o jogador.
        """
        self.__user = user
        self.reset_cards()

    def add_card(self, card: Card) -> None:
        """
        Adiciona uma carta na mão do jogador.

        Args:
            card (Card): Objeto Card que representa a carta a ser adicionada na mão do jogador.
        """
        self.__cards.append(card)

    def get_user(self) -> User:
        """
        Retorna o objeto User do jogador.

        Returns:
            User: Objeto User que representa o jogador.
        """
        return self.__user

    def reset_cards(self) -> None:
        """
        Limpa as cartas da mão do jogador.
        """
        self.__cards = []

    def get_hand(self) -> list:
        """
        Retorna as cartas da mão do jogador.

        Returns:
            list: Lista de objetos Card que representa as cartas da mão do jogador.
        """
        return self.__cards

    def get_hand_value(self) -> int:
        """
        Retorna o valor da mão do jogador.

        Returns:
            int: Valor total da mão do jogador.
        """
        hand_value = sum(card.value for card in self.__cards)
        aces_count = sum(1 for card in self.__cards if card.name == 'Ace')
        while hand_value > 21 and aces_count > 0:
            hand_value -= 10
            aces_count -= 1
        return hand_value

    @abstractmethod
    def play(self) -> str:
        """
        Método abstrato que representa a jogada do jogador.
        """
        pass