import pygame as pg
#draw all lines of the board
def draw_lines(screen, board_size, line_color, space_between_columns, space_between_lines, line_width, board_width, board_height):
    for i in range(1,board_size):
        #horizontal lines
        pg.draw.line(screen, line_color, (0, space_between_lines*i), (board_width, space_between_lines*i), line_width)
        #vertical lines
        pg.draw.line(screen, line_color, (space_between_columns*i, 0), (space_between_columns*i, board_height), line_width)

#draw a line on the board
def draw_line(screen, line_color, initial_pos, final_pos, width):
    return false