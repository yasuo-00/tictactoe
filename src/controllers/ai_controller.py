from controllers import winner_controller
from classes.board import Board
from classes.ai import AI
from copy import deepcopy
import sys


def make_move(board, ai, is_player_one):

    if ai.is_random:
        move = ai.make_move(board.size)
        # while ai move is invalid (square is occupied)
        while not board.is_square_available(move):
            move = ai.make_move(board.size)

        # marks on the board
        #board.mark_square(move, False)
        # return move position

    else:
        score, move = minmax(board, False,0)
        print(score)
    board.mark_square(move, is_player_one)
    return move


def minmax(board, is_max_player, depth):
    # copy original board
    # tmp_board=Board(board.size)
    # tmp_board=board
    #tmp_board = deepcopy(board)
    best_move = (-1, -1)

    if winner_controller.check_win(board) != 0:
        if is_max_player:
            return -1*depth, best_move  
        else:
            return 1*depth, best_move

    elif board.is_full():
        #print(board.board)
        #print("")
        return 0, best_move

    best_move_score =  -sys.maxsize if is_max_player else sys.maxsize

    for i in range(board.size):
        for j in range(board.size):
            if board.is_square_available((i,j)):
                board.mark_square((i,j), not is_max_player)
                score,_ = minmax(board, is_max_player, depth+1)
                #print(board.board)
                #print("")
                board.clear_square((i,j))
                if is_max_player:
                    if(best_move_score< score):
                        best_move_score=score
                        best_move=(i,j)
                else:
                    if(best_move_score> score):
                        best_move_score=score
                        best_move=(i,j)
    return best_move_score, best_move