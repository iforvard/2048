import random

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
print(f'{"*" * 5} x - exit {"*" * 5}')
print('move: left, right, up, down, restart, x')
for i in board:
    print(i)


def x_move(step):
    coordinate_line = []
    coordinate_col = []
    for index, row in enumerate(board):
        if step == 'left':
            board[index] = line_shift(row)
        if step == 'right':
            board[index] = line_shift(reversed(row))[::-1]
        if 0 in row:
            coordinate_line.append(index)
    coordinate_line = random.choices(coordinate_line)[0]
    for index_num, num in enumerate(board[coordinate_line]):
        if num == 0:
            coordinate_col.append(index_num)
    coordinate_col = random.choices(coordinate_col)[0]
    board[coordinate_line][coordinate_col] = gen_num()


def y_move(step):
    coordinate_line = []
    coordinate_col = []
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
        if 0 in line:
            coordinate_line.append(col_board)

    coordinate_line = random.choices(coordinate_line)[0]
    for index, num in enumerate(board[coordinate_line]):
        if num == 0:
            coordinate_col.append(index)
    coordinate_col = random.choices(coordinate_col)[0]
    board[coordinate_line][coordinate_col] = gen_num()


while True:
    step = input('Enter move: ')
    if step in ('right', 'left'):
        x_move(step)
    if step in ('down', 'up'):
        y_move(step)
    if step in ('c', 'clear', 'now', 'restart'):
        board = gen_start_board()
    if step == 'x':
        exit(0)
    print(f'{"*" * 5} x - exit {"*" * 5}')
    print('move: left, right, up, down, restart, x')
    for i in board:
        print(i)
