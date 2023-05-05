from enum import Enum

class Level(Enum):
    BEGINNER = (1, 16)
    INTERMEDIATE = (2, 17)
    ADVANCED = (3, 18)

    def __init__(self, level, threshold):
        self.level = level
        self.threshold = threshold

    def get_threshold(self):
        return self.threshold