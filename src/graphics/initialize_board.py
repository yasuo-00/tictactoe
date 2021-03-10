import pygame as pg
from graphics import draw_lines

def initialize_board(width, height, bg_color, board_size, line_color, space_between_columns, space_between_lines, line_width):
    # set window size
    screen = pg.display.set_mode((width, height))
    
    # set window background color
    screen.fill(bg_color)

    #draw lines on the board
    draw_lines.draw_board_lines(screen, board_size, line_color, space_between_columns, space_between_lines, line_width, width, height)
    return screen