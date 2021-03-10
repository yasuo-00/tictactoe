import pygame as pg
import sys
import numpy as np
from graphics import initialize_board, draw_figures, draw_lines
from controllers import movement_controller, winner_controller

PLAYER_ONE_COLOR=(255,255,255)
PLAYER_TWO_COLOR=(0,0,0)

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
    
            # read move while game is not over
            if event.type == pg.MOUSEBUTTONDOWN and not game_over:
                #get x,y position of mouse when it clicks
                #and transform into correspondent matrix position
                clicked_row = int(event.pos[1]//space_between_lines)
                clicked_col = int (event.pos[0] //space_between_columns)

                if(movement_controller.is_square_available(board, clicked_row, clicked_col)):
                    movement_controller.mark_square(board, clicked_row, clicked_col, is_player_one)
                    winner = winner_controller.check_win(board)
                    if(winner!=0):
                        if(is_player_one):
                            draw_lines.draw_winner_line(screen, winner, is_player_one, board_size, height, width, space_between_lines, space_between_columns, (clicked_row, clicked_col), line_width, PLAYER_ONE_COLOR)
                        else:
                            draw_lines.draw_winner_line(screen, winner, is_player_one, board_size, height, width, space_between_lines, space_between_columns, (clicked_row, clicked_col), line_width, PLAYER_TWO_COLOR)
                        print("Winner")
                        game_over=True

                    is_player_one= not is_player_one
                    
                    draw_figures.draw_figures(screen, board, space_between_columns, space_between_lines, (0,0,0), (255,255,255))

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    screen = restart_screen(width, height, bg_color,
                                                board_size, line_color, space_between_columns,
                                                space_between_lines, line_width)
                    board = restart_board(board)
                    is_player_one = True
                    game_over=False
        pg.display.update()

#restart screen with initial screen
def restart_screen(width, height, bg_color,board_size, line_color, space_between_columns, space_between_lines, line_width):
    screen = initialize_board.initialize_board(width, height, bg_color,
                                                board_size, line_color, space_between_columns,
                                                space_between_lines, line_width)
    return screen

#overwrite board with 0 (empty)
def restart_board(board):
    return np.zeros((len(board), len(board)))