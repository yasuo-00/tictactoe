from controllers import ai_controller
from classes.board import Board
from classes.ai import AI


def make_move(player, pos, board, is_player_one):
    if isinstance(player, AI):
        return ai_controller.make_move(board, player, is_player_one)
    else:
        board.mark_square(pos, is_player_one)
    return pos