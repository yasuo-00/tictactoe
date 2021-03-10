from controllers import game_controller

#global variables
WIDTH = 900
HEIGHT = 900
LINE_WIDTH = 15
BOARD_SIZE = 3
# color section
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

def main():
    game_controller.initialize(WIDTH, HEIGHT, BOARD_SIZE, BG_COLOR, LINE_COLOR, LINE_WIDTH)


if __name__ == "__main__":
    main()