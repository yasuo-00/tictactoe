import pygame as pg
import sys
import numpy as np
from graphics import initialize_board, draw_figures
from controllers import movement_controller



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
    is_player_one=True
    game_over = False
    # main loop
    # while user doesn't close application
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and not game_over:
                #get x,y position of mouse when it clicks
                #and transform into correspondent matrix position
                clicked_row = int(event.pos[1]//space_between_lines)
                clicked_col = int (event.pos[0] //space_between_columns)

                if(movement_controller.is_square_available(board, clicked_row, clicked_col)):
                    movement_controller.mark_square(board, clicked_row, clicked_col, is_player_one)
                    is_player_one= not is_player_one
                    
                    draw_figures.draw_figures(screen, board, space_between_columns, space_between_lines, (0,0,0), (255,255,255))

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    screen = restart_screen(width, height, bg_color,
                                                board_size, line_color, space_between_columns,
                                                space_between_lines, line_width)
                    board = restart_board(board)
                    is_player_one = True
        pg.display.update()

def restart_screen(width, height, bg_color,board_size, line_color, space_between_columns, space_between_lines, line_width):
    screen = initialize_board.initialize_board(width, height, bg_color,
                                                board_size, line_color, space_between_columns,
                                                space_between_lines, line_width)
    return screen

def restart_board(board):
    return np.zeros((len(board), len(board)))