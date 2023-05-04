from typing import Any

class User:
    def __init__(self, name: str, money : float) -> None:
        self.__name = name
        self.__money = money
    
    def get_name(self) -> Any:
         return self.__name
    
    def get_money(self) -> Any:
         return self.__money
    

