def santa_position(matrix):
    result = []

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'S':
                result.append(r)
                result.append(c)
                break

    return result


def nice_kids_positions(matrix):
    result = []

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'V':
                result.append([r, c])

    return result


def get_kids(matrix, row, col):
    result = []
    possible = [
        [row, col - 1],
        [row, col + 1],
        [row + 1, col],
        [row - 1, col]

    ]
    for child_row, child_col in possible:
        if matrix[child_row][child_col] == 'V' or matrix[child_row][child_col] == 'X':
            result.append([child_row, child_col])

    return result


presents = int(input())
rows = int(input())

matrix = [list(input().split()) for x in range(rows)]

happy_kids = 0
left_kids = 0

command = input()

while command != 'Christmas morning':
    santa_coordinates = santa_position(matrix)
    current_row = santa_coordinates[0]
    current_col = santa_coordinates[1]
    next_row = 0
    next_col = 0
    nice_kids = nice_kids_positions(matrix)

    if command == 'up':
        next_row = current_row - 1
        next_col = current_col
    elif command == 'down':
        next_row = current_row + 1
        next_col = current_col
    elif command == 'right':
        next_row = current_row
        next_col = current_col + 1
    elif command == 'left':
        next_row = current_row
        next_col = current_col - 1

    if matrix[next_row][next_col] == 'X':
        matrix[next_row][next_col] = 'S'
        matrix[current_row][current_col] = '-'

    elif matrix[next_row][next_col] == 'V':
        matrix[next_row][next_col] = 'S'
        matrix[current_row][current_col] = '-'
        presents -= 1
        happy_kids += 1

    elif matrix[next_row][next_col] == '-':
        matrix[next_row][next_col] = 'S'
        matrix[current_row][current_col] = '-'

    elif matrix[next_row][next_col] == 'C':
        childs = get_kids(matrix, next_row, next_col)
        for gave_row, gave_col in childs:
            matrix[gave_row][gave_col] = '-'
            presents -= 1
            happy_kids += 1
        matrix[next_row][next_col] = 'S'
        matrix[current_row][current_col] = '-'


    nice_kids = nice_kids_positions(matrix)
    left_kids = len(nice_kids)

    if presents == 0:
        if left_kids > 0:
            print(f"Santa ran out of presents!")
        break

    # [print(" ".join(x)) for x in matrix]
    # print()

    command = input()

[print(" ".join(x)) for x in matrix]
if left_kids == 0:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {left_kids} nice kid/s.")
