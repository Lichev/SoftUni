import re

matrix = [input().split() for x in range(6)]


first_position = input()


samle = r'[0-9]+'
matches = re.findall(samle, first_position)
row = int(matches[0])
col = int(matches[1])


command = input()
while command != 'Stop':

    data = command.split(", ")
    action = data[0]
    direction = data[1]

    if direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1

    if action == 'Create':
        value = data[2]
        if matrix[row][col] == '.':
            matrix[row][col] = value

    elif action == 'Update':
        value = data[2]
        if matrix[row][col] != '.':
            matrix[row][col] = value

    elif action == 'Delete':
        if matrix[row][col] != '.':
            matrix[row][col] = '.'

    elif action == 'Read':
        if matrix[row][col] != '.':
            print(matrix[row][col])

    command = input()

[print(" ".join(x)) for x in matrix]
