class Suit:
    def __init__(self, name: str, symbol: str) -> None:
        self.__name = name
        self.__symbol = symbol

    @property
    def name(self) -> str:
        return self.__name

    @property
    def symbol(self) -> str:
        return self.__symbol

    def __str__(self) -> str:
        return self.__name

'''♠ ♥ ♦ ♣'''