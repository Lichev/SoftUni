rows = int(input())

matrix = []

for _ in range(rows):
    columns = list(map(int, input().split(", ")))
    evens = [x for x in columns if x % 2 == 0]
    matrix.append(evens)

print(matrix)