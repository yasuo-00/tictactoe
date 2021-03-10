import numpy as np

# check if someone won
# 0 - no one won
# 1 - Horizontal Win
# 2 - Vertical Win
# 3 - Diagonal Win
def check_win(board):
    col_sum = np.zeros((len(board)))
    prim_diag_sum = 0
    sec_diag_sum = 0

    for row in range(len(board)):
        board_size = len(board)
        # print(board_size)
        sec_diag_sum += board[row][board_size-1-row]
        row_sum = 0
        for col in range(len(board[0])):
            col_sum[col] += board[row][col]
            row_sum += board[row][col]
            if row == col:
                prim_diag_sum += board[row][col]
        # check if row has the winner sum (size of the board or size of the board * -1)
        if(row_sum == board_size or row_sum == (board_size*-1)):
            return 1  # "Horizontal"

    # check if one of the columns has the winner sum (size of the board or size of the board * -1)
    if(board_size in col_sum or (board_size*-1) in col_sum):
        return 2  # "Vertical Win"

    # check if either diagonals has the winner sum (size of the board or size of the board * -1)
    if((prim_diag_sum == board_size or prim_diag_sum == (board_size*-1)) or (sec_diag_sum == board_size or sec_diag_sum == (board_size*-1))):
        return 3  # "Diagonal Win"

    return 0
