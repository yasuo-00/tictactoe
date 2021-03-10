import pygame as pg
import sys
import numpy as np
from graphics import initialize_board, draw_figures


# mark chosen square
# marks as 1 if it's player one and -1 if player 2
def mark_square(board, row, col, is_player_one):
    board[row][col] = 1 if is_player_one else -1

def is_square_available(board, row, col):
    # if position on board == 0 then it's available
    return board[row][col] == 0


def initialize(width, height, board_size, bg_color, line_color, line_width):
    space_between_lines=height/board_size
    space_between_columns=width/board_size
    # initialize pygame
    pg.init()
    # set window title
    pg.display.set_caption('TIC TAC TOE')
    # paint empty board
    screen = initialize_board.initialize_board(width, height, bg_color,
                                                board_size, line_color, space_between_columns,
                                                space_between_lines, line_width)

    # initialize board matrix
    board = np.zeros((board_size, board_size))
    player=True
    # main loop
    # while user doesn't close application
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                #get x,y position of mouse when it clicks
                #and transform into correspondent matrix position
                clicked_row = int(event.pos[1]//space_between_lines)
                clicked_col = int (event.pos[0] //space_between_columns)

                if(is_square_available(board, clicked_row, clicked_col)):
                    mark_square(board, clicked_row, clicked_col, player)
                    player= not player
                    #print(board)
                    
                    draw_figures.draw_figures(screen, board, space_between_columns, space_between_lines, (0,0,0), (255,255,255))


        pg.display.update()
