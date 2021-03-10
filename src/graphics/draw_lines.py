import pygame as pg
#draw all lines of the board
def draw_board_lines(screen, board_size, line_color, space_between_columns, space_between_lines, line_width, board_width, board_height):
    for i in range(1,board_size):
        #horizontal lines
        pg.draw.line(screen, line_color, (0, space_between_lines*i), (board_width, space_between_lines*i), line_width)
        #vertical lines
        pg.draw.line(screen, line_color, (space_between_columns*i, 0), (space_between_columns*i, board_height), line_width)

#draw horizontal line in the middle of the line
def draw_horizontal_line(screen, board_width, board_line, space_between_lines, color):
    pg.draw.line(screen, color, (0,board_line*space_between_lines+(space_between_lines//2)), (board_width, board_line*space_between_lines+(space_between_lines//2)))

#draw vertical line in the middle of the column
def draw_vertical_line(screen, board_height, board_column, space_between_columns, color):
    pg.draw.line(screen, color, (board_column*space_between_columns+(space_between_columns//2),0), (board_column*space_between_columns+(space_between_columns//2), board_height))

#draw diagonal line across board
def draw_diagonal_line(screen, board_height, board_width, initial_cell, final_cell, color):
    return false