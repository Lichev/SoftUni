rows, cols = tuple(map(int, input().split(", ")))

matrix = []

for row in range(rows):
    temp = list(map(int, input().split()))
    matrix.append(temp)

for c in range(cols):
    result = 0
    for r in range(rows):
        result += matrix[r][c]

    print(result)

