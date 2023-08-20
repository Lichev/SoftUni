rows = int(input())

matrix = [list(map(int, input().split())) for x in range(rows)]
primary = []
secondary = []

for row in range(rows):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][rows - row - 1])

sum_primary = sum(primary)
sum_secondary = sum(secondary)
final = abs(sum_secondary - sum_primary)

print(final)