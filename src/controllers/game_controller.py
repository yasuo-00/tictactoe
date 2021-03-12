import pygame as pg
import sys
import numpy as np
from controllers import winner_controller, ai_controller
from classes.board import Board
from classes.painter import Painter

PLAYER_ONE_COLOR=(255,255,255)
PLAYER_TWO_COLOR=(0,0,0)

def initialize(width, height, board_size, bg_color, line_color, line_width):
    is_player_one=True
    game_over = False
    space_between_lines=height/board_size
    space_between_columns=width/board_size
    # initialize pygame
    pg.init()
    # set window title
    pg.display.set_caption('TIC TAC TOE')


    # initialize boar and screen
    board =Board(board_size)
    painter = Painter(line_width,line_color, height, width)
    painter.initialize_board_screen(bg_color, board_size, space_between_columns, space_between_lines)

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
                
                #if the square clicked is available, mark the square and check for win condition
                if(board.is_square_available((clicked_row, clicked_col))):
                    board.mark_square((clicked_row, clicked_col), is_player_one)
                    winner = winner_controller.check_win(board)
                    if(winner!=0):
                        if(is_player_one):
                            painter.draw_winner_line(winner, is_player_one, board.size, space_between_lines, space_between_columns, (clicked_row, clicked_col), PLAYER_ONE_COLOR)
                        else:
                            painter.draw_winner_line(winner, is_player_one, board.size, space_between_lines, space_between_columns, (clicked_row, clicked_col), PLAYER_TWO_COLOR)
                        print("Winner")
                        game_over=True

                    #is_player_one= not is_player_one
                    ai_controller.mark_square(board)
                    winner = winner_controller.check_win(board)
                    
                    painter.draw_figures_on_board(board, space_between_columns, space_between_lines, (0,0,0), (255,255,255))
            
            #check if player wants to reset game
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    painter.initialize_board_screen(bg_color, board_size, space_between_columns, space_between_lines)
                    board.clear()
                    is_player_one = True
                    game_over=False
        pg.display.update()