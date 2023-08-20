rows, columns = tuple(map(int, input().split(", ")))

matrix = []

for i in range(rows):
    text = [int(x) for x in input().split(", ")]
    matrix.append(text)


result = 0
new_lst = []

for row in range(rows):
    for col in range(columns - 1):
        if row < len(matrix) - 1:
            first = [matrix[row][col], matrix[row][col + 1]]
            second = [matrix[row+1][col], matrix[row+1][col + 1]]
        else:
            first = [matrix[row-1][col], matrix[row-1][col + 1]]
            second = [matrix[row][col], matrix[row][col + 1]]

        current_result = sum(first) + sum(second)

        if current_result > result:
            result = current_result
            new_lst.clear()
            new_lst.append(first)
            new_lst.append(second)

[print(' '.join(map(str, x))) for x in new_lst]
print(result)
