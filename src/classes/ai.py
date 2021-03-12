import random
from datetime import datetime

class AI ():
    
    def __init__(self, isRandom):
        self.__isRandom=isRandom
    

    def make_move(self, board_size):
        if self.__isRandom:
            return self.__random_move(board_size)
        else:
            return self.__random_move(board_size)



    def __random_move(self,board_size):
        random.seed(datetime.now())
        i = random.randint(0,board_size-1)
        j = random.randint(0,board_size-1)
        return (i,j)

    @property
    def isRandom(self):
        return self.__isRandom
    
    @property
    def isRandom(self, isRandom):
        self.__isRandom=isRandom