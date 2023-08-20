rows, columns = tuple(map(int, input().split()))

matrix = []

start = 97

for row in range(rows):
    current_column = []
    second = start
    for colum in range(columns):
        text = ''
        text += chr(start)
        text += chr(second)
        text += chr(start)

        second += 1

        current_column.append(text)

    matrix.append(current_column)
    start += 1

[print(' '.join(x)) for x in matrix]