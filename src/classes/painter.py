import pygame as pg
from classes.board import Board

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25


class Painter():
    def __init__(self, line_width, line_color, screen_height, screen_width):
        self.__line_width=line_width
        self.__line_color=line_color
        self.__screen_height = screen_height
        self.__screen_width = screen_width
        self.__screen = pg.display.set_mode((screen_width, screen_height))

#-----------------GETTERS AND SETTERS-------------------
    @property
    def line_width(self):
        return self.__line_width

    @property
    def line_color(self):
        return self.__line_color
    
    @property
    def screen_height(self):
        return self.__screen_height

    @property
    def screen_width(self):
        return self.__screen_width

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, screen):
        self.__screen = screen


    
#-----------------PUBLIC METHODS-------------------------

    def initialize_board_screen(self, bg_color, board_size, space_between_columns, space_between_lines):
        # set window background color
        self.__screen.fill(bg_color)
        # draw lines on the board
        self.__draw_board_lines(board_size, space_between_columns, space_between_lines)

    #iterate through board and draw its correspondent figures(circle, cross) on the marked squares
    def draw_figures_on_board(self, board, space_between_columns, space_between_lines, circle_color, cross_color):
        for row in range(board.size):
            for col in range(board.size):
                if board.board_at((row,col)) == -1:
                    self.__draw_circle(col, row, space_between_columns, space_between_lines, circle_color)

                elif board.board_at((row,col)) == 1:
                    self.__draw_cross(col, row, space_between_columns, space_between_lines, cross_color)

    def draw_winner_line(self, win_condition, is_player_one, board_size, space_between_lines, space_between_columns, clicked_pos, color):
            if(win_condition==1):
                self.__draw_horizontal_line( clicked_pos[0], space_between_lines, color)
            elif(win_condition ==2):
                self.__draw_vertical_line( clicked_pos[1], space_between_columns, color)
            else:
                self.__draw_diagonal_line(board_size, win_condition, color)


#---------------PRIVATE METHODS-------------------------
    def __draw_board_lines(self, board_size, space_between_columns, space_between_lines):
        for i in range(1,board_size):
            #horizontal lines
            pg.draw.line(self.__screen, self.__line_color, (0, space_between_lines*i), (self.__screen_width, space_between_lines*i), self.__line_width)
            #vertical lines
            pg.draw.line(self.__screen, self.__line_color, (space_between_columns*i, 0), (space_between_columns*i, self.__screen_height), self.__line_width)

    def __draw_circle(self, col, row, space_between_columns, space_between_lines, circle_color):
        # get circle radius based on the smaller space
        circle_radius = int(
            (min(space_between_columns, space_between_lines))//3)
        # get cell center coordinates ((x1+x2)/2,(y1+,y2)/2)
        circle_center_x = int(((col * space_between_columns) +
                               (col * space_between_columns+space_between_columns))//2)
        circle_center_y = int(
            ((row * space_between_lines+space_between_lines)+(row * space_between_lines))//2)

        pg.draw.circle(self.__screen, circle_color,
                        (circle_center_x, circle_center_y),
                        circle_radius, CIRCLE_WIDTH)

    def __draw_cross(self, col, row, space_between_columns, space_between_lines, cross_color):
        cross_padding=int(
                        (min(space_between_columns, space_between_lines))//4)
        
        #draw primary diagonal
        pg.draw.line(self.__screen, cross_color,
                                 (col * space_between_columns+cross_padding, row *
                                space_between_lines+space_between_lines-cross_padding),
                                 (col * space_between_columns+space_between_columns -
                                  cross_padding, row * space_between_lines+cross_padding),
                                CROSS_WIDTH)

        #draw secondary diagonal
        pg.draw.line(self.__screen, cross_color,
                                 (col * space_between_columns+cross_padding,
                                row*space_between_lines+cross_padding),
                                 (col * space_between_columns+space_between_columns-cross_padding,
                                  row * space_between_lines+space_between_lines-cross_padding),
                                CROSS_WIDTH)

    #draw horizontal line in the middle of the line
    def __draw_horizontal_line(self, board_line, space_between_lines, color):
        pg.draw.line(self.__screen, color, (0,board_line*space_between_lines+(space_between_lines//2)), (self.__screen_width, board_line*space_between_lines+(space_between_lines//2)), self.__line_width)

    #draw vertical line in the middle of the column
    def __draw_vertical_line(self, board_column, space_between_columns, color):
        pg.draw.line(self.__screen, color, (board_column*space_between_columns+(space_between_columns//2),0), (board_column*space_between_columns+(space_between_columns//2), self.__screen_height), self.__line_width)

    #draw diagonal line across board
    def __draw_diagonal_line(self, board_size, win_condition, color):
        #check if it's to draw primary or secondary diagonal
        if win_condition==3:
            pg.draw.line(self.__screen, color,(0,0), (self.__screen_height, self.__screen_width), self.__line_width)
        else:
            pg.draw.line(self.__screen, color,(0,self.__screen_width), (self.__screen_height, 0), self.__line_width)
