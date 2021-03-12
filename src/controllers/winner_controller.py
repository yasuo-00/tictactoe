import numpy as np
from classes.board import Board
# check if someone won
# 0 - no one won
# 1 - Horizontal Win
# 2 - Vertical Win
# 3 - Diagonal Win
def check_win(board):
    teste = board.size
    col_sum = np.zeros(teste)
    prim_diag_sum = 0
    sec_diag_sum = 0

    for row in range(board.size):
        sec_diag_sum += board.board_at((row,board.size-1-row))
        row_sum = 0
        for col in range(board.size):
            col_sum[col] += board.board_at((row,col))
            row_sum += board.board_at((row,col))
            if row == col:
                prim_diag_sum += board.board_at((row,col))
        # check if row has the winner sum (size of the board or size of the board * -1)
        if(row_sum == board.size or row_sum == (board.size*-1)):
            return 1  # "Horizontal"

    # check if one of the columns has the winner sum (size of the board or size of the board * -1)
    if(board.size in col_sum or (board.size*-1) in col_sum):
        return 2  # "Vertical Win"

    # check if either diagonals has the winner sum (size of the board or size of the board * -1)
    if((prim_diag_sum == board.size or prim_diag_sum == (board.size*-1)) or (sec_diag_sum == board.size or sec_diag_sum == (board.size*-1))):
        return 3  # "Diagonal Win"

    return 0
