class User:
    def __init__(self, name: str, balance: float = 0.0) -> None:
        self.__name = name
        self.__balance = balance
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    def add_funds(self, amount: float) -> None:
        self.__balance += amount

    def remove_funds(self, amount: float) -> None:
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount


