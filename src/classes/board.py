import numpy as np


class Board():

    def __init__(self, board_size):
        self.__board = np.zeros((board_size, board_size))
        self.__size = board_size

    def mark_square(self, pos, is_player_one):
        self.__board[pos[0]][pos[1]] = 1 if is_player_one else -1

    def is_square_available(self, pos):
        if(pos[0] < 0):
            return False
        # if position on board == 0 then it's available
        return self.__board[pos[0]][pos[1]] == 0

    def is_full(self):
        for row in self.__board:
            for e in row:
                if e == 0:
                    return False
        return True
    
    def num_available_spaces(self):
        count =0
        for row in self.__board:
            for e in row:
                if e == 0:
                    count+=1
        return count
    
    def count_pieces_on_row(self, is_player_one, row):
        count =0
        for i in range(self.__board_size):
            if is_player_one:
                if self.__board[row][i]==1:
                    count+=1
            else:
                if self.__board[row][i]==-1:
                    count+=1
        return count

    def count_pieces_on_col(self, is_player_one, col):
        count =0
        for i in range(self.__board_size):
            if is_player_one:
                if self.__board[i][col]==1:
                    count+=1
            else:
                if self.__board[i][col]==-1:
                    count+=1
        return count

    def count_pieces_on_primary_diag(self, is_player_one):
        count =0
        for i in range(self.__board_size):
            if is_player_one:
                if self.__board[i][i]==1:
                    count+=1
            else:
                if self.__board[i][i]==-1:
                    count+=1
        return count
    
    def count_pieces_on_secondary_diag(self, is_player_one):
        count =0
        for i in range(self.__board_size):
            if is_player_one:
                if self.__board[i][i]==1:
                    count+=1
            else:
                if self.__board[i][i]==-1:
                    count+=1
        return count
    
    def clear(self):
        self.__board = np.zeros((self.__size, self.__size))

    # changing board size will make new empty board with new size

    @property
    def size(self):
        return self.__size

    def board_at(self, pos):
        return self.__board[pos[0]][pos[1]]
    
    def clear_square(self, pos):
        self.__board[pos[0]][pos[1]]=0

    @property
    def board(self):
        return self.__board