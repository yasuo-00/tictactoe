import pygame as pg

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25


def draw_figures(screen, board, space_between_columns, space_between_lines, circle_color, cross_color):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == -1:
                # get circle radius based on the smaller space
                circle_radius = int(
                    (min(space_between_columns, space_between_lines))//3)
                #get cell center coordinates ((x1+x2)/2,(y1+,y2)/2)
                circle_center_x = int(((col * space_between_columns)+(col * space_between_columns+space_between_columns))//2)
                circle_center_y = int(((row * space_between_lines+space_between_lines)+(row * space_between_lines))//2)
                
                pg.draw.circle(screen, circle_color,
                                (circle_center_x, circle_center_y),
                                circle_radius, CIRCLE_WIDTH)

            elif board[row][col] == 1:
                cross_padding = int((min(space_between_columns, space_between_lines))//4)

                pg.draw.line(screen, cross_color,
                             (col * space_between_columns+cross_padding, row *
                                space_between_lines+space_between_lines-cross_padding),
                             (col * space_between_columns+space_between_columns -
                              cross_padding, row * space_between_lines+cross_padding),
                            CROSS_WIDTH)

                pg.draw.line(screen, cross_color,
                             (col * space_between_columns+cross_padding,
                            row*space_between_lines+cross_padding),
                             (col * space_between_columns+space_between_columns-cross_padding,
                              row * space_between_lines+space_between_lines-cross_padding),
                            CROSS_WIDTH)
