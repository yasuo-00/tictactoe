import random
from datetime import datetime


class AI ():

    def __init__(self, is_random, first_player):
        self.__is_random = is_random
        self.__first_player = first_player

    def make_move(self, board_size):
        if self.__is_random:
            return self.__random_move(board_size)
        else:
            return self.__random_move(board_size)

    def __random_move(self, board_size):
        random.seed(datetime.now())
        i = random.randint(0, board_size-1)
        j = random.randint(0, board_size-1)
        return (i, j)

    @property
    def is_random(self):
        return self.__is_random

    @is_random.setter
    def is_random(self, is_random):
        self.__is_random = is_random

    @property
    def first_player(self):
        return self.__is_random

