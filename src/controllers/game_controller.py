import pygame as pg
import sys
import numpy as np
from controllers import winner_controller, ai_controller, move_controller
from classes.board import Board
from classes.painter import Painter
from classes.ai import AI

PLAYER_ONE_COLOR=(255,255,255)
PLAYER_TWO_COLOR=(0,0,0)

def initialize(width, height, board_size, bg_color, line_color, line_width):
    ai = AI(False, False)
    ai_enabled=True
    player_turn=True
    is_player_one=True
    game_over = False
    pos=(-1,-1)
    win_condition=0
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
        pg.display.update()
        game_over= (board.is_full() or win_condition!=0)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            #if game is not over
            if not game_over:

                #check if someone won
                win_condition = winner_controller.check_win(board)
                
                #if no one won yet
                if(win_condition==0):
                    if ai_enabled:
                        if not player_turn:
                            pos = move_controller.make_move(ai, None, board, is_player_one)
                            painter.draw_figures_on_board(board, space_between_columns, space_between_lines, (0,0,0), (255,255,255))
                            is_player_one = not is_player_one
                            player_turn = not player_turn
                            #print(pos)
                            #print("Changed")
                else:
                    #since is_player_one status has already changed
                    if not is_player_one:
                        painter.draw_winner_line(win_condition, is_player_one, board.size, space_between_lines, space_between_columns, pos, PLAYER_ONE_COLOR)
                    else:
                        painter.draw_winner_line(win_condition, is_player_one, board.size, space_between_lines, space_between_columns, pos, PLAYER_TWO_COLOR)
                    print("Winner")
                    print(win_condition)
                
                # read move while game is not over and is player turn (if ai is enabled)
                if event.type == pg.MOUSEBUTTONDOWN and player_turn:
                    #get x,y position of mouse when it clicks
                    #and transform into correspondent matrix position
                    clicked_row = int(event.pos[1]//space_between_lines)
                    clicked_col = int (event.pos[0] //space_between_columns)
                    pos=(clicked_row,clicked_col)

                    if(board.is_square_available(pos)):
                        move_controller.make_move("player", pos, board, is_player_one)
                        if ai_enabled:
                            player_turn = not player_turn
                        is_player_one = not is_player_one
                    
                    painter.draw_figures_on_board(board, space_between_columns, space_between_lines, (0,0,0), (255,255,255))
                    

            #check if player wants to reset game
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    painter.initialize_board_screen(bg_color, board_size, space_between_columns, space_between_lines)
                    board.clear()
                    #is_player_one = not is_player_one
                    game_over=False
                    pos=(-1,-1)
                    #player_turn= not player_turn
                    win_condition=0