import random
import time

import keyboard


def line_shift(line):
    new_row = []
    for num_line in line:
        if num_line != 0:
            if len(new_row) > 0:
                if new_row[-1][1] == 0:
                    if new_row[-1][0] == num_line:
                        new_row[-1] = [num_line * 2, 1]
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


def gen_num_in_board():
    list_index_row = []
    num_list = []
    for index_row, row in enumerate(board):
        if 0 in row:
            list_index_row.append(index_row)
    if len(list_index_row) == 0:
        print('GAME OVER!!!')
        exit(0)
    row = random.choice(list_index_row)
    for index_num, num in enumerate(board[row]):
        if num == 0:
            num_list.append(index_num)
    num = random.choice(list_index_row)
    board[row][num] = gen_num()


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


board = gen_start_board()
print(f'{"*" * 5} x - exit, r - restart {"*" * 5}')
print('move: left, right, up, down')
for i in board:
    print(i)


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


while True:
    time.sleep(0.25)
    step = keyboard.read_key()
    if step in ('right', 'left'):
        x_move(step)
    if step in ('down', 'up'):
        y_move(step)
    if step in ('r'):
        print('NEW GAME:')
        board = gen_start_board()
    if step == 'x':
        exit(0)
    gen_num_in_board()
    print(f'{"*" * 5} x - exit, r - restart {"*" * 5}')
    print('move: left, right, up, down')
    for i in board:
        print(i)
