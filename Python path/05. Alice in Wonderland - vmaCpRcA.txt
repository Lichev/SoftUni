def alice(matrix, num):
    alice_coordinates = []

    for r in range(num):
        for c in range(num):
            if matrix[r][c] == 'A':
                alice_coordinates.append(r)
                alice_coordinates.append(c)
                break
    return alice_coordinates

num = int(input())

matrix = [input().split() for x in range(num)]

bags_of_tea = 0

lose = False

while True:
    command = input()
    row, col = alice(matrix, num)
    next_row = 0
    next_col = 0

    if command == 'right':
        next_row = row
        next_col = col + 1
    elif command == 'left':
        next_row = row
        next_col = col - 1
    elif command == 'down':
        next_row = row + 1
        next_col = col
    elif command == 'up':
        next_row = row - 1
        next_col = col

    if 0 <= next_row < num and 0 <= next_col < num:
            if matrix[next_row][next_col] == 'R':
                lose = True
                matrix[row][col] = '*'
                matrix[next_row][next_col] = '*'
                break
            elif matrix[next_row][next_col].isdigit():
                bags_of_tea += int(matrix[next_row][next_col])
                matrix[row][col] = '*'
                matrix[next_row][next_col] = 'A'
            else:
                matrix[row][col] = '*'
                matrix[next_row][next_col] = 'A'

            if bags_of_tea >= 10:
                matrix[next_row][next_col] = '*'
                break

    else:
        lose = True
        matrix[row][col] = '*'
        break


if lose:
    print(f"Alice didn't make it to the tea party.")
    [print(" ".join(x)) for x in matrix]
elif not lose or bags_of_tea >= 10:
    print(f'She did it! She went to the party.')
    [print(" ".join(x)) for x in matrix]
