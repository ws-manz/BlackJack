from enum import Enum

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    
    def symbol(self):
        return '♂' if self == Gender.MALE else '♀'