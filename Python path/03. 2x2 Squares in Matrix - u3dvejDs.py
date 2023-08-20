rows, columns = tuple(map(int, input().split()))

matrix = [input().split() for x in range(rows)]
count = 0
for row in range(rows-1):
    for col in range(columns - 1):
        if row < rows - 1:
            first_pair = [matrix[row][col], matrix[row][col + 1]]
            second_pair = [matrix[row + 1][col], matrix[row + 1][col + 1]]

        if first_pair[0] == first_pair[1] and second_pair[0] == second_pair[1] and first_pair == second_pair:
            count += 1

print(count)
