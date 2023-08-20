def miner_position(matrix):
    coordinates = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 's':
                coordinates.extend([row, col])
                break

    return coordinates


def check_coals(matrix, rows):
    count = 0

    for x in range(rows):
        count += matrix[x].count('c')

    return count


def validation_index(matrix, row, col):
    validation = False
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        validation = True

    return validation


rows = int(input())
movements = list(input().split())
matrix = [input().split() for x in range(rows)]


game_over = False

for move in movements:
    miner_row, miner_col = miner_position(matrix)
    number_of_coals = check_coals(matrix, rows)
    count_coals = number_of_coals

    if number_of_coals == 0:
        break

    if move == 'left':
        left_column = miner_col - 1
        left_row = miner_row
        left_valid = validation_index(matrix, left_row, left_column)

        if left_valid:
            if matrix[left_row][left_column] == 'e':
                matrix[left_row][left_column] = 's'
                matrix[miner_row][miner_col] = '*'
                game_over = True
                break
            elif matrix[left_row][left_column] == 'c':
                matrix[left_row][left_column] = 's'
                matrix[miner_row][miner_col] = '*'
            else:
                matrix[left_row][left_column] = 's'
                matrix[miner_row][miner_col] = '*'
    elif move == 'right':
        right_column = miner_col + 1
        right_row = miner_row
        right_valid = validation_index(matrix, right_row, right_column)

        if right_valid:
            if matrix[right_row][right_column] == 'e':
                matrix[right_row][right_column] = 's'
                matrix[miner_row][miner_col] = '*'
                game_over = True
                break
            elif matrix[right_row][right_column] == 'c':
                matrix[right_row][right_column] = 's'
                matrix[miner_row][miner_col] = '*'
            else:
                matrix[right_row][right_column] = 's'
                matrix[miner_row][miner_col] = '*'
    elif move == 'up':
        up_row = miner_row - 1
        up_column = miner_col
        up_validation = validation_index(matrix, up_row, up_column)

        if up_validation:
            if matrix[up_row][up_column] == 'e':
                matrix[up_row][up_column] = 's'
                matrix[miner_row][miner_col] = '*'
                game_over = True
                break
            elif matrix[up_row][up_column] == 'c':
                matrix[up_row][up_column] = 's'
                matrix[miner_row][miner_col] = '*'
            else:
                matrix[up_row][up_column] = 's'
                matrix[miner_row][miner_col] = '*'

    elif move == 'down':
        down_row = miner_row + 1
        down_col = miner_col
        down_validation = validation_index(matrix, down_row, down_col)

        if down_validation:
            if matrix[down_row][down_col] == 'e':
                matrix[down_row][down_col] = 's'
                matrix[miner_row][miner_col] = '*'
                game_over = True
                break
            elif matrix[down_row][down_col] == 'c':
                matrix[down_row][down_col] = 's'
                matrix[miner_row][miner_col] = '*'
            else:
                matrix[down_row][down_col] = 's'
                matrix[miner_row][miner_col] = '*'

    # [print(' '.join(x)) for x in matrix]
    # print()


last_row, last_col = miner_position(matrix)
count_coals = check_coals(matrix, rows)
if game_over:
    print(f"Game over! ({last_row}, {last_col})")
elif count_coals == 0:
    print(f"You collected all coal! ({last_row}, {last_col})")
elif count_coals > 0:
    print(f'{count_coals} pieces of coal left. ({last_row}, {last_col})')