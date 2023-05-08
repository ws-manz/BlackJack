class HandPlayerRect:
    def __init__(self, player, rects : list):
        self.__player = player
        self.__rects = rects

    def get_player(self):
        return self.__player

    def get_rects(self):
        return self.__rects