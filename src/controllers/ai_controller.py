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
        score, move = minimax(board, is_player_one,0)
        print(score)
    board.mark_square(move, is_player_one)
    return move


def minimax(board, is_max_player, depth, alpha=-sys.maxsize, beta=sys.maxsize, move=None):

    if winner_controller.check_win(board) != 0:
        if is_max_player:
            return -1, move
        else:
            return 1*(depth+1), move
    elif board.is_full():
        return 0, move

    if is_max_player:
        max_score = -sys.maxsize
        for i in range(board.size):
            for j in range(board.size):
                if board.is_square_available((i, j)):
                    board.mark_square((i, j), True)
                    score,_ = minimax(board, False, depth + 1, alpha, beta)
                    board.clear_square((i, j))

                    if score > max_score:
                        max_score = score
                        alpha = score
                        move = (i, j)
                    if alpha >= beta:
                        break
        return max_score, move

    else:
        min_score = sys.maxsize
        for i in range(board.size):
            for j in range(board.size):
                if board.is_square_available((i, j)):
                    board.mark_square((i, j), False)
                    score,_ = minimax(board, True, depth + 1, alpha, beta)
                    board.clear_square((i, j))

                    if score < min_score:
                        min_score = score
                        beta = score
                        move = (i, j)

                    if alpha >= beta:
                        break
        return min_score, move
