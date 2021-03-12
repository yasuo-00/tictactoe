from classes.board import Board
from classes.ai import AI

def mark_square(board):
    ai = AI(True)

    move = ai.make_move(board.size)
    while not board.is_square_available(move):
        move = ai.make_move(board.size)
    
    board.mark_square(move, False)