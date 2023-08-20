rows = int(input())

matrix = [list(map(int, input().split())) for x in range(rows)]

while True:
    command = input()

    if command == 'END':
        break

    data = command.split()
    action = data[0]
    row = int(data[1])
    col = int(data[2])
    value = int(data[3])

    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if action == 'Add':
            matrix[row][col] += value
        else:
            matrix[row][col] -= value

    else:
        print(f'Invalid coordinates')


[print(' '.join(map(str, x))) for x in matrix]
