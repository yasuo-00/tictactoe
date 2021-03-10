import pygame as pg
#draw all lines of the board
def draw_board_lines(screen, board_size, line_color, space_between_columns, space_between_lines, line_width, screen_width, screen_height):
    for i in range(1,board_size):
        #horizontal lines
        pg.draw.line(screen, line_color, (0, space_between_lines*i), (screen_width, space_between_lines*i), line_width)
        #vertical lines
        pg.draw.line(screen, line_color, (space_between_columns*i, 0), (space_between_columns*i, screen_height), line_width)

#draw horizontal line in the middle of the line
def draw_horizontal_line(screen, screen_width, board_line, space_between_lines, color, line_width):
    pg.draw.line(screen, color, (0,board_line*space_between_lines+(space_between_lines//2)), (screen_width, board_line*space_between_lines+(space_between_lines//2)), line_width)

#draw vertical line in the middle of the column
def draw_vertical_line(screen, screen_height, board_column, space_between_columns, color, line_width):
    pg.draw.line(screen, color, (board_column*space_between_columns+(space_between_columns//2),0), (board_column*space_between_columns+(space_between_columns//2), screen_height), line_width)

#draw diagonal line across board
def draw_diagonal_line(screen, screen_height, screen_width, board_size, clicked_cell_pos, color, line_width):
    #check if it's to draw primary or secondary diagonal
    if(clicked_cell_pos==(0,0) or clicked_cell_pos==(board_size-1, board_size-1)):
        pg.draw.line(screen, color,(0,0), (screen_height, screen_width), line_width)
    else:
        pg.draw.line(screen, color,(0,screen_width), (screen_height, 0), line_width)


def draw_winner_line(screen, win_condition, is_player_one, board_size, screen_height, screen_width, space_between_lines, space_between_columns, clicked_pos, line_width, color):
        if(win_condition==1):
            draw_horizontal_line(screen, screen_width, clicked_pos[0], space_between_lines, color, line_width)
        elif(win_condition ==2):
            draw_vertical_line(screen, screen_height, clicked_pos[1], space_between_columns, color, line_width)
        else:
            draw_diagonal_line(screen, screen_height, screen_width, board_size, clicked_pos, color, line_width)