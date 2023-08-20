from collections import deque

def collect(matrix, row, col):
    result = 0
    for x in range(7):
        if matrix[row][x].isdigit():
            num1 = int(matrix[row][x])
            result += num1
        if matrix[x][col].isdigit():
            num2 = int(matrix[x][col])
            result += num2

    if matrix[row][col] == 'D':
        return result * 2
    elif matrix[row][col] == 'T':
        return result * 3


players = deque(input().split(", "))
matrix = [input().split() for x in range(7)]

dct = {}
count_turns = {}

for x in players:
    dct[x] = 501
    count_turns[x] = 0
while True:
    coordinates = input().strip("()").split(", ")
    turn = players.popleft()
    row = int(coordinates[0])
    col = int(coordinates[1])
    count_turns[turn] += 1
    if 0 <= row < 7 and 0 <= col < 7:
        if matrix[row][col].isdigit():
            num = int(matrix[row][col])
            dct[turn] -= num
        elif matrix[row][col] == 'B':
            print(f'{turn} won the game with {count_turns[turn]} throws!')
            break
        else:
            num1 = collect(matrix, row, col)
            dct[turn] -= num1
    else:
        players.append(turn)
        continue

    if dct[turn] <= 0:
        print(f'{turn} won the game with {count_turns[turn]} throws!')
        break

    players.append(turn)