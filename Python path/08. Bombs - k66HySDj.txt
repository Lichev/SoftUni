from collections import deque

def get_children(matrix, row, column):
    possible = [
        [row - 1, column - 1],
        [row - 1, column],
        [row - 1, column + 1],
        [row, column - 1],
        [row, column + 1],
        [row + 1, column - 1],
        [row + 1, column],
        [row + 1, column + 1]
    ]
    result = []

    for child_row , child_col in possible:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])

    return result


rows = int(input())

matrix = [list(map(int, input().split())) for x in range(rows)]

coordinates = deque(input().split())




while coordinates:
    current_coordinated = coordinates.popleft().split(",")
    row = int(current_coordinated[0])
    column = int(current_coordinated[1])

    power_of_bomb = matrix[row][column]

    if power_of_bomb <= 0:
        continue

    get = get_children(matrix, row, column)

    matrix[row][column] = 0
    for active_row, active_col in get:
        matrix[active_row][active_col] -= power_of_bomb


active_cells = 0
sum_active = 0
for r in matrix:
    for c in r:
        if c > 0:
            active_cells += 1
            sum_active += c

print(f'Alive cells: {active_cells}')
print(f'Sum: {sum_active}')
[print(f' '.join(map(str, x))) for x in matrix]
