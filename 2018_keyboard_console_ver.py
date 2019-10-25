import random
import time
import keyboard

score = 0
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
    if step not in ('right', 'left', 'down', 'up', 'r', 'x'):
        continue
    if step in ('right', 'left'):
        x_move(step)
    if step in ('down', 'up'):
        y_move(step)
    if step == 'r':
        print('NEW GAME:')
        board = gen_start_board()
    if step == 'x':
        print('You pressed x - exit the game')
        exit(0)
    place_num_on_the_board()
    print(f'{"*" * 5} x - exit, r - restart {"*" * 5}')
    print('move: left, right, up, down')
    print(f'Score: {score}')
    for i in board:
        print(i)
