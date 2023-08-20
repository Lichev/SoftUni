rows, cols = tuple(map(int, input().split(", ")))

matrix = []
result = 0


for r in range(rows):
    cols = [int(x) for x in input().split(", ")]
    matrix.append(cols)

    result += sum(cols)

print(result)
print(matrix)