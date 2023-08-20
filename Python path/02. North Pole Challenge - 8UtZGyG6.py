def count_items(matrix):
    items = 0

    for x in matrix:
        for c in x:
            if c != '.' and c != 'Y' and c != 'x':
                items += 1

    return items


def santa_position(matrix, rows, cols):
    position = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'Y':
                position.append(r)
                position.append(c)
    return position


def walk(matrix, direction, steps, rows, cols):
    santa_row, santa_col = santa_position(matrix, rows, cols)
    lst_with_items = []

    if direction == 'right':
        for x in range(int(steps)):
            santa_col += 1
            if santa_col > cols - 1:
                santa_col = 0
            lst_with_items.append([santa_row, santa_col])

    elif direction == 'left':
        for x in range(int(steps)):
            santa_col -= 1
            if santa_col < 0:
                santa_col = cols - 1
            lst_with_items.append([santa_row, santa_col])
    elif direction == 'up':
        for x in range(int(steps)):
            santa_row -= 1
            if santa_row < 0:
                santa_row = rows - 1
            lst_with_items.append([santa_row, santa_col])
    elif direction == 'down':
        for x in range(int(steps)):
            santa_row += 1
            if santa_row > rows - 1:
                santa_row = 0
            lst_with_items.append([santa_row, santa_col])

    return lst_with_items


rows, cols = map(int,input().split(", "))

matrix = []
for r in range(rows):
    current_row = input().split()
    matrix.append(current_row)

dct = {
    "Christmas decorations": 0,
    "Gifts": 0,
    'Cookies': 0
}

no_items = False
while True:
    command = input()

    if command == 'End':
        break

    directions, steps = command.split("-")
    positions_of_items = walk(matrix, directions, steps, rows, cols)
    santa_row, santa_col = santa_position(matrix, rows, cols)
    matrix[santa_row][santa_col] = 'x'

    for x in range(len(positions_of_items)):
        next_row, next_col = positions_of_items[x]
        if matrix[next_row][next_col] == 'D':
            dct['Christmas decorations'] += 1
        elif matrix[next_row][next_col] == 'G':
            dct['Gifts'] += 1
        elif matrix[next_row][next_col] == 'C':
            dct['Cookies'] += 1

        if x < len(positions_of_items) - 1:
            matrix[next_row][next_col] = 'x'

        else:
            matrix[next_row][next_col] = 'Y'

        items = count_items(matrix)
        if items == 0:
            matrix[next_row][next_col] = 'Y'
            no_items = True
            break
    if no_items:
        break
    #
    # [print(' '.join(x))for x in matrix]
    # print()

if no_items:
    print(f"Merry Christmas!")
print(f"You've collected:")
[print(f'- {value} {key}') for key, value in dct.items()]
[print(' '.join(x))for x in matrix]