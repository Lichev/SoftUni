rows = int(input())

matrix = []

for _ in range(rows):

    matrix.append(list(map(int, input(). split())))

result = 0
for m in range(rows):
    result += matrix[m][m]

print(result)