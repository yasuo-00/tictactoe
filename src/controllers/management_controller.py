# mark chosen square
# marks as 1 if it's player one and -1 if player 2
def mark_square(board, row, col, is_player_one):
    board[row][col] = 1 if is_player_one else -1

def is_square_available(board, row, col):
    # if position on board == 0 then it's available
    return board[row][col] == 0