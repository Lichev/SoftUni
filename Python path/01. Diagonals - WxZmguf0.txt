rows = int(input())


matrix = []

for _ in range(rows):
    m = [int(x) for x in input().split(", ")]
    matrix.append(m)


primary_daigonal = []
secondary_diagonal = []

for row in range(rows):
    primary_daigonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][rows - row - 1])


print(f'Primary diagonal: {", ".join(map(str, primary_daigonal))}. Sum: {sum(primary_daigonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')