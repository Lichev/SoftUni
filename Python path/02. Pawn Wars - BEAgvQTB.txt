from collections import deque

def board(row, col):
    result = ''
    if col == 0:
        result += 'a'
    elif col == 1:
        result += 'b'
    elif col == 2:
        result += 'c'
    elif col == 3:
        result += 'd'
    elif col == 4:
        result += 'e'
    elif col == 5:
        result += 'f'
    elif col == 6:
        result += 'g'
    elif col == 7:
        result += 'h'


    if row == 0:
        result += '8'
    elif row == 1:
        result += '7'
    elif row == 2:
        result += '6'
    elif row == 3:
        result += '5'
    elif row == 4:
        result += '4'
    elif row == 5:
        result += '3'
    elif row == 6:
        result += '2'
    elif row == 7:
        result += '1'


    return result


def white_attack(matrix, row, col):
    result = []
    lst = [
        [row - 1, col + 1],
        [row - 1, col - 1]
    ]

    for child_row, child_col in lst:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix):
            if matrix[child_row][child_col] == 'b':
                result.append(child_row)
                result.append(child_col)

    return result


def black_attack(matrix, row, col):
    result = []
    lst = [
        [row + 1, col + 1],
        [row + 1, col - 1]
    ]

    for child_row, child_col in lst:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix):
            if matrix[child_row][child_col] == 'w':
                result.append(child_row)
                result.append(child_col)

    return result

matrix = []
white = []
black = []

for r in range(8):
    columns = input().split()
    matrix.append(columns)
    for c in range(len(columns)):
        if columns[c] == 'w':
            white.append(r)
            white.append(c)
        elif columns[c] == 'b':
            black.append(r)
            black.append(c)


turns = deque(['white', 'black'])

while True:
    current_turn = turns.popleft()
    turns.append(current_turn)

    if current_turn == 'white':
        white_row, white_col = white

        w = white_attack(matrix, white_row, white_col)

        if w:
            print(f'Game over! White win, capture on {board(w[0], w[1])}.')
            break
        else:
            matrix[white_row][white_col] = '-'
            white_row -= 1
            matrix[white_row][white_col] = 'w'

        if white_row == 0:
            print(f"Game over! White pawn is promoted to a queen at {board(white_row, white_col)}.")
            break

        white = [white_row, white_col]

    else:
        black_row, black_col = black

        b = black_attack(matrix, black_row, black_col)
        if b:
            print(f'Game over! Black win, capture on {board(b[0], b[1])}.')
            break
        else:
            matrix[black_row][black_col] = '-'
            black_row += 1
            matrix[black_row][black_col] = 'b'

        if black_row == 7:
            print(f"Game over! Black pawn is promoted to a queen at {board(black_row, black_col)}.")
            break

        black = [black_row, black_col]

        # [print(' '.join(x))for x in matrix]
        # print()