import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.level import Level
from game.result import Result
    
class User:
    def __init__(self, name: str, level: Level= Level.BEGINNER, balance: float = 0.0) -> None:
        self.__name = name
        self.__balance = balance
        self.__level = level
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    @property
    def level(self) -> Level:
        return self.__level
    
    def add_funds(self, amount: float) -> None:
        self.__balance += amount

    def remove_funds(self, amount: float) -> None:
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
    
    def update_balance(self, result: Result, bet:float) -> None:
        if result == Result.WIN:
            self.add_funds(bet)
        elif result == Result.LOSS:
            self.remove_funds(bet)
    
    def can_afford_bet(self, amount: float) -> bool:
        return amount <= self.__balance
        
    def __str__(self):
        return f"User {self.__name} - Level: {self.__level.value} - Balance: {self.__balance}"


