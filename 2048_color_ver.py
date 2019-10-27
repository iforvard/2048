from colorama import Fore, Back, Style, init
from sys import platform
import random
import time
import keyboard
import os

init()
score = 0
color = {
    0: Back.LIGHTWHITE_EX,
    2: Back.BLUE,
    4: Back.YELLOW,
    8: Back.LIGHTBLACK_EX,
    16: Back.BLACK,
    32: Back.LIGHTCYAN_EX,
    64: Back.LIGHTGREEN_EX,
    128: Back.LIGHTMAGENTA_EX,
    256: Back.GREEN,
    512: Back.RED,
    1024: Back.WHITE,
    2048: Back.LIGHTRED_EX,
    4096: Back.MAGENTA
}


def color_print_row(stack_number):
    for num_row in range(3):
        for num in stack_number:
            if num_row in (0, 2):
                print(f"{color[num]}{' ' * 8}", end='')
            else:
                size = 8 - len(str(num))
                size_left = size // 2
                size_right = size - (size // 2)
                srt_and_num = f"{' ' * size_left}{num}{' ' * size_right}"
                print(f"{color[num]}{srt_and_num}", end='')
        print(Back.RESET)


def line_shift(line):
    global score
    new_row = []
    for num_line in line:
        if num_line != 0:
            if len(new_row) > 0:
                if new_row[-1][1] == 0:
                    if new_row[-1][0] == num_line:
                        new_row[-1] = [num_line * 2, 1]
                        score += num_line * 2
                    else:
                        new_row.append([num_line, 0])
                else:
                    new_row.append([num_line, 0])

            else:
                new_row.append([num_line, 0])

    # convert in stack
    stack_row = []
    for nun in new_row:
        if nun[0] != 0:
            stack_row.append(nun[0])
    size = 4 - len(stack_row)
    for num_line in range(size):
        stack_row.append(0)
    return stack_row


def gen_num():
    num = (random.choices([4, 2], weights=[10, 90]))[0]
    return num


def place_num_on_the_board():
    place_list = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                place_list.append((i, j))
    if len(place_list) == 0:
        print('GAME OVER!!!')
        exit(0)
    place = random.choice(place_list)
    board[place[0]][place[1]] = gen_num()


def gen_start_board(size_row=4, size_col=4):
    board = [[0] * size_row for i in range(size_col)]
    while True:
        gen_coordinate_num1 = [random.randint(0, 3), random.randint(0, 3)]
        gen_coordinate_num2 = [random.randint(0, 3), random.randint(0, 3)]
        if gen_coordinate_num1 != gen_coordinate_num2:
            break
    gen_num1 = gen_num()
    gen_num2 = gen_num()
    board[gen_coordinate_num1[0]][gen_coordinate_num1[1]] = gen_num1
    board[gen_coordinate_num2[0]][gen_coordinate_num2[1]] = gen_num2
    return board


def x_move(step):
    for index, row in enumerate(board):
        if step == 'left':
            board[index] = line_shift(row)
        if step == 'right':
            board[index] = line_shift(reversed(row))[::-1]


def y_move(step):
    for col_board in range(4):
        line = []
        for row_board in range(4):
            line.append(board[row_board][col_board])
        if step == 'down':
            line = line_shift(reversed(line))[::-1]
        if step == 'up':
            line = line_shift(line)
        for row_board in range(4):
            board[row_board][col_board] = line[row_board]


def print_game_screen():
    if platform == 'win32':
        os.system('cls')
    if 'linux' in platform:
        os.system('clear')

    print(Fore.LIGHTWHITE_EX + f'{"*" * 5} x - exit, r - restart {"*" * 5}')
    print('move: left, right, up, down')
    print(f'Score: {score}')
    for i in board:
        color_print_row(i)


board = gen_start_board()
while True:
    print_game_screen()
    time.sleep(0.5)
    step = keyboard.read_key()
    tmp_board = [row[:] for row in board]
    if step in ('right', 'left'):
        x_move(step)
    elif step in ('down', 'up'):
        y_move(step)
    elif step == 'r':
        board = gen_start_board()
        score = 0
        continue
    elif step == 'x':
        print('You pressed x - exit the game')
        exit(0)
    else:
        continue
    if tmp_board == board:
        continue
    place_num_on_the_board()
