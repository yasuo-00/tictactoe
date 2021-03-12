import numpy as np

class Board():
    
    def __init__(self, board_size):
        self.__board=np.zeros((board_size, board_size))
        self.__size=board_size
    
    def mark_square(self, pos, is_player_one):
        self.__board[pos[0]][pos[1]]= 1 if is_player_one else -1

    def is_square_available(self, pos):
        if(pos[0]<0):
            return False
        # if position on board == 0 then it's available
        return self.__board[pos[0]][pos[1]] == 0

    def is_full(self):
        for row in self.__board:
            for e in row:
                if e==0:
                    return False
        return True

    def clear(self):
        self.__board=np.zeros((self.__size, self.__size))


    #changing board size will make new empty board with new size
    @property
    def size(self, board_size):
        self.__size=board_size
        #self.__board=np.zeros((board_size, board_size))
    
    @property
    def size(self):
        return self.__size
    
    def board_at(self, pos):
        return self.__board[pos[0]][pos[1]]