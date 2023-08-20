rows = int(input())

matrxi = []

for i in range(rows):
    text = [x for x in input()]
    matrxi.append(text)


symbol = input()

result = ''

valid = False
for row in range(rows):
    for col in range(len(matrxi[row])):
        if matrxi[row][col] == symbol:
            valid = True
            result = f'({row}, {col})'
            break
    if valid:
        break

if valid:
    print(result)
else:
    print(f'{symbol} does not occur in the matrix')