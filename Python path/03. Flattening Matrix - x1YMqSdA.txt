rows = int(input())

matrix = []

for _ in range(rows):
    columns = list(map(int, input().split(", ")))
    matrix.extend(columns)

print(matrix)