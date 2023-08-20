import sys


def postion(matrix, rows):
    coordinates = []

    for r in range(rows):
        for c in range(rows):
            if matrix[r][c] == 'B':
                coordinates.append(r)
                coordinates.append(c)
                break
    return coordinates


def up(matrix, row, col):
    up_coordinates = []

    for r in range(row - 1, -1, - 1):
        if matrix[r][col] != 'X':
            up_coordinates.append([r, col])
        else:
            break
    return  up_coordinates


def down(matrix, row, col):
    down_coordinates = []

    for r in range(row + 1, len(matrix)):
        if matrix[r][col] != 'X':
            down_coordinates.append([r, col])
        else:
            break
    return down_coordinates


def right(matrix, row, col):
    left_coordinates = []

    for c in range(col + 1, len(matrix)):
        if matrix[row][c] != 'X':
            left_coordinates.append([row, c])
        else:
            break
    return left_coordinates


def left(matrix, row, col):
    right_coordinates = []

    for c in range(col - 1, -1, -1):
        if matrix[row][c] != 'X':
            right_coordinates.append([row, c])
        else:
            break
    return right_coordinates


def final_calculate(matrix, matrix_coordinaton):
    result = 0
    for row, col in matrix_coordinaton:
        result += int(matrix[row][col])

    return (result)


row = int(input())
matrix = [input().split() for x in range(row)]
movements = ['up', 'down', 'left', 'right']

winner_coordinates = []
winner_result = -sys.maxsize
direction = ''

for x in movements:
    current_movement = x
    bunny_row, bunny_col = postion(matrix, row)
    current_coordinates = []

    if current_movement == 'up':
        current_coordinates = up(matrix, bunny_row, bunny_col)

    elif current_movement == 'down':
        current_coordinates = down(matrix, bunny_row, bunny_col)

    elif current_movement == 'left':
        current_coordinates = left(matrix, bunny_row, bunny_col)

    elif current_movement == 'right':
        current_coordinates = right(matrix, bunny_row, bunny_col)


    temp_result = final_calculate(matrix, current_coordinates)

    if temp_result > winner_result and current_coordinates:
        winner_result = temp_result
        winner_coordinates = current_coordinates
        direction = current_movement


print(direction)
[print(x) for x in winner_coordinates]
print(winner_result)
